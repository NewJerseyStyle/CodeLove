#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Source Realm - Story Linter

This script validates label usage in Ren'Py scripts based on configuration.
It checks:
1. Labels follow naming conventions
2. Story labels are reachable from start
3. No dead-ends in main story
4. Endings are reachable
5. Random events are properly categorized
"""

import os
import re
import sys
import json
import yaml
from pathlib import Path
from typing import Dict, List, Set, Tuple, Any
from collections import defaultdict, deque

# Set UTF-8 encoding for output
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')


class StoryLinter:
    """Story linter with configuration-based validation"""

    def __init__(self, config_path: str, images_dir: str = None):
        self.config = self._load_config(config_path)
        self.labels: Dict[str, str] = {}  # label_name -> file_path
        self.jumps: Dict[str, List[str]] = defaultdict(list)  # label_name -> [target_labels]
        self.reverse_jumps: Dict[str, List[str]] = defaultdict(list)  # label_name -> [source_labels]
        self.start_label = "start"

        # Image validation
        self.show_statements: Dict[str, List[Tuple[str, str]]] = defaultdict(list)  # label -> [(image_name, file_path), ...]
        self.available_images: Set[str] = set()
        if images_dir:
            self.collect_available_images(images_dir)

        # Build category lookups from config
        self.category_prefixes = {}
        self.category_rules = {}
        for cat_name, cat_config in self.config.get('label_categories', {}).items():
            for prefix in cat_config.get('prefixes', []):
                self.category_prefixes[prefix] = cat_name
            self.category_rules[cat_name] = cat_config

        # Compile ignored labels list
        self.ignored_labels = set(self.config.get('ignored_labels', []))

    def _load_config(self, config_path: str) -> Dict:
        """Load configuration from YAML file"""
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            print(f"Warning: Config file not found at {config_path}, using defaults")
            return self._default_config()

    def _default_config(self) -> Dict:
        """Return default configuration"""
        return {
            'label_categories': {
                'story': {'prefixes': [], 'needs_path_from_start': True, 'must_reach_ending': True},
                'random_events': {'prefixes': ['event_', 'holiday_', 'sleep_', 'quiz_'],
                                  'needs_path_from_start': False, 'check_dynamic_jump_sources': True},
                'debug': {'prefixes': ['debug_', 'test_', 'example_'],
                         'needs_path_from_start': False, 'must_reach_ending': False, 'can_be_dead_end': True},
                'system': {'prefixes': ['show_', 'display_', 'check_', 'init_'],
                          'needs_path_from_start': False, 'must_reach_ending': False, 'can_be_dead_end': True},
                'endings': {'prefixes': ['ending_', 'end_'],
                           'needs_path_from_start': True, 'must_reach_ending': False, 'can_be_dead_end': True},
            },
            'ignored_labels': [],
        }

    def _get_label_category(self, label_name: str) -> str:
        """Get the category of a label based on its prefix"""
        for prefix, category in self.category_prefixes.items():
            if label_name.startswith(prefix):
                return category

        # Default to 'story' if no prefix matches
        return 'story'

    def _should_ignore_label(self, label_name: str) -> bool:
        """Check if a label should be ignored"""
        if label_name in self.ignored_labels:
            return True
        return False

    def _is_ending_label(self, label_name: str) -> bool:
        """Check if a label is an ending"""
        return label_name.startswith('ending_') or label_name.endswith('_end')

    def add_label(self, label_name: str, file_path: str):
        """Add a label to the graph"""
        self.labels[label_name] = file_path

    def add_jump(self, source_label: str, target_label: str):
        """Add a jump relationship"""
        self.jumps[source_label].append(target_label)
        self.reverse_jumps[target_label].append(source_label)

    def add_show_statement(self, label: str, image_name: str, file_path: str):
        """Add a show/scene statement to track"""
        self.show_statements[label].append((image_name, file_path))

    def collect_available_images(self, images_dir: str):
        """Scan images directory and build lookup"""
        supported_extensions = ['.png', '.jpg', '.jpeg', '.webp']
        images_path = Path(images_dir)

        if not images_path.exists():
            return

        for ext in supported_extensions:
            for img_file in images_path.rglob(f'*{ext}'):
                # Ren'Py uses only filename (not directory path) for image names
                filename = img_file.stem  # filename without extension

                # Normalize filename for comparison:
                # 1. Replace spaces and hyphens with underscores
                normalized = filename.replace(' ', '_').replace('-', '_')
                self.available_images.add(normalized)

                # Create aliases based on filename patterns

                # Pattern 1: "bg xxx" → already handled by normalization above
                # (e.g., "bg contract_office.jpeg" → "bg_contract_office")

                # Pattern 2: Character directory mappings
                # Map directory names to character prefixes
                # "C/cee tired.png" → "cee_tired"
                # "Java/jawa normal.png" → "jawa_normal"
                # "Python/py smile.png" → "py_smile"
                # "Go/golly think.png" → "golly_think"
                # "Rust/rusty worried.png" → "rusty_worried"
                char_mappings = {
                    'C': 'cee',
                    'Java': 'jawa',
                    'Python': 'py',
                    'Go': 'golly',
                    'Rust': 'rusty'
                }

                # Check if this file is in a character directory
                parent_dir = img_file.parent.name
                if parent_dir in char_mappings:
                    char_prefix = char_mappings[parent_dir]

                    # Check if filename already starts with the character name
                    # If so, keep it as is
                    if not normalized.lower().startswith(char_prefix.lower() + '_'):
                        # "tired" → "cee_tired"
                        alias = char_prefix + '_' + normalized
                        self.available_images.add(alias)

                    # Also handle Java-specific naming
                    # "Jawa normal" → "jawa_normal"
                    if parent_dir == 'Java':
                        # Convert "Jawa" to lowercase
                        if 'Jawa' in normalized:
                            normalized_jawa = normalized.replace('Jawa', 'jawa')
                            self.available_images.add(normalized_jawa)


    def validate_images(self) -> List[Dict[str, str]]:
        """Check all show statements have corresponding images"""
        missing = []

        # Get ignored images list from config
        ignored_images = set(self.config.get('ignored_images', []))

        for label, shows in self.show_statements.items():
            for image_name, file_path in shows:
                # Skip ignored images (like "black" screen)
                if image_name in ignored_images:
                    continue

                # Normalize image name for comparison
                normalized = image_name.replace(' ', '_').replace('-', '_')

                # Generate multiple possible patterns to match
                possible_patterns = [normalized]

                # If starts with "bg_", also try with "background_"
                if normalized.startswith('bg_'):
                    possible_patterns.append('background_' + normalized[3:])

                # Check if image exists (with multiple possible patterns)
                found = False
                for pattern in possible_patterns:
                    for available in self.available_images:
                        if pattern == available:
                            found = True
                            break
                    if found:
                        break

                if not found:
                    missing.append({
                        'label': label,
                        'image': image_name,
                        'file': file_path,
                        'message': f"Image '{image_name}' not found in images/",
                    })

        return missing

    def get_reachable_labels(self, start_label: str) -> Set[str]:
        """Use BFS to find all reachable labels from a start label"""
        if start_label not in self.labels:
            return set()

        visited = set()
        queue = deque([start_label])

        while queue:
            current = queue.popleft()
            if current in visited:
                continue
            visited.add(current)

            for next_label in self.jumps[current]:
                if next_label not in visited:
                    queue.append(next_label)

        return visited

    def validate(self) -> Dict[str, Any]:
        """Perform validation based on configuration"""
        errors = []
        warnings = []
        info = []

        # Validate images if enabled
        if 'missing_images' in self.config.get('validation', {}).get('error_on', []):
            missing_images = self.validate_images()
            error_level = 'error' if 'missing_images' in self.config.get('validation', {}).get('error_on', []) else 'warning'
            for img_error in missing_images:
                if error_level == 'error':
                    errors.append(img_error)
                else:
                    warnings.append(img_error)

        # Get all labels by category
        labels_by_category = defaultdict(list)
        for label in self.labels:
            if self._should_ignore_label(label) or label == self.start_label:
                continue
            category = self._get_label_category(label)
            labels_by_category[category].append(label)

        # Validate each category
        for category, rules in self.category_rules.items():
            labels = labels_by_category.get(category, [])

            # Check if story labels need path from start
            if rules.get('needs_path_from_start', False):
                reachable = self.get_reachable_labels(self.start_label)
                for label in labels:
                    if label not in reachable:
                        error_level = 'error' if 'orphaned_story_labels' in self.config.get('validation', {}).get('error_on', []) else 'warning'
                        error_msg = {
                            'label': label,
                            'category': category,
                            'file': self.labels.get(label, 'Unknown'),
                            'message': f"Label '{label}' in category '{category}' is not reachable from start",
                            'rule': 'needs_path_from_start',
                        }
                        if error_level == 'error':
                            errors.append(error_msg)
                        else:
                            warnings.append(error_msg)

            # Check if labels must reach endings
            if rules.get('must_reach_ending', False) and not rules.get('can_be_dead_end', False):
                for label in labels:
                    # BFS to check if ending is reachable
                    can_reach_ending = False
                    visited = set()
                    queue = deque([label])

                    while queue and not can_reach_ending:
                        current = queue.popleft()
                        if current in visited:
                            continue
                        visited.add(current)

                        if self._is_ending_label(current):
                            can_reach_ending = True
                            break

                        for next_label in self.jumps[current]:
                            if next_label not in visited:
                                queue.append(next_label)

                    if not can_reach_ending:
                        error_level = 'error' if 'dead_ends_in_story' in self.config.get('validation', {}).get('error_on', []) else 'warning'
                        error_msg = {
                            'label': label,
                            'category': category,
                            'file': self.labels.get(label, 'Unknown'),
                            'message': f"Label '{label}' in category '{category}' cannot reach any ending",
                            'rule': 'must_reach_ending',
                        }
                        if error_level == 'error':
                            errors.append(error_msg)
                        else:
                            warnings.append(error_msg)

            # Check for orphaned labels (no jumps to them)
            if not rules.get('check_dynamic_jump_sources', False):
                for label in labels:
                    if len(self.reverse_jumps[label]) == 0:
                        # This is fine for some categories
                        error_msg = {
                            'label': label,
                            'category': category,
                            'file': self.labels.get(label, 'Unknown'),
                            'message': f"Label '{label}' has no incoming jumps",
                            'rule': 'no_incoming_jumps',
                        }
                        info.append(error_msg)

        # Check for uncategorized labels (labels that don't match any category)
        all_categorized_labels = set()
        for category_labels in labels_by_category.values():
            all_categorized_labels.update(category_labels)

        for label in self.labels:
            if self._should_ignore_label(label) or label == self.start_label:
                continue
            if label not in all_categorized_labels:
                warnings.append({
                    'label': label,
                    'category': 'uncategorized',
                    'file': self.labels.get(label, 'Unknown'),
                    'message': f"Label '{label}' does not match any category prefix",
                    'rule': 'label_categorization',
                })

        return {
            'errors': errors,
            'warnings': warnings,
            'info': info,
            'total_labels': len(self.labels),
            'labels_by_category': {k: len(v) for k, v in labels_by_category.items()},
        }


def parse_rpy_file(file_path: str, linter: StoryLinter):
    """Parse a .rpy file and add labels/jumps to the linter"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse label definitions
    label_pattern = r'^label\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*:'
    for match in re.finditer(label_pattern, content, re.MULTILINE):
        label_name = match.group(1)
        linter.add_label(label_name, file_path)

    # Parse jump statements
    lines = content.split('\n')
    current_label = None

    for line in lines:
        # Check if this line is a label definition
        label_match = re.match(r'^label\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*:', line)
        if label_match:
            current_label = label_match.group(1)
            continue

        # Skip if we're not in a label block
        if current_label is None:
            continue

        # Parse jump statements
        jump_pattern = r'jump\s+([a-zA-Z_][a-zA-Z0-9_]*)'
        for match in re.finditer(jump_pattern, line):
            target_label = match.group(1)
            linter.add_jump(current_label, target_label)

        # Parse show/scene statements in current label block
        # Match: show/scene followed by image name (stop at 'at' keyword or end of line)
        show_scene_match = re.match(r'^\s*(?:show|scene)\s+(.+?)(?:\s+at\s|$)', line)
        if show_scene_match:
            image_name = show_scene_match.group(1).strip()
            linter.add_show_statement(current_label, image_name, file_path)


