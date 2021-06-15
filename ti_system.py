"""
A class containing all the TI-System commands
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

def recall_value(name:str):
    """
    Recalls a predefined OS variable (value) named "name".
    
    
    Category: TI System
    
    
    Returns an array / list: [name]
    """
    try:
        str(name)
    except ValueError:
        raise ValueError(errormsg_type("str", "name")) from None
    
    print("Fetching value of system variable '" + name + "'")
    return [name]

###########################################################################################

def store_value(name:str, value):
    """
    Stores a Python variable (value) to an OS variable named "name".
    
    
    Category: TI System
    
    
    Returns an array / list: [name, value]
    """
    print("Storing data '" + str(value) + "' to variable '" + name + "'")
    return [name, value]

###########################################################################################

def recall_list(name:str):
    """
    Recalls a predefined OS list (list) named "name".
    
    
    Category: TI System
    
    
    Returns an array / list: [name]
    """
    
    print("Fetching value of system list '" + name + "'")
    return [name]

###########################################################################################

def store_list(name:str, list):
    """
    Stores a Python list (list) to an OS variable named "name".
    
    
    Category: TI System
    
    
    Returns an array / list: [name, list]
    """
    print("Storing data '" + str(list) + "' to variable '" + name + "'")
    return [name, list]

###########################################################################################

def eval_function(name:str, value):
    """
    Evaluates a predefined OS function at the specified value

    
    Category: TI System
    
    
    Returns an array / list: [name, value]
    """
    print("Evaluating result of '" + name + "' for value '" + str(value) + "'")
    return [name, value]

###########################################################################################

def get_platform():
    """
    Returns 'hh' for handeld and 'dt' for desktop
    
    
    Category: TI System
    
    
    Returns None
    """
    print("Fetching platform type")
    return None

###########################################################################################

def get_key(paramter = None):
    """
    Returns a string representing the key pressed. The '1' key returns "1", 'esc' returns "esc", and so on. When called without any parameters - get_key() - it  returns immediately. When called with a parameter - get_key(1) - it waits until a key is pressed.


    Default values: parameter: None
    
    
    Category: TI System
    
    
    Returns an array / list: [parameter]
    """
    print("Fetching Key-String for '" + str(paramter) + "'")
    return [paramter]

###########################################################################################

def get_mouse():
    """
    Returns mouse coordinates as a two element tuple, either the canvas pixel position or (-1,-1) if outside the canvas.
    
    
    Category: TI System
    
    
    Returns None
    """
    print("Fetching position of mouse cursor")
    return None

###########################################################################################

def clear_history():
    """
    Clears the shell history
    
    
    Category: TI System
    
    
    Returns None
    """
    print("Clearung Shell history")
    return None

###########################################################################################

def get_time_ms():
    """
    Returns time in milliseconds with millisecond precision. This functionality can be used to calculate a duration rather than determine the actual clock time.
    
    
    Category: TI System
    
    
    Returns None
    """
    print("Fetching time in milliseconds")
    return None