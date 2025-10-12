# TODO: Add images
label day_one: 

    # Epilogue

    scene map:
        xzoom 0.7 yzoom 0.45

    "The year is 3127. Advances in Assisted Reproductive Technologies during the 28th century and several wars caused humanity to separate itself into three nations."

    scene map_hetero:
        xzoom 0.7 yzoom 0.45

    "The Straight Empire."

    scene map_yaoi:
        xzoom 0.7 yzoom 0.45

    "The reclusive Yaoisreal"

    scene map_yuri:
        xzoom 0.7 yzoom 0.45

    "And our great homeland, Yuristan."

    scene map:
        xzoom 0.7 yzoom 0.45

    "Until two decades ago, the three nations remained balanced, each attending to their own affairs. But no longer. The leader of YaoIsreal, rumored to have the biggest forehead in all existence"

    show yaoikub with fade

    "revealed himself as Yaoikub, inventor of mlm."
    extend "\nUnfortunately for the rest of humanity, he had not stopped at inventing mlm. "
    
    "His latest creation was GayGas, a gas that made any male into an obedient puppet to the YaoIsreali cause, while also turning him into a raging homosexual."

    scene map_yaoisreal:
        xzoom 0.7 yzoom 0.45

    "The YaoIsreali air force let this gas loose all over the Straight Empire, and within weeks it collapsed."
    
    scene black

    "As billions of refugees fled to Yuristan, you realized that you had to reinstate Yuristans military power, inorder to protect your new citizens as well as your old."

    "Yet, your predecessor had gutted Yuristans witch militia, reallocating the funds towards affordable housing."

    "While at the time this was a popular and effective policy, today it has endangered the lives of all of the remaining women in the world,"

    "for the Angst Army once capable of inflicting emotional pain so severe it caused physical injuries upon any offending force, now refuses to fight without appeasement."

    "They want reparations for their slighted honor, and their conditions are as follows."

    scene normal_silhouette:
        xzoom 0.7 yzoom 0.45

    "As punishment, the nation that had cut their salaries in half must sacrifice one of its most valued treasures."

    "You, as representative of the people, must sacrifice a popular yuri trope, never to be seen again."
    # Add x images

    "According to your wishes, we, your most trusted yuri scientists, have temporarily wiped your memory and placed you within this simulation. At the end of the simulation you must make The Sacrifice for Yuristan."

    scene highschool_front

    "Good luck, miss president.\nGood luck Yuri-San."

    # Day one starts
    show screen day_screen

    ys "Oh No! I'm late!!"

    call late_to_school_options

# For the first scene of day one
menu late_to_school_options:
    
    "Oh god I can't be late on the first day! (Run to school)":
        jump first_day_variation_one
        return

    "Well not much I can do about it now (Eat breakfest and brisk walk to school)":
        jump karoin_route

    "First day is never that serious (Walk to school)":
        jump sd_route


label first_day_variation_one:

    # Add shake scene
    scene bg road with vpunch
    scene bg road with vpunch
    scene bg road with vpunch
    scene bg road with vpunch
    
    "why do those damn witches demand a sacrifice anyway?" 
    extend "\nDo they not stand for the same flag as the rest of us?\n" 
    extend "Do they not care for their own countrywomen?\n"
    extend "And surely whichever the sacrificial trope would also stop existing within their ranks.\nSomething seems-"

    vc "Yuri-Saaan! Yuri-San wait up!"
    vc "Oh crap."

    scene bg bang with vpunch
    "BANG!" # Possible sound effect her

    vc "Yowch owch ow"

    ys "*I wonder what trope she could possible represent. Quite puzzling.*"

    show vc_neutral at Position(xalign = 0.5, yalign = 0.5)

    vc "I'm okay, I'm fine"

    menu meeting_1:
        "Need a hand?":
                vc "Please and thank you"
                # {rotate mc by a couple fo degrees towards the floor, and then rotate her back then show Cere on the screen. Put them right next to each other to signify hand holding}
                vc "You can let go of my hand now"

                menu meeting_sub_1:
                    "Don't want to":
                        show cere_blushing
                        
                        # They hold hands?
                        vc "D-don’t be silly we’re going to be late for school!"
                        ys "If you really want me to"
                        jump first_day_scene_one

                    "sure":
                        jump first_day_scene_one

# Second scene school where they arrive after the 3 meeting scenarios
label first_day_scene_one:
    scene bg black
    " Off to the yuri club, of which you are president. Hip Hip Hooray for the President of Yuri"
    
    scene bg school hallway with fade

    ys " I cant wait to lead the Yuri Girl Love Manga Club to another year of resounding success "

    scene bg book club room with fade

    show kh happy at Position(xalign = 0.9, yalign = 0.5)

    kh "Q-queen Yuri!"
    kh "I'm not worthy"

    ys "Its just president Kaorin. "
    ys "This is a democracy."
    ys "And all who love Wuh Luh Wuh are worthy. Even the most hateful of wretches may find comfort within these hallowed halls"

    "*knock knock*"

    sd "Is this the Anti-Stupid Pole of Stupidity club?"

    menu:
        "Yes, it is":
            
            # check this image
            show fkds at Position(xalign = 0.5, yalign = 0.5)

            sd "That sign says I <3 Yuri."

            ys "were multitasking"

            sd "I think im going to go-"

            ys "PLEASE PLEASE PLEASE STAY"
            ys "I finally became president of yuri but ill get demoted if we dont get any members"

            sd "okay? I guess?"

        "No this is the Yuri club, but your not going anywhere":
            sd "Says who?"

            kh "FOOL!"
            kh "You speak to the president of Yuri!"

            sd "Oh crap, do I have to bow or something?"

            ys "No your fine\n For Now."

    vc "Yuri-san. you called me?" 

    show vin cere neutral at Position(xalign = 0.0, yalign = 0.5) 

    ys "Welcome to the Yuri club my childhood best friend"

    vc "Uhh I don't like girls actually"

    ys "Yeah, thats what they all say"

    vc "I think im going to leave"

    menu:
        "can't, doors locked":
            vc "Who has the key?"

            show vin cere neutral

            ys "Kaorin! Window! NOW"

            kh "Yes miss president!"

            hide vin cere neutral
            hide kh
            hide fkds

            scene bg window

            # Key flys here linux boy
            show key at Transform(xalign=0.0, yalign=0.5)
            with None

            show key at Transform(xalign=1.0, yalign=0.5)
            with move
            ys "I have no clue where the keys are actually."

        "I love you":
            vc "I love you too sister!"

            kh "Yowch"

            sd "Yikes"

            ys "I'm working on it"

            vc "Working on what?"


    scene bg book club room with fade

    show kh happy at Position(xalign = 0.9, yalign = 0.5)
    show fkds at Position(xalign = 0.5, yalign = 0.5)
    show vin cere neutral at Position(xalign = 0.0, yalign = 0.5) 

    ys "On to more important matters!\nWhat Yuri Girl Love Manga are we reading this month?"

    sd "Can we do the Green Yuri"

    kh "We always do the green yuri"

    vc "GUys can I please leave"

    menu:
        "Green Yuri again":
            sd "I-its not like I want to though!"

        "Pink Yuri":
            kh "I love the Pink Yuri!"

    
    ys "What if we did our own Yuri"

    kh "Great idea miss president!"
    
    ys "That decides it. Yuri club we're researching our favourite yuri tropes tonight."

    hide kh happy 
    hide fkds 
    hide vin cere 

    # Fix the jump here