def analyze_all_rpy_files(project_root: str, config_path: str, images_dir: str = None) -> StoryLinter:
    """Analyze all .rpy files"""
    linter = StoryLinter(config_path, images_dir)

    # Iterate through all .rpy files
    for rpy_file in Path(project_root).rglob('*.rpy'):
        # Skip files in examples/ directory
        if 'examples' in rpy_file.parts:
            continue
        parse_rpy_file(str(rpy_file), linter)

    return linter


def print_report(result: Dict[str, Any], output_format: str = 'text'):
    """Print validation report in specified format"""
    if output_format == 'json':
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return

    # Text format
    print("=" * 80)
    print("源界 (Source Realm) - Story Linter 報告")
    print("=" * 80)
    print()

    print(f"總標籤數: {result['total_labels']}")
    print(f"標籤分類:")
    for category, count in result['labels_by_category'].items():
        print(f"  - {category}: {count}")
    print()

    # Errors
    print("=" * 80)
    print(f"錯誤 ({len(result['errors'])})")
    print("=" * 80)
    if result['errors']:
        for error in result['errors']:
            short_path = error['file'].split('\\')[-1] if '\\' in error['file'] else error['file'].split('/')[-1]
            print(f"  [ERROR] {error['label']} ({short_path})")
            print(f"          {error['message']}")
        print()
    else:
        print("  ✓ 沒有錯誤")
        print()

    # Warnings
    print("=" * 80)
    print(f"警告 ({len(result['warnings'])})")
    print("=" * 80)
    if result['warnings']:
        for warning in result['warnings']:
            short_path = warning['file'].split('\\')[-1] if '\\' in warning['file'] else warning['file'].split('/')[-1]
            print(f"  [WARNING] {warning['label']} ({short_path})")
            print(f"            {warning['message']}")
        print()
    else:
        print("  ✓ 沒有警告")
        print()

    # Info
    if result['info']:
        print("=" * 80)
        print(f"資訊 ({len(result['info'])})")
        print("=" * 80)
        for info_item in result['info']:
            short_path = info_item['file'].split('\\')[-1] if '\\' in info_item['file'] else info_item['file'].split('/')[-1]
            print(f"  [INFO] {info_item['label']} ({short_path})")
            print(f"         {info_item['message']}")
        print()

    # Summary
    print("=" * 80)
    print("摘要")
    print("=" * 80)
    total_issues = len(result['errors']) + len(result['warnings'])
    if total_issues == 0:
        print("✓ 劇情驗證通過，沒有發現問題。")
    else:
        print(f"發現 {total_issues} 個問題 ({len(result['errors'])} 錯誤, {len(result['warnings'])} 警告)")
        if len(result['errors']) > 0:
            print("  請修復所有錯誤後再提交 PR。")
    print()


