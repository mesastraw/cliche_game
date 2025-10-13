label day_two_start:
    show screen day_screen

    if chosen_sale_option == 1:
        jump bake_sale_route
    elif chosen_sale_option == 2:
        jump book_sale_route
    elif chosen_sale_option == 3:
        jump work_route


label bake_sale_route:
    scene kitchen:
        xzoom 4.1  yzoom 4

    show ys_sprite at left
    show kh_blushing at right
    
    kh "W-welcome to my house miss yuri san!"
    extend " Y-you can sit down, I- I'll bake all the banana bread!!"

    ys "No, no. we’ll work together."

    hide kh_blushing
    show kh_happy at right

    kh "Your so kind miss yuri san!"

    ys "Why banana bread though?"

    kh "I make very good banana bread!"

    ys "Mom’s secret recipe eh?"

    hide kh_happy
    show kh_question at right

    kh "huh?"

    hide kh_question
    show kh_exclimation at right

    extend "Oh! Did I not tell you?"

    ys "Tell me what?"

    kh "I don’t really have moms."

    menu:
        "I’m so sorry for your loss":
            kh "Their not dead or anything, I just never had any."
            
            ys "I don't understand?"

            kh "Have you heard of the tube company whose headquarters burnt down several years ago?"

            ys "I think I read about it once?"

            hide kh_exclimation
            show kh_sad at right

            kh "That was my birth company." 
            extend " A lot of records were lost in that fire, including my expected delivery date and my gene parents."

            kh "On top of that, by the time my incubation period was finished, the company had already filed for bankruptcy," 
            extend " and few remaining staff were overwhelmed by the workload."
            extend " Because of that I was taken out of my tube more than a year overdue."

            ys "Wait, so that means we’re the same age?"

            hide kh_sad
            show kh_happy at right

            kh "Yup!"

            hide kh_happy
            show kh_neutral at right
            
            kh "It took those poor employees another year to track down my gene donors, and in that time my moms-to-be had already ordered and received a different little girl."

            hide kh_neutral
            show kh_sad at right

            kh "They had no want for me. The employees took care of me until all of the company's loose ends were tied, which took several years"

        "What do you mean?":
            kh "Have you heard of the tube company whose headquarters burnt down several years ago?"

            ys "I think I read about it once?"

            hide kh_exclimation
            show kh_sad at right

            kh "That was my birth company." 
            extend " A lot of records were lost in that fire, including my expected delivery date and my gene parents."

            kh "On top of that, by the time my incubation period was finished, the company had already filed for bankruptcy," 
            extend " and few remaining staff were overwhelmed by the workload."
            extend " Because of that I was taken out of my tube more than a year overdue."

            ys "Wait, so that means we’re the same age?"

            hide kh_sad
            show kh_happy at right

            kh "Yup!"

            hide kh_happy
            show kh_neutral at right
            
            kh "It took those poor employees another year to track down my gene donors, and in that time my moms-to-be had already ordered and received a different little girl."

            hide kh_neutral
            show kh_sad at right

            kh "They had no want for me. The employees took care of me until all of the company's loose ends were tied, which took several years"

    ys "I don’t even know what to say"

    hide kh_sad
    show kh_happy at right

    kh "it’s okay, I can’t miss mothers I never had."

    ys "That's even worse."
    extend " Did you teach yourself to bake then?"

    kh "No actually, this recipe was the warehouse canteen's specialty though! The head chef lady always made me help her make it."

    ys "Isn’t that child labour?"

    kh "I thought so too, I used to hate having to work as a kid."
    extend " But now I think that was her way of making sure I could feed myself later on."

    menu:
        "Hey if you ever want a mom-cooked meal your welcome at my house":
            hide kh_happy
            show kh_blushing at right

            kh "M-meet your parents?!"
            extend " I-i’d be honored!"

        "You must be a really good cook then":
            kh "I guess we’ll find out!"

    ys "Well, for now I think 6 pounds of banana bread should be enough."

    hide kh_blushing
    hide kh_happy
    show kh_question at right

    kh "Why 6?"
    
    ys "5 for the bake sale, one for me."

    hide kh_question
    show kh_happy at right

    kh "Okei Dokei!"
    
    $ day_number = 3
    jump start

