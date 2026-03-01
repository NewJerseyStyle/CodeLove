# ============================================================================
# 廣場背景音樂系統 (Plaza Background Music System)
# ============================================================================

init python:
    # 追蹤廣場音樂是否正在播放
    if not hasattr(persistent, "plaza_music_playing"):
        persistent.plaza_music_playing = False

    def play_plaza_music():
        """播放廣場背景音樂並循環"""
        if not persistent.plaza_music_playing:
            renpy.music.play("audio/Gemini-ELITE_REMIX_STUDIOv3.wav", loop=True, fadein=2.0)
            persistent.plaza_music_playing = True

    def stop_plaza_music():
        """停止廣場背景音樂"""
        if persistent.plaza_music_playing:
            renpy.music.stop(fadeout=2.0)
            persistent.plaza_music_playing = False
