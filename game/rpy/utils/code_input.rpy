# ============================================================================
# 源界 (Source Realm) - 語法互動工具
# ============================================================================

init python:
    def check_syntax_assignment(input_str, expected_type, expected_var, expected_value):
        """
        驗證簡單的賦值語法：型別 變數 = 值;
        例如: int energy = 100;
        """
        import re
        # 移除前後空格
        s = input_str.strip()
        
        # 檢查分號
        if not s.endswith(";"):
            return False, "缺少分號 ';'"
            
        # 使用正則表達式拆解: (型別) (變數) = (值);
        pattern = r"^(\w+)\s+(\w+)\s*=\s*(.+);$"
        match = re.match(pattern, s)
        
        if not match:
            return False, "語法格式錯誤。應為：型別 變數 = 值;"
            
        t, v, val = match.groups()
        
        if t != expected_type:
            return False, f"型別錯誤。預期為 '{expected_type}'。"
            
        if v != expected_var:
            return False, f"變數名稱錯誤。預期為 '{expected_var}'。"
            
        if val != str(expected_value):
            return False, f"數值錯誤。預期為 '{expected_value}'。"
            
        return True, "語法正確！"

    def check_pointer_syntax(input_str, expected_var):
        """
        驗證指標語法：int* ptr = &var;
        """
        import re
        s = input_str.strip()
        if not s.endswith(";"):
            return False, "缺少分號 ';'"
            
        pattern = r"^int\*\s+(\w+)\s*=\s*&(\w+);$"
        match = re.match(pattern, s)
        
        if not match:
            return False, "語法錯誤。指標賦值應為：int* 指標名 = &變數名;"
            
        ptr_name, var_name = match.groups()
        
        if var_name != expected_var:
            return False, f"位址取值錯誤。應該取變數 '{expected_var}' 的位址。"
            
        return True, "指標語法正確！"