label book_sale_route:
    scene goon_shelf

    show ys_sprite at left
    show sd_neutral at right

    ys "How do your parents let you live like this?"

    hide sd_neutral
    show sd_angry at right

    sd "What are you implying"

    menu:
        "These posters are concerning.":
            ys "These posters are concerning."
            extend " Is that a child???"
            
            sd "She's five thousand years old actually"

            ys "Of course she is."


        "I wish my parents let me put up posters like these":
            ys "I wish my parents let me put up posters like these"

            hide sd_angry
            show sd_happy at right

            sd "They're pretty cool aren’t they?"

    hide sd_happy
    hide sd_angry

    show sd_neutral at right

    ys "So what are we taking?"

    sd "I have some old timey classics, like “Asumi Chan is Interested in Lesbian Brothels”"

    ys "Yeah so we're not taking that."

    sd "How about “My Sisters Daughter”"

    ys "Nope."

    sd "Surely we can bring “Cat Maid and Mistress”"

    ys "How about you let me sort through them?"

    hide sd_neutral
    show sd_angry at right

    sd "Fine!"

    ys "Oh Madoka Magica! We can take that for sure."

    sd "Everyone already knows Madoka Magica though!"

    ys "I’m sure it’ll be fine."
    extend " “Shy Girl Handsome Girl” thats coming too"
    extend " “The Guy She Was Interested in Wasn't a Guy at All”"
    extend " Actually most of this section is fine!"
    
    sd "How come you're only taking the mainstream ones?"

    ys "I mean we do have to sell these, catering to the largest demographic should help with that."

    sd "Ugh, Lame."

    ys "Anyway this is only half the job."

    hide sd_angry
    show sd_question at right

    ys "we also need to build a table to display them on."

    hide sd_question
    show sd_exclimation at right

    ys "the planks are outside, I brought them with me."

    scene house_front with fade:
        xzoom 3.14 yzoom 2.6
    
    show planks at center:
        zoom 5
    
    show ys_sprite at left

    show sd_happy at right

    sd "Did you bring the screws?"

    ys "Yeah I bought all four!"
    show three_screws_test at left

    extend " Wait a second, one"
    extend " Two"
    extend " Three"

    hide sd_happy
    show sd_angry at right
    
    sd "did you lose a screw?"

    ys "uha"
    extend " Wait!"
    extend " Found it"
    hide three_screws_test
    show four_screws_test at left
    extend " We almost got screwed there"
    # Sound effect

    sd "Go die."

    # Play lego brick sound effect
    # Shake clouds
    
    scene house_front with fade:
        xzoom 3.14 yzoom 2.6

    show table

    show ys_sprite at left
    show sd_happy at right

    ys "I think we’re ready for the book sale now."

    $ day_number = 3
    jump start

