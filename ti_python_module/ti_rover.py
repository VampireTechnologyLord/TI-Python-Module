"""
Class containing all TI-Rover commands. Used for debugging
"""
from ti_python_module.err import withConsole as err
from ti_python_module.err import onlyCheck as cerr
from ti_python_module.file_handler import create_log as log


###########################################################################################

def text_at(line: int, text: str, align: str):
    """
    Displays "text" in plotting area at specified "align".

    Args:
        line (int): The line of the text. Possible Options: 'line, 'text', 'align'.
        text (str): The text of the displayed text.
        align (str): The texts alignment. Possible Options: 'left', 'center', 'right'.

    Returns:
        list: list: list: a list containing the following data: [line, text, align]
    """

    if cerr.type_error(int, line) == False: log("Argument 'line' has to be type integer!", "ERROR", "TI Hub", "Text At")
    if cerr.type_error(str, text) == False: log("Argument 'text' has to be type string!", "ERROR", "TI Hub", "Text At")
    if cerr.type_error(str, align) == False: log("Argument 'align' has to be type string!", "ERROR", "TI Hub", "Text At")
    if cerr.argument_error(align, "left", "center", "right") == False: log("Argument 'align' can only be one of these: 'left', 'center', 'right'!", "ERROR", "TI Hub", "Text At")
    if cerr.range_error(1, 13, line) == False: log("Argument 'line' has to be between the values 1 and 13 (included)!", "ERROR", "TI Hub", "Text At")


    err.type_error(int, "int", line)
    err.type_error(str, "str", text)
    err.type_error(str, "str", align)
    err.argument_error(align, "left", "center", "right")
    err.range_error(1, 13, line)

    log("Showing text '" + text + "' at line " + str(line) + " with alignment '" + align + "'", "INFO", "TI Hub", "Text At")
    print("Showing text '" + text + "' at line " + str(line) + " with alignment '" + align + "'")
    return [text, line, align]


###########################################################################################

def sleep(seconds: float):
    """
    Waits for the given amount of time in seconds, until the script continues to run.

    Args:
        seconds (float): The amount of seconds to wait.

    Returns:
        list: a list containing the following data: [seconds]
    """
    if cerr.type_error(float, seconds) == False: log("Argument 'seconds' has to be type float!", "ERROR", "TI Hub", "Sleep")

    if cerr.range_error(0, None, seconds) == False: log("Argument 'seconds' has to be larger then 0!", "ERROR", "TI Hub", "Sleep")

    err.type_error(float, "float", seconds)

    err.range_error(0, None, seconds)

    log("Waiting for '" + str(seconds) + "' seconds", "INFO", "TI Hub", "Sleep")
    print("Waiting for " + str(seconds) + " seconds")
    return [seconds]


###########################################################################################

def get_key():
    """
    Gets the pressed key.

    Returns:
        string: the pressed key
    """
    key = input("Requesting Key input: ")
    log("Got key '" + key + "' from user input", "INFO", "TI Hub", "Get Key")
    return key

###########################################################################################

def cls():
    """
    Clears the plotting canvas.

    Returns:
        None: None
    """
    print("Clearing screen / display")
    log("Clearing the display / screen", "INFO", "TI Hub", "Clear Screen")
    return None

###########################################################################################

