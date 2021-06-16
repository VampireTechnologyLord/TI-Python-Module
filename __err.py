"""
Class used for Error Methods

DO NOT USE IN ACTUAL SCRIPT
"""




def range_error(rangeMin: float, rangeMax:float, parameter):
    """
    Takes in a range Minimum and a range Maximum. Throws an Error if the given parameter exceeds either of theese boundaries.\n
    If the maximum is None, it will be set to the int-limit(2147483647).
    """
    if(rangeMax == None):
        rangeMax = 2147483647
    if(parameter > rangeMax or parameter < rangeMin):
        raise ValueError("ERROR: Parameter <" + str(parameter) + "> has to be in range between '" + str(rangeMin) + "' and '" + str(rangeMax) + "'") from None

def type_error(requiredDataType, requiredDataTypeName:str, parameter):
    """
    Checks if the given parameter can be translated / is from the given type. Data Type Name is for formatting purposes. If None, it will be '<class 'TYPE'>'.
    """
    if(requiredDataType == None):
        requiredDataType = str(requiredDataType)
    try:
        requiredDataType(parameter)
    except:
        raise TypeError("ERROR: Parameter <" + str(parameter) + "> has to be type '" + requiredDataTypeName + "'") from None

def argument_error(parameter, givenArgument, *validArguments):
    """
    Checks if the given argument is contained in the validArguments.
    """
    if(givenArgument in validArguments):
        return None
    else:
        raise ValueError("ERROR: Parameter <" + str(parameter) + "> can only be " + str(validArguments)) from None