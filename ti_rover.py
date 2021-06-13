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
            print(errormsg_range(1, 13, "line"))
            return
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

def forward(distance:float):
    """
    Moves Rover forward the specified distance in grid units. 1 Grid Unit = 10cm.
    
    
    Category: Rover / Driving
    
    
    Returns an array / list: [grid_distance, distance]
    """
    try:
        float(distance)
    except ValueError:
        raise ValueError(errormsg_type("float", "distance")) from None
    if(distance > 2147483648 or distance < 0):
        print(errormsg_range(0, 2147483648, "distance"))
        return

    cm:float = distance * 10
    print("Moving the rover forward by '" + str(distance) + "' griduntis (" + str(cm) + ") cm")
    return [distance, cm]

###########################################################################################

def backward(distance:float):
    """
    Moves Rover backwards the specified distance in grid units. 1 Grid Unit = 10cm.
    
    
    Category: Rover / Driving
    
    
    Returns an array / list: [grid_distance, distance]
    """
    try:
        float(distance)
    except ValueError:
        raise ValueError(errormsg_type("float", "distance")) from None
    if(distance > 2147483648 or distance < 0):
        print(errormsg_range(0, 2147483648, "distance"))
        return

    cm:float = distance * 10
    print("Moving the rover backwards by '" + str(distance) + "' griduntis (" + str(cm) + ") cm")
    return [distance, cm]

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
        