def forward(distance:float, distance_unit:str = None, speed:float = None, speed_unit:str = None):
    """
    Moves Rover forward by the specified distance in in the given unit (optional). If given, the speed and the speed unit will be as specified. Note: If you set the speed, you HAVE to set speed_unit! Otherwise, this will cause errors.

    Args:
        distance (float): The distance to drive.
        distance_unit (str, optional): The distance unit to drive. Possible Options: 'units', 'm', 'revs'. Defaults to None.
        speed (float, optional): The speed to drive. Also needs `speed_unit` to be specified. Defaults to None.
        speed_unit (str, optional): The speed unit. Possible Options: 'units/s', 'm/s', 'revs/s'. Defaults to None.

    Raises:
        ValueError: If the speed is set, but not the speed unit.

    Returns:
        list: a list containing the following values: [distance, distance_unit, speed, speed_unit]
    """
    if(distance_unit == None and speed == None and speed_unit == None):
        if cerr.type_error(float, distance) == False: log("Argument 'distance' has to be type float!", "ERROR", "TI Rover", "Forward")
        if cerr.range_error(0, None, distance) == False: log("Argument 'distance' has to be greater then 0!", "ERROR", "TI Rover", "Forward")

        err.type_error(float, "float", distance)
        err.range_error(0, None, distance)

        log("Moving the Rover forward by '" + str(distance) + "'", "INFO", "TI Rover", "Forward")
        print("Moving Rover forward by '" + str(distance) + "'")
        return [distance, distance_unit, speed, speed_unit]

    elif(distance_unit != None and speed == None and speed_unit == None):

        if cerr.type_error(float, distance) == False: log("Argument 'distance' has to be type float!", "ERROR", "TI Rover", "Forward")
        if cerr.type_error(str, distance_unit) == False: log("Argument 'distance_unit' has to be type string!", "ERROR", "TI Rover", "Forward")
        if cerr.range_error(0, None, distance) == False: log("Argument 'distance' has to be greater then 0!", "ERROR", "TI Rover", "Forward")
        if cerr.argument_error(distance_unit, "units", "m", "revs") == False: log("Argument 'distance_unit' has to be one of these: 'units', 'm', 'revs'!", "ERROR", "TI Rover", "Forward")

        err.type_error(float, "float", distance)
        err.type_error(str, "str", distance_unit)
        err.range_error(0, None, distance)
        err.argument_error(distance_unit, "units", "m", "revs")

        log("Moving the rover forward by '" + str(distance) + " " + distance_unit + "'", "INFO", "TI Rover", "Forward")
        print("Moving Rover forward by '" + str(distance) + " " + distance_unit + "'")
        return [distance, distance_unit, speed, speed_unit]

    elif(distance_unit != None and speed != None and speed_unit != None):

        if cerr.type_error(float, distance) == False: log("Argument 'distance' has to be type float!", "ERROR", "TI Rover", "Forward")
        if cerr.type_error(str, distance_unit) == False: log("Argument 'distance_unit' has to be type string!", "ERROR", "TI Rover", "Forward")
        if cerr.type_error(float, speed) == False: log("Argument 'speed' has to be type float!", "ERROR", "TI Rover", "Forward")
        if cerr.type_error(str, speed_unit) == False: log("Argument 'speed_unit' has to be type string!", "ERROR", "TI Rover", "Forward")
        if cerr.range_error(0, None, distance) == False: log("Argument 'distance' has to be greater then 0!", "ERROR", "TI Rover", "Forward")
        if cerr.range_error(0.1, 10, speed) == False: log("Argument 'speed' has to be between the values 0.1 and 10!", "ERROR", "TI Rover", "Forward")
        if cerr.argument_error(speed_unit, "units/s", "m/s", "revs/s") == False: log("Argument 'speed_unit' has to be one of these: 'units/s', 'm/s', 'revs/s'", "ERROR", "TI Rover", "Forward")
        if cerr.argument_error(distance_unit, "units", "m", "revs") == False: log("Argument 'distance_unit' has to be one of these: 'units', 'm', 'revs'!", "ERROR", "TI Rover", "Forward")


        err.type_error(float, "float", distance)
        err.type_error(str, "str", distance_unit)
        err.type_error(float, "float", speed)
        err.type_error(str, "str", speed_unit)
        err.range_error(0, None, distance)
        err.range_error(0.1, 10, speed)
        err.argument_error(distance_unit, "units", "m", "revs")
        err.argument_error(speed_unit, "units/s", "m/s", "revs/s")

        log("Moving the Rover forward by '" + str(distance) + " " + distance_unit + "' with a speed of '" + str(speed) + " " + speed_unit + "'", "INFO", "TI Rover", "Forward")
        print("Moving Rover forward by '" + str(distance) + " " + distance_unit + "' with a speed of '" + str(speed) + " " + speed_unit + "'")
        return [distance, distance_unit, speed, speed_unit]

    else:
        raise ValueError("ERROR: You have to set both 'speed' and 'speed_unit' in order to set one of these!")
        


###########################################################################################

def backward(distance:float, distance_unit:str = None, speed:float = None, speed_unit:str = None):
    """
    Moves Rover backwards by the specified distance in in the given unit (optional). If given, the speed and the speed unit will be as specified. Note: If you set the speed, you HAVE to set speed_unit! Otherwise, this will cause errors.

    Args:
        distance (float): The distance to drive.
        distance_unit (str, optional): The distance unit to drive. Possible Options: 'units', 'm', 'revs'. Defaults to None.
        speed (float, optional): The speed to drive. Also needs `speed_unit` to be specified. Defaults to None.
        speed_unit (str, optional): The speed unit. Possible Options: 'units/s', 'm/s', 'revs/s'. Defaults to None.

    Raises:
        ValueError: If the speed is set, but not the speed unit.

    Returns:
        list: a list containing the following values: [distance, distance_unit, speed, speed_unit]
    """
    if(distance_unit == None and speed == None and speed_unit == None):
        if cerr.type_error(float, distance) == False: log("Argument 'distance' has to be type float!", "ERROR", "TI Rover", "Backward")
        if cerr.range_error(0, None, distance) == False: log("Argument 'distance' has to be greater then 0!", "ERROR", "TI Rover", "Backward")

        err.type_error(float, "float", distance)
        err.range_error(0, None, distance)

        log("Moving the Rover backwards by '" + str(distance) + "'", "INFO", "TI Rover", "Backward")
        print("Moving Rover backwards by '" + str(distance) + "'")
        return [distance, distance_unit, speed, speed_unit]

    elif(distance_unit != None and speed == None and speed_unit == None):

        if cerr.type_error(float, distance) == False: log("Argument 'distance' has to be type float!", "ERROR", "TI Rover", "Backward")
        if cerr.type_error(str, distance_unit) == False: log("Argument 'distance_unit' has to be type string!", "ERROR", "TI Rover", "Backward")
        if cerr.range_error(0, None, distance) == False: log("Argument 'distance' has to be greater then 0!", "ERROR", "TI Rover", "Backward")
        if cerr.argument_error(distance_unit, "units", "m", "revs") == False: log("Argument 'distance_unit' has to be one of these: 'units', 'm', 'revs'!", "ERROR", "TI Rover", "Backward")

        err.type_error(float, "float", distance)
        err.type_error(str, "str", distance_unit)
        err.range_error(0, None, distance)
        err.argument_error(distance_unit, "units", "m", "revs")

        log("Moving the rover backwards by '" + str(distance) + " " + distance_unit + "'", "INFO", "TI Rover", "Backward")
        print("Moving Rover backwards by '" + str(distance) + " " + distance_unit + "'")
        return [distance, distance_unit, speed, speed_unit]

    elif(distance_unit != None and speed != None and speed_unit != None):

        if cerr.type_error(float, distance) == False: log("Argument 'distance' has to be type float!", "ERROR", "TI Rover", "Backward")
        if cerr.type_error(str, distance_unit) == False: log("Argument 'distance_unit' has to be type string!", "ERROR", "TI Rover", "Backward")
        if cerr.type_error(float, speed) == False: log("Argument 'speed' has to be type float!", "ERROR", "TI Rover", "Backward")
        if cerr.type_error(str, speed_unit) == False: log("Argument 'speed_unit' has to be type string!", "ERROR", "TI Rover", "Backward")
        if cerr.range_error(0, None, distance) == False: log("Argument 'distance' has to be greater then 0!", "ERROR", "TI Rover", "Backward")
        if cerr.range_error(0.1, 10, speed) == False: log("Argument 'speed' has to be between the values 0.1 and 10!", "ERROR", "TI Rover", "Backward")
        if cerr.argument_error(speed_unit, "units/s", "m/s", "revs/s") == False: log("Argument 'speed_unit' has to be one of these: 'units/s', 'm/s', 'revs/s'", "ERROR", "TI Rover", "Backward")
        if cerr.argument_error(distance_unit, "units", "m", "revs") == False: log("Argument 'distance_unit' has to be one of these: 'units', 'm', 'revs'!", "ERROR", "TI Rover", "Backward")


        err.type_error(float, "float", distance)
        err.type_error(str, "str", distance_unit)
        err.type_error(float, "float", speed)
        err.type_error(str, "str", speed_unit)
        err.range_error(0, None, distance)
        err.range_error(0.1, 10, speed)
        err.argument_error(distance_unit, "units", "m", "revs")
        err.argument_error(speed_unit, "units/s", "m/s", "revs/s")

        log("Moving the Rover backwards by '" + str(distance) + " " + distance_unit + "' with a speed of '" + str(speed) + " " + speed_unit + "'", "INFO", "TI Rover", "Backward")
        print("Moving Rover backwards by '" + str(distance) + " " + distance_unit + "' with a speed of '" + str(speed) + " " + speed_unit + "'")
        return [distance, distance_unit, speed, speed_unit]

    else:
        raise ValueError("ERROR: You have to set both 'speed' and 'speed_unit' in order to set one of these!")
        
