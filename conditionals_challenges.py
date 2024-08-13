def can_climb(has_helmet: bool, has_rope: bool):
    """To go rock climbing, you need a helmet and some rope. This function 
    calculates whether you are able to go rock climbing.

    Arguments:
        - has_helmet: a boolean representing whether or not the climber has their helmet
        - has_rope: a boolean representing whether or not the climber has their rope

    Returns:
        - a boolean that is true when the climber is allowed to climb, and false otherwise.
    """
    can_climb = True
    cannot_climb = False

    if has_helmet and has_rope:
        return can_climb
    else: 
        return cannot_climb

def red_light_camera(light_colour: str, car_detected: bool):
    """A function to determine whether or not a driver should get a ticket 
    for running a red light.

    Arguments:
        - light_colour: a string representing the colour of the light. 
            Valid colours are "Red", "Amber", or "Green"
        - car_detected: a boolean representing whether or not a car 
            is driving through the intersection.

    Returns: A boolean that is true if a car ran the red light, and false otherwise.
    """
    get_ticket = True
    no_ticket = False
    if light_colour == 'Red' and car_detected:
         return get_ticket
    else:
        return no_ticket

def can_ride_rollercoaster(rider_height: float):
    """Only people who are over 120cm in height can ride the rollercoaster.
    
    Arguments:
        - rider_height: a float representing the height of the prospective rider in centimetres
        
    Returns: a boolean representing whether or not the prospective rider is allowed on the rollercoaster.
    """
    allowed_on = True
    not_allowed = False

    if rider_height > 120: 
        return allowed_on
    else:
        return not_allowed

def login(password: str):
    """Only users who enter the password "quartzgleam?1" can log in successfully.

    Arguments:
        - password: a string representing the user's password input.

    Returns:
        - a boolean representing whether or not the user's password was correct.
    """

    pass_correct = True
    pass_incorrect = False

    if password == 'quartzgleam?1':
        return pass_correct
    else:
        return pass_incorrect

print (can_climb(False, True))
print (can_ride_rollercoaster(121))
print (red_light_camera('Red', True))
print (login('quartzgleam?1'))