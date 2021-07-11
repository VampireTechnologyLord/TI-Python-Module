"""
A class containing all the TI-System commands
"""
from ti_python_module.err import withConsole as err
from ti_python_module.err import onlyCheck as cerr
from ti_python_module.file_handler import create_log as log

###########################################################################################

def recall_value(name:str):
    """
    Recalls a predefined OS variable (value) named "name".

    args:
        name (str): The name of the variable from which to recall the value.
    
    Returns:
        list: a list containing the following data: [name]
    """
    if cerr.type_error(str, name) == False: log("Argument 'name' has to be type string", "ERROR", "TI System", "Recall Value")

    err.type_error(str, "str", name)
    
    log("Fetchint the value stored in the system variable with the name '" + name + "'", "INFO", "TI System", "Recall Value")
    print("Fetching value of system variable '" + name + "'")
    return [name]

###########################################################################################

def store_value(name:str, value):
    """
    Stores a Python variable (value) to an OS variable named "name".
    
    args:
        name (str): The name of the variable from which to recall the value.
        value (any): The value to store.
    
    Returns:
        list: a list containing the following data: [name, value]
    """
    if cerr.type_error(str, name) == False: log("Argument 'name' has to be type string", "ERROR", "TI System", "Store Value")
    err.type_error(str, "str", name)
    log("Storing data '" + str(value) + "' to variable '" + name + "'", "INFO", "TI System", "Store Value")
    print("Storing data '" + str(value) + "' to variable '" + name + "'")
    return [name, value]
###########################################################################################

def recall_list(name:str):
    """
    Recalls a predefined OS list (list) named "name".
    
    args:
        name (str): The name of the list from which to recall the value.
    
    Returns:
        list: a list containing the following data: [name]
    """

    if cerr.type_error(str, name) == False: log("Argument 'name' has to be type string", "ERROR", "TI System", "Recall List")

    err.type_error(str, "str", name)
    log("Recalling values of system list '" + name + "'", "INFO", "TI System", "Recall List")
    print("Fetching value of system list '" + name + "'")
    return [name]

###########################################################################################

def store_list(name:str, list:list):
    """
    Stores a Python list (list) to an OS variable named "name".
    
    args:
        name (str): The name of the variable from which to recall the value.
        list (list): The values to store int the list.
    
    Returns:
        list: a list containing the following data: [name, list]
    """

    if cerr.type_error(str, name) == False: log("Argument 'name' has to be type string", "ERROR", "TI System", "Store List")

    err.type_error(str, "str", name)
    
    log("Storing the data from the given list to system list '" + name + "'", "INFO", "TI System", "Store List")
    print("Storing data '" + str(list) + "' to variable '" + name + "'")
    return [name, list]

###########################################################################################

def eval_function(name:str, value):
    """
    Evaluates a predefined OS function at the specified value

    args:
        name (str): The name of the function.
        value (any): The value to use for the function
    
    Returns:
        list: a list containing the following data: [name, value]
    """

    if cerr.type_error(str, name) == False: log("Argument 'name' has to be type string", "ERROR", "TI System", "Evaluate Function")

    err.type_error(str, "str", name)
    log("Evaluating the result of using the function '" + name +"' with the value '" + str(value) + "'", "INFO", "TI System", "Evaluate Function")
    print("Evaluating result of '" + name + "' for value '" + str(value) + "'")
    return [name, value]

###########################################################################################

def get_platform():
    """
    Returns 'hh' for handeld and 'dt' for desktop
    
    Returns
        None: None
    """
    log("Fetching current platform type", "INFO", "TI System", "Get Platform")
    print("Fetching platform type")
    return None

###########################################################################################

def get_key(parameter = None):
    """
    Returns a string representing the key pressed. The '1' key returns "1", 'esc' returns "esc", and so on. When called without any parameters - get_key() - it  returns immediately. When called with a parameter - get_key(1) - it waits until a key is pressed.

    Args:
        parameter (any, optional): Optional Parameter. If given, waits until key is pressed. Defaults to None.

    Returns:
        list: a list containing the following data: [parameter]
    """
    log("Fetching Key-String fot '" + str(parameter) + "'", "INFO", "TI System", "Get Key")
    print("Fetching Key-String for '" + str(parameter) + "'")
    return [parameter]

###########################################################################################

def get_mouse():
    """
    Returns mouse coordinates as a two element tuple, either the canvas pixel position or (-1,-1) if outside the canvas.
    
    Returns
        None: None
    """
    log("Fetching the position of the mouse cursor", "INFO", "TI System", "Get Mouse")
    print("Fetching position of mouse cursor")
    return None

###########################################################################################

def clear_history():
    """
    Clears the shell history.
    
    Returns
        None: None
    """
    log("Clearing the content and history of the output shell", "INFO", "TI System", "Clear History")
    print("Clearing Shell history")
    return None

###########################################################################################

def get_time_ms():
    """
    Returns time in milliseconds with millisecond precision. This functionality can be used to calculate a duration rather than determine the actual clock time.
    
    Returns
        None: None
    """
    log("Fetching the time in milliseconds", "INFO", "TI System", "Get Time Milliseconds")
    print("Fetching time in milliseconds")
    return None