###########################################################################################

def left(degrees:float):
    """
    Turns the rover left by the specified amount of degrees.

    Args:
        degrees (float): The angle to turn left.

    Returns:
        list: a list containing the following data: [degrees]
    """

    if cerr.type_error(float, degrees) == False: log("Argument 'degrees' has to be type float", "ERROR", "TI Rover", "Left")
    err.type_error(float, "float", degrees)

    log("Turning the rover left by '" + str(degrees) + "' degrees", "INFO", "TI Rover", "Left")
    print("Turning rover left by '" + str(degrees) + "' degrees")
    return [degrees]

###########################################################################################

def right(degrees:float):
    """
    Turns the rover right by the specified amount of degrees.

    Args:
        degrees (float): The angle to turn right.

    Returns:
        list: a list containing the following data: [degrees]
    """

    if cerr.type_error(float, degrees) == False: log("Argument 'degrees' has to be type float", "ERROR", "TI Rover", "Right")
    err.type_error(float, "float", degrees)

    log("Turning the rover right by '" + str(degrees) + "' degrees", "INFO", "TI Rover", "Right")
    print("Turning rover right by '" + str(degrees) + "' degrees")
    return [degrees]
###########################################################################################

def stop():
    """
    Stops any current movement immediately. Pending commands will be executed.

    Returns:
        None: None
    """
    log("Stopping Rover Movement. Pending commands will be executed", "INFO", "TI Rover", "Stop")
    print("Stopping Rover Movement")
    return None

###########################################################################################

def stop_clear():
    """
    Stops any current movement immediately. Pending commands will cleared.

    Returns:
        None: None
    """
    log("Stopping Rover Movement. Pending commands will be cleared", "INFO", "TI Rover", "Stop Clear")
    print("Stopping Rover Movement and clearing all pending commands")
    return None

###########################################################################################

def resume():
    """
    Resumes the processing of commands, that are pending.

    Returns:
        None: None
    """
    log("Resuming pending Rover movement commands", "INFO", "TI Rover", "Resume")
    print("Resuming Rover Movement")
    return None

###########################################################################################

def stay(time:int=30):
    """
    Rover stays in place for the specified amount of time in seconds (optional). If no time is specified, the Rover stays for 30 seconds.

    Args:
        time (int, optional): The time to stay. Defaults to 30.

    Returns:
        list: a list containing the following data: [time]
    """

    if cerr.type_error(int, time) == False: log("Argument 'time' has to be type integer!", "ERROR", "TI Rover", "Stay")
    if cerr.range_error(0, None, time) == False: log("Argument 'time' has to be greater then 0!", "ERROR", "TI Rover", "Stay")

    err.type_error(int, "int", time)
    err.range_error(0, None, time)

    log("Staying at the current location for '" + str(time) + "' seconds", "INFO", "TI Rover", "Stay")
    print("Rover stays at current location for '" + str(time) + "' seconds")
    return [time]

###########################################################################################

def to(x:float, y:float):
    """
    Moves Rover to coordinate position (x,y) on virtual grid. Distance in GridUnits.

    Args:
        x (float): The x coordinate to go to.
        y (float): The y coordinate to go to.
    
    Returns:
        list: a list containing the following data: [x, y]
    """
    if cerr.type_error(float, x) == False: log("Argument 'x' has to be type float!", "ERROR", "TI Rover", "To")
    if cerr.type_error(float, y) == False: log("Argument 'y' has to be type float!", "ERROR", "TI Rover", "To")

    err.type_error(float, "float", x)
    err.type_error(float, "float", y)

    log("Moving the rover to ( " + str(x) + " | " + str(y) + " ) on the virtual grid", "INFO", "TI Rover", "To")
    print("Rover moves to '(" + str(x) + " | " + str(y) + ")' on the virtual grid.")
    return [x, y, x*10, y*10]

