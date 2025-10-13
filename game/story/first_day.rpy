default day_one_chosen_variation = 0
default chosen_sale_option = 0

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

    show x_mark at left
    pause(1)
    show x_mark at center
    pause(1)
    show x_mark at right 

    "According to your wishes, we, your most trusted yuri scientists, have temporarily wiped your memory and placed you within this simulation. At the end of the simulation you must make The Sacrifice for Yuristan."

    scene highschool_front

    "Good luck, miss president.\nGood luck Yuri-San."

    jump day_one_start

label day_one_start:
    show screen day_screen

    scene bedroom
    
    show ys_sprite

    ys "Oh No! I'm late!!"

    call late_to_school_options

# For the first scene of day one
menu late_to_school_options:
    
    "Oh god I can't be late on the first day! (Run to school)":
        $ day_one_chosen_variation = 1
        jump first_day_variation_one

    "Well not much I can do about it now (Eat breakfest and brisk walk to school)":
        $ day_one_chosen_variation = 1
        jump first_day_variation_two

    "First day is never that serious (Walk to school)":
        $ day_one_chosen_variation = 1
        jump first_day_variation_three

label first_day_variation_one:

    # Add shake scene
    scene bg road with vpunch:
        xzoom 1.6 yzoom 1.5
    scene bg road with vpunch:
        xzoom 1.6 yzoom 1.5
    scene bg road with vpunch:
        xzoom 1.6 yzoom 1.5
    scene bg road with vpunch:
        xzoom 1.6 yzoom 1.5
    
    "why do those damn witches demand a sacrifice anyway?" 
    extend "\nDo they not stand for the same flag as the rest of us?\n" 
    extend "Do they not care for their own countrywomen?\n"
    extend "And surely whichever the sacrificial trope would also stop existing within their ranks. Something seems-"

    vc "Yuri-Saaan! Yuri-San wait up!"
    vc "Oh crap."

    scene bg bang with vpunch:
        xzoom 2.5 yzoom 1.5
    "BANG!!" # Possible sound effect her

    scene bg road:
        xzoom 1.6 yzoom 1.5

    vc "Yowch owch ow"

    show ys_sprite at left
    show vc_neutral at right

    ys "*I wonder what trope she could possible represent. Quite puzzling.*"

    vc "I'm okay, I'm fine"

    menu meeting_1:
        "Need a hand?":
                vc "Please and thank you"
                # {rotate mc by a couple fo degrees towards the floor, and then rotate her back then show Cere on the screen. Put them right next to each other to signify hand holding}
                vc "You can let go of my hand now"

                menu meeting_sub_1:
                    "Don't want to":
                        hide vc_neutral
                        show vc_blushing at right
                        
                        # They hold hands?
                        vc "D-don’t be silly we’re going to be late for school!"
                        ys "If you really want me to"
                        jump route_one_end

                    "sure":
                        jump route_one_end

        "How did you fall anyway?":
            vc "Another stupid pothole."
            extend " Useless Yuristan government"

            ys "Hey now, funding is really tight you know. I’m sure they’ll fix them eventually."

            vc "Funding wouldn't be so tight if they didn’t spend so much on that idiotic Yuri Festival."

            ys "We can’t put patching potholes above celebrating our heritage Cere."

            vc "All I know is back home in the Great Straight Empire, we didn’t have a Yuri Festival, and we also didn’t have potholes."

    jump route_one_end 

label route_one_end:
        vc "Can we hurry now? I need perfect attendance this year."
        jump first_day_scene_one



label first_day_variation_two:
    # Add walking animation here
    scene bg road with vpunch:
        xzoom 1.6 yzoom 1.5

    "why do those damn witches demand a sacrifice anyway?" 
    extend "\nDo they not stand for the same flag as the rest of us?\n" 
    extend "Do they not care for their own countrywomen?\n"
    extend "And surely whichever the sacrificial trope would also stop existing within their ranks. Something seems-"

    ys "Whoa watch out-"

    scene bg bang with vpunch:
        xzoom 2.5 yzoom 1.5
    "BANG!!" # Possible sound effect her
    # Animatge

    scene bg road:
        xzoom 1.6 yzoom 1.5

    show kh_blushing at center
 
    kh "OH MY GOSH MISS YURI! Are you okay??"

    sim "Kaorin Womenlover, your junior and head of the Secret Yuri San Fanclub"
    
    ys "{i}head of the {b}what??{/i}{/b}"
    
    ys "ow ow ouchie ow ow yowch"

    hide kh_blushing
    show kh_sad at center

    kh "I’M SO SORRY YURI SAN! FORGIVE ME PLEASE"   

    menu:
        "Aren’t you hurt too?":
            hide kh_sad
            show kh_happy at center

            kh "Oh you see I was born hard headed. When I was born my nurse dropped me and my skull left a crack in the floor."
            
            # Mc gets up
            show kh_happy at left
            show ys_sprite at right

            ys "Explains a lot"

        "It’s okay, I’m fine, I’ll be all right":
            kh "are you sure? you look very.. Green"

            ys "Thats just my complexion- *throws up*"

            hide kh_blushing
            show kh_sad at center

            kh "Oh no oh no oh no oh no."
            extend " I’m calling an ambulance!"

            ys"No wait, "
            show kh_sad at left
            show ys_sprite at right
            extend "I'm fine now."

    ys "Run to school with me?" 
    
    show kh_blushing at left

    kh "C-can I?!"

    menu:
        "of course":
            show kh_happy at left
            kh "Thank you thank you thank you thank you thank you thank you thank you thank you thank you thank you  tha"
            jump first_day_scene_one

        "I’d appreciate it":
            kh "I-I’ll do my best!"

    jump first_day_scene_one


