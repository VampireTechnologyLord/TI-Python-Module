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


    Category: Hub / Miscellaneous


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
    cm:float = distance * 10
    print("Moving the rover backwards by '" + str(distance) + "' griduntis (" + str(cm) + ") cm")
    return [distance, cm]