###########################################################################################

def to_polar(radius:float, theta_degrees:float):
    """
    Moves Rover to polar coordinate position (r, theta) on virtual grid. The angle is specified in degrees.

    Args:
        radius (float): The radius to move to.
        theta_degrees (float): The angle to move to.

    Returns:
        list: a list containing the following values: [radius, theta_degrees]
    """
    if cerr.type_error(float, radius) == False: log("Argument 'radius' has to be type float!", "ERROR", "TI Rover", "To Polar")
    if cerr.type_error(float, theta_degrees) == False: log("Argument 'theta_degrees' has to be type float!", "ERROR", "TI Rover", "To Polar")

    err.type_error(float, "float", radius)
    err.type_error(float, "float", theta_degrees)

    log("Moving the Rover to polar with a radius of '" + str(radius) + "' and an angle of '" + str(theta_degrees) + "' degrees", "INFO", "TI Rover", "To Polar")
    print("Rover moves to polar with radius '" + str(radius) + "' and '" + str(theta_degrees) + "' degrees")
    return [radius, theta_degrees]

###########################################################################################

def to_angle(degrees:float, unit:str):
    """
    Spins Rover to the specified angle in the virtual grid. The angle is relative to a zero angle which points down the x-axis in the virtual grid.

    Args:
        degrees (float): The degrees to spin.
        unit (str): The unit to spin. Possible Options: 'degrees', 'radians', 'gradians'.

    Returns:
        list: a list containing the following data: [degrees, unit]
    """
    if cerr.type_error(float, degrees) == False: log("Argument 'degrees' has to be type float!", "ERROR", "TI Rover", "To Angle")
    if cerr.type_error(str, unit) == False: log("Argument 'unit' has to be type string!", "ERROR", "TI Rover", "To Angle")

    if cerr.argument_error(unit, "degrees", "radians", "gradians") == False: log("Argument 'unit' has to be one of these: 'degrees', 'radians', 'gradians'!", "ERROR", "TI Rover", "To Angle")



    err.type_error(float, "float", degrees)
    err.type_error(str, "str", unit)

    err.argument_error(unit, "degrees", "radians", "gradians")
    
    log("Turning the rover by " + str(degrees) + " '" + unit + "'", "INFO", "TI Rover", "To Angle")
    print("Rover turns by angle '" + str(degrees) + "' with unit type '" + unit + "' degrees")
    return [degrees, unit]

        
###########################################################################################

def backward_time(time:float, speed:float = 1, unit:str = "units/s"):
    """
    Moves Rover backward for the specified time at the specified speed. The speed can be specified in grid units/s, meters/s, or wheel revolutions/s.

    Args:
        time (float): The time in seconds to move. Ranges from 0.1 to 100.
        speed (float, optional): The speed at which to move. Ranges from 0.1 to 10. Defaults to 1.
        unit (str, optional): The unit of speed. Possible Options: 'units/s', 'm/s', 'revs/s'. Defaults to "units/s".

    Returns:
        list: a list containing the following data: [time, speed, unit]
    """
    if cerr.type_error(float, time) == False: log("Argument 'time' has to be type float!", "ERROR", "TI Rover", "Backward Time")
    if cerr.type_error(float, speed) == False: log("Argument 'speed' has to be type float!", "ERROR", "TI Rover", "Backward Time")
    if cerr.type_error(str, unit) == False: log("Argument 'unit' has to be type string!", "ERROR", "TI Rover", "Backward Time")
    if cerr.range_error(0.1, 100, time) == False: log("Argument 'time' has to be between the values 0.1 and 100 (inclusive)!", "ERROR", "TI Rover", "Backward Time")
    if cerr.range_error(0.1, 10, speed) == False: log("Argument 'speed' has to be between the values 0.1 and 10 (inclusive)!", "ERROR", "TI Rover", "Backward Time")
    if cerr.argument_error(unit, "units/s", "m/s", "revs/s") == False: log("Argument 'unit' can only be on of these: 'units/s', 'm/s', 'revs/s'!", "ERROR", "TI Rover", "Backward Time")

    err.type_error(float, "float", time)
    err.type_error(float, "float", speed)
    err.type_error(str, "str", unit)
    err.range_error(0.1, 100, time)
    err.range_error(0.1, 10, speed)
    err.argument_error(unit, "units/s", "m/s", "revs/s")

    log("Moving the rover backwards for '" + str(time) + "' seconds with a speed of " + str(speed) + " '" + unit + "'", "INFO", "TI Rover", "Backward Time")
    print("Moving the rover backwards for '" + str(time) + "' seconds with a speed of '" + str(speed) + unit + "'")
    return [time, speed, unit]


###########################################################################################