label first_day_variation_three:
    scene bg road with vpunch:
        xzoom 1.6 yzoom 1.5
    
    "why do those damn witches demand a sacrifice anyway?" 
    extend "\nDo they not stand for the same flag as the rest of us?\n" 
    extend "Do they not care for their own countrywomen?\n"
    extend "And surely whichever the sacrificial trope would also stop existing within their ranks. Something seems-"

    #Crash sound effect
    unknown "OW"
    extend "STUPID POLE"

    # metal pipe falling
    "WHANG"

    ys "????"

    # metal pipe
    "WHANG"

    ys "what's going on"

    scene bg sutpid pole:
        "bg stupid pole.webp"
        xzoom 1.9

    show sd_angry at right
    
    show ys_sprite at left

    sim "Sune Derei, your short fused friend"

    sd "Who"

    "*WHANG*"
    # metal pipe

    sd "Put this"

    "*WHANG*"
    # metal pipe

    sd "Stupid fucking pole"

    "*WHANG*"
    # metal pipe

    sd "in the middle of the sidewalk" 

    ys "Sune Derei! Are you okay?"

    show sd_blushing at right

    sd "Y-Yuri-San! What are you d-doing here"

    ys "I heard some concerning noises so I came to check"

    sd "It’s nothing really,"
    
    hide sd_blushing
    show sd_angry at right

    extend "just this stupid pole of stupidity that some stupid idiot put in the middle of the sidewalk for some stupid reason."

    menu:
        "Be more careful of where your walking, you could get a concussion!":
            hide sd_angry
            show sd_sad
            
            sd "Your right, I'm sorry."
    
        "What a stupid pole":
            hide sd_angry
            show sd_happy at right

            sd "I know right?!"

    ys "Let’s get you to the nurses office, you might have gotten a concussion."

    show sd_neutral at right

    sd "But you're already late!"

    menu:
        "You’re much more important":
            show sd_blushing at right
            sd "O-oh"
            extend " T-thank you!"

        "Your right I need to get to class":
            show sd_angry at right
            
            # Change the text smaller for grumbling
            sd "I mean you could have been a little more persistent"

            ys "What was that?"

            hide sd_angry
            show sd_blushing at right

            sd "N-nothing!"

    jump first_day_scene_one

