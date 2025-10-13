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
    
    show planks at center
    
    show ys_sprite at left

    show sd_happy at right

    sd "Did you bring the screws?"

    ys "Yeah I bought all four!"
    extend " Wait a second, one"
    show screw_one at left
    extend " Two"
    show screw_two at left
    extend " Three"
    show screw_three at left

    hide sd_happy
    show sd_angry at right
    
    sd "did you lose a screw?"

    ys "uha"
    extend " Wait!"
    extend " Found it"
    show screw_fourth at left
    extend "We almost got screwed there"
    # Sound effect

    sd "Go die."
    "test"

    hide ys_sprite
    hide sd_angry

    show ys_sprite at center
    show sd_neutral at center
    show cloud at center

    # Play lego brick sound effect
    # Shake clouds
    
    hide ys_sprite
    hide sd_neutral
    hide planks
    hide cloud

    show table
    show ys_sprite at left
    show sd_happy at right

    ys "I think we’re ready for the book sale now."

    $ day_number = 3
    jump start

label work_route:
    "test"
