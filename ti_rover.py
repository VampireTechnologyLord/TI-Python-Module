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

###########################################################################################

def ranger_measurement():
    """
    Reads the ultrasonic distance sensor on the front of the Rover, returning the current distance in meters.
    
    
    Category: Rover / Input
    
    
    Returns None
    """
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
        9 = white\n
    
    
    Category: Rover / Input
    
    
    Returns None
    """
    print("Measuring dominant colour from colour sensor")
    return None

###########################################################################################

def red_measurement():
    """
    Returns a value between 0 and 255 that indicates the perceived red level being seen by the color input sensor.
    
    
    Category: Rover / Input
    
    
    Returns None
    """
    print("Measuring red level from the colour sensor")
    return None

###########################################################################################

def green_measurement():
    """
    Returns a value between 0 and 255 that indicates the perceived green level being seen by the color input sensor.
    
    
    Category: Rover / Input
    
    
    Returns None
    """
    print("Measuring green level from the colour sensor")
    return None

###########################################################################################

def blue_measurement():
    """
    Returns a value between 0 and 255 that indicates the perceived blue level being seen by the color input sensor.
    
    
    Category: Rover / Input
    
    
    Returns None
    """
    print("Measuring blue level from the colour sensor")
    return None

###########################################################################################

def gray_measurement():
    """
    Returns a value between 0 and 255 that indicates the perceived gray level being seen by the color input sensor with 0 being black and 255 being white.
    
    
    Category: Rover / Input
    
    
    Returns None
    """
    print("Measuring gray level from the colour sensor")
    return None

###########################################################################################

def encoders_gyro_measurement():
    """
    Returns a list of values that contains the left and right wheel encoder counts as well as the current gyro heading.
    
    
    Category: Rover / Input
    
    
    Returns None
    """
    print("Measuring gyroscope values for heading, left wheel and right wheel")
    return None

###########################################################################################

def gyro_measurement():
    """
    Returns a value that represents the current gyro reading, including drift, in the degrees.
    
    
    Category: Rover / Input
    
    
    Returns None
    """
    print("Measuring gyroscope values")
    return None

###########################################################################################

def colour_rgb(red:float, green:float, blue:float):
    """
    Description
    
    
    Category: Rover / Output
    
    
    Returns an array / a list [red, green, blue]
    """
    try:
        float(red)
    except ValueError:
        raise ValueError(errormsg_type("float", "red")) from None
    try:
        float(green)
    except ValueError:
        raise ValueError(errormsg_type("float", "green")) from None
    try:
        float(blue)
    except ValueError:
        raise ValueError(errormsg_type("float", "blue")) from None
    
    if(red > 255 or red < 0):
        raise ValueError(errormsg_range(0, 255, "red"))
    if(green > 255 or green < 0):
        raise ValueError(errormsg_range(0, 255, "green"))
    if(blue > 255 or blue < 0):
        raise ValueError(errormsg_range(0, 255, "blue"))
    
    print("Setting the RGB-Led to '" + str(red) + " red', '"+ str(green) + " green', '" + str(blue) + " blue'")
    return [red, green, blue]

###########################################################################################

def blink(frequency: float, time: float):
    """
    Blinks the RGB-LED at the given frequency (in Hertz) for the given time. The frequency ranges between 0.1 - 20 Hz and the time between 0.1 - 100 seconds.


    Category: Rover / Output


    Returns an array / list: [frequency, time, totalBlinks]
    """

    try:
        float(frequency)
    except ValueError:
        raise ValueError(errormsg_type("float", "frequency")) from None

    try:
        float(time)
    except ValueError:
        raise ValueError(errormsg_type("float", "time")) from None

    if(frequency > 20 or frequency < 0.1):
        raise ValueError(errormsg_range(0.1, 20, "frequency"))
            
    if(time > 100 or time < 0.1):
        raise ValueError(errormsg_range(0.1, 100, "time"))
            

    print("Blinking the RGB-LED at a frequency of " + str(frequency) + "Hz for " + str(time) + " seconds (" + str(time * frequency) + ") times")
    return [frequency, time, time * frequency]

###########################################################################################

def off():
    """
    Turns the RGB-LED off.


    Category: Rover / Output


    Returns None
    """

    print("Turning RGB-LED off")
    return None

###########################################################################################

def motor_left(speed:int, time:float = 5):
    """
    Sets the left motor power to the specified value for the specified duration. The speed is in the range -255 to 255 with 0 being stop. Positive speed values are counter-clockwise rotation, and negative speed values are clockwise. The optional time parameter, if specified, has a valid range of 0.1 to 100 seconds. If not specified, a default of 5 seconds is used. 


    Default Values: time: 5
    
    
    Category: Rover / Output
    
    
    Returns an array / a list [speed, time]
    """
    try:
        int(speed)
    except ValueError:
        raise ValueError(errormsg_type("int", "speed")) from None
    try:
        float(time)
    except ValueError:
        raise ValueError(errormsg_type("float", "time")) from None
    
    if(speed > 255 or speed < -255):
        raise ValueError(errormsg_range(-255, 255, "speed"))
    if(time > 100 or time < 0.1):
        raise ValueError(errormsg_range(0.1, 100, "time"))
    
    print("Setting the left motor power to 'speed " + str(speed) + "' for a time of '" + str(time) + " seconds'")
    return [float(speed), time]

###########################################################################################

def motor_right(speed:int, time:float = 5):
    """
    Sets the right motor power to the specified value for the specified duration. The speed is in the range -255 to 255 with 0 being stop. Positive speed values are counter-clockwise rotation, and negative speed values are clockwise. The optional time parameter, if specified, has a valid range of 0.1 to 100 seconds. If not specified, a default of 5 seconds is used. 


    Default Values: time: 5
    
    
    Category: Rover / Output
    
    
    Returns an array / a list [speed, time]
    """
    try:
        int(speed)
    except ValueError:
        raise ValueError(errormsg_type("int", "speed")) from None
    try:
        float(time)
    except ValueError:
        raise ValueError(errormsg_type("float", "time")) from None
    
    if(speed > 255 or speed < -255):
        raise ValueError(errormsg_range(-255, 255, "speed"))
    if(time > 100 or time < 0.1):
        raise ValueError(errormsg_range(0.1, 100, "time"))
    
    print("Setting the right motor power to 'speed " + str(speed) + "' for a time of '" + str(time) + " seconds'")
    return [float(speed), time]

###########################################################################################

def motors(left_direction:str, left_speed:int, right_direction:str, right_speed:int, time:float = 5):
    """
    Sets the left and right wheel to the specified speed levels, for an optional amount of time in seconds. The speed (left_speed, right_speed) values are in the range 0 to 255 with 0 being stop. The left_direction and right_direction parameters specify CW or CCW rotation of the respective wheels. The optional time parameter, if specified, has a valid range of 0.1 to 100 seconds. If not specified, a default of 5 seconds is used.
    
    
    Category: Rover / Output
    
    
    Returns an array / a list [left_direction, left_speed, right_direction, right_speed, time]
    """
    try:
        str(left_direction)
    except ValueError:
        raise ValueError(errormsg_type("str", "left_direction")) from None
    try:
        int(left_speed)
    except ValueError:
        raise ValueError(errormsg_type("int", "left_speed")) from None
    try:
        str(right_direction)
    except ValueError:
        raise ValueError(errormsg_type("str", "right_direction")) from None
    try:
        int(right_speed)
    except ValueError:
        raise ValueError(errormsg_type("int", "right_speed")) from None
    try:
        float(time)
    except ValueError:
        raise ValueError(errormsg_type("float", "time")) from None
    
    
    if(left_speed > 255 or left_speed < -255):
        raise ValueError(errormsg_range(-255, 255, "left_speed"))
    if(right_speed > 255 or right_speed < -255):
        raise ValueError(errormsg_range(-255, 255, "right_speed"))
    if(time > 100 or time < 0.1):
        raise ValueError(errormsg_range(0.1, 100, "time"))
    
    
    if(left_direction == "cw" or left_direction == "ccw"):

        if(right_direction == "cw" or right_direction == "ccw"):
            print("Setting the left motor to rotate '" + left_direction + "' with a speed of '" + str(left_speed) + "'. Setting the right motor to rotate '" + right_direction + "' with a speed of '" + str(right_speed) + "'. Both motors are running for '" + str(time) + " seconds'")
            return [left_direction, left_speed, right_direction, right_speed, time]
        else:
            raise("ERROR: Parameter <right_direction> can only be 'cw' or 'ccw'")
    else:
        raise("ERROR: Parameter <left_direction> can only be 'cw' or 'ccw'")

###########################################################################################

def waypoint_xythdrn():
    """
    Reads the x-coord, y-coord, time, heading, distance traveled, number of wheel revolutions, command number of the current waypoint. Returns a list with all these values as elements.
    
    
    Category: Rover / Path
    
    
    Returns None
    """
    print("Fetching the x-coord, y-coord, time, heading, distance traveled, number of wheel revolutions and command number of the current waypoint")
    return None

###########################################################################################

def waypoint_prev():
    """
    Reads the x-coord, y-coord, time, heading, distance traveled, number of wheel revolutions, command number of the previous waypoint.

    
    
    Category: Rover / Path
    
    
    Returns None
    """
    print("Fetching the x-coord, y-coord, time, heading, distance traveled, number of wheel revolutions and command number of the previous waypoint")
    return None

###########################################################################################

def waypoint_eta():
    """
    Fetches the estimated time to drive to a waypoint.
    
    
    Category: Rover / Path
    
    
    Returns None
    """
    print("Fetching estimated time to reach next waypoint")
    return None

###########################################################################################

def path_done():
    """
    Returns a value of 0 or 1 depending on whether the Rover is moving (0) or finished with all movement (1).
    
    
    Category: Rover / Path
    
    
    Returns None
    """
    print("Checking if the rover is done with it's path")
    return None

###########################################################################################

def pathlist_x():
    """
    Returns a list of X values from the beginning to and including the current Waypoint X value.
    
    
    Category: Rover / Path
    
    
    Returns None
    """
    print("Fetching x values of previous and current waypoints")
    return None

###########################################################################################

def pathlist_y():
    """
    Returns a list of y values from the beginning to and including the current Waypoint Y value.
    
    
    Category: Rover / Path
    
    
    Returns None
    """
    print("Fetching y values of previous and current waypoints")
    return None

###########################################################################################

def pathlist_time():
    """
    Returns a list of the time in seconds from the beginning to and including the current Waypoint time value.
    
    
    Category: Rover / Path
    
    
    Returns None
    """
    print("Fetching time since first waypoint")
    return None

###########################################################################################

def pathlist_heading():
    """
    Returns a list of the headings from the beginning to and including the current Waypoint heading value.
    
    
    Category: Rover / Path
    
    
    Returns None
    """
    print("Fetching headings since first waypoint")
    return None

###########################################################################################

def pathlist_distance():
    """
    Returns a list of the distances traveled from the beginning to and including the current Waypoint distance value.

    
    Category: Rover / Path
    
    
    Returns None
    """
    print("Fetching distances traveled since first waypoint")
    return None

###########################################################################################

def pathlist_revs():
    """
    Returns a list of the number of revolutions traveled from the beginning to and including the current Waypoint revolutions value.
    
    
    Category: Rover / Path
    
    
    Returns None
    """
    print("Fetching wheel revolutions since first waypoint")
    return None

###########################################################################################

def pathlist_cmdnum():
    """
    Returns a list of command numbers for the path.
    
    
    Category: Rover / Path
    
    
    Returns None
    """
    print("Fetching list of waypoint numbers since first waypoint")
    return None

###########################################################################################

def waypoint_x():
    """
    Returns x coordinate of current waypoint.
    
    
    Category: Rover / Path
    
    
    Returns None
    """
    print("Fetchin x coordinate of current waypoint")
    return None

###########################################################################################

def waypoint_y():
    """
    Returns y coordinate of current waypoint.
    
    
    Category: Rover / Path
    
    
    Returns None
    """
    print("Fetchin y coordinate of current waypoint")
    return None

###########################################################################################

def waypoint_time():
    """
    Returns time spent traveling from previous to current waypoint.
    
    
    Category: Rover / Path
    
    
    Returns None
    """
    print("Fetching time spent travelling to current waypoint")
    return None

###########################################################################################

def waypoint_heading():
    """
    Returns absolute heading of current waypoint.
    
    
    Category: Rover / Path
    
    
    Returns None
    """
    print("Fetching absolute heding of current waypoint")
    return None

###########################################################################################

def waypoint_distance():
    """
    Returns distance traveled between previous and current waypoint.
    
    
    Category: Rover / Path
    
    
    Returns None
    """
    print("Fetching distance traveled between current and previous waypoint")
    return None

###########################################################################################

def waypoint_revs():
    """
    Returns number of revolutions needed to travel between previous and current waypoint.
    
    
    Category: Rover / Path
    
    
    Returns None
    """
    print("Fetching wheel revolutions since last waypoint")
    return None