# Second scene school where they arrive after the 3 meeting scenarios
label first_day_scene_one:
    scene highschool_front with fade

    sim "After-school, Yuri Club meeting. The club of which you are president."

    ys "I can't wait to lead the Yuri Girl Love Manga Club to another year of resounding success."

    scene book_club with fade:
        xzoom 3.0 yzoom 3.0

    show ys_sprite at left

    show kh_neutral at right

    if day_one_chosen_variation == 1: 
        sim "Kaorin Womenlover, your junior and head of the Secret Yuri San Fanclub"
    elif day_one_chosen_variation == 3:
        sim "Kaorin Womenlover, your junior and head of the Secret Yuri San Fanclub"
    
    kh "Miss President I did so much Yuri research over the summer vacation!"

    menu:
        "I’d expect nothing less from you kaorin":
            hide kh_neutral
            show kh_blushing at right
            pause(1)

        "That’s some good dedication Kaorin. Keep at it and you’ll be leading this club after I graduate":
            hide kh_neutral
            show kh_sad at right

            kh "oh yeah"
            extend "Your leaving me behind"
            
            ys "you’ll be fine, its only for a year. You're going to the National Yuriversity too right?"

            hide kh_sad
            show kh_happy at right

            kh "I’m going wherever you are, miss yuri san!"
    
    hide kh_neutral
    hide kh_blushing
    show kh_neutral at right

    "*knock knock knock*"

    show sd_neutral at center

    sd "Hello Yuri-San. Hi Kaorin."

    if day_one_chosen_variation == 1:
        sim "Sune Derei, your short fused friend"
    elif day_one_chosen_variation == 2:
        sim "Sune Derei, your short fused friend"

    ys "Hey!"
    extend " Anyone seen Cere?"
    
    hide sd_neutral
    show sd_exclimation at center
    
    sd "Oh she told me that she’s putting her foot down this year, she wants nothing to do with the Yuri club."

    ys "she says that every year, I’ll go get her"

    scene bg school hallway with fade

    show ys_sprite at left
    show vc_neutral at right
    
    ys "Cere hurry up clubs starting"
    
    if day_one_chosen_variation == 2:
        sim "Cere Dunoshesgay, your childhood bestfriend and closest compatriot"
    elif day_one_chosen_variation == 3:
        sim "Cere Dunoshesgay, your childhood bestfriend and closest compatriot"

    hide vc_neutral
    show vc_angry at right

    vc "I keep telling you! I definitely have no interest in Yuri! I’m not coming!"

    ys "Okay okay but don’t you want to come say high to Sune and Kaorin?"

    hide vc_angry
    show vc_exclimation at right

    vc "Okay but I’m meeting them and leaving!"

    ys "Sure sure."

    scene book_club with fade:
        xzoom 3.0 yzoom 3.0

    show ys_sprite at left
    show vc_neutral at center

    show kh_neutral at right
    show sd_neutral:
        xalign 1.41

    kh "Hi Miss Cere!"

    sd "Where have you been?"

    vc "I don’t want to join this year, I’m just dropping in to say hi."
    extend "\nSo I guess I’ll be leaving now."

    ys "Can't. Doors locked."
    
    hide vc_neutral
    show vc_question

    vc "What??"

    ys "Door won't open, its locked."

    hide vc_question
    show vc_angry at center

    vc "Who has the key then?"

    ys "Uhh.."
    extend "KAORIN! WINDOW! NOW!"

    hide kh_neutral
    show kh_blushing at right

    scene bg window:
        xzoom 0.5 yzoom 2

    # Key flys here linux boy
    show key at Transform(xalign=0.0, yalign=0.5)
    with None

    show key at Transform(xalign=1.0, yalign=0.5)
    with move

    scene book_club with fade:
        xzoom 3.0 yzoom 3.0

    show ys_sprite at left
    show vc_angry at center

    show kh_neutral at right
    show sd_neutral:
        xalign 1.41

    ys "I actually have no idea where the key is really."

    vc "I knew you would do this!"
    extend " I don’t want to be in the Yuri club!" 
    extend "\nI’ve never wanted to be in the Yuri club!"

    menu:
        "How come you always have the most detailed book reports then?":
            hide vc_angry
            show vc_blushing at center
            
            vc "I just like literature!"

            ys "Uh-huh"
            extend " Anyway it’s not even like a serious club anyway, its more like a place to hang out"

            vc "That's what you always say!"
        
        "Please stay, it’ll be lonely without you":
            hide vc_angry
            show vc_blushing at center
            
            vc "I have to focus on my grades this year Yuri-San"

            hide vc_blushing
            show vc_sad at center

            extend "You know I need a scholarship for uni."

            ys " I swear I’ll tutor you if you stay"

            hide vc_sad
            show vc_happy at center

            vc "your going to do that anyway though"

    ys "Come onn"

    hide vc_sad
    hide vc_blushing
    show vc_angry at center

    vc "Fine!"

    ys "No new members this year either?" 

    hide vc_angry
    show vc_neutral at center

    hide kh_neutral
    show kh_sad at right

    kh "Afraid not"

    ys "Well I guess introductions are pointless then."
    extend " We need to fundraise for our annual Yuri Exhibit though. Any ideas?"

    hide kh_sad
    show kh_exclimation at right

    kh "We could do a bake sale!"

    sd "I guess I could donate some of my Yuri collection, and we could host a book sale."

    vc "I have work after school. Though my manager did mention she needs an extra pair of hands for this weekend."


    menu:
        "Prep a bake sale with Kaorin":
            ys "We should do a bake sale."
            extend " Me and Kaorin can bake the products and you two can help us sell them later"

            hide kh_exclimation
            show kh_blushing at right

            kh "T-thank you!"

            vc "Works for me"

            sd "Sure."
            
            $ chosen_sale_option = 1

        "Sort through Sune Derei’s Yuri collection":
            ys "A book sale sounds good"

            hide sd_neutral
            show sd_happy:
                xalign 1.41

            sd "Okay I’ll pick out some-"

            ys "Not a chance. I’m coming with you and picking them out myself"

            hide sd_happy
            show sd_angry:
                xalign 1.41

            sd "What?"

            vc "You have very.. Interesting taste"

            ys "We can’t sell your picks at a school event."

            sd "Fine!"

            $ chosen_sale_option = 2

        "Work part time with Cere":
            ys "I'll come help out at your job"

            $ chosen_sale_option = 3

    scene black with fade

    sim "would you like to proceed to the next day, or start over and try a different route?"

    menu:
        "Next Day":
            $day_number = 2
            jump start

        "Start over":
            sim "Are you sure?"
            menu:
                "Yes":
                    jump day_one_start

                "No end the day":
                    $day_number = 2
                    jump start
