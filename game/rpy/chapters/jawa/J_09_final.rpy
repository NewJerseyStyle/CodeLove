# ============================================================================
# 源界 (Source Realm) - Jawa Chapter 9: 秩序之眼 (The Eye of Order)
# ============================================================================

label jawa_J09_start:
    scene bg contract_office_chaos
    
    show jawa normal at left
    show rusty normal at center
    show py normal at right
    
    jawa "（周圍飄浮著無數巨大的合約，它們互相連結，形成了一個巨大的、閃著紅光的複雜網格）"
    
    jawa "警告：循環依賴（Circular Dependency）。合約 A 等待 B，B 等待 C，C 等待 A。"
    
    jawa "系統已進入死鎖狀態。無法推進，無法退回。"
    
    # Rusty 出現
    show rusty normal at center
    
    rusty "（焦急地）Jawa 姐！如果我們不打破這個循環，整個契約局的法律效力都會失效，源界會陷入無序的混亂！"
    
    py "（懶洋洋地在一旁看戲）哎呀，乾脆把這些合約全撕了，大家隨性一點不就好了？"
    
    jawa "（嚴肅地）絕對不行。規則是源界的基石。如果沒有契約，這裡就不再是源界。"
    
    jawa "（看向你）你。空白指標。這是我一生中最大的邏輯挑戰。規則之間發生了衝突，我必須在『秩序』與『生存』之間做出選擇。"
    
    narrator "你需要幫 Jawa 解決這個複雜的架構問題：解耦 (Decoupling) 與 仲裁者模式 (Mediator Pattern)。"

    menu:
        "建議引入『中介者』 (Mediator) 來統一調度，打破循環":
            jump jawa_09_suggest_mediator

        "建議將核心合約『解耦』 (Decoupling)，讓它們獨立運行":
            jump jawa_09_suggest_decoupling

        "建議將自己的意識作為『最終仲裁者』，手動處理所有依賴":
            jump jawa_09_suggest_personal_control

label jawa_09_suggest_mediator:
    player "Jawa，我們別讓合約直接互相對話了。建立一個『中介者』(Mediator) 辦公室吧。"
    
    player "所有的合約都把需求發給中介者，由中介者統一安排先後順序。這樣它們就不會互相等待，循環也就打破了！"
    
    jawa "（眼神發光，好像很努力在思考）……"
    
    pause 2.0
    
    jawa "（若無其事地繼續）...架構解耦。中介者模式。"
    
    jawa "（在網格中心敲下指令，一個巨大的紫色水晶球出現，合約紛紛向它匯集）"
    
    jawa "依賴關係已理順。系統恢復流轉。"
    
    jawa "（看向你）很好的建議。你理解了秩序的真諦：不是死板的限制，而是高效的組織。"
    
    # 追蹤
    $ track_learned_concept("mediator_pattern")
    $ track_affection("jawa", 15)
    $ jawa_relationship = "SYNCHRONIZED"
    $ set_chapter_status("J_09", "completed")
    
    jump jawa_09_end

label jawa_09_suggest_decoupling:
    player "把它們拆開吧。讓合約 A 不再依賴 B。雖然短時間內會不穩定，但至少能動起來。"
    
    jawa "（沉默 2 秒）"
    
    jawa "這是對規範的妥協。但... 為了生存。"
    
    jawa "（強行切斷合約間的連結。網格崩解，紅光消失，但係統留下了許多警告資訊）"
    
    jawa "死鎖解除。但合約一致性受到損傷。我們需要很久才能修復。"
    
    # 追蹤
    $ track_choice("logic", is_optimal=False)
    $ track_affection("jawa", -5)
    $ set_chapter_status("J_09", "completed")
    
    jump jawa_09_end

label jawa_09_suggest_personal_control:
    player "Jawa，把所有合約的依賴都連結到你身上吧。你來當那個最終的節點。"
    
    jawa "（愣住）那意味著我必須時時刻刻監控每一個細節。那壓力會... 非常大。"
    
    player "我會在你身邊，幫你一起監看。"
    
    jawa "（看著你的眼睛，微微一笑，這是她最溫柔的表情）"
    
    jawa "好。集中化管理。同步開始。"
    
    # 追蹤
    $ track_choice("emotion", is_optimal=True)
    $ track_affection("jawa", 25)
    $ jawa_relationship = "PARTNER"
    $ set_chapter_status("J_09", "completed")
    
    jump jawa_09_end

label jawa_09_end:
    scene black
    with Dissolve(2.0)

    narrator "J_01 到 J_09 全部完成。Jawa 線迎來了最終的巔峰。"

    teaching "你學會了：在大型 Java 系統中，架構的設計決定了系統的生死。透過設計模式（如中介者模式）來解耦複雜的依賴關係，可以防止系統陷入死鎖，並提高其維護性和靈活性。而最完美的規則，永遠是為了守護生命而存在的。"

    pause 2.0

    # 推進時間
    $ advance_time_to_next_period()

    jump time_choice_menu
