"""
Class used for Error Methods

DO NOT USE IN ACTUAL SCRIPT
"""


class withConsole():

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

    def argument_error(parameter, *validArguments):
        """
        Checks if the given argument is contained in the validArguments.
        """
        if(parameter in validArguments):
            return None
        else:
            raise ValueError("ERROR: Parameter <" + str(parameter) + "> can only be " + str(validArguments)) from None


    class relation():

        def smaller_error(smaller_parameter, larger_parameter):

            if(smaller_parameter < larger_parameter):
                return None
            else:
                raise ValueError("ERROR: Parameter <" + str(smaller_parameter) + "> has to be smaller then <" + str(larger_parameter) + ">")

        def smaller_equal_error(smaller_parameter, larger_parameter):

            if(smaller_parameter <= larger_parameter):
                return None
            else:
                raise ValueError("ERROR: Parameter <" + str(smaller_parameter) + "> has to be smaller or equal to/then <" + str(larger_parameter) + ">")

        def larger_error(larger_parameter, smaller_parameter):

            if(larger_parameter > smaller_parameter):
                return None
            else:
                raise ValueError("ERROR: Parameter <" + str(larger_parameter) + "> has to be greater then <" + str(smaller_parameter) + ">")

        def larger_equal_error(larger_parameter, smaller_parameter):

            if(larger_parameter >= smaller_parameter):
                return None
            else:
                raise ValueError("ERROR: Parameter <" + str(larger_parameter) + "> has to be greater or equal to/then <" + str(smaller_parameter) + ">")

        def equal_error(parameter_1, parameter_2):

            if(parameter_1 == parameter_2):
                return None
            else:
                raise ValueError("ERROR: Parameter <" + str(parameter_1) + "> and Parameter <" + str(parameter_2) + "> have to be the same value")






class onlyCheck():



    def range_error(rangeMin: float, rangeMax:float, parameter):
        """
        Takes in a range Minimum and a range Maximum. Throws an Error if the given parameter exceeds either of theese boundaries.\n
        If the maximum is None, it will be set to the int-limit(2147483647).
        """
        if(rangeMax == None):
            rangeMax = 2147483647
        if(parameter > rangeMax or parameter < rangeMin):
            return False

    def type_error(requiredDataType, parameter):
        """
        Checks if the given parameter can be translated / is from the given type. Data Type Name is for formatting purposes. If None, it will be '<class 'TYPE'>'.
        """
        if(requiredDataType == None):
            requiredDataType = str(requiredDataType)
        try:
            requiredDataType(parameter)
        except:
            return False

    def argument_error(parameter, *validArguments):
        """
        Checks if the given argument is contained in the validArguments.
        """
        if(parameter in validArguments):
            return None
        else:
            return False


    class relation():

        def smaller_error(smaller_parameter, larger_parameter):

            if(smaller_parameter < larger_parameter):
                return None
            else:
                return False

        def smaller_equal_error(smaller_parameter, larger_parameter):

            if(smaller_parameter <= larger_parameter):
                return None
            else:
                return False

        def larger_error(larger_parameter, smaller_parameter):

            if(larger_parameter > smaller_parameter):
                return None
            else:
                return False

        def larger_equal_error(larger_parameter, smaller_parameter):

            if(larger_parameter >= smaller_parameter):
                return None
            else:
                return False

        def equal_error(parameter_1, parameter_2):

            if(parameter_1 == parameter_2):
                return None
            else:
                return False

