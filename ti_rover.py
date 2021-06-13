"""
Class containing all TI-Rover commands. Used for debugging
"""



def errormsg_type(requiredDataType: str, parameter: str):
    msg = "ERROR: Parameter <" + parameter + \
        "> has to be data-type " + requiredDataType + "!"
    return msg


def errormsg_range(rangeMin: float, rangeMax: float, parameter: str):
    msg = "ERROR: Parameter <" + parameter + \
        "> has to be in range between " + str(rangeMin) + " and " + str(rangeMax) + "!"
    return msg

###########################################################################################

def text_at(line: int, text: str, align: str):
    """
    Displays text at the given line (ranging between 1 and 13) and with the given alignment ('left' or 'center' or 'right').


    Category: Rover / Miscellaneous


    Returns an array / list: [text, line, align]
    """
    try:
        int(line)
    except ValueError:
        raise ValueError(errormsg_type("int", "line")) from None

    try:
        str(text)
    except ValueError:
        raise ValueError(errormsg_type("str", "text")) from None

    try:
        str(align)
    except ValueError:
        raise ValueError(errormsg_type("str", "align")) from None

    if(align == "left" or align == "center" or align == "left"):
        if(line > 0 and line < 14):
            print("Showing text '" + text + "' at line " +
                  str(line) + " with alignement '" + align + "' !")
            return [text, line, align]
        else:
            raise ValueError(errormsg_range(1, 13, "line"))
            
    else:
        print("ERROR: Paramteter <align> can only be 'left' or 'right' or 'center'!")
        return

###########################################################################################

def sleep(seconds: float):
    """
    Waits for the given amount of time in seconds, until the script continues to run.


    Category: Rover / Miscellaneous


    Returns an array / list: [seconds]
    """
    try:
        float(seconds)
    except ValueError:
        raise ValueError(errormsg_type("float", "seconds")) from None

    if(seconds > 0):
        print("Waiting for " + str(seconds) + " seconds")
        return [seconds]
    else:
        print("ERROR: Parameter <seconds> has to be greater then 0!")
        return

###########################################################################################

def get_key():
    """
    Gets the pressed key.


    Category: Rover / Miscellaneous


    Returns None
    """
    print("Getting Pressed key")
    return None

###########################################################################################

def cls():
    """
    Clears all currently displayed content from the screen / display.


    Category: Rover / Miscellaneous


    Returns None
    """
    print("Clearing screen / display")
    return None


###########################################################################################

def forward(distance:float, distance_unit:str = "units", speed:float = 1, speed_unit:str = "units/s"):
    """
    Moves Rover forward by the specified distance in in the given unit (optional). If given, the speed and the speed unit will be as specified.

    Note: If you set the speed, you HAVE to set speed_unit! Otherwise, this might cause ERRORS!


    Default Values: distance_unit: units; speed: 1; speed_unit: units/s
    
    
    Category: Rover / Driving
    
    
    Returns an array / list: [distance, distance_unit, speed, speed_unit]
    """
    try:
        float(distance)
    except ValueError:
        raise ValueError(errormsg_type("float", "distance")) from None
    try:
        str(distance_unit)
    except ValueError:
        raise ValueError(errormsg_type("str", "distance_unit")) from None
    try:
        float(speed)
    except ValueError:
        raise ValueError(errormsg_type("float", "speed")) from None
    try:
        str(speed_unit)
    except ValueError:
        raise ValueError(errormsg_type("str", "speed_unit")) from None
    
    if(distance > 2147483648 or distance < 0):
        raise ValueError(errormsg_range(0, 2147483648, "distance"))
    
    if(speed > 10 or speed < 0.1):
        raise ValueError(errormsg_range(0.1, 10, "speed"))

    if(distance_unit == "units" or distance_unit == "m" or distance_unit == "revs"):

        if(speed_unit == "units/s" or speed_unit == "m/s" or speed_unit == "revs/s"):

            print("Moving Rover forward by '" + str(distance) + distance_unit + "' with a speed of '" + str(speed) + speed_unit + "'")
            return [distance, distance_unit, speed, speed_unit]
        
        else:
            raise ValueError("ERROR: Parameter <speed_unit> has to be one of these: 'units/s', 'm/s', 'revs/s'")
    else:
        raise ValueError("ERROR: Parameter <distance_units> has to be one of these: 'units', 'm', 'revs'")

###########################################################################################