def forward_time(time:float, speed:float = 1, unit:str = "units/s"):
    """
    Moves Rover forward for the specified time at the specified speed. The speed can be specified in grid units/s, meters/s, or wheel revolutions/s.

    Args:
        time (float): The time in seconds to move. Ranges from 0.1 to 100.
        speed (float, optional): The speed at which to move. Ranges from 0.1 to 10. Defaults to 1.
        unit (str, optional): The unit of speed. Possible Options: 'units/s', 'm/s', 'revs/s'. Defaults to "units/s".

    Returns:
        list: a list containing the following data: [time, speed, unit]
    """
    if cerr.type_error(float, time) == False: log("Argument 'time' has to be type float!", "ERROR", "TI Rover", "Forward Time")
    if cerr.type_error(float, speed) == False: log("Argument 'speed' has to be type float!", "ERROR", "TI Rover", "Forward Time")
    if cerr.type_error(str, unit) == False: log("Argument 'unit' has to be type string!", "ERROR", "TI Rover", "Forward Time")
    if cerr.range_error(0.1, 100, time) == False: log("Argument 'time' has to be between the values 0.1 and 100 (inclusive)!", "ERROR", "TI Rover", "Forward Time")
    if cerr.range_error(0.1, 10, speed) == False: log("Argument 'speed' has to be between the values 0.1 and 10 (inclusive)!", "ERROR", "TI Rover", "Forward Time")
    if cerr.argument_error(unit, "units/s", "m/s", "revs/s") == False: log("Argument 'unit' can only be on of these: 'units/s', 'm/s', 'revs/s'!", "ERROR", "TI Rover", "Forward Time")

    err.type_error(float, "float", time)
    err.type_error(float, "float", speed)
    err.type_error(str, "str", unit)
    err.range_error(0.1, 100, time)
    err.range_error(0.1, 10, speed)
    err.argument_error(unit, "units/s", "m/s", "revs/s")

    log("Moving the rover forwards for '" + str(time) + "' seconds with a speed of " + str(speed) + " '" + unit + "'", "INFO", "TI Rover", "Forward Time")
    print("Moving the rover forwards for '" + str(time) + "' seconds with a speed of '" + str(speed) + unit + "'")
    return [time, speed, unit]
    

###########################################################################################

def ranger_measurement():
    """
    Reads the ultrasonic distance sensor on the front of the Rover, returning the current distance in meters.

    Returns:
        None: None
    """
    log("Fetching the value measured by the ultrasonic sensor", "INFO", "TI Rover", "Ranger Measurement")
    print("Fetching data from ultrasonic sensor")
    return None

###########################################################################################

def colour_measurement():
    """
    Returns a value from 1 to 9, indicating the predominant color being "seen" by the Rover color input sensor.\n
        1 = red\n
        2 = green\n
        3 = blue\n
        4 = cyan\n
        5 = magenta\n
        6 = yellow\n
        7 = black\n
        8 = grey\n
        9 = white    
    
    Returns
        None: None
    """
    log("Measuring the dominant colour from the colour sensor", "INFO", "TI Rover", "Colour Measurement")
    print("Measuring dominant colour from colour sensor")
    return None

###########################################################################################

def red_measurement():
    """
    Returns a value between 0 and 255 that indicates the perceived red level being seen by the color input sensor.
    
    Returns
        None: None
    """
    log("Measuring red level from the colour sensor", "INFO", "TI Rover", "Red Measurement")
    print("Measuring red level from the colour sensor")
    return None

###########################################################################################

def green_measurement():
    """
    Returns a value between 0 and 255 that indicates the perceived green level being seen by the color input sensor.
    
    Returns
        None: None
    """
    log("Measuring green level from the colour sensor", "INFO", "TI Rover", "Green Measurement")
    print("Measuring green level from the colour sensor")
    return None

###########################################################################################

def blue_measurement():
    """
    Returns a value between 0 and 255 that indicates the perceived blue level being seen by the color input sensor.
    
    Returns
        None: None
    """
    log("Measuring blue level from the colour sensor", "INFO", "TI Rover", "Blue Measurement")
    print("Measuring blue level from the colour sensor")
    return None

###########################################################################################

def gray_measurement():
    """
    Returns a value between 0 and 255 that indicates the perceived gray level being seen by the color input sensor with 0 being black and 255 being white.
    
    Returns
        None: None
    """
    log("Measuring gray level from the colour sensor", "INFO", "TI Rover", "Gray Measurement")
    print("Measuring gray level from the colour sensor")
    return None

###########################################################################################

def encoders_gyro_measurement():
    """
    Returns a list of values that contains the left and right wheel encoder counts as well as the current gyro heading.
    
    Returns
        None: None
    """
    log("Measuring the gyroscope values for heading, left wheel and right wheel", "INFO", "TI Rover", "Encoders Gyroscope Measurement")
    print("Measuring gyroscope values for heading, left wheel and right wheel")
    return None

###########################################################################################

def gyro_measurement():
    """
    Returns a value that represents the current gyro reading, including drift, in the degrees.
    
    Returns
        None: None
    """
    log("Getting the values measured by the gyroscope", "INFO", "TI Rover", "Gyroscope Measurement")
    print("Measuring gyroscope values")
    return None

###########################################################################################

