label ending:
    show screen day_screen

    scene black with fade

    show witch at right

    show ys_sprite at left

    witch "Have you made your choice President?"

    pres "Wait, wait, hold on."

    menu: 
        "Why would you want a yuri trope gone?":
            

            jump final_choice

        "I have made my choice.":
            jump final_choice

    "test"

label final_choice:
    $ made_choice = ""

    menu:
        "Take out all Tsunderes":
            $ made_choice = "Tsunderes" 

        "Remove all Girls In Denial":
            $ made_choice = "Girl In Denial"

        "Delete All Derederes":
            $ made_choice = "Derederes"


    hide witch

    show npc at right:
        zoom 0.35
    
    sci "*sniff* Miss president! you're finally awake!"

    pres "What happened? Did it not work? Are we still under attack??"

    sci "N-No we’re safe, YaoIsreal is no more., *sniff*"

    pres "Then why are you crying??"

    sci "I-Its just "
    extend "My wife was a [made_choice]"

    pres "Oh. I'm sorry.."
    extend " Would you like a hug?"

    sci "y-yeah."

    scene hug
    
    "test"
    return