label work_route:
    scene cafe:
        xzoom 3.0 yzoom 2.0

    show ys_apron at left
    show vc_neutral_apron at right
    
    ys "you never told me you worked at a maid cafe!"

    hide vc_neutral_apron
    show vc_angry_apron at right

    vc "because I dont work at a maid cafe. This is a regular cafe."

    ys "whatever you say.."
    
    vc "We’re not even wearing maid outfits!"

    menu:
        "What a shame..":
            ys "What a shame.."

            hide vc_angry_apron
            show vc_blushing_apron at right

            vc "Whats that supposed to mean??"
            
            menu:

                "I’d love to see you in a maid outfit":
                    vc "Hu-Whu- "
                    extend " Shut up! We have customers!"

                "Oh look! Customers!":
                    pass

        "Uh-huh":
            vc "Whatever!"
            extend " We've got customers"

    hide vc_angry_apron
    hide vc_blushing_apron
    show vc_happy_apron at right
    
    vc "Hi! What can I get for you?"
    
    scene break_room with fade:
        xzoom 2.7 yzoom 2.0

    show ys_apron at left
    show vc_sad_apron at right

    vc "Since when is 6 PM rush hour??"


    menu:
        "You call that rush hour?":
            ys " You call that rush hour? Hah."

            hide vc_sad_apron
            show vc_angry_apron at right

            vc "I am going to physically assault you."

            ys "I think the employee handbook says thats not allowed"

        "Really needed this break":
            ys "It’s crazy out there. I really needed this break."

            vc "tell me about it."
        
    hide vc_angry_apron
    show vc_neutral_apron at right

    vc "I can’t wait to get out of here.."

    ys "Our shift ends at eight right?"

    vc "No I don’t mean out of work"
    extend " I mean like out of this city, this country."

    menu:
        "Why?":
            ys "What? Why? It’s great here!"

            hide vc_neutral_apron
            show vc_angry_apron at right

            vc "For you maybe. All anyone ever talks about is yuri here. I mean for god sake, its literally your NAME. It pisses me off."
            
            ys "Yuri pisses you off?"
            extend " Why?"

            vc "You know my Moms a POS right?"

            ys "Which one?"

            vc "I only have one. That other witch’s blood doesn’t run through my veins."

            ys "That’s a pretty harsh thing to say about your stepmom."

            vc "I told you that harlot is not my mother! She’s just Mom’s latest replacement for Dad."

        "I’m coming with you":
            hide vc_neutral_apron
            show vc_blushing_apron at right

            vc "what? Why??"

            ys "I’ll go wherever you go."

            vc "whats that supposed to mean?"

            ys "you’ll understand when your older."

            vc "I don’t like women like that Yuri-San."

            ys "For now.."

            hide vc_blushing_apron
            show vc_angry_apron at right

            vc "No! Forever! I’m not going to end up like Mom."


    hide vc_angry_apron
    show vc_sad_apron at right

    vc "You know after Dad died and we decided to move to Yuristan, I was actually pretty excited."
    extend " I’d finally get to get away from all those memories"
    extend " I could start anew "

    vc "But Mom started anew as well. Every week it was a new woman. I was too small to understand, but she was throwing all our money at “companions”"
    extend " We were never rich, but by the time I was old enough to understand that none of these women were ever meant to be an actual stepmom," 
    extend " my mom was working two different jobs, just to keep going on more dates, while I went hungry at home."

    hide vc_sad_apron
    show vc_angry_apron at right

    vc "Yuri fucking ruined my life."
    extend " For some reason, maybe because it was WLW, my mom couldn’t see just how pathetic she was. Nor could anyone else."
    extend " Aunts and cousins would all tell me that my mom was just “finding herself” and that I needed to give her time."
    extend " All while I sat at their table eating my first actual meal in days. I learnt to nod my head and agree, because it always meant there was a next time, it kept me fed."

    vc "But I knew, even as a kid, I knew my Mom was lost. And she definitely couldn’t “find herself”"
    extend "  don’t think I could find her either."

    menu:
        "Can you really blame Yuri for that?":
            vc "What else am I supposed to blame??"
            extend " I have to get perfect grades while working two part time jobs, just so I can make it to University on a scholarship!"
            extend "Who do I blame? What do I hold accountable?"
            
            ys "Try letting go."
            extend " You're already fighting an uphill battle. The weight of your hatred, of your anger won't make it easier. Anger never lifts anything up Cere, it only weighs it down."

            hide vc_angry_apron
            show vc_sad_apron at right

            extend " And sure, extra weight is helpful when you're rolling downhill, when you're destroying things, but that isn’t what you're trying to do."

            vc "I don’t know. Maybe you're right. Maybe I’m holding on to something I don’t need. But I don’t know if I can let go. Not just yet."

        "I don’t know why your mom did what she did. But I know you, I know you could never end up like her":
            ys "I can’t defend your mom. I don't know why she did what she did. But I know that you aren’t like her."
            extend " I know you could never do something like that. And you should know that if you were ever lost, If you were ever unable to find yourself, I would come find you."

            hide vc_angry_apron
            show vc_sad_apron at right

            vc "I can’t believe you. Not yet."


    ys "I’ll wait. As long as it takes."

    hide vc_sad_apron
    show vc_happy_apron at right
    
    vc "I know you will."
    extend " Thank you."

    ys "By the way how much are we getting paid for this?"

    vc " Let’s see.."
    extend " Ten Yuribucks an hour, for five hours, multiplied by two.."
    extend " Around 100 Yuribucks."
    
    ys "Good god, someone needs to boost the minimum wage."

    vc "Tell me about it"

    jump ending
