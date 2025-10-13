default day_number = 1
# default points = 0 # Implement later on when we got time

label start:
    scene bg room

    if day_number == 1:
        jump day_one
    elif day_number == 2:
        jump day_two_start 
    elif day_number == 3:
        jump ending

    return