def colour_rgb(red:float, green:float, blue:float):
    """
    Sets the rgb led to the given red, green and blue colours. Colours are ranging between 0 and 255.

    Args:
        red (int): The red value (0 - 255).
        green (int): The green value (0 - 255).
        blue (int): The blue value (0 - 255).

    Returns:
        list: a list containing the following data: [red, green, blue]
    """

    if cerr.type_error(int, red) == False: log("Argument 'red' has to be type integer!", "ERROR", "TI Rover", "Colour RGB")
    if cerr.type_error(int, green) == False: log("Argument 'green' has to be type integer!", "ERROR", "TI Rover", "Colour RGB")
    if cerr.type_error(int, blue) == False: log("Argument 'blue' has to be type integer!", "ERROR", "TI Rover", "Colour RGB")

    if cerr.range_error(0, 255, red) == False: log("Argument 'arg' has to be between the values 0 and 255 (included)!", "ERROR", "TI Rover", "Colour RGB")
    if cerr.range_error(0, 255, green) == False: log("Argument 'arg' has to be between the values 0 and 255 (included)!", "ERROR", "TI Rover", "Colour RGB")
    if cerr.range_error(0, 255, blue) == False: log("Argument 'arg' has to be between the values 0 and 255 (included)!", "ERROR", "TI Rover", "Colour RGB")

    if red == 0 and green == 0 and blue == 0: log("Please use the function 'off()' instead of setting each value to 0, since this does not fully turn off the RGB-LED", "WARNING", "TI Rover", "Colour RGB")

    err.type_error(int, "int", red)
    err.type_error(int, "int", green)
    err.type_error(int, "int", blue)

    err.range_error(0, 255, red)
    err.range_error(0, 255, green)
    err.range_error(0, 255, blue)
        
    log("Setting RGB-Led to '" + str(red) + "' red, '" + str(green) + "' green , '" + str(blue) + "' blue", "INFO", "TI Rover", "Colour RGB")
    print("Setting RGB-Led to Red: " + str(red) + ", Green: " + str(green) + ", Blue: " + str(blue))
    return [red, green, blue]

###########################################################################################

def blink(frequency: float, time: float):
    """
    Blinks the RGB-LED at the given frequency (in Hertz) for the given time. The frequency ranges between 0.1 - 20 Hz and the time between 0.1 - 100 seconds.

    Args:
        frequency (float): The frequency to blink in Hertz. Ranges from 0.1 to 20.
        time (float): The time to blink in seconds. Ranges from 0.1 to 100.

    Returns:
        list: a list containing the following data: [frequency, time, total_blinks]
    """

    if cerr.type_error(float, frequency) == False: log("Argument 'frequency' has to be type integer!", "ERROR", "TI Rover", "Blink")
    if cerr.type_error(float, time) == False: log("Argument 'time' has to be type integer!", "ERROR", "TI Rover", "Blink")
    if cerr.range_error(0.1, 20, frequency) == False: log("Argument 'frequency' has to be between the values 0.1 and 20!", "ERROR", "TI Rover", "Blink")
    if cerr.range_error(0.1, 100, time) == False: log("Argument 'time' has to be between the values 0.1 and 100!", "ERROR", "TI Rover", "Blink")

    if frequency > 5 and time > 5: log("Blinking the LED at a high frequency for a longer time decreases its life-time!", "WARNING", "TI Rover", "Blink")

    err.type_error(float, "float", frequency)
    err.type_error(float, "float", time)
    err.range_error(0.1, 20, frequency)
    err.range_error(0.1, 100, time)

    log("Blinking the RGB-LED at a frequency of '" + str(frequency) + "' Hz for a time of '" + str(time) + "' seconds (" + str(time * frequency) + ") times", "INFO", "TI Rover", "Blink")
    print("Blinking the RGB-LED at a frequency of " + str(frequency) + "Hz for " + str(time) + " seconds (" + str(time * frequency) + ") times")
    return [frequency, time, time * frequency]

###########################################################################################

def off():
    """
    Turns the RGB-LED off.

    Returns:
        None: None
    """

    log("Turning the RGB-LED off", "INFO", "TI Rover", "Off")
    print("Turning RGB-LED off")
    return None

###########################################################################################

def motor_left(speed:int, time:float = 5):
    """
    Sets the left motor power to the specified value for the specified duration. The speed is in the range -255 to 255 with 0 being stop. Positive speed values are counter-clockwise rotation, and negative speed values are clockwise. The optional time parameter, if specified, has a valid range of 0.1 to 100 seconds. If not specified, a default of 5 seconds is used. 

    Args:
        speed (int): The speed of the left wheels motor. Ranges from -255 to 255 with 0 being stop.
        time (float, optional): The time to spin. Ranges from 0.1 to 100. Defaults to 5.

    Returns:
        list: a list containing the following data: [speed, time]
    """
    if cerr.type_error(int, speed) == False: log("Argument 'speed' has to be type integer!", "ERROR", "TI Rover", "Left Motor")
    if cerr.type_error(float, time) == False: log("Argument 'time' has to be type float!", "ERROR", "TI Rover", "Left Motor")
    if cerr.range_error(-255, 255, speed) == False: log("Argument 'speed' has to be between the values -255 and 255!", "ERROR", "TI Rover", "Left Motor")
    if cerr.range_error(0.1, 100, time) == False: log("Argument 'time' has to be between the values 0.1 and 100!", "ERROR", "TI Rover", "Left Motor")

    err.type_error(int, "int", speed)
    err.type_error(float, "float", time)
    err.range_error(-255, 255, speed)
    err.range_error(0.1, 100, time)
    
    log("Setting the left motor to counter-clockwise with a speed of '" + str(speed) + "' for a time of '" + str(time) + "' seconds", "INFO", "TI Rover", "Left Motor")
    print("Setting the left motor power to 'speed " + str(speed) + "' for a time of '" + str(time) + " seconds'")
    return [float(speed), time]

###########################################################################################

