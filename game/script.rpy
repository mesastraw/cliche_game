default day_number = 1
# default points = 0 # Implement later on when we got time

label start:

    scene bg room

    if day_number == 1:
        jump day_one
    elif day_number == 2:
        jump day_two 
    elif day_number == 3:
        jump day_three
    elif day_number == 4:
        jump ending

    return