def main():
    """Main function"""
    import argparse

    parser = argparse.ArgumentParser(description='Story Linter for Source Realm')
    parser.add_argument('--config', '-c', default='linter_config.yaml',
                        help='Path to linter configuration file')
    parser.add_argument('--format', '-f', choices=['text', 'json'], default='text',
                        help='Output format (default: text)')
    parser.add_argument('--project-root', '-p', default=None,
                        help='Project root directory (default: script directory)')
    parser.add_argument('--images-dir', '-i', default=None,
                        help='Images directory for validation (default: <project-root>/images)')

    args = parser.parse_args()

    # Get project root
    if args.project_root:
        project_root = args.project_root
    else:
        project_root = os.path.dirname(os.path.abspath(__file__))

    # Get images directory
    if args.images_dir:
        images_dir = args.images_dir
    else:
        images_dir = os.path.join(project_root, 'images')

    # Analyze all .rpy files
    print(f"正在分析項目: {project_root}")
    print(f"正在掃描 .rpy 文件...")
    print(f"正在掃描圖片: {images_dir}")
    print()

    linter = analyze_all_rpy_files(project_root, args.config, images_dir)

    # Validate
    result = linter.validate()

    # Print report
    print_report(result, args.format)

    # Exit with appropriate code
    sys.exit(1 if result['errors'] else 0)


if __name__ == "__main__":
    main()