def motor_right(speed:int, time:float = 5):
    """
    Sets the right motor power to the specified value for the specified duration. The speed is in the range -255 to 255 with 0 being stop. Positive speed values are counter-clockwise rotation, and negative speed values are clockwise. The optional time parameter, if specified, has a valid range of 0.1 to 100 seconds. If not specified, a default of 5 seconds is used. 

    Args:
        speed (int): The speed of the right wheels motor. Ranges from -255 to 255 with 0 being stop.
        time (float, optional): The time to spin. Ranges from 0.1 to 100. Defaults to 5.

    Returns:
        list: a list containing the following data: [speed, time]
    """
    if cerr.type_error(int, speed) == False: log("Argument 'speed' has to be type integer!", "ERROR", "TI Rover", "Right Motor")
    if cerr.type_error(float, time) == False: log("Argument 'time' has to be type float!", "ERROR", "TI Rover", "Right Motor")
    if cerr.range_error(-255, 255, speed) == False: log("Argument 'speed' has to be between the values -255 and 255!", "ERROR", "TI Rover", "Right Motor")
    if cerr.range_error(0.1, 100, time) == False: log("Argument 'time' has to be between the values 0.1 and 100!", "ERROR", "TI Rover", "Right Motor")

    err.type_error(int, "int", speed)
    err.type_error(float, "float", time)
    err.range_error(-255, 255, speed)
    err.range_error(0.1, 100, time)
    
    log("Setting the right motor to counter-clockwise with a speed of '" + str(speed) + "' for a time of '" + str(time) + "' seconds", "INFO", "TI Rover", "Right Motor")
    print("Setting the right motor power to 'speed " + str(speed) + "' for a time of '" + str(time) + " seconds'")
    return [float(speed), time]

###########################################################################################

def motors(left_direction:str, left_speed:int, right_direction:str, right_speed:int, time:float = 5):
    """
    Sets the left and right wheel to the specified speed levels, for an optional amount of time in seconds. The speed (left_speed, right_speed) values are in the range 0 to 255 with 0 being stop. The left_direction and right_direction parameters specify CW or CCW rotation of the respective wheels. The optional time parameter, if specified, has a valid range of 0.1 to 100 seconds. If not specified, a default of 5 seconds is used.

    Args:
        left_direction (str): The direction of the left wheel. Possible Options: 'cw', 'ccw'.
        left_speed (int): The speed of the left wheel. Ranges from -255 to 255 with 0 being stop.
        right_direction (str): The direction of the right wheel. Possible Options: 'cw', 'ccw'.
        right_speed (int): The speed of the right wheel. Ranges from -255 to 255 with 0 being stop.
        time (float, optional): The time to spin the wheels. Defaults to 5.

    Returns:
        list: a list containing the following data: [left_direction, left_speed, right_direction, right_speed, time]
    """
    if cerr.type_error(str, left_direction) == False: log("Argument 'left_direction' has to be type string!", "ERROR", "TI Rover", "Motors")
    if cerr.type_error(int, left_speed) == False: log("Argument 'left_speed' has to be type integer!", "ERROR", "TI Rover", "Motors")
    if cerr.type_error(str, right_direction) == False: log("Argument 'right_direction' has to be type string!", "ERROR", "TI Rover", "Motors")
    if cerr.type_error(int, right_speed) == False: log("Argument 'right_speed' has to be type integer!", "ERROR", "TI Rover", "Motors")
    if cerr.type_error(float, time) == False: log("Argument 'time' has to be type float!", "ERROR", "TI Rover", "Motors")

    if cerr.range_error(-255, 255, left_speed) == False: log("Argument 'left_speed' has to be between the values -255 and 255!", "ERROR", "TI Rover", "Motors")
    if cerr.range_error(-255, 255, right_speed) == False: log("Argument 'right_speed' has to be between the values -255 and 255!", "ERROR", "TI Rover", "Motors")
    if cerr.range_error(0.1, 100, time) == False: log("Argument 'time' has to be between the values 0.1 and 100!", "ERROR", "TI Rover", "Motors")
    
    if cerr.argument_error(left_direction, "cw", "ccw") == False: log("Argument 'left_direction' has to be one of these: 'cw', 'ccw'!", "ERROR", "TI Rover", "Motors")
    if cerr.argument_error(right_direction, "cw", "ccw") == False: log("Argument 'right_direction' has to be one of these: 'cw', 'ccw'!", "ERROR", "TI Rover", "Motors")


    err.type_error(str, "str", left_direction)
    err.type_error(int, "int", left_speed)
    err.type_error(str, "str", right_direction)
    err.type_error(int, "int", right_speed)
    err.type_error(float, "float", time)

    err.range_error(-255, 255, left_speed)
    err.range_error(-255, 255, right_speed)
    err.range_error(0.1, 100, time)
    
    err.argument_error(left_direction, "cw", "ccw")
    err.argument_error(right_direction, "cw", "ccw")
    
    
    log("Setting the left motor to rotate '" + left_direction + "' with a speed of '" + str(left_speed) + "'. Setting the right motor to rotate '" + right_direction + "' with a speed of '" + str(right_speed) + "'. Both motors are running for '" + str(time) + "' seconds", "INFO", "TI Rover", "Motors")
    print("Setting the left motor to rotate '" + left_direction + "' with a speed of '" + str(left_speed) + "'. Setting the right motor to rotate '" + right_direction + "' with a speed of '" + str(right_speed) + "'. Both motors are running for '" + str(time) + " seconds'")
    return [left_direction, left_speed, right_direction, right_speed, time]


###########################################################################################

def waypoint_xythdrn():
    """
    Reads the x-coord, y-coord, time, heading, distance traveled, number of wheel revolutions, command number of the current waypoint. Returns a list with all these values as elements.
    
    Returns:
        None: None
    """
    log("Fetching the x-coord, y-coord, time, heading, distance traveled, number of wheel revolutions and command number of the current waypoint", "INFO", "TI Rover", "Waypoint Xythdrn")
    print("Fetching the x-coord, y-coord, time, heading, distance traveled, number of wheel revolutions and command number of the current waypoint")
    return None

