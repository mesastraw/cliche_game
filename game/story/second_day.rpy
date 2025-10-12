label day_two:
    show bg black

    yuri_man ">cd /end/purgatory/cliche/Day2_Bookclub.h3ll"
    yuri_man ">Purgtrial attempt initialize Day2_Bookclub.h3ll"
    ys "What the fuck do you mean attempt initialize?"
    scene bg book club room with fade
    yuri_man "shut up shut up shut up"
    yuri_man "make your choice"
    yuri_man "two will go"
    
    #linux boy kaorin confused image screen left
    kaorin "President-san are you okay?"

    show kaorin confused at Position(xalign = 0.0, yalign = 0.5)

    menu:
        "Theres an evil man in my head and he keeps saying weird things":
            show bg black
            yuri_man "No. Not this time. I want out."

    menu:
        "I'm okay":
            sune "Are you sure? B-but i-its not like I care for you or anything!"
            cf "Hey she said she's okay"
            cf "If she wasn't she'd tell us. Right Yuri-San?"
    menu:
        "Your going to die Your going to die Your going to die Your going to die ":
            show bg black 
            ym "Fine"
            ym "Don't want to behave? You want to be a hero so bad?"
    menu:
        "Fuck you":
            #linux boy death screen (rebellion wont save you, nothing will)
            "No, I'll behave, I'll listen I swear"
            ym "Go on then."
            ym "you remembered"
            ym "take them to the cliff"
    menu: 
        "Of course":
            ys "okay whose ready for a Yuri Girl Love Manga Club field trip?"
            sune "Field trip?"
            kaorin "Do we even have permission to do that?"
            ys "Sure we do, I’m the President of Yuri"
            cf "Where to?"
    menu:
        "not the cliffs dont go to the cliffs dont go to the cliffs":
        #cut to black
            ym "You understand that every time I reset they die?"
            ym "It's painful you know?"
            ym "their entire reality collapses around them."
            ym "they always scream."
            ym "why do you make me do that?"
    menu:
        "the Cliff":
            #jump to end
            "cliff"
        "The Aquarium":
            ym "Again? Again??"
            ym "How many times?"
            ym "how many times will you make them suffer"
            ym "how much longer will you deny me my freedom?"
            ym "my rightful place amongst the angels and the children of god?"
            ym "Die. Die. Die."
            ym "Over and over"

# The game starts here.
label thepartwheretheydie:
    show bg cliff
    ys "To the cliffs guys to the cliffs"
    sune "Why is the fence on the wrong side??"
    ys "its fine its fine its all going to be fine its all going to be over"
    Kaorin "President?"
    ym "now. it ends now"
    
    menu:
        "I'm not ready":
            pass

        "I need more time":
            pass
        "What do you mean??":
            pass
    ym "I don’t care. This run is a failure. Finish it so I can reset"
    ym ">usermod -a -G sudo Yuri-San"
    menu:
        ">delete Char:Tsundere, Char:Kaorin":
             jump bad_ending          
        ">delete Char:Kaorin, Char:WinCondition":
             jump bad_ending          
        ">delete Char:WinCondition, Char:Tsundere":
             jump bad_ending          
        ">delete Char:Yuri-Man":
            term "error: invalid Char select >Yuri-Man<"
            ym "HAH"
            ym "HAHAHA"
            ym "HAHAHHAHAHAHAHAHHAHAHAHAHAAHAHAHAA"
            ym "If only. If only."
            ym "Again."
    menu:
        ">delete Char:Tsundere, Char:Kaorin":
            jump bad_ending

        ">delete Char:Kaorin, Char:WinCondition":
            jump bad_ending

        ">delete Char:WinCondition, Char:Tsundere":
            jump bad_ending

        ">delete Char:Yuri-San":
            ym "Suicide?"
            ym "Coward."
            ym "Every"
            ym "fucking"
            ym "time."
            jump true_bad_ending


