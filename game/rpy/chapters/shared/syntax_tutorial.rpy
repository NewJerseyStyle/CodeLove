# ============================================================================
# 源界 (Source Realm) - 語法入門：標籤寫入
# ============================================================================

label syntax_tutorial_start:
    scene bg information_square
    
    show cee normal at left
    show rusty normal at right
    
    rusty "嘿，在你開始幫忙之前，我們先來學學怎麼寫『標籤』吧！"
    
    cee "（停在一台閃爍著紅光的終端機前）"
    
    cee "能量耗盡。編號 1024。"
    
    rusty "這台機器的能量歸零了，我們得用指令幫它補充能量。"
    
    rusty "寫指令就像寫標籤一樣，有固定的格式哦！"
    
    rusty "首先是『種類』(int 代表整數)，然後是『名字』(energy)，接著是『數值』(100)，最後一定要記得加個『分號』(;)，代表這句話說完了！"
    
    cee "（轉頭看著你）你。試著寫入。"

    $ syntax_correct = False
    
    while not syntax_correct:
        python:
            player_input = renpy.input("請輸入：int energy = 100;", length=30)
            is_valid, message = check_syntax_assignment(player_input, "int", "energy", 100)
            
        if is_valid:
            $ syntax_correct = True
            rusty "哇！你寫得太標準了！看，終端機亮起來了！"
            cee "（點頭）語法正確。連結成功。"
        else:
            rusty "哎呀，好像差了一點點... [message]"
            rusty "別擔心，再試一次！記得空格和最後的分號哦。"

    pause 1.0
    
    cee "有效率。"
    
    rusty "太棒了！你現在已經掌握了源界最基礎的語法了。"
    
    cee "（看著恢復綠光的終端機）權限已提升。"
    
    rusty "走吧，我們去處理更複雜的標籤！"

    jump time_choice_menu