###########################################################################################

def waypoint_prev():
    """
    Reads the x-coord, y-coord, time, heading, distance traveled, number of wheel revolutions, command number of the previous waypoint.

    Returns:
        None: None
    """
    log("Fetching the x-coord, y-coord, time, heading, distance traveled, number of wheel revolutions and command number of the previous waypoint", "INFO", "TI Rover", "Waypoint Previous")
    print("Fetching the x-coord, y-coord, time, heading, distance traveled, number of wheel revolutions and command number of the previous waypoint")
    return None

###########################################################################################

def waypoint_eta():
    """
    Fetches the estimated time to drive to a waypoint.
    
    Returns:
        None: None
    """
    log("Fetching estimated time to reach the next waypoint", "INFO", "TI Rover", "Waypoint ETA")
    print("Fetching estimated time to reach next waypoint")
    return None

###########################################################################################

def path_done():
    """
    Returns a value of 0 or 1 depending on whether the Rover is moving (0) or finished with all movement (1).
    
    Returns:
        None: None
    """
    log("Checking if the rover is done with the current path", "INFO", "TI Rover", "Path Done")
    print("Checking if the rover is done with it's path")
    return None

###########################################################################################

def pathlist_x():
    """
    Returns a list of X values from the beginning to and including the current Waypoint X value.
    
    Returns:
        None: None
    """
    log("Fetching the x values of the previous and current waypoints", "INFO", "TI Rover", "Pathlist X")
    print("Fetching x values of previous and current waypoints")
    return None

###########################################################################################

def pathlist_y():
    """
    Returns a list of y values from the beginning to and including the current Waypoint Y value.
    
    Returns:
        None: None
    """
    log("Fetching the y values of the previous and current waypoints", "INFO", "TI Rover", "Pathlist Y")
    print("Fetching y values of previous and current waypoints")
    return None

###########################################################################################

def pathlist_time():
    """
    Returns a list of the time in seconds from the beginning to and including the current Waypoint time value.
    
    Returns:
        None: None
    """
    log("Fetching the time passed since the first waypoint", "INFO", "TI Rover", "Pathlist Time")
    print("Fetching time since first waypoint")
    return None

###########################################################################################

def pathlist_heading():
    """
    Returns a list of the headings from the beginning to and including the current Waypoint heading value.
    
    Returns:
        None: None
    """
    log("Fetching the headings since the fist waypoint", "INFO", "TI Rover", "Pathlist Heading")
    print("Fetching headings since first waypoint")
    return None

###########################################################################################

def pathlist_distance():
    """
    Returns a list of the distances traveled from the beginning to and including the current Waypoint distance value.

    Returns:
        None: None
    """
    log("Fetching the distances traveled since the first waypoint", "INFO", "TI Rover", "Pathlist Distance")
    print("Fetching distances traveled since first waypoint")
    return None

###########################################################################################

def pathlist_revs():
    """
    Returns a list of the number of revolutions traveled from the beginning to and including the current Waypoint revolutions value.
    
    Returns:
        None: None
    """
    log("Fetching the number of wheel revolutions since the first waypoint", "INFO", "TI Rover", "Pathlist Revolutions")
    print("Fetching wheel revolutions since first waypoint")
    return None

###########################################################################################

def pathlist_cmdnum():
    """
    Returns a list of command numbers for the path.
    
    Returns:
        None: None
    """
    log("Fetching list of waypoints numbers since the first waypoint", "INFO", "TI Rover", "Pathlist CMDNUM")
    print("Fetching list of waypoint numbers since first waypoint")
    return None

###########################################################################################

def waypoint_x():
    """
    Returns x coordinate of current waypoint.
    
    Returns:
        None: None
    """
    log("Fetching the x coordinate of the current waypoint", "INFO", "TI Rover", "Waypoint X")
    print("Fetching x coordinate of current waypoint")
    return None

###########################################################################################

def waypoint_y():
    """
    Returns y coordinate of current waypoint.
    
    Returns:
        None: None
    """
    log("Fetching the y coordinate of the current waypoint", "INFO", "TI Rover", "Waypoint Y")
    print("Fetching y coordinate of current waypoint")
    return None

###########################################################################################

def waypoint_time():
    """
    Returns time spent traveling from previous to current waypoint.
    
    Returns:
        None: None
    """
    log("Fetching the time spent travelling to the current waypoint", "INFO", "TI Rover", "Waypoint Time")
    print("Fetching time spent travelling to current waypoint")
    return None

###########################################################################################

def waypoint_heading():
    """
    Returns absolute heading of current waypoint.
    
    Returns:
        None: None
    """
    log("Fetching the absolute heading of the current waypoint", "INFO", "TI Rover", "Waypoint Heading")
    print("Fetching absolute heading of current waypoint")
    return None

###########################################################################################

def waypoint_distance():
    """
    Returns distance traveled between previous and current waypoint.
    
    Returns:
        None: None
    """
    log("Fetching the distance traveled between the current and the previous waypoint", "INFO", "TI Rover", "Waypoint Distance")
    print("Fetching distance traveled between current and previous waypoint")
    return None

###########################################################################################

def waypoint_revs():
    """
    Returns number of revolutions needed to travel between previous and current waypoint.
    
    Returns:
        None: None
    """
    log("Fetching the wheel revolutions since the last waypoint", "INFO", "TI Rover", "Waypoint Revolutions")
    print("Fetching wheel revolutions since last waypoint")
    return None