def backward(distance:float, distance_unit:str = "units", speed:float = 1, speed_unit:str = "units/s"):
    """
    Moves Rover backward by the specified distance in in the given unit (optional). If given, the speed and the speed unit will be as specified.

    Note: If you set the speed, you HAVE to set speed_unit! Otherwise, this might cause ERRORS!


    Default Values: distance_unit: units; speed: 1; speed_unit: units/s
    
    
    Category: Rover / Driving
    
    
    Returns an array / list: [distance, distance_unit, speed, speed_unit]
    """
    try:
        float(distance)
    except ValueError:
        raise ValueError(errormsg_type("float", "distance")) from None
    try:
        str(distance_unit)
    except ValueError:
        raise ValueError(errormsg_type("str", "distance_unit")) from None
    try:
        float(speed)
    except ValueError:
        raise ValueError(errormsg_type("float", "speed")) from None
    try:
        str(speed_unit)
    except ValueError:
        raise ValueError(errormsg_type("str", "speed_unit")) from None
    
    if(distance > 2147483648 or distance < 0):
        raise ValueError(errormsg_range(0, 2147483648, "distance"))
    
    if(speed > 10 or speed < 0.1):
        raise ValueError(errormsg_range(0.1, 10, "speed"))

    if(distance_unit == "units" or distance_unit == "m" or distance_unit == "revs"):

        if(speed_unit == "units/s" or speed_unit == "m/s" or speed_unit == "revs/s"):

            print("Moving Rover backwards by '" + str(distance) + distance_unit + "' with a speed of '" + str(speed) + speed_unit + "'")
            return [distance, distance_unit, speed, speed_unit]
        
        else:
            raise ValueError("ERROR: Parameter <speed_unit> has to be one of these: 'units/s', 'm/s', 'revs/s'")
    else:
        raise ValueError("ERROR: Parameter <distance_units> has to be one of these: 'units', 'm', 'revs'")


###########################################################################################

def left(degrees:float):
    """
    Turns the rover left by the specified amount of degrees
    
    
    Category: Rover / Driving
    
    
    Returns an array / list: [degrees]
    """
    try:
        float(degrees)
    except ValueError:
        raise ValueError(errormsg_type("float", "degrees")) from None
    print("Turning rover left by '" + str(degrees) + "' degrees")
    return [degrees]

###########################################################################################

def right(degrees:float):
    """
    Turns the rover right by the specified amount of degrees
    
    
    Category: Rover / Driving
    
    
    Returns an array / list: [degrees]
    """
    try:
        float(degrees)
    except ValueError:
        raise ValueError(errormsg_type("float", "degrees")) from None
    print("Turning rover right by '" + str(degrees) + "' degrees")
    return [degrees]

###########################################################################################

def stop():
    """
    Stops any current movement immediately. Pending commands will be executed.
    
    
    Category: Rover / Driving
    
    
    Returns None
    """
    print("Stopping Rover Movement")
    return None

###########################################################################################

def stop_clear():
    """
    Stops any current movement immediately. Pending commands will cleared.
    
    
    Category: Rover / Driving
    
    
    Returns None
    """
    print("Stopping Rover Movement and clearing all pending commands")
    return None

###########################################################################################

def resume():
    """
    Resumes the processing of commands, that are pending.
    
    
    Category: Rover / Driving
    
    
    Returns None
    """
    print("Resuming Rover Movement")
    return None

###########################################################################################

def stay(time:int=30):
    """
    Rover stays in place for the specified amount of time in seconds (optional). If no time is specified, the Rover stays for 30 seconds
    
    
    Category: Rover / Driving
    
    
    Returns an array / list: [degrees]
    """
    try:
        int(time)
    except ValueError:
        raise ValueError(errormsg_type("int", "time")) from None
    print("Rover stays at current location for '" + str(time) + "' seconds")
    return [time]

###########################################################################################

def to(x:float, y:float):
    """
    Moves Rover to coordinate position (x,y) on virtual grid. Distance in GridUnits.
    
    
    Category: Rover / Driving
    
    
    Returns an array / list: [x (gridUnits), y (gridUnits), x (cm), y (cm)]
    """
    try:
        float(x)
    except ValueError:
        raise ValueError(errormsg_type("float", "x")) from None
    try:
        float(y)
    except ValueError:
        raise ValueError(errormsg_type("float", "y")) from None
    
    print("Rover moves to '(" + str(x) + " | " + str(y) + ")' on the virtual grid.")
    return [x, y, x*10, y*10]

###########################################################################################

def to_polar(radius:float, theta_degrees:float):
    """
    Moves Rover to polar coordinate position (r, theta) on virtual grid. The angle is specified in degrees.
    
    
    Category: Rover / Driving
    
    
    Returns an array / list: [radius, theta_degrees]
    """
    try:
        float(radius)
    except ValueError:
        raise ValueError(errormsg_type("float", "radius")) from None
    try:
        float(theta_degrees)
    except ValueError:
        raise ValueError(errormsg_type("float", "theta_degrees")) from None
    
    print("Rover moves to polar with radius '" + str(radius) + "' and '" + str(theta_degrees) + "' degrees")
    return [radius, theta_degrees]

###########################################################################################

def to_angle(degrees:float, unit:str):
    """
    Spins Rover to the specified angle in the virtual grid. The angle is relative to a zero angle which points down the x-axis in the virtual grid.


    Valid Units: 'degrees', 'radians', 'gradians'
    
    
    Category: Rover / Driving
    
    
    Returns an array / list: [degrees, unit]
    """
    try:
        float(degrees)
    except ValueError:
        raise ValueError(errormsg_type("float", "degrees")) from None
    try:
        str(unit)
    except ValueError:
        raise ValueError(errormsg_type("str", "unit")) from None
    
    if(unit == "degrees" or unit == "radians" or unit == "gradians"):
        print("Rover turns by angle '" + str(degrees) + "' with unit type '" + unit + "' degrees")
        return [degrees, unit]
    else:
        raise ValueError("Parameter <unit> can only be 'degrees', 'radians', 'gradians'")
        
###########################################################################################

def backward_time(time:float, speed:float = 1, unit:str = "units/s"):
    """
    Moves Rover backward for the specified time at the specified speed. The speed can be specified in grid units/s, meters/s, or wheel revolutions/s.\n
    Valid Arguments for <unit>: 'units/s', 'm/s', 'revs/s'


    Default Values: speed = 1; unit = units/s
    
    
    Category: Rover / Driving / Driving With Options
    
    
    Returns an array / list: [time, speed, unit]
    """

    try:
        float(time)
    except ValueError:
        raise ValueError(errormsg_type("float", "time")) from None
    try:
        float(speed)
    except ValueError:
        raise ValueError(errormsg_type("float", "speed")) from None
    try:
        str(unit)
    except ValueError:
        raise ValueError(errormsg_type("str", "unit")) from None

    if(time > 100 or time < 0.1):
        raise ValueError(errormsg_range(0.1, 100, "time"))
    if(speed > 10 or speed < 0.1):
        raise ValueError(errormsg_range(0.1, 10, "speed"))
    if(unit == "units/s" or unit == "m/s" or unit == "revs/s"):
        print("Moving the rover backwards for '" + str(time) + "' seconds with a speed of '" + str(speed) + unit + "'")
        return [time, speed, unit]
    else:
        raise ValueError("ERROR: Parameter <unit> can only be one of these: 'units/s', 'm/s', 'revs/s'")

###########################################################################################

def forward_time(time:float, speed:float = 1, unit:str = "units/s"):
    """
    Moves Rover forward for the specified time at the specified speed. The speed can be specified in grid units/s, meters/s, or wheel revolutions/s.\n
    Valid Arguments for <unit>: 'units/s', 'm/s', 'revs/s'


    Default Values: speed = 1; unit = units/s
    
    
    Category: Rover / Driving / Driving With Options
    
    
    Returns an array / list: [time, speed, unit]
    """

    try:
        float(time)
    except ValueError:
        raise ValueError(errormsg_type("float", "time")) from None
    try:
        float(speed)
    except ValueError:
        raise ValueError(errormsg_type("float", "speed")) from None
    try:
        str(unit)
    except ValueError:
        raise ValueError(errormsg_type("str", "unit")) from None

    if(time > 100 or time < 0.1):
        raise ValueError(errormsg_range(0.1, 100, "time"))
    if(speed > 10 or speed < 0.1):
        raise ValueError(errormsg_range(0.1, 10, "speed"))
    if(unit == "units/s" or unit == "m/s" or unit == "revs/s"):
        print("Moving the rover forwards for '" + str(time) + "' seconds with a speed of '" + str(speed) + unit + "'")
        return [time, speed, unit]
    else:
        raise ValueError("ERROR: Parameter <unit> can only be one of these: 'units/s', 'm/s', 'revs/s'")

