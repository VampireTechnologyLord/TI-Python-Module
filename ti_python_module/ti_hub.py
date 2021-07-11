from ti_python_module.err import withConsole as err
from ti_python_module.err import onlyCheck as cerr
from ti_python_module.file_handler import create_log as log
"""
Class containing all TI-Hub commands. Used for debugging
"""



###########################################################################################

def text_at(line: int, text: str, align: str):
    """
    Displays "text" in plotting area at specified "align".

    Args:
        line (int): The line of the text. Possible Options: 'line, 'text', 'align'.
        text (str): The text of the displayed text.
        align (str): The texts alignment. Possible Options: 'left', 'center', 'right'.

    Returns:
        list: a list containing the following data: [line, text, align]
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
class colour():

    """
    Class for managing the RGB-LED commands for the TI-Hub

    Commands:
        rgb \n
        blink \n
        off \n
    """
    def rgb(red: int, green: int, blue: int):
        """
        Sets the rgb led to the given red, green and blue colours. Colours are ranging between 0 and 255.

        Args:
            red (int): The red value (0 - 255).
            green (int): The green value (0 - 255).
            blue (int): The blue value (0 - 255).

        Returns:
            list: a list containing the following data: [red, green, blue]
        """

        if cerr.type_error(int, red) == False: log("Argument 'red' has to be type integer!", "ERROR", "TI Hub", "Colour")
        if cerr.type_error(int, green) == False: log("Argument 'green' has to be type integer!", "ERROR", "TI Hub", "Colour")
        if cerr.type_error(int, blue) == False: log("Argument 'blue' has to be type integer!", "ERROR", "TI Hub", "Colour")

        if cerr.range_error(0, 255, red) == False: log("Argument 'arg' has to be between the values 0 and 255 (included)!", "ERROR", "TI Hub", "Colour")
        if cerr.range_error(0, 255, green) == False: log("Argument 'arg' has to be between the values 0 and 255 (included)!", "ERROR", "TI Hub", "Colour")
        if cerr.range_error(0, 255, blue) == False: log("Argument 'arg' has to be between the values 0 and 255 (included)!", "ERROR", "TI Hub", "Colour")

        if red == 0 and green == 0 and blue == 0: log("Please use the function 'colour.off()' instead of setting each value to 0, since this does not fully turn off the RGB-LED", "WARNING", "TI Hub", "Colour")

        err.type_error(int, "int", red)
        err.type_error(int, "int", green)
        err.type_error(int, "int", blue)

        err.range_error(0, 255, red)
        err.range_error(0, 255, green)
        err.range_error(0, 255, blue)
            
        log("Setting RGB-Led to '" + str(red) + "' red, '" + str(green) + "' green , '" + str(blue) + "' blue", "INFO", "TI Hub", "Colour")
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

        if cerr.type_error(float, frequency) == False: log("Argument 'frequency' has to be type integer!", "ERROR", "TI Hub", "Colour")
        if cerr.type_error(float, time) == False: log("Argument 'time' has to be type integer!", "ERROR", "TI Hub", "Colour")
        if cerr.range_error(0.1, 20, frequency) == False: log("Argument 'frequency' has to be between the values 0.1 and 20!", "ERROR", "TI Hub", "Colour")
        if cerr.range_error(0.1, 100, time) == False: log("Argument 'time' has to be between the values 0.1 and 100!", "ERROR", "TI Hub", "Colour")

        if frequency > 5 and time > 5: log("Blinking the LED at a high frequency for a longer time decreases its life-time!", "WARNING", "TI Hub", "Colour")

        err.type_error(float, "float", frequency)
        err.type_error(float, "float", time)
        err.range_error(0.1, 20, frequency)
        err.range_error(0.1, 100, time)

        log("Blinking the RGB-LED at a frequency of '" + str(frequency) + "' Hz for a time of '" + str(time) + "' seconds (" + str(time * frequency) + ") times", "INFO", "TI Hub", "Colour")
        print("Blinking the RGB-LED at a frequency of " + str(frequency) + "Hz for " + str(time) + " seconds (" + str(time * frequency) + ") times")
        return [frequency, time, time * frequency]


    ###########################################################################################

    def off():
        """
        Turns the RGB-LED off.

        Returns:
            None: None
        """

        log("Turning the RGB-LED off", "INFO", "TI Hub", "Colour")
        print("Turning RGB-LED off")
        return None

###########################################################################################

class light():

    """
    Class for managing the Light-LED commands for the TI-Hub

    Commands:
        on \n
        off \n
        blink \n
    """

    ###########################################################################################


    def off():
        """
        Turns the Light-LED off.

        Returns:
            None: None
        """
        log("Turned the Light-LED off", "INFO", "TI Hub", "Light")
        print("Turning Light-LED off")
        return None

    ###########################################################################################

    def on():
        """
        Turns the Light-LED on

        Returns:
            None: None
        """
        log("Turned the Light-LED on", "INFO", "TI Hub", "Light")
        print("Turning Light-LED on")
        return None

    ###########################################################################################

    def blink(frequency: float, time: float):
        """
        Blinks the Light-LED at the given frequency (in Hertz) for the given time. The frequency ranges between 0.1 - 20 Hz and the time between 0.1 - 100 seconds.

        Args:
            frequency (float): The frequency to blink in Hertz. Ranges from 0.1 to 20.
            time (float): The time to blink in seconds. Ranges from 0.1 to 100.

        Returns:
            list: a list containing the following data: [frequency, time, total_blinks]
        """

        if cerr.type_error(float, frequency) == False: log("Argument 'frequency' has to be type integer!", "ERROR", "TI Hub", "Light")
        if cerr.type_error(float, time) == False: log("Argument 'time' has to be type integer!", "ERROR", "TI Hub", "Light")
        if cerr.range_error(0.1, 20, frequency) == False: log("Argument 'frequency' has to be between the values 0.1 and 20!", "ERROR", "TI Hub", "Light")
        if cerr.range_error(0.1, 100, time) == False: log("Argument 'time' has to be between the values 0.1 and 100!", "ERROR", "TI Hub", "Light")

        if frequency > 5 and time > 5: log("Blinking the LED at a high frequency for a longer time decreases its life-time!", "WARNING", "TI Hub", "Light")

        err.type_error(float, "float", frequency)
        err.type_error(float, "float", time)
        err.range_error(0.1, 20, frequency)
        err.range_error(0.1, 100, time)

        log("Blinking the Light-LED at a frequency of '" + str(frequency) + "' Hz for a time of '" + str(time) + "' seconds (" + str(time * frequency) + ") times", "INFO", "TI Hub", "Light")
        print("Blinking the Light-LED at a frequency of " + str(frequency) + "Hz for " + str(time) + " seconds (" + str(time * frequency) + ") times")
        return [frequency, time, time * frequency]

###########################################################################################

class sound():
    """
    Class for managing the Sound commands for the TI-Hub

    Commands:
        tone \n
        note \n
    """


    ###########################################################################################

    def tone(frequency :float, duration :float):
        """
        Sets the speaker frequency to the given frequency for the given duration. The frequency ranges between 0 and 8000 Hz. The duration ranges between 0.1 and 100 seconds.

        Args:
            frequency (float): The frequency in Hertz. Ranges from 0.1 to 8000.
            duration (float): The duration of the tone. Ranges from 0.1 to 100.

        Returns:
            list: a list containing the following data: [frequency, duration]
        """

        if cerr.type_error(float, frequency) == False: log("Argument 'frequency' has to be type float!", "ERROR", "TI Hub", "Sound")
        if cerr.type_error(float, duration) == False: log("Argument 'duration' has to be type float!", "ERROR", "TI Hub", "Sound")

        if cerr.range_error(0.1, 8000, frequency) == False: log("Argument 'frequency' has to be between the values 0.1 and 8000 (included)!", "ERROR", "TI Hub", "Sound")
        if cerr.range_error(0.1, 100, duration) == False: log("Argument 'duration' has to be between the values 0.1 and 100 (included)!", "ERROR", "TI Hub", "Sound")


        err.type_error(float, "float", frequency)
        err.type_error(float, "float", duration)

        err.range_error(0.1, 8000, frequency)
        err.range_error(0.1, 100, duration)
            
        log("Setting the frequency of the speakers to '" + str(frequency) + "' Hz for a duration of '" + str(duration) + "' seconds", "INFO", "TI Hub", "Sound")
        print("Setting the speakers frequency to " + str(frequency) + "Hz for " + str(duration) + " seconds")
        return [frequency, duration]

    ###########################################################################################

    def note(note :str, duration :float):
        """
        Plays the given note for the given duration. An example for the note is 'A4'. The duration ranges between 0.1 and 100 seconds. The note names are `C, CS, D, DS, E, F, FS, G, GS, A, AS, and B`. The octave numbers range from 1 to 9 (inclusive).

        Args:
            note (str): The note to play with the octave. Example: `A2`, `CS3`.
            duration (float): The duration of the note in seconds. Ranges from 0.1 to 100.

        Returns:
            list: a list containing the following data: [note, duration]
        """

        if cerr.type_error(str, note) == False: log("Argument 'note' has to be type string!", "ERROR", "TI Hub", "Sound")
        if cerr.type_error(float, duration) == False: log("Argument 'duration' has to be type float!", "ERROR", "TI Hub", "Sound")

        if cerr.range_error(0.1, 100, duration) == False: log("Argument 'duration' has to be between the values 0.1 and 100!", "ERROR", "TI Hub", "Sound")

        if cerr.argument_error(note, "C1", "CS1", "D1", "DS1", "E1", "F1", "FS1", "G1", "GS1", "A1", "AS1", "B1", "C2", "CS2", "D2", "DS2", "E2", "F2", "FS2", "G2", "GS2", "A2", "AS2", "B2", "C3", "CS3", "D3", "DS3", "E3", "F3", "FS3", "G3", "GS3", "A3", "AS3", "B3", "C4", "CS4", "D4", "DS4", "E4", "F4", "FS4", "G4", "GS4", "A4", "AS4", "B4", "C5", "CS5", "D5", "DS5", "E5", "F5", "FS5", "G5", "GS5", "A5", "AS5", "B5", "C6", "CS6", "D6", "DS6", "E6", "F6", "FS6", "G6", "GS6", "A6", "AS6", "B6", "C7", "CS7", "D7", "DS7", "E7", "F7", "FS7", "G7", "GS7", "A7", "AS7", "B7", "C8", "CS8", "D8", "DS8", "E8", "F8", "FS8", "G8", "GS8", "A8", "AS8", "B8", "C9", "CS9", "D9", "DS9", "E9", "F9", "FS9", "G9", "GS9", "A9", "AS9", "B9") == False: log("Argument 'note' has to be one of these: 'C1', 'CS1', 'D1', 'DS1', 'E1', 'F1', 'FS1', 'G1', 'GS1', 'A1', 'AS1', 'B1', 'C2', 'CS2', 'D2', 'DS2', 'E2', 'F2', 'FS2', 'G2', 'GS2', 'A2', 'AS2', 'B2', 'C3', 'CS3', 'D3', 'DS3', 'E3', 'F3', 'FS3', 'G3', 'GS3', 'A3', 'AS3', 'B3', 'C4', 'CS4', 'D4', 'DS4', 'E4', 'F4', 'FS4', 'G4', 'GS4', 'A4', 'AS4', 'B4', 'C5', 'CS5', 'D5', 'DS5', 'E5', 'F5', 'FS5', 'G5', 'GS5', 'A5', 'AS5', 'B5', 'C6', 'CS6', 'D6', 'DS6', 'E6', 'F6', 'FS6', 'G6', 'GS6', 'A6', 'AS6', 'B6', 'C7', 'CS7', 'D7', 'DS7', 'E7', 'F7', 'FS7', 'G7', 'GS7', 'A7', 'AS7', 'B7', 'C8', 'CS8', 'D8', 'DS8', 'E8', 'F8', 'FS8', 'G8', 'GS8', 'A8', 'AS8', 'B8', 'C9', 'CS9', 'D9', 'DS9', 'E9', 'F9', 'FS9', 'G9', 'GS9', 'A9', 'AS9', 'B9'!", "ERROR", "TI Hub", "Sound")

        err.type_error(str, "str", note)
        err.type_error(float, "float", duration)

        err.range_error(0.1, 100, duration)

        err.argument_error(note, "C1", "CS1", "D1", "DS1", "E1", "F1", "FS1", "G1", "GS1", "A1", "AS1", "B1", "C2", "CS2", "D2", "DS2", "E2", "F2", "FS2", "G2", "GS2", "A2", "AS2", "B2", "C3", "CS3", "D3", "DS3", "E3", "F3", "FS3", "G3", "GS3", "A3", "AS3", "B3", "C4", "CS4", "D4", "DS4", "E4", "F4", "FS4", "G4", "GS4", "A4", "AS4", "B4", "C5", "CS5", "D5", "DS5", "E5", "F5", "FS5", "G5", "GS5", "A5", "AS5", "B5", "C6", "CS6", "D6", "DS6", "E6", "F6", "FS6", "G6", "GS6", "A6", "AS6", "B6", "C7", "CS7", "D7", "DS7", "E7", "F7", "FS7", "G7", "GS7", "A7", "AS7", "B7", "C8", "CS8", "D8", "DS8", "E8", "F8", "FS8", "G8", "GS8", "A8", "AS8", "B8", "C9", "CS9", "D9", "DS9", "E9", "F9", "FS9", "G9", "GS9", "A9", "AS9", "B9")
            
        log("Playing the note '" + note + "' for a duration of '" + duration + "' seconds", "INFO", "TI Hub", "Sound")
        print("Playing the note '" + note + "' for " + str(duration) + " second(s)")
        return [note, duration]

###########################################################################################

class brightness():
    """
    Class for managing the Brightness commands for the TI-Hub

    Commands:
        measurement \n
        range \n
    """


    ###########################################################################################

    def measurement():
        """
        Reads the built-in BRIGHTNESS (light level) sensor and returns a reading. The default range is 0 to 100. This can be changed using the 'range()' function.

        Returns:
            None: None
        """
        log("Reading the value currently measured by the brightness sensor", "INFO", "TI Hub", "Brightness")
        print("Reading Brightness Sensor")
        return None

    ###########################################################################################

    def range(self, min:float, max:float):
        """
        Sets the range for mapping the readings from the light level sensor.

        Args:
            min (float): The minimum range of the brightness sensor.
            max (float): The maximum range of the brightness sensor.

        Returns:
            list: a list containing the following data: [min, max]
        """

        if cerr.type_error(float, min) == False: log("Argument 'min' has to be type float!", "ERROR", "TI Hub", "Brightness")
        if cerr.type_error(float, max) == False: log("Argument 'max' has to be type float!", "ERROR", "TI Hub", "Brightness")


        err.type_error(float, "float", min)       
        err.type_error(float, "float", max)       

        log("Setting the value range of the brightness sensor from '" + str(min) + "' to '" + str(max) + "'", "INFO", "TI Hub", "Brightness")
        print("Setting the range of the brightness sensor to " + str(min) + " to " + str(max))
        return [min, max]

###########################################################################################

class dht():
    """
    This device outputs a list consisting of the current temperature, humidity, type of sensor, and last cached read status.

    Available Ports: 'IN 1', 'IN 2'


    Category: Hub / Add Input Device


    Returns None
    """

    def __init__(self, port:str) -> None:
        """
        This device outputs a list consisting of the current temperature, humidity, type of sensor, and last cached read status. Available Ports: 'IN 1', 'IN 2'.

        Args:
            port (str): The port of the device. Possible Options: 'IN 1', 'IN 2'.
        """

        if cerr.type_error(str, port) == False: log("Argument 'port' has to be type string!", "ERROR", "TI Hub", "DHT")
        if cerr.argument_error(port, "IN 1", "IN 2") == False: log("Argument 'port' can only be one of these: 'IN 1', 'IN 2'!", "ERROR", "TI Hub", "DHT")

        err.type_error(str, "str", port)
        err.argument_error(port, "IN 1", "IN 2")

        log("Setting the port for the device DHT to '" + port + "'", "INFO", "TI Hub", "DHT")
        print("Setting port for input device 'dht' to '" + port + "'")
        return


    def temp_measurement(self):
        """
        Measures the temperature from the dht sensor.

        Returns:
            None: None
        """

        log("Getting the measured temperature", "INFO", "TI Hub", "DHT")
        print("[dht] getting measured temperature")
        return None

    def humidity_measurement(self):
        """
        Measures the humidity from the dht sensor.

        Returns:
            None: None
        """
        log("Getting the measured humidity", "INFO", "TI Hub", "DHT")
        print("[dht] getting measured humidity")
        return None

    def t_h_measurement(self):
        """
        Measures the temperature and the humidity from the dht sensor.

        Returns:
            None: None
        """
        log("Getting the measured temperature and humidity", "INFO", "TI Hub", "DHT")
        print("[dht] getting measured temperature and humidity")
        return None
      
###########################################################################################

class ranger():
    """
    This device outputs the current distance measurement from the specified ultrasonic ranger.

    Available Ports: 'IN 1', 'IN 2'


    Category: Hub / Add Input Device


    Returns None
    """

    def __init__(self, port:str) -> None:
        """
        This device outputs the current distance measurement from the specified ultrasonic ranger. Available Ports: 'IN 1', 'IN 2'.

        Args:
            port (str): The port of the device. Possible Options: 'IN 1', 'IN 2'.
        """

        if cerr.type_error(str, port) == False: log("Argument 'port' has to be type string!", "ERROR", "TI Hub", "Ranger")
        if cerr.argument_error(port, "IN 1", "IN 2") == False: log("Argument 'port' can only be one of these: 'IN 1', 'IN 2'!", "ERROR", "TI Hub", "Ranger")

        err.type_error(str, "str", port)
        err.argument_error(port, "IN 1", "IN 2")

        log("Setting the port for the device Ranger to '" + port + "'", "INFO", "TI Hub", "Ranger")
        print("Setting port for input device 'dht' to '" + port + "'")
        return


    def measurement(self):
        """
        Returns the measured values from the ultrasonic-ranger sensor in cm.

        Returns:
            None: None
        """
        log("Getting the measured distance to the facing object in cm", "INFO", "TI Hub", "Ranger")
        print("[ultrasonic] getting measured distance in cm")
        return None

        
        
###########################################################################################

class light_level():
    """
    This device outputs the brightness level from the external light level (brightness) sensor.


    Available Ports: 'IN 1', 'IN 2', 'IN 3'


    Category: Hub / Add Input Device


    Returns None
    """

    def __init__(self, port:str) -> None:
        """
        This device outputs the brightness level from the external light level (brightness) sensor. Available Ports: 'IN 1', 'IN 2', 'IN 3'.

        Args:
            port (str): The port of the device. Possible Options: 'IN 1', IN 2', 'IN 3'.
        """

        if cerr.type_error(str, port) == False: log("Argument 'port' has to be type string!", "ERROR", "TI Hub", "Light Level")
        if cerr.argument_error(port, "IN 1", "IN 2", "IN 3") == False: log("Argument 'port' can only be one of these: 'IN 1', 'IN 2', 'IN 3'!", "ERROR", "TI Hub", "Light Level")

        err.type_error(str, "str", port)
        err.argument_error(port, "IN 1", "IN 2", "IN 3")

        log("Setting the port for the device Lightlevel Sensor to '" + port + "'", "INFO", "TI Hub", "Light Level")
        print("Setting port for input device 'light_level' to '" + port + "'")
        return

    def measurement(self):
        """
        Returns the measured light-level value.

        Returns:
            None: None
        """
        log("Getting the measured value of the lightlevel sensor", "INFO", "TI Hub", "Light Level")
        print("[light_level] getting measured brightness")
        return None
    def range(self, min:float, max:float):
        """
        Reconfigures the range of the light_level sensor.

        Args:
            min (float): The minimum range of the light level sensor.
            max (float): The maximum range of the light level sensor.

        Returns:
            list: a list containing the following data: [min, max]
        """

        if cerr.type_error(float, min) == False: log("Argument 'min' has to be type float!", "ERROR", "TI Hub", "Light Level")
        if cerr.type_error(float, max) == False: log("Argument 'max' has to be type float!", "ERROR", "TI Hub", "Light Level")


        err.type_error(float, "float", min)       
        err.type_error(float, "float", max)       

        log("Setting the value range of the light level sensor from '" + str(min) + "' to '" + str(max) + "'", "INFO", "TI Hub", "Light Level")
        print("Setting the range of the light level sensor to " + str(min) + " to " + str(max))
        return [min, max]

            
###########################################################################################

class temperature():
    """
    This device outputs the temperature reading from the external temperature sensor. The default configuration is to support the Seed temperature sensor in 'IN 1', 'IN 2' or 'IN 3' ports. To use the TI LM19 Temperature sensor from the TI-Innovator™ Hub breadboard pack, edit the port to the BB pin in use and use an optional argument Example: mylm19=temperature("BB 5","TIANALOG")


    Available Ports: 'IN 1', 'IN 2', 'IN 3'


    Category: Hub / Add Input Device


    Returns None
    """
    def __init__(self, port:str, extra:str=None) -> None:
        """
        This device outputs the temperature reading from the external temperature sensor. The default configuration is to support the Seed temperature sensor in 'IN 1', 'IN 2' or 'IN 3' ports. To use the TI LM19 Temperature sensor from the TI-Innovator™ Hub breadboard pack, edit the port to the BB pin in use and use an optional argument Example: mylm19=temperature("BB 5","TIANALOG"). Available Ports: 'IN 1', 'IN 2', 'IN 3'.

        Args:
            port (str): The port for the device. Possible Options: 'IN 1', 'IN 2', 'IN 3'.
            extra (str, optional): The optional additional Port. Information for checks are missing here. Defaults to None.
        """
        if cerr.type_error(str, port) == False: log("Argument 'port' has to be type string!", "ERROR", "TI Hub", "Temperature")
        if cerr.type_error(str, extra) == False: log("Argument 'extra' has to be type string!", "ERROR", "TI Hub", "Temperature")
        if cerr.argument_error(port, "IN 1", "IN 2", "IN 3") == False: log("Argument 'port' can only be one of these: 'IN 1', 'IN 2', 'IN 3'!", "ERROR", "TI Hub", "Temperature")
        if extra != None: log("Due to missing documentation, it is not possible to check, which options are available for argument 'extra'!", "WARNING", "TI Hub", "Temperature")

        err.type_error(str, "str", port)
        err.argument_error(port, "IN 1", "IN 2", "IN 3")

        log("Setting the port for device temperature sensor to '" + port + "' with the extra argument '" + str(extra) + "'", "INFO", "TI Hub", "Temperature")
        print("Setting port for input device 'temperature' to '" + port + "'")
        return


    def measurement(self):
        """
        Gets the measured temperature.

        Returns:
            None: None
        """
        log("Getting the measured value of the temperature sensor", "INFO", "TI Hub", "Temperature")
        print("[temperature] getting measued temperature")
        return None
        
###########################################################################################

class moisture():
    """
    This device outputs the moisture sensor reading.


    Available Ports: 'IN 1', 'IN 2', 'IN 3'


    Category: Hub / Add Input Device


    Returns None
    """
    def __init__(self, port:str) -> None:
        """
        This device outputs the moisture sensor reading. Available Ports: 'IN 1', 'IN 2', 'IN 3'.

        Args:
            port (str): The port of the device. Available Options: 'IN 1', 'IN 2', 'IN 3'.
        """
        if cerr.type_error(str, port) == False: log("Argument 'port' has to be type string!", "ERROR", "TI Hub", "Moisture")
        if cerr.argument_error(port, "IN 1", "IN 2", "IN 3") == False: log("Argument 'port' can only be one of these: 'IN 1', 'IN 2', 'IN 3'!", "ERROR", "TI Hub", "Moisture")

        err.type_error(str, "str", port)
        err.argument_error(port, "IN 1", "IN 2", "IN 3")

        log("Setting the port for device moisture Sensor to '" + port + "'", "INFO", "TI Hub", "Moisture")
        print("Setting port for input device 'moisture' to '" + port + "'")
        return

    def measurement(self):
        """
        Gets the measured moisture.

        Returns:
            None: None
        """
        log("Getting the measured value of the moisture sensor", "INFO", "TI Hub", "Moisture")
        print("[moisture] getting measued moisture")
        return None

    def range(self, min:float, max:float):
        """
        Reconfigures the range of the moisture sensor.

        Args:
            min (float): The minimum range of the moisture sensor.
            max (float): The maximum range of the moisture sensor.

        Returns:
            list: a list containing the following data: [min, max]
        """

        if cerr.type_error(float, min) == False: log("Argument 'min' has to be type float!", "ERROR", "TI Hub", "Moisture")
        if cerr.type_error(float, max) == False: log("Argument 'max' has to be type float!", "ERROR", "TI Hub", "Moisture")


        err.type_error(float, "float", min)       
        err.type_error(float, "float", max)       

        log("Setting the value range of the moisture sensor from '" + str(min) + "' to '" + str(max) + "'", "INFO", "TI Hub", "Moisture")
        print("Setting the range of the moisture sensor to " + str(min) + " to " + str(max))
        return [min, max]
        
###########################################################################################

class magnetic():
    """
    This device detects the presence of a magnetic field. The threshold value to determine the presence of the field is set through the trigger() function. The default value of the threshold is 150. Available Ports: 'IN 1', 'IN 2', 'IN 3'


    Category: Hub / Add Input Device


    Returns None
    """
    def __init__(self, port:str) -> None:
        """
        This device detects the presence of a magnetic field. The threshold value to determine the presence of the field is set through the trigger() function. The default value of the threshold is 150. Available Ports: 'IN 1', 'IN 2', 'IN 3'.

        Args:
            port (str): The port of the device. Possible Options: 'IN 1', 'IN 2', 'IN 3'.
        """

        if cerr.type_error(str, port) == False: log("Argument 'port' has to be type string!", "ERROR", "TI Hub", "Magnetic")
        if cerr.argument_error(port, "IN 1", "IN 2", "IN 3") == False: log("Argument 'port' can only be one of these: 'IN 1', 'IN 2', 'IN 3'!", "ERROR", "TI Hub", "Magnetic")

        err.type_error(str, "str", port)
        err.argument_error(port, "IN 1", "IN 2", "IN 3")

        log("Setting the port for device magnetic Sensor to '" + port + "'", "INFO", "TI Hub", "Magnetic")
        print("Setting port for input device 'magnetic' to '" + port + "'")
        return

    def measurement(self):
        """
        Returns the measured magnetic value.

        Returns:
            None: None
        """
        log("Measuring the magnetic value", "INFO", "TI Hub", "Magnetic")
        print("[magnetic] measuring magnetic value")
        return None

    def magnet_close(self):
        """
        Says, whether a magnet is close, by checking if the magnetic value is over the threshold. This can be changed using the threshold function.

        Returns:
            None: None
        """
        log("Checking, if a magnet is close to the sensor, by using the value modifyable with the 'threshold()' function", "INFO", "TI Hub", "Magnetic")
        print("[magnetic] checking if magnet is close (magnetic value is over threshold)")
        return None

    def trigger(self, threshold:int):
        """
        Sets the threshold of the magnetic value, at which the magnet_close functions triggers. This ranges from 0 to 16383. The default is 150.

        Args:
            threshold (int): The threshold, at which the function `magnet_close()` returns True.

        Returns:
            list: a list containing the following data: [threshold]
        """
        if err.type_error(int, threshold) == False: log("Argument 'threshold' has to be type integer!", "ERROR", "TI Hub", "Magnetic")
        if err.range_error(0, 16383, threshold) == False: log("Argument 'threshold' has to be between the values 0 and 16383 (included)!", "ERROR", "TI Hub", "Magnetic")

        err.type_error(int, "int", threshold)
        err.range_error(0, 16383, threshold)

        log("Setting the threshold for the function 'magnet_close()' to " + str(threshold) + "'", "INFO", "TI Hub", "Magnetic")
        print("[magnetic] setting threshold to '" + str(threshold) + "'")
        return [threshold]

###########################################################################################

class vernier():
    """
    This device reads the value from the vernier analog sensor specified by the <sensor_type>.\n
    Supported Features:\n
    • temperature - Stainless Steel Temperature sensor.\n
    • lightlevel - TI Light level sensor.\n
    • pressure - Original gas pressure sensor\n
    • pressure2 - Newer gas pressure sensor.\n
    • pH - pH sensor.\n
    • force10 - ±10 N setting, Dual Force Sensor.\n
    • force50 - ±50 N setting, Dual Force Sensor.\n
    • accelerometer - Low-G Accelerometer.\n
    • generic - Allows setting of other sensors not supported directly above, and use of the calibrate() API above to set equation coefficients\n<


    Available Ports: 'IN 1', 'IN 2', 'IN 3'


    Category: Hub / Add Input Device


    Returns an array / list: [port]
    """
    def __init__(self, port:str, sensor_type:str) -> None:
        """
        This device reads the value from the vernier analog sensor specified by the <sensor_type>.\n
        Supported Features:\n
        • temperature - Stainless Steel Temperature sensor.\n
        • lightlevel - TI Light level sensor.\n
        • pressure - Original gas pressure sensor\n
        • pressure2 - Newer gas pressure sensor.\n
        • pH - pH sensor.\n
        • force10 - ±10 N setting, Dual Force Sensor.\n
        • force50 - ±50 N setting, Dual Force Sensor.\n
        • accelerometer - Low-G Accelerometer.\n
        • generic - Allows setting of other sensors not supported directly above, and use of the calibrate() API above to set equation coefficients\n<

        Args:
            port (str): The port for the device. Possible Options: 'IN 1', 'IN 2', 'IN 3'.
            sensor_type (str): The type of sensor. Possible option: 'temperature', 'lightlevel', 'pressure', 'pressure2', 'pH', 'force10', 'force50', 'accelerometer', 'generic'.
        
        Returns:
            None: None
        """

        

        if cerr.type_error(str, port) == False: log("Argument 'port' has to be type string!", "ERROR", "TI Hub", "Vernier")
        if cerr.type_error(str, sensor_type) == False: log("Argument 'sensor_type' has to be type string!", "ERROR", "TI Hub", "Vernier")
        if cerr.argument_error(port, "IN 1", "IN 2", "IN 3") == False: log("Argument 'port' can only be one of these: 'IN 1', 'IN 2', 'IN 3'!", "ERROR", "TI Hub", "Vernier")
        if cerr.argument_error(sensor_type, "temperature", "lightlevel", "pressure", "pressure2", "pH", "force10", "force50", "accelerometer", "generic") == False: log("Argument 'sensor_type' can only be one of these: 'temperature', 'lightlevel', 'pressure', 'pressure2', 'pH', 'force10', 'force50', 'accelerometer', 'generic'!", "ERROR", "TI Hub", "Vernier")

        err.type_error(str, "str", port)
        err.type_error(str, "str", sensor_type)
        err.argument_error(port, "IN 1", "IN 2", "IN 3")
        err.argument_error(sensor_type, "temperature", "lightlevel", "pressure", "pressure2", "pH", "force10", "force50", "accelerometer", "generic")

        log("Setting the port of the vernier sensor to '" + port + "' with the sensor / measurement type '" + sensor_type + "'", "INFO", "TI Hub", "Vernier")
        print("Setting port for input device 'vernier' to '" + port + "' with sensor type '" + sensor_type + "'")
        return

    def measurement(self):
        """
        Returns the measured magnetic value.

        Returns:
            None: None
        """
        log("Measuring the value of the specified sensor", "INFO", "TI Hub", "Vernier")
        print("[vernier] measuring value of set sensor")
        return None

    def calibrate(self, a, b, c = None, d = None):
        """
        Calibrates the sensor. Use type 1: a, b ==> linear: ax + b. Use type 2: a, b, c, d.

        Args:
            a ([type]): Argument 1 of a linear or normal calibration.
            b ([type]): Argument 2 of a linear or normal calibration.
            c ([type], optional): Argument 3 of a normal calibration. Also requires argument `d`. Defaults to None.
            d ([type], optional): Argument 4 of a normal caibration. Defaults to None.

        Raises:
            ValueError: If only a, b, c are specified, while d is unspecified.

        Returns:
            list: a list containing the following data: [a, b, c, d]
        """
        if(c == None and d == None):
            log("Calibrating linearly (ax + b) with the values '" + str(a) + "' as 'a' and '" + str(b) + "' as 'b'", "INFO", "TI Hub", "Vernier")
            print("[vernier] calibrating linearly with '" + str(a) + "' and '" + str(b) + "'")
        elif(c != None and d == None):
            log("You need to specify 'c' and 'd', if you want to use 'c' too!", "ERROR", "TI Hub", "Vernier")
            raise ValueError("ERROR: If you specify 'c' you also need to specify 'd'")
        else:
            log("Calibrating with the values '" + str(a) + "' as 'a' and '" + str(b) + "' as 'b' and '" + str(c) + "' as 'c' and '" + str(d) + "' as 'd'" , "INFO", "TI Hub", "Vernier")
            print("[vernier] calibrating with '" + str(a) + "', '" + str(b) + "', '" + str(c) + "' and '" + str(d) + "'")

        return [a, b, c, d]

        
        
###########################################################################################

class analog_in():

    """
    This device supports the use of analog input generic devices.



    Available Ports: 'IN 1', 'IN 2', 'IN 3', 'BB 5', 'BB 6', 'BB 7'


    Category: Hub / Add Input Device


    Returns None
    """
    def __init__(self, port:str) -> None:
        """
        This device supports the use of analog input generic devices. Available Ports: 'IN 1', 'IN 2', 'IN 3', 'BB 5', 'BB 6', 'BB 7'.

        Args:
            port (str): The port of the device. Possible Options: 'IN 1', 'IN 2', 'IN 3', 'BB 5', 'BB 6', 'BB 7'.
        """

        if cerr.type_error(str, port) == False: log("Argument 'port' has to be type string!", "ERROR", "TI Hub", "Analog In")
        if cerr.argument_error(port, "IN 1", "IN 2", "IN 3", "BB 5", "BB 6", "BB 7") == False: log("Argument 'port' can only be one of these: 'IN 1', 'IN 2', 'IN 3', 'BB 5', 'BB 6', 'BB 7'!", "ERROR", "TI Hub", "Analog In")

        err.type_error(str, "str", port)
        err.argument_error(port, "IN 1", "IN 2", "IN 3", "BB 5", "BB 6", "BB 7")

        log("Setting the port for the device analog_in to '" + port + "'", "INFO", "TI Hub", "Analog In")
        print("Setting port for input device 'analog_in' to '" + port + "'")
        return

    def measurement(self):
        """
        Outputs the measured value from the sensor set to 'analog_in'.

        Returns:
            None: None
        """
        log("Getting value measured by the sensor at 'analog in'", "INFO", "TI Hub", "Analog In")
        print("[analog_in] measuring sensor value")
        return None

    def range(self, min:float, max:float):
        """
        Reconfigures the range of the sensor set to `analog_in`.

        Args:
            min (float): The minimum range of the sensor at `analog_in`.
            max (float): The maximum range of the sensor at `analog_in`.

        Returns:
            list: a list containing the following data: [min, max]
        """

        if cerr.type_error(float, min) == False: log("Argument 'min' has to be type float!", "ERROR", "TI Hub", "Analog In")
        if cerr.type_error(float, max) == False: log("Argument 'max' has to be type float!", "ERROR", "TI Hub", "Analog In")


        err.type_error(float, "float", min)       
        err.type_error(float, "float", max)       

        log("Setting the value range of the sensor at 'analog_in' from '" + str(min) + "' to '" + str(max) + "'", "INFO", "TI Hub", "Analog In")
        print("Setting the range of the sensor at 'analog_in' to " + str(min) + " to " + str(max))
        return [min, max]
        
        
###########################################################################################

class potentiometer():
    """
    This device supports a potentiometer sensor. The range of the sensor can be changed by the range() function.



    Available Ports: 'IN 1', 'IN 2', 'IN 3', 'BB 5', 'BB 6', BB 7'


    Category: Hub / Add Input Device


    Returns None
    """
    def __init__(self, port:str) -> None:
        """
        This device supports a potentiometer sensor. The range of the sensor can be changed by the range() function. Available Ports: 'IN 1', 'IN 2', 'IN 3', 'BB 5', 'BB 6', 'BB 7'.

        Args:
            port (str): The port of the device. Possible Options: 'IN 1', 'IN 2', 'IN 3', 'BB 5', 'BB 6', 'BB 7'.
        """

        if cerr.type_error(str, port) == False: log("Argument 'port' has to be type string!", "ERROR", "TI Hub", "Potentiometer")
        if cerr.argument_error(port, "IN 1", "IN 2", "IN 3", "BB 5", "BB 6", "BB 7") == False: log("Argument 'port' can only be one of these: 'IN 1', 'IN 2', 'IN 3', 'BB 5', 'BB 6', 'BB 7'!", "ERROR", "TI Hub", "Potentiometer")

        err.type_error(str, "str", port)
        err.argument_error(port, "IN 1", "IN 2", "IN 3", "BB 5", "BB 6", "BB 7")

        log("Setting the port for the potentiometer to '" + port + "'", "INFO", "TI Hub", "Potentiometer")
        print("Setting port for potentiometer to '" + port + "'")
        return

    def measurement(self):
        """
        Outputs the measured value from the potentiometer.

        Returns:
            None: None
        """
        log("Getting value measured by the potentiometer", "INFO", "TI Hub", "Potentiometer")
        print("[potentiometer] measuring sensor value")
        return None

    def range(self, min:float, max:float):
        """
        Reconfigures the range of the potentiometer.

        Args:
            min (float): The minimum range of the potentiometer.
            max (float): The maximum range of the potentiometer.

        Returns:
            list: a list containing the following data: [min, max]
        """

        if cerr.type_error(float, min) == False: log("Argument 'min' has to be type float!", "ERROR", "TI Hub", "Potentiometer")
        if cerr.type_error(float, max) == False: log("Argument 'max' has to be type float!", "ERROR", "TI Hub", "Potentiometer")


        err.type_error(float, "float", min)       
        err.type_error(float, "float", max)       

        log("Setting the value range of the potentiometer from '" + str(min) + "' to '" + str(max) + "'", "INFO", "TI Hub", "Potentiometer")
        print("Setting the range of the potentiometer to " + str(min) + " to " + str(max))
        return [min, max]
        
###########################################################################################

class thermistor():
    """
    This device reads thermistor sensors. The default coefficients are designed to match the thermistor included in the Breadboard Pack of the TI-Innovator™ Hub, when used with a 10KΩ fixed resistor. A new set of calibration coefficients and reference resistance for the thermistor can be configured using the calibrate() function.



    Available Ports: 'IN 1', 'IN 2', 'IN 3', 'BB 5', 'BB 6', BB 7'


    Category: Hub / Add Input Device


    Returns None
    """
    def __init__(self, port:str) -> None:
        """
        This device reads thermistor sensors. The default coefficients are designed to match the thermistor included in the Breadboard Pack of the TI-Innovator™ Hub, when used with a 10KΩ fixed resistor. A new set of calibration coefficients and reference resistance for the thermistor can be configured using the calibrate() function. Available Ports: 'IN 1', 'IN 2', 'IN 3', 'BB 5', 'BB 6', BB 7'.

        Args:
            port (str): The port for the device. Possible Options: 'IN 1', 'IN 2', 'IN 3', 'BB 5', 'BB 6', BB 7'.
        """

        if cerr.type_error(str, port) == False: log("Argument 'port' has to be type string!", "ERROR", "TI Hub", "Thermistor")
        if cerr.argument_error(port, "IN 1", "IN 2", "IN 3", "BB 5", "BB 6", "BB 7") == False: log("Argument 'port' can only be one of these: 'IN 1', 'IN 2', 'IN 3', 'BB 5', 'BB 6', 'BB 7'!", "ERROR", "TI Hub", "Thermistor")

        err.type_error(str, "str", port)
        err.argument_error(port, "IN 1", "IN 2", "IN 3", "BB 5", "BB 6", "BB 7")

        log("Setting the port for the thermistor to '" + port + "'", "INFO", "TI Hub", "Thermistor")
        print("Setting port for input device thermistor to '" + port + "'")
        return

    def measurement(self):
        """
        Outputs the measured value from the thermistor.

        Returns:
            None: None
        """
        log("Getting value measured by the thermistor", "INFO", "TI Hub", "Thermistor")
        print("[thermistor] measuring sensor value")
        return None

    def calibrate(self, a, b, c = None, d = None):
        """
        Calibrates the sensor. Use type 1: a, b ==> linear: ax + b. Use type 2: a, b, c, d.

        Args:
            a ([type]): Argument 1 of a linear or normal calibration.
            b ([type]): Argument 2 of a linear or normal calibration.
            c ([type], optional): Argument 3 of a normal calibration. Also requires argument `d`. Defaults to None.
            d ([type], optional): Argument 4 of a normal caibration. Defaults to None.

        Raises:
            ValueError: If only a, b, c are specified, while d is unspecified.

        Returns:
            list: a list containing the following data: [a, b, c, d]
        """
        if(c == None and d == None):
            log("Calibrating linearly (ax + b) with the values '" + str(a) + "' as 'a' and '" + str(b) + "' as 'b'", "INFO", "TI Hub", "Thermistor")
            print("[thermistor] calibrating linearly with '" + str(a) + "' and '" + str(b) + "'")
        elif(c != None and d == None):
            log("You need to specify 'c' and 'd', if you want to use 'c' too!", "ERROR", "TI Hub", "Thermistor")
            raise ValueError("ERROR: If you specify 'c' you also need to specify 'd'")
        else:
            log("Calibrating with the values '" + str(a) + "' as 'a' and '" + str(b) + "' as 'b' and '" + str(c) + "' as 'c' and '" + str(d) + "' as 'd'" , "INFO", "TI Hub", "Thermistor")
            print("[thermistor] calibrating with '" + str(a) + "', '" + str(b) + "', '" + str(c) + "' and '" + str(d) + "'")

        return [a, b, c, d]
        
###########################################################################################

class loudness():
    """
    This device supports sound loudness sensors.


    Available Ports: 'IN 1', 'IN 2', 'IN 3'


    Category: Hub / Add Input Device


    Returns None
    """
    def __init__(self, port:str) -> None:
        """
        This device supports sound loudness sensors. Available Ports: 'IN 1', 'IN 2', 'IN 3'.

        Args:
            port (str): The port of the device. Possible Options: 'IN 1', 'IN 2', 'IN 3'.
        """

        if cerr.type_error(str, port) == False: log("Argument 'port' has to be type string!", "ERROR", "TI Hub", "Loudness")
        if cerr.argument_error(port, "IN 1", "IN 2", "IN 3") == False: log("Argument 'port' can only be one of these: 'IN 1', 'IN 2', 'IN 3'!", "ERROR", "TI Hub", "Loudness")

        err.type_error(str, "str", port)
        err.argument_error(port, "IN 1", "IN 2", "IN 3")

        log("Setting the port for the loudness sensor to '" + port + "'", "INFO", "TI Hub", "Loudness")
        print("Setting port for loudness sensor to '" + port + "'")
        return

    def measurement(self):
        """
        Outputs the measured value from the loudness sensor.

        Returns:
            None: None
        """
        log("Getting value measured by the loudness sensor", "INFO", "TI Hub", "Loudness")
        print("[loudness] measuring sensor value")
        return None

    def range(self, min:float, max:float):
        """
        Reconfigures the range of the loudness sensor.

        Args:
            min (float): The minimum range of the loudness sensor.
            max (float): The maximum range of the loudness sensor.

        Returns:
            list: a list containing the following data: [min, max]
        """

        if cerr.type_error(float, min) == False: log("Argument 'min' has to be type float!", "ERROR", "TI Hub", "Loudness")
        if cerr.type_error(float, max) == False: log("Argument 'max' has to be type float!", "ERROR", "TI Hub", "Loudness")


        err.type_error(float, "float", min)       
        err.type_error(float, "float", max)       

        log("Setting the value range of the loudness sensor from '" + str(min) + "' to '" + str(max) + "'", "INFO", "TI Hub", "Loudness")
        print("Setting the range of the loudness sensor to " + str(min) + " to " + str(max))
        return [min, max]
###########################################################################################
class colour_input():

    """
    This device provides interfaces to an I2C-connected Color Input sensor. The bb_port pin is used in addition to the I2C port to control the LED on the color sensor.\n
    • color_number(): Returns a value from 1 to 9 that represents the color the sensor is detecting. The numbers represent the colors per the following mapping:\n
        1: Red\n
        2: Green\n
        3: Blue\n
        4: Cyan\n
        5: Magenta\n
        6: Yellow\n
        7: Black\n
        8: White\n
        9: Gray\n

    • red(): Returns a value from 0 to 255 that represents the intensity of the RED color level being detected.\n
    • green(): Returns a value from 0 to 255 that represents the intensity of the GREEN color level being detected.\n
    • blue(): Returns a value from 0 to 255 that represents the intensity of the BLUE color level being detected.\n
    • gray(): Returns a value from 0 to 255 that represents the gray level being detected, where 0 is black and 255 is white.\n



    Available Ports: 'BB 1', 'BB 2', 'BB 3', 'BB 4', 'BB 5', 'BB 6', 'BB 7', 'BB 8', 'BB 9', 'BB 10'


    Category: Hub / Add Input Device


    Returns None
    """
    
    
    def __init__(self, port:str) -> None:
        """
        This device provides interfaces to an I2C-connected Color Input sensor. The bb_port pin is used in addition to the I2C port to control the LED on the color sensor.\n
        • color_number(): Returns a value from 1 to 9 that represents the color the sensor is detecting. The numbers represent the colors per the following mapping:\n
            1: Red\n
            2: Green\n
            3: Blue\n
            4: Cyan\n
            5: Magenta\n
            6: Yellow\n
            7: Black\n
            8: White\n
            9: Gray\n

        • red(): Returns a value from 0 to 255 that represents the intensity of the RED color level being detected.\n
        • green(): Returns a value from 0 to 255 that represents the intensity of the GREEN color level being detected.\n
        • blue(): Returns a value from 0 to 255 that represents the intensity of the BLUE color level being detected.\n
        • gray(): Returns a value from 0 to 255 that represents the gray level being detected, where 0 is black and 255 is white.\n
        Available Ports: 'BB 1', 'BB 2', 'BB 3', 'BB 4', 'BB 5', 'BB 6', 'BB 7', 'BB 8', 'BB 9', 'BB 10'.

        Args:
            port (str): The port of the device. Possible Options: 'BB 1', 'BB 2', 'BB 3', 'BB 4', 'BB 5', 'BB 6', 'BB 7', 'BB 8', 'BB 9', 'BB 10'.
        """
        
        
        if cerr.type_error(str, port) == False: log("Argument 'port' has to be type string!", "ERROR", "TI Hub", "Colour Input")
        if cerr.argument_error(port, "BB 1", "BB 2", "BB 3", "BB 4", "BB 5", "BB 6", "BB 7", "BB 8", "BB 9", "BB 10") == False: log("Argument 'port' has to be one of these values: 'BB 1', 'BB 2', 'BB 3', 'BB 4', 'BB 5', 'BB 6', 'BB 7', 'BB 8', 'BB 9', 'BB 10'!", "ERROR", "TI Hub", "Colour Input")

        err.type_error(str, "str", port)
        err.argument_error(port, "BB 1", "BB 2", "BB 3", "BB 4", "BB 5", "BB 6", "BB 7", "BB 8", "BB 9", "BB 10")

        log("Setting the port for the colour input sensor to '" + port + "'", "INFO", "TI Hub", "Colour Input")
        print("Setting port for input device 'colour_input' to '" + port + "'")
        return
            
    

    def colour_number(self):
        """
        Returns a value from 1 to 9 that represents the color the sensor is detecting. The numbers represent the colors per the following mapping:\n
            1: Red\n
            2: Green\n
            3: Blue\n
            4: Cyan\n
            5: Magenta\n
            6: Yellow\n
            7: Black\n
            8: White\n
            9: Gray\n
        """
        log("Fetching the number of the colour by the predefined mapping", "INFO", "TI Hub", "Colour Input")
        print("[Colour_Input] fetching colour number")
        return None
    
    def red(self):
        """
        Returns a value from 0 to 255 that represents the intensity of the RED color level being detected.\n
        """
        log("Fetching the amount of 'red' in the measured colour. Ranges from 0 to 255 (inclusive)", "INFO", "TI Hub", "Colour Input")
        print("[Colour_Input] fetching red value")
        return None
    
    def green(self):
        """
        Returns a value from 0 to 255 that represents the intensity of the GREEN color level being detected.\n
        """
        log("Fetching the amount of 'green' in the measured colour. Ranges from 0 to 255 (inclusive)", "INFO", "TI Hub", "Colour Input")
        print("[Colour_Input] fetching green value")
        return None
    
    def blue(self):
        """
        Returns a value from 0 to 255 that represents the intensity of the BLUE color level being detected.\n
        """
        log("Fetching the amount of 'blue' in the measured colour. Ranges from 0 to 255 (inclusive)", "INFO", "TI Hub", "Colour Input")
        print("[Colour_Input] fetching blue value")
        return None

    def gray(self):
        """
        Returns a value from 0 to 255 that represents the gray level being detected, where 0 is black and 255 is white.\n
        """
        log("Fetching the amount of 'gray' in the measured colour. Ranges from 0 to 255 (inclusive). 0 is black and 255 is white", "INFO", "TI Hub", "Colour Input")
        print("[Colour_Input] fetching gray value")
        return None

###########################################################################################

class hub_time():
    """
    This device provides access to the internal millisecond timer of the HUB.


    Category: Hub / Add Input Device


    Returns None
    """
    def __init__(self) -> None:
        """
        This device provides access to the internal millisecond timer of the HUB.
        """
        return

    def measurement(self):
        """
        Outputs the measured value from the 'hub_time'.

        Returns:
            None: None
        """
        log("Fetching the value of the internal millisecond timer of the HUB", "INFO", "TI Hub", "Hub Time")
        print("[hub_time] Fetching millisecond timer of HUB")
        return None

    def reset_time(self):
        """
        Resets the HUB-intern millisecond counter.

        Returns:
            None: None
        """
        log("Resetting the internal millisecond timer of the HUB", "INFO", "TI Hub", "Hub Time")
        print("[hub_time] resetting hub timer")
        return None

###########################################################################################
class rgb_array():
    """
    Provides functions for programming the TI-RGB Array. The initialization function accepts an optional "LAMP" parameter to enable a high-brightness mode for the TI-RGB Array that requires an external power supply.\n
    • set(led_position, r,g,b): Sets a specific led_position (0-15) to the specified r,g,b value, where r,g,b are values from 0 to 255.\n
    • set_all(r,g,b): Sets all RGB LEDs in the array to the same r,g,b value.\n
    • all_off(): Turns off all RGBs in the array.\n
    • measurement(): Returns the approximate current draw that the RGB array is using from the TI-Innovator™ in milliAmps.\n
    • pattern(pattern): Using the value of the argument as a binary value in the range 0 to 65535, turns on pixels where a 1 value in the representation would be. LEDs are turned on as RED with pwm level value of 255.


    Category: Hub / Add Input Device


    Returns None
    """
    def __init__(self) -> None:
        """
        Provides functions for programming the TI-RGB Array. The initialization function accepts an optional "LAMP" parameter to enable a high-brightness mode for the TI-RGB Array that requires an external power supply.\n
        • set(led_position, r,g,b): Sets a specific led_position (0-15) to the specified r,g,b value, where r,g,b are values from 0 to 255.\n
        • set_all(r,g,b): Sets all RGB LEDs in the array to the same r,g,b value.\n
        • all_off(): Turns off all RGBs in the array.\n
        • measurement(): Returns the approximate current draw that the RGB array is using from the TI-Innovator™ in milliAmps.\n
        • pattern(pattern): Using the value of the argument as a binary value in the range 0 to 65535, turns on pixels where a 1 value in the representation would be. LEDs are turned on as RED with pwm level value of 255.
        """
    def set(self, position:int, red:int, green:int, blue:int):
        """
        Sets a specific led_position (0-15) to the specified r,g,b value, where r,g,b are values from 0 to 255.

        Args:
            position (int): The LED position. Ranges from 0 to 15.
            red (int): The red part of the colour. Ranges from 0 to 255.
            green (int): The green part of the colour. Ranges from 0 to 255.
            blue (int): The blue part of the colour. Ranges from 0 to 255.

        Returns:
            list: a list containing the following data: [position, red, green, blue]
        """
        if cerr.type_error(int, position) == False: log("Argument 'position' has to be type integer!", "ERROR", "TI Hub", "RGB Array")
        if cerr.type_error(int, red) == False: log("Argument 'red' has to be type integer!", "ERROR", "TI Hub", "RGB  Array")
        if cerr.type_error(int, green) == False: log("Argument 'green' has to be type integer!", "ERROR", "TI Hub", "RG Array")
        if cerr.type_error(int, blue) == False: log("Argument 'blue' has to be type integer!", "ERROR", "TI Hub", "RGB Array")

        if cerr.range_error(0, 15, position) == False: log("Argument 'position' has to be between the values 0 and 15 (included)", "ERROR", "TI Hub", "RGB Array")
        if cerr.range_error(0, 255, red) == False: log("Argument 'red' has to be between the values 0 and 255 (included)!", "ERROR", "TI Hub", "RGB Array")
        if cerr.range_error(0, 255, green) == False: log("Argument 'green' has to be between the values 0 and 255 (included)!", "ERROR", "TI Hub", "RGB Array")
        if cerr.range_error(0, 255, blue) == False: log("Argument 'blue' has to be between the values 0 and 255 (included)!", "ERROR", "TI Hub", "RGB Array")

        err.type_error(int, "int", position)
        err.type_error(int, "int", red)
        err.type_error(int, "int", green)
        err.type_error(int, "int", blue)

        err.range_error(0, 15, position)
        err.range_error(0, 255, red)
        err.range_error(0, 255, green)
        err.range_error(0, 255, blue)

          
        log("Setting the LED-Position of the LEDs at the RGB Array to '" + str(position) + "' with the RGB-Values '" + str(red) + " red', '"+ str(green) + " green', '" + str(blue) + " blue'", "INFO", "TI Hub", "RGB Array")
        print("[RGB-Array] Setting the LED-Position to '" + str(position) + "' with the RGB-Values '" + str(red) + " red', '"+ str(green) + " green', '" + str(blue) + " blue'")
        return [position, red, green, blue]


    def set_all(self, red:int, green:int, blue:int):
        """
        Sets all RGB LEDs in the array to the same r,g,b value.

        Args:
            red (int): The red part of the colour. Ranges from 0 to 255.
            green (int): The green part of the colour. Ranges from 0 to 255.
            blue (int): The blue part of the colour. Ranges from 0 to 255.

        Returns:
            list: a list containing the following data: [red, green, blue]
        """
        if cerr.type_error(int, red) == False: log("Argument 'red' has to be type integer!", "ERROR", "TI Hub", "RGB  Array")
        if cerr.type_error(int, green) == False: log("Argument 'green' has to be type integer!", "ERROR", "TI Hub", "RG Array")
        if cerr.type_error(int, blue) == False: log("Argument 'blue' has to be type integer!", "ERROR", "TI Hub", "RGB Array")

        if cerr.range_error(0, 255, red) == False: log("Argument 'red' has to be between the values 0 and 255 (included)!", "ERROR", "TI Hub", "RGB Array")
        if cerr.range_error(0, 255, green) == False: log("Argument 'green' has to be between the values 0 and 255 (included)!", "ERROR", "TI Hub", "RGB Array")
        if cerr.range_error(0, 255, blue) == False: log("Argument 'blue' has to be between the values 0 and 255 (included)!", "ERROR", "TI Hub", "RGB Array")

        err.type_error(int, "int", red)
        err.type_error(int, "int", green)
        err.type_error(int, "int", blue)

        err.range_error(0, 255, red)
        err.range_error(0, 255, green)
        err.range_error(0, 255, blue)
            
        log("Setting all RGB-LEDs from the RGB Array to the RGB-Values '" + str(red) + " red', '"+ str(green) + " green', '" + str(blue) + " blue'", "INFO", "TI Hub", "RGB Array")
        print("[RGB-Array] Setting all RGB-LEDs to the RGB-Values '" + str(red) + " red', '"+ str(green) + " green', '" + str(blue) + " blue'")
        return [red, green, blue]


    def all_off(self):
        """
        Turns off all RGB LEDs in the array.

        Returns:
            None: None
        """
        log("Turning off all RGB-LEDs in the Array", "INFO", "TI Hub", "RGB Array")
        print("[RGB-Array] Turning off all RGB LEDs")
        return None

    def measurement(self):
        """
        Returns the approximate current draw that the RGB array is using from the TI-Innovator™ in milliAmps.

        Returns:
            None: None
        """
        log("Measuring the current energy draw of the RGB Array", "INFO", "TI Hub", "RGB Array")
        print("[RGB-Array] measuring current draw of the HUB")
        return None

    def pattern(self, pattern:int):
        """
        Using the value of the argument as a binary value in the range 0 to 65535, turns on pixels where a 1 value in the representation would be. LEDs are turned on as RED with pwm level value of 255.

        Args:
            pattern (int): The value for the pattern. 0 - 65535

        Returns:
            list: a list containing the following data: [pattern]
        """
        if cerr.type_error(int, pattern) == False: log("Argument 'pattern' has to be type integer!", "ERROR", "TI Hub", "RGB Array")
        if cerr.range_error(0, 65535, pattern) == False: log("Argument 'pattern' has to be between the values 0 and 65535 (included)!", "ERROR", "TI Hub", "RGB Array")

        err.type_error(int, "int", pattern)

        err.range_error(0, 65535, pattern)

        decoded_pattern = bin(pattern)

        log("Turning on the LEDs from binary value '" + str(pattern) + "'. '1 => on'  '2 => off'. Pattern: '" + decoded_pattern + "'", "INFO", "TI Hub", "RGB Array")
        print("[RGB-Array] Turning on pixels from binary value '" + str(pattern) + "' (1 => on ; 0 => off)")
        return [pattern]

###########################################################################################

class led():
    """
    This device manages functions for controlling externally connected LEDs.


    Available Ports: 'OUT 1', 'OUT 2', 'OUT 3'
    
    
    Category: Hub / Add Output Device
    
    
    Returns None
    """
    def __init__(self, port:str) -> None:
        """
        This device manages functions for controlling externally connected LEDs. Available Ports: 'OUT 1', 'OUT 2', 'OUT 3'.

        Args:
            port (str): The port of the device. Possible Options: 'OUT 1', 'OUT 2', 'OUT 3'.
        """
        if cerr.type_error(str, port) == False: log("Argument 'port' has to be type string!", "ERROR", "TI Hub", "LED")
        if cerr.argument_error(port, "OUT 1", "OUT 2", "OUT 3") == False: log("Argument 'port' has to be one of these values: 'OUT 1', 'OUT 2', 'OUT 3'!", "ERROR", "TI Hub", "LED")


        err.type_error(str, "str", port)

        err.argument_error(port, "OUT 1", "OUT 2", "OUT 3")

        log("Setting the port for the device LED to '" + port + "'", "INFO", "TI Hub", "LED")
        print("Setting port for output device 'led' to '" + port + "'")
        return
    
    def on(self):
        """
        Turns the led on.
        """
        log("Turning the LED on", "INFO", "TI Hub", "LED")
        print("Setting output device 'led' to 'on'")

    def off(self):
        """
        Turns the led off.
        """
        log("Turning the LED off", "INFO", "TI Hub", "LED")
        print("Setting output device 'led' to 'off'")

    def blink(self, frequency:int, time:int):
        """
        Blinks the led for the given time in seconds with the set frequency in Hz.

        Returns:
            list: a list containing the following data: [frequency, time, total_blinks]
        """
        if cerr.type_error(int, frequency) == False: log("Argument 'frequency' has to be type integer", "ERROR", "TI Hub", "LED")
        if cerr.type_error(int, time) == False: log("Argument 'time' has to be type integer", "ERROR", "TI Hub", "LED")

        if cerr.range_error(1, 20, frequency) == False: log("Argument 'frequency' has to be between the values 1 and 20", "ERROR", "TI Hub", "LED")
        if cerr.range_error(1, 100, time) == False: log("Argument 'time' has to be between the values 1 and 100", "ERROR", "TI Hub", "LED")

        if frequency > 5 and time > 5: log("Blinking the LED at a high frequency for a longer time decreases its life-time!", "WARNING", "TI Hub", "LED")

        err.type_error(int, "int", frequency)
        err.type_error(int, "int", time)

        err.range_error(1, 20, frequency)
        err.range_error(1, 100, time)

        log("Blinking the LED for '" + str(time) + "' seconds with a frequency of '" + str(frequency) + "' Hz. (" + str(time * frequency) + ") times.", "INFO", "TI Hub", "LED")
        print("Blinking output device 'led' for '" + str(time) + " seconds' with a frequency of '" + str(frequency) + " Hz'. (" + str(time * frequency) + ") times.")
        return [frequency, time, time * frequency]
###########################################################################################

class rgb():
    """
    Description


    Available Ports: 'OUT 1', 'OUT 2', 'OUT 3'
    
    
    Category: Hub / Add Output Device
    
    
    Returns None
    """
    def __init__(self, port:str) -> None:
        """
        Description


        Available Ports: 'OUT 1', 'OUT 2', 'OUT 3'
        
        
        Category: Hub / Add Output Device
        
        
        Returns None
        """
        err.type_error(str, "str", port)

        err.argument_error(port, "OUT 1", "OUT 2", "OUT 3")

        log("Setting the port for the RGB-LED to '" + port + "'", "INFO", "TI Hub", "RGB")
        print("Setting port for output device 'rgb' to '" + port + "'")
        return

    def off(self):
        """
        Turns the led off.
        """
        log("Turning the LED off", "INFO", "TI Hub", "RGB")
        print("Setting output device 'rgb' to 'off'")

    def blink(self, frequency:int, time:int):
        """
        Blinks the led for the given time in seconds with the set frequency in Hz.

        Returns:
            list: a list containing the following data: [frequency, time, total_blinks]
        """
        if cerr.type_error(int, frequency) == False: log("Argument 'frequency' has to be type integer", "ERROR", "TI Hub", "RGB")
        if cerr.type_error(int, time) == False: log("Argument 'time' has to be type integer", "ERROR", "TI Hub", "RGB")

        if cerr.range_error(1, 20, frequency) == False: log("Argument 'frequency' has to be between the values 1 and 20", "ERROR", "TI Hub", "RGB")
        if cerr.range_error(1, 100, time) == False: log("Argument 'time' has to be between the values 1 and 100", "ERROR", "TI Hub", "RGB")

        if frequency > 5 and time > 5: log("Blinking the LED at a high frequency for a longer time decreases its life-time!", "WARNING", "TI Hub", "RGB")

        err.type_error(int, "int", frequency)
        err.type_error(int, "int", time)

        err.range_error(1, 20, frequency)
        err.range_error(1, 100, time)

        log("Blinking the RGB-LED for '" + str(time) + "' seconds with a frequency of '" + str(frequency) + "' Hz. (" + str(time * frequency) + ") times.", "INFO", "TI Hub", "RGB")
        print("Blinking output device 'rgb' for '" + str(time) + " seconds' with a frequency of '" + str(frequency) + " Hz'. (" + str(time * frequency) + ") times.")

    def rgb(red: int, green: int, blue: int):
        """
        Sets the rgb led to the given red, green and blue colours. Colours are ranging between 0 and 255.

        Args:
            red (int): The red value (0 - 255).
            green (int): The green value (0 - 255).
            blue (int): The blue value (0 - 255).

        Returns:
            list: a list containing the following data: [red, green, blue]
        """

        if cerr.type_error(int, red) == False: log("Argument 'red' has to be type integer!", "ERROR", "TI Hub", "RGB")
        if cerr.type_error(int, green) == False: log("Argument 'green' has to be type integer!", "ERROR", "TI Hub", "RGB")
        if cerr.type_error(int, blue) == False: log("Argument 'blue' has to be type integer!", "ERROR", "TI Hub", "RGB")

        if cerr.range_error(0, 255, red) == False: log("Argument 'arg' has to be between the values 0 and 255 (included)!", "ERROR", "TI Hub", "RGB")
        if cerr.range_error(0, 255, green) == False: log("Argument 'arg' has to be between the values 0 and 255 (included)!", "ERROR", "TI Hub", "RGB")
        if cerr.range_error(0, 255, blue) == False: log("Argument 'arg' has to be between the values 0 and 255 (included)!", "ERROR", "TI Hub", "RGB")

        if red == 0 and green == 0 and blue == 0: log("Please use the function 'rgb.off()' instead of setting each value to 0, since this does not fully turn off the RGB-LED", "WARNING", "TI Hub", "RGB")

        err.type_error(int, "int", red)
        err.type_error(int, "int", green)
        err.type_error(int, "int", blue)

        err.range_error(0, 255, red)
        err.range_error(0, 255, green)
        err.range_error(0, 255, blue)
            
        log("Setting RGB-Led to '" + str(red) + "' red, '" + str(green) + "' green , '" + str(blue) + "' blue", "INFO", "TI Hub", "RGB")
        print("Setting RGB-Led to Red: " + str(red) + ", Green: " + str(green) + ", Blue: " + str(blue))
        return [red, green, blue]
###########################################################################################

class speaker():
    """
    This device manages functions for supporting an external speaker with the TI-Innovator™ Hub. The functions are the same as the ones for "tone".

    
    
    Available Ports: 'OUT 1', 'OUT 2', 'OUT 3', 'BB 1', 'BB 2', 'BB 3', 'BB 4', 'BB 5', 'BB 6', 'BB 7', 'BB 8', 'BB 9', 'BB 10'


    Category: Hub / Add Output Device


    Returns None
    """
    def __init__(self, port:str) -> None:
        """
        This device manages functions for supporting an external speaker with the TI-Innovator™ Hub. The functions are the same as the ones for "tone". Available Ports: 'OUT 1', 'OUT 2', 'OUT 3', 'BB 1', 'BB 2', 'BB 3', 'BB 4', 'BB 5', 'BB 6', 'BB 7', 'BB 8', 'BB 9', 'BB 10'.

        Args:
            port (str): The port of the device. Possible Options:
        """

        if cerr.type_error(str, port) == False: log("Argument 'port' has to be type string!", "ERROR", "TI Hub", "Speaker")

        if cerr.argument_error(port, "OUT 1", "OUT 2", "OUT 3", "BB 1", "BB 2", "BB 3", "BB 4", "BB 5", "BB 6", "BB 7", "BB 8", "BB 9", "BB 10") == False: log("Argument 'port' has to be one of these: 'OUT 1', 'OUT 2', 'OUT 3', 'BB 1', 'BB 2', 'BB 3', 'BB 4', 'BB 5', 'BB 6', 'BB 7', 'BB 8', 'BB 9', 'BB 10'!", "ERROR", "TI Hub", "Speaker")

        err.type_error(str, "str", port)

        err.argument_error(port, "OUT 1", "OUT 2", "OUT 3", "BB 1", "BB 2", "BB 3", "BB 4", "BB 5", "BB 6", "BB 7", "BB 8", "BB 9", "BB 10")

        log("Setting the port for the speakers to '" + port + "'", "INFO", "TI Hub", "Speaker")
        print("Setting port for output device 'speaker' to '" + port + "'")
        return

    def tone(frequency :float, duration :float):
        """
        Sets the speaker frequency to the given frequency for the given duration. The frequency ranges between 0 and 8000 Hz. The duration ranges between 0.1 and 100 seconds.

        Args:
            frequency (float): The frequency in Hertz. Ranges from 0.1 to 8000.
            duration (float): The duration of the tone. Ranges from 0.1 to 100.

        Returns:
            list: a list containing the following data: [frequency, duration]
        """

        if cerr.type_error(float, frequency) == False: log("Argument 'frequency' has to be type float!", "ERROR", "TI Hub", "Speaker")
        if cerr.type_error(float, duration) == False: log("Argument 'duration' has to be type float!", "ERROR", "TI Hub", "Speaker")

        if cerr.range_error(0.1, 8000, frequency) == False: log("Argument 'frequency' has to be between the values 0.1 and 8000 (included)!", "ERROR", "TI Hub", "Speaker")
        if cerr.range_error(0.1, 100, duration) == False: log("Argument 'duration' has to be between the values 0.1 and 100 (included)!", "ERROR", "TI Hub", "Speaker")


        err.type_error(float, "float", frequency)
        err.type_error(float, "float", duration)

        err.range_error(0.1, 8000, frequency)
        err.range_error(0.1, 100, duration)
            
        log("Setting the frequency of the speakers to '" + str(frequency) + "' Hz for a duration of '" + str(duration) + "' seconds", "INFO", "TI Hub", "Speaker")
        print("Setting the speakers frequency to " + str(frequency) + "Hz for " + str(duration) + " seconds")
        return [frequency, duration]

    ###########################################################################################

    def note(note :str, duration :float):
        """
        Plays the given note for the given duration. An example for the note is 'A4'. The duration ranges between 0.1 and 100 seconds. The note names are `C, CS, D, DS, E, F, FS, G, GS, A, AS, and B`. The octave numbers range from 1 to 9 (inclusive).

        Args:
            note (str): The note to play with the octave. Example: `A2`, `CS3`.
            duration (float): The duration of the note in seconds. Ranges from 0.1 to 100.

        Returns:
            list: a list containing the following data: [note, duration]
        """

        if cerr.type_error(str, note) == False: log("Argument 'note' has to be type string!", "ERROR", "TI Hub", "Speaker")
        if cerr.type_error(float, duration) == False: log("Argument 'duration' has to be type float!", "ERROR", "TI Hub", "Speaker")

        if cerr.range_error(0.1, 100, duration) == False: log("Argument 'duration' has to be between the values 0.1 and 100!", "ERROR", "TI Hub", "Speaker")

        if cerr.argument_error(note, "C1", "CS1", "D1", "DS1", "E1", "F1", "FS1", "G1", "GS1", "A1", "AS1", "B1", "C2", "CS2", "D2", "DS2", "E2", "F2", "FS2", "G2", "GS2", "A2", "AS2", "B2", "C3", "CS3", "D3", "DS3", "E3", "F3", "FS3", "G3", "GS3", "A3", "AS3", "B3", "C4", "CS4", "D4", "DS4", "E4", "F4", "FS4", "G4", "GS4", "A4", "AS4", "B4", "C5", "CS5", "D5", "DS5", "E5", "F5", "FS5", "G5", "GS5", "A5", "AS5", "B5", "C6", "CS6", "D6", "DS6", "E6", "F6", "FS6", "G6", "GS6", "A6", "AS6", "B6", "C7", "CS7", "D7", "DS7", "E7", "F7", "FS7", "G7", "GS7", "A7", "AS7", "B7", "C8", "CS8", "D8", "DS8", "E8", "F8", "FS8", "G8", "GS8", "A8", "AS8", "B8", "C9", "CS9", "D9", "DS9", "E9", "F9", "FS9", "G9", "GS9", "A9", "AS9", "B9") == False: log("Argument 'note' has to be one of these: 'C1', 'CS1', 'D1', 'DS1', 'E1', 'F1', 'FS1', 'G1', 'GS1', 'A1', 'AS1', 'B1', 'C2', 'CS2', 'D2', 'DS2', 'E2', 'F2', 'FS2', 'G2', 'GS2', 'A2', 'AS2', 'B2', 'C3', 'CS3', 'D3', 'DS3', 'E3', 'F3', 'FS3', 'G3', 'GS3', 'A3', 'AS3', 'B3', 'C4', 'CS4', 'D4', 'DS4', 'E4', 'F4', 'FS4', 'G4', 'GS4', 'A4', 'AS4', 'B4', 'C5', 'CS5', 'D5', 'DS5', 'E5', 'F5', 'FS5', 'G5', 'GS5', 'A5', 'AS5', 'B5', 'C6', 'CS6', 'D6', 'DS6', 'E6', 'F6', 'FS6', 'G6', 'GS6', 'A6', 'AS6', 'B6', 'C7', 'CS7', 'D7', 'DS7', 'E7', 'F7', 'FS7', 'G7', 'GS7', 'A7', 'AS7', 'B7', 'C8', 'CS8', 'D8', 'DS8', 'E8', 'F8', 'FS8', 'G8', 'GS8', 'A8', 'AS8', 'B8', 'C9', 'CS9', 'D9', 'DS9', 'E9', 'F9', 'FS9', 'G9', 'GS9', 'A9', 'AS9', 'B9'!", "ERROR", "TI Hub", "Speaker")

        err.type_error(str, "str", note)
        err.type_error(float, "float", duration)

        err.range_error(0.1, 100, duration)

        err.argument_error(note, "C1", "CS1", "D1", "DS1", "E1", "F1", "FS1", "G1", "GS1", "A1", "AS1", "B1", "C2", "CS2", "D2", "DS2", "E2", "F2", "FS2", "G2", "GS2", "A2", "AS2", "B2", "C3", "CS3", "D3", "DS3", "E3", "F3", "FS3", "G3", "GS3", "A3", "AS3", "B3", "C4", "CS4", "D4", "DS4", "E4", "F4", "FS4", "G4", "GS4", "A4", "AS4", "B4", "C5", "CS5", "D5", "DS5", "E5", "F5", "FS5", "G5", "GS5", "A5", "AS5", "B5", "C6", "CS6", "D6", "DS6", "E6", "F6", "FS6", "G6", "GS6", "A6", "AS6", "B6", "C7", "CS7", "D7", "DS7", "E7", "F7", "FS7", "G7", "GS7", "A7", "AS7", "B7", "C8", "CS8", "D8", "DS8", "E8", "F8", "FS8", "G8", "GS8", "A8", "AS8", "B8", "C9", "CS9", "D9", "DS9", "E9", "F9", "FS9", "G9", "GS9", "A9", "AS9", "B9")
            
        log("Playing the note '" + note + "' for a duration of '" + duration + "' seconds", "INFO", "TI Hub", "Speaker")
        print("Playing the note '" + note + "' for " + str(duration) + " second(s)")
        return [note, duration]
        
###########################################################################################
class power():
    """
    Manages functions for controlling external power with the TI-Innovator™ Hub.\n
    • set(value): Sets the Power level to the specified value, between 0 and 100.\n
    • on(): Sets the Power level to 100.\n
    • off(): Sets the Power level to 0.\n



    Available Ports: 'OUT 1', 'OUT 2', 'OUT 3'


    Category: Hub / Add Output Device


    Returns None
    """

    def __init__(self, port:str) -> None:
        """
        Manages functions for controlling external power with the TI-Innovator™ Hub.\n
        • set(value): Sets the Power level to the specified value, between 0 and 100.\n
        • on(): Sets the Power level to 100.\n
        • off(): Sets the Power level to 0.\n

        Args:
            port (str): The port of the device. Possible Options: 'OUT 1', 'OUT 2', 'OUT 3'.
        """
        if cerr.type_error(str, port) == False: log("Argument 'port' has to be type string!", "ERROR", "TI Hub", "Power")

        if cerr.argument_error(port, "OUT 1", "OUT 2", "OUT 3") == False: log("Argument 'port' has to be one of these: 'OUT 1', 'OUT 2', 'OUT 3'!", "ERROR", "TI Hub", "Power")

        err.type_error(str, "str", port)

        err.argument_error(port, "OUT 1", "OUT 2", "OUT 3")

        log("Setting the port of the power device to '" + port + "'", "INFO", "TI Hub", "Power")
        print("Setting port for output device 'power' to '" + port + "'")
        return 
            

    def set(self, value:int):
        """
        Sets the Power level to the specified value, between 0 and 100.

        Returns:
            list: a list containing the following data: [value]
        """
        if cerr.type_error(int, value) == False: log("Argument value has to be type integer!", "ERROR", "TI Hub", "Power")

        if cerr.range_error(0, 100, value) == False: log("Argument value has to be between the values 0 and 100!", "ERROR", "TI Hub", "Power")

        err.type_error(int, "int", value)

        err.range_error(0, 100, value)
            
        log("Setting the powerlevel of the power device to '" + str(value) + "'", "INFO", "TI Hub", "Power")
        print("[Power] Setting the powerlevel to '" + str(value) + "'")
        return [value]

    def on(self):
        """
        Sets the powerlevel to 100
        """
        log("Setting the powerlevel to 100", "INFO", "TI Hub", "Power")
        print("[Power] Setting the powerlevel to '100'")
        return None

    def off(self):
        """
        Sets the powerlevel to 0
        """
        log("Setting the powerlevel to 0", "INFO", "TI Hub", "Power")
        print("[Power] Setting the powerlevel to '0'")
        return

###########################################################################################
class continuous_servo():

    """
    Manages functions for controlling continuous servo motors.\n
    • set_cw(speed,time): The servo will spin in the clockwise direction at the specified speed (0-255) and for the specific duration in seconds.\n
    • set_ccw(speed,time): The servo will spin in the counter-clockwise direction at the specified speed (0-255) and for the specific duration in seconds.\n
    • stop(): Stops the continuous servo.


    Available Ports: 'OUT 3'
   
    
    Category: Hub / Add Output Device
  
    
    Returns None
    """

    def __init__(self, port:str) -> None:
        
        """
        Manages functions for controlling continuous servo motors.\n
        • set_cw(speed,time): The servo will spin in the clockwise direction at the specified speed (0-255) and for the specific duration in seconds.\n
        • set_ccw(speed,time): The servo will spin in the counter-clockwise direction at the specified speed (0-255) and for the specific duration in seconds.\n
        • stop(): Stops the continuous servo.

        args:
            port (str): The port of the device. Possible Options: 'OUT 3'.
        """
        if cerr.type_error(str, port) == False: log("Argument 'port' has to be type string!", "ERROR", "TI Hub", "Continuous Servo")

        if cerr.argument_error(port, "OUT 3") == False: log("Argument 'port' has to be one of these: 'OUT 3'!", "ERROR", "TI Hub", "Continuous Servo")

        err.type_error(str, "str", port)

        err.argument_error(port, "OUT 3")

        log("Setting the port for the continuous servo to '" + port + "'", "INFO", "TI Hub", "Continuous Servo")
        print("Setting port for output device 'continuous_servo' to '" + port + "'")
        return
    
            


    def set_cw(self, speed:int, time:float):
        """
        The servo will spin in the clockwise direction at the specified speed (0-255) and for the specific duration in seconds.

        Args:
            speed (int): The speed of the continuous servo. Ranges from 0 to 255.
            time (float): The duration of how long the continuous servo spins. Ranges from 0.1 to 100.

        Returns:
            list: a list containing the following data: [speed, time]
        """

        if cerr.type_error(int, speed) == False: log("Argument 'speed' has to be type integer!", "ERROR", "TI Hub", "Continuous Servo")
        if cerr.type_error(float, time) == False: log("Argument 'time' has to be type float!", "ERROR", "TI Hub", "Continuous Servo")

        if cerr.range_error(0, 255, speed) == False: log("Argument 'speed' has to be between the values 0 and 255!", "ERROR", "TI Hub", "Continuous Servo")
        if cerr.range_error(0.1, 100, time) == False: log("Argument 'time' has to be between the values 0.1 and 100!", "ERROR", "TI Hub", "Continuous Servo")

        if speed == 0: log("Please use 'continuous_servo(\"OUT 3\").stop()' if you want to turn it off instead of setting the speed to 0, since this does not turn the servo off", "WARNING", "TI Hub", "Continuous Servo")

        err.type_error(int, "int", speed)
        err.type_error(float, "float", time)

        err.range_error(0, 255, speed)
        err.range_error(0.1, 100, time)

            
        log("Spinning the continuous servo clockwise for '" + str(time) + "' seconds with a speed of '" + str(speed) + "'", "INFO", "TI Hub", "Continuous Servo")
        print("[Continuous Servo] Spinning the servo clockwise for '" + str(time) + "' seconds with speed '" + str(speed) + "'")
        return [speed, time]

    def set_xcw(self, speed:int, time:float):
        """
        The servo will spin in the anti-clockwise direction at the specified speed (0-255) and for the specific duration in seconds.

        Args:
            speed (int): The speed of the continuous servo. Ranges from 0 to 255.
            time (float): The duration of how long the continuous servo spins. Ranges from 0.1 to 100.

        Returns:
            list: a list containing the following data: [speed, time]
        """

        if cerr.type_error(int, speed) == False: log("Argument 'speed' has to be type integer!", "ERROR", "TI Hub", "Continuous Servo")
        if cerr.type_error(float, time) == False: log("Argument 'time' has to be type float!", "ERROR", "TI Hub", "Continuous Servo")

        if cerr.range_error(0, 255, speed) == False: log("Argument 'speed' has to be between the values 0 and 255!", "ERROR", "TI Hub", "Continuous Servo")
        if cerr.range_error(0.1, 100, time) == False: log("Argument 'time' has to be between the values 0.1 and 100!", "ERROR", "TI Hub", "Continuous Servo")

        if speed == 0: log("Please use 'continuous_servo(\"OUT 3\").stop()' if you want to turn it off instead of setting the speed to 0, since this does not turn the servo off", "WARNING", "TI Hub", "Continuous Servo")

        err.type_error(int, "int", speed)
        err.type_error(float, "float", time)

        err.range_error(0, 255, speed)
        err.range_error(0.1, 100, time)

            
        log("Spinning the continuous servo anti-clockwise for '" + str(time) + "' seconds with a speed of '" + str(speed) + "'", "INFO", "TI Hub", "Continuous Servo")
        print("[Continuous Servo] Spinning the servo anti-clockwise for '" + str(time) + "' seconds with speed '" + str(speed) + "'")
        return [speed, time]

    def stop(self):
        """
        Stops the continuous servo.
        """
        log("Stopping the continuous servo", "INFO", "TI Hub", "Continuous Servo")
        print("[Continuous Servo] Stopping the continuous servo")
        return None

###########################################################################################

class analog_out():
    """
    Functions for the use of analog input generic devices.
    
    
    Available Ports: 'OUT 1', 'OUT 2', 'OUT 3', 'BB 1', 'BB 2', 'BB 3', 'BB 4', 'BB 5', 'BB 6', 'BB 7', 'BB 8', 'BB 9', 'BB 10'
    
    
    Category: Hub / Add Output Device
    
    
    Returns None
    """
    def __init__(self, port:str) -> None:
        """
        Functions for the use of analog input generic devices. Available Ports: 'OUT 1', 'OUT 2', 'OUT 3', 'BB 1', 'BB 2', 'BB 3', 'BB 4', 'BB 5', 'BB 6', 'BB 7', 'BB 8', 'BB 9', 'BB 10'.

        Args:
            port (str): The port of the device. Possible Options: 'OUT 1', 'OUT 2', 'OUT 3', 'BB 1', 'BB 2', 'BB 3', 'BB 4', 'BB 5', 'BB 6', 'BB 7', 'BB 8', 'BB 9', 'BB 10'.
        """
        if cerr.type_error(str, port) == False: log("Argument 'port' has to be type string!", "ERROR", "TI Hub", "Analog Out")
        if cerr.argument_error(port, "OUT 1", "OUT 2", "OUT 3", "BB 1", "BB 2", "BB 3", "BB 4", "BB 5", "BB 6", "BB 7", "BB 8", "BB 9", "BB 10") == False: log("Argument 'port' has to be one of these: 'OUT 1', 'OUT 2', 'OUT 3', 'BB 1', 'BB 2', 'BB 3', 'BB 4', 'BB 5', 'BB 6', 'BB 7', 'BB 8', 'BB 9', 'BB 10!", "ERROR", "TI Hub", "Analog Out")


        err.type_error(str, "str", port)

        err.argument_error(port, "OUT 1", "OUT 2", "OUT 3", "BB 1", "BB 2", "BB 3", "BB 4", "BB 5", "BB 6", "BB 7", "BB 8", "BB 9", "BB 10")
        
        log("Setting the port for the output device set to analog out to '" + port + "'", "INFO", "TI Hub", "Analog Out")
        print("Setting port for output device 'analog_out' to '" + port + "'")
        return

    def off(self):
        """
        Setts the output device set as 'analog out' to off.
        """
        log("Turning off the device set as analog out", "INFO", "TI Hub", "Analog Out")
        print("Setting output device for 'analog_out' to 'off'")
        return None
    def on(self):
        """
        Setts the output device set as 'analog out' to on.
        """
        log("Turning on the device set as analog out", "INFO", "TI Hub", "Analog Out")
        print("Setting output device for 'analog_out' to 'on'")
        return None

    def set(self, value:float):
        """
        Setts the value of the output device set as 'analog out'.
        """
        if cerr.type_error(float, value) == False: log("Argument 'value' has to be type float!", "ERROR", "TI Hub", "Analog Out")
        if cerr.range_error(0, None, value) == False: log("Argument 'value' has to be greater then 0!", "ERROR", "TI Hub", "Analog Out")

        err.type_error(float, "float", value)
        err.range_error(0, None, value)
        log("Setting the value of the output device set as analog out to '" + str(value) + "'", "INFO", "TI Hub", "Analog Out")
        print("Setting the value of output device 'analog_out' to '" + str(value) + "'")
        return [value]

###########################################################################################

class vibration_motor():
    """
    Manages functions for controlling vibration motors.\n
    • set(val): Sets the vibration motor intensity to "val" (0-255).\n
    • off(): Turns the vibration motor off.\n
    • on(): Turns the vibration motor on at the highest level.\n


    Available Ports: 'OUT 3'
   
    
    Category: Hub / Add Output Device
  
    
    Returns None
    """

    def __init__(self, port:str) -> None:
        """
        Manages functions for controlling vibration motors.\n
        • set(val): Sets the vibration motor intensity to "val" (0-255).\n
        • off(): Turns the vibration motor off.\n
        • on(): Turns the vibration motor on at the highest level.\n

        Args:
            port (str): The port of the device. Possible Options: 'OUT 3'.
        """

        if cerr.type_error(str,port) == False: log("Argument 'port' has to be type string!", "ERROR", "TI Hub", "Vibration Motor")

        if cerr.argument_error(port, "OUT 3") == False: log("Argument 'port' has to be one of these: 'OUT 3'!", "ERROR", "TI Hub", "Vibration Motor")


        err.type_error(str, "str", port)

        err.argument_error(port, "OUT 3")

        log("Setting the port of the vibration motor to '" + port + "'", "INFO", "TI Hub", "Vibration Motor")
        print("Setting port for output device 'vibration_motor' to '" + port + "'")
        return
            

    def set(self, value:int):
        """
         Sets the vibration motor intensity to the given value.

        Args:
            value (int): The intensity of the motor (0 - 255).

        Returns:
            list: a list containing the following data: [value]
        """
        if cerr.type_error(int, value) == False: log("Argument 'value' has to be type integer!", "ERROR", "TI Hub", "Vibration Motor")
        
        if cerr.range_error(0, 255, value) == False: log("Argument 'value' has to be between the values 0 and 255!", "ERROR", "TI Hub", "Vibration Motor")

        if value == 0: log("If you want to turn the vibration motor off, please use 'vibration_motor(\"OUT 3\").off()' instead, since this might not turn the motor fully off'", "WARNING", "TI Hub", "Vibration Motor")

        err.type_error(int, "int", value)
        
        err.range_error(0, 255, value)
            

        log("Setting the intensity of the vibration motor to '" + str(value) + "'", "INFO", "TI Hub", "Vibration Motor")
        print("[Vibration Motor] Setting the intensity of the vibration motor to '" + str(value) + "'")
        return [value]

    def off(self):
        """
        Turns the vibration motor off.
        """
        log("Turning the vibration motor off", "INFO", "TI Hub", "Vibration Motor")
        print("[Vibration Motor] Turning the motor off")
        return None

    def on(self):
        """
        Turns the vibration motor on (intensity: 255).
        """
        log("Turning the vibration motor on (intensity: 255)", "INFO", "TI Hub", "Vibration Motor")
        print("[Vibration Motor] Setting the intensity of the vibration motor to '255'")
        return None

###########################################################################################

class relay():
    """
    Controls interfaces for controlling relays.\n
    • on(): Sets the relay to the ON state.\n
    • off(): Sets the relay to the OFF state.


    Available Ports: 'OUT 3'
   
    
    Category: Hub / Add Output Device
  
    
    Returns None
    """

    def __init__(self, port:str) -> None:
        """
        Controls interfaces for controlling relays.\n
        • on(): Sets the relay to the ON state.\n
        • off(): Sets the relay to the OFF state.

        Args:
            port (str): The port of the device. Possible Options: 'OUT 3'.
        """

        if cerr.type_error(str, port) == False: log("Argument 'port' has to be type string!", "ERROR", "TI Hub", "Relay")
        
        if cerr.argument_error(port, "OUT 3") == False: log("Argument 'port' has to be one of these: 'OUT 3'!", "ERROR", "TI Hub", "Relay")



        err.type_error(str, "str", port)
        
        err.argument_error(port, "OUT 3")
        
        log("Setting the port for the relay to '" + port + "'", "INFO", "TI Hub", "Relay")
        print("Setting port for output device 'relay' to '" + port + "'")
        return
            

    def on(self):
        """
        Sets the relay state to the ON state
        """
        log("Setting the state of the relay to 'on'", "INFO", "TI Hub", "Relay")
        print("[Relay] Setting relay state to 'ON'")
        return None

    def off(self):
        """
        Sets the relay state to the OFF state
        """
        log("Setting the state of the relay to 'off'", "INFO", "TI Hub", "Relay")
        print("[Relay] Setting relay state to 'OFF'")
        return None

###########################################################################################

class servo():
    """
    Manages functions for controlling servo motors.\n
    • set_position(pos): Sets the sweep servo position within a range of -90 to +90.\n
    • zero(): Sets the sweep servo to the zero position.


    Available Ports: 'OUT 3'
   
    
    Category: Hub / Add Output Device
  
    
    Returns None
    """

    def __init__(self, port:str) -> None:
        """
        Manages functions for controlling servo motors.\n
        • set_position(pos): Sets the sweep servo position within a range of -90 to +90.\n
        • zero(): Sets the sweep servo to the zero position.    

        args:
            port (str): The port of the device. Possible Options: 'OUT 3'.
        """

        if cerr.type_error(str, port) == False: log("Argument 'port' has to be type string!", "ERROR", "TI Hub", "Servo")

        if cerr.argument_error(port, "OUT 3") == False: log("Argument 'port' has to be one of these: 'OUT 3'!", "ERROR", "TI Hub", "Servo")


        err.type_error(str, "str", port)

        err.argument_error(port, "OUT 3")
        
        log("Setting the port of the servo to '" + port + "'", "INFO", "TI Hub", "Servo")
        print("Setting port for output device 'servo' to '" + port + "'")
        return
            

    def set_position(self, pos:int):
        """
        Sets the sweep servo position within a range of -90 to +90.

        args:
            pos (int): The position to rotate the servo to. Ranges from -90 to 90.

        Returns:
            list: a list containing the following data: [pos]
        """

        if cerr.type_error(int, pos) == False: log("Argument 'pos' has to type integer!", "ERROR", "TI Hub", "Servo")

        if cerr.range_error(-90, 90, pos) == False: log("Argument 'pos' has to between the values -90 and 90", "ERROR", "TI Hub", "Servo")


        err.type_error(int, "int", pos)

        err.range_error(-90, 90, pos)


            
        log("Setting the servos position to '" + str(pos) + "'", "INFO", "TI Hub", "Servo")
        print("[Servo] Setting the servo position to '" + str(pos) + "'")
        return [pos]

    def zero(self):
        """
        Sets the sweep servo position to 0
        """
        log("Setting the position of the servo to 0", "INFO", "TI Hub", "Servo")
        print("[Servo] Setting the servo position to '0'")
        return None

###########################################################################################

class squarewave():
    """
    Manages functions for generating a square wave.\n
    • set(frequency,duty,time): Sets the output squarewave with a default duty cycle of 50% (if duty is not specified) and an output frequency specified by "frequency". The frequency may be from 1 to 500 Hz. The duty cycle, if specified, may be from 0 to 100%.\n
    • off(): Turns the squarewave off.\n
    
    
    Available Ports: 'OUT 1', 'OUT 2', 'OUT 3', 'BB 1', 'BB 2', 'BB 3', 'BB 4', 'BB 5', 'BB 6', 'BB 7', 'BB 8', 'BB 9', 'BB 10'
    
    
    Category: Hub / Add Output Device
    
    
    Returns None
    """
    def __init__(self, port:str) -> None:
        """
        Manages functions for generating a square wave.\n
        • set(frequency,duty,time): Sets the output squarewave with a default duty cycle of 50% (if duty is not specified) and an output frequency specified by "frequency". The frequency may be from 1 to 500 Hz. The duty cycle, if specified, may be from 0 to 100%.\n
        • off(): Turns the squarewave off.\n
    
        args:
            port (str): Possible Options: 'OUT 1', 'OUT 2', 'OUT 3', 'BB 1', 'BB 2', 'BB 3', 'BB 4', 'BB 5', 'BB 6', 'BB 7', 'BB 8', 'BB 9', 'BB 10'
        """

        if cerr.type_error(str, port) == False: log("Argument 'port' has to be type string!", "ERROR", "TI Hub", "Squarewave")

        if cerr.argument_error(port, "OUT 1", "OUT 2", "OUT 3", "BB 1", "BB 2", "BB 3", "BB 4", "BB 5", "BB 6", "BB 7", "BB 8", "BB 9", "BB 10") == False: log("Argument 'port' has to be one of these: 'OUT 1', 'OUT 2', 'OUT 3', 'BB 1', 'BB 2', 'BB 3', 'BB 4', 'BB 5', 'BB 6', 'BB 7', 'BB 8', 'BB 9', 'BB 10'!", "ERROR", "TI Hub", "Squarewave")
        
        err.type_error(str, "str", port)

        err.argument_error(port, "OUT 1", "OUT 2", "OUT 3", "BB 1", "BB 2", "BB 3", "BB 4", "BB 5", "BB 6", "BB 7", "BB 8", "BB 9", "BB 10")    
        
        log("Setting the port for the squarewave to '" + port + "'", "INFO", "TI Hub", "Squarewave")
        print("Setting port for output device 'squarewave' to '" + port + "'")
        return 
            

    def set(self, frequency:int, duty:int, time:float):
        """
        Sets the output squarewave with an output frequency specified by "frequency". The frequency may be from 1 to 500 Hz. The duty cycle may be from 0 to 100%.

        Args:
            frequency (int): The frequency of the squarewave (1 - 500).
            duty (int): The duty of the squarewave (0 - 100).
            time (float): The duration of the squarewave (0.1 - 100).

        Returns:
            list: a list containing the following data: [frequency, duty, time]
        """

        if cerr.type_error(int, frequency) == False: log("Argument 'frequency' has to be type integer!", "ERROR", "TI Hub", "Squarewave")
        if cerr.type_error(int, duty) == False: log("Argument 'duty' has to be type integer!", "ERROR", "TI Hub", "Squarewave")
        if cerr.type_error(float, time) == False: log("Argument 'time' has to be type float!", "ERROR", "TI Hub", "Squarewave")

        if cerr.range_error(1, 500, frequency) == False: log("Argument 'frequency' has to be between the values 1 and 500 (included)!", "ERROR", "TI Hub", "Squarewave")
        if cerr.range_error(0, 100, duty) == False: log("Argument 'duty' has to be between the values 0 and 100 (included)!", "ERROR", "TI Hub", "Squarewave")
        if cerr.range_error(0.1, 100, time) == False: log("Argument 'time' has to be between the values 0.1 and 100 (included)!", "ERROR", "TI Hub", "Squarewave")

        if frequency == 0 and duty == 0: log("If you want to turn off the squarewave, please use 'squarewave(PORT).off()' instead, because this might not turn the squarewave off entirely", "WARNING", "TI Hub", "Squarewave")

        err.type_error(int, "int", frequency)
        err.type_error(int, "int", duty)
        err.type_error(float, "float", time)

        err.range_error(1, 500, frequency)
        err.range_error(0, 100, duty)
        err.range_error(0.1, 100, time)

        log("Setting the frequency of the squarewave to '" + str(frequency) + "' Hz, the duty to '" + str(duty) + "%' and the duration to '" + str(time) + "' seconds", "INFO", "TI Hub", "Squarewave")
        print("[Square Wave] Setting the frequency to '" + str(frequency) + "Hz', the duty to '" + str(duty) + "%' and the duration to '" + str(time) + "' seconds")
        return [frequency, duty, time]

    def off(self):
        """
        Turns the squarewave off.
        """
        log("Turning the squarewave off", "INFO", "TI Hub", "Squarewave")
        print("[Square Wave] Turning squarewave off")
        return None


class digital():
    """
    INPUT: This device outputs the current state of the digital pin connected to the 'DIGITAL' object, or the cached state of the digital output value last 'SET' to the object.\n
    OUTPUT: Interface for controlling a digital output



    INPUT: Available Ports: 'IN 1', 'IN 2', 'IN 3', 'BB 1', 'BB 2', 'BB 3', 'BB 4', 'BB 5', 'BB 6', 'BB 7', 'BB 8', 'BB 9', 'BB 10'\n
    INPUT: Available Ports: 'OUT 1', 'OUT 2', 'OUT 3', 'BB 1', 'BB 2', 'BB 3', 'BB 4', 'BB 5', 'BB 6', 'BB 7', 'BB 8', 'BB 9', 'BB 10'
    """

    def __init__(self, port:str) -> None:
        """
        INPUT: This device outputs the current state of the digital pin connected to the 'DIGITAL' object, or the cached state of the digital output value last 'SET' to the object.\n
        OUTPUT: Interface for controlling a digital output



        INPUT: Available Ports: 'IN 1', 'IN 2', 'IN 3', 'BB 1', 'BB 2', 'BB 3', 'BB 4', 'BB 5', 'BB 6', 'BB 7', 'BB 8', 'BB 9', 'BB 10'\n
        INPUT: Available Ports: 'OUT 1', 'OUT 2', 'OUT 3', 'BB 1', 'BB 2', 'BB 3', 'BB 4', 'BB 5', 'BB 6', 'BB 7', 'BB 8', 'BB 9', 'BB 10'

        args:
            port (str): The port of the device. Possible Options: 'IN 1', 'IN 2', 'IN 3','OUT 1', 'OUT 2', 'OUT 3', 'BB 1', 'BB 2', 'BB 3', 'BB 4', 'BB 5', 'BB 6', 'BB 7', 'BB 8', 'BB 9', 'BB 10'
        """

        if cerr.type_error(str, port) == False: log("Argument 'port' has to be type string!", "ERROR", "TI Hub", "Digital")
        if cerr.argument_error(port, "OUT 1", "OUT 2", "OUT 3", "IN 1", "IN 2", "IN 3", "BB 1", "BB 2", "BB 3", "BB 4", "BB 5", "BB 6", "BB 7", "BB 8", "BB 9", "BB 10") == False: log("Argument 'port' has to be one of these: 'IN 1', 'IN 2', 'IN 3','OUT 1', 'OUT 2', 'OUT 3', 'BB 1', 'BB 2', 'BB 3', 'BB 4', 'BB 5', 'BB 6', 'BB 7', 'BB 8', 'BB 9', 'BB 10'!", "ERROR", "TI Hub", "Digital")

        err.type_error(str, "str", port)
        err.argument_error(port, "OUT 1", "OUT 2", "OUT 3", "IN 1", "IN 2", "IN 3", "BB 1", "BB 2", "BB 3", "BB 4", "BB 5", "BB 6", "BB 7", "BB 8", "BB 9", "BB 10")

        log("Setting the port for the input or output device set to digital to '" + port + "'", "INFO", "TI Hub", "Digital")
        print("Setting port for input / output device 'digital' to '" + port + "'")


    def measurement(self):
        """
        Returns the value of the digital input device.
        """
        log("Measuring the value of the input device set to digital", "INFO", "TI Hub", "Digital")
        print("Measuring value of digital input device")


    def set(self, value:int):
        """
        Sets the digital output to the value specified by "value" (0 or 1).

        args:
            value (int): The value to set (0 - 1).

        Returns:
            list: a list containing the following values: [value]
        """

        if cerr.type_error(int, value) == False: log("Argument 'value' has to be type integer!", "ERROR", "TI Hub", "Digital")
        if cerr.range_error(0, 1, value) == False: log("Argument 'value' has to be between the values 0 and 1!", "ERROR", "TI Hub", "Digital")

        err.type_error(int, "int", value)
        err.range_error(0, 1, value)

        log("Setting the value of the output device set to digital to '" + str(value) + "'", "INFO", "TI Hub", "Digital")
        print("Setting digital output to '" + str(value) + "'")
        return [value]


    def on(self):
        """
        Sets the state of the digital output to on (1).
        """
        log("Setting the state / value of the device set to digital to 'on' (1)", "INFO", "TI Hub", "Digital")
        print("Setting state of digital output device to 'on' (1)")
        return None

    def off(self):
        """
        Sets the state of the digital output to off (0).
        """
        log("Setting the state / value of the device set to digital to 'off' (0)", "INFO", "TI Hub", "Digital")
        print("Setting state of digital output device to 'off' (0)")
        return None

###########################################################################################

class bb_port():
    """
    This device provides support for using all 10 BB port pins as a combined digital input/output port. The initialization functions have an optional "mask" parameter that allows the use of the subset of the 10 pins.\n
    • read_port(): Reads the current values on the input pins of the BB port.\n
    • write_port(value): Sets the output pin values to the specified value, where value is between 0 and 1023. Note that the value is also adjusted against the mask value in the var=bbport(mask) operation, if a mask was provided.


    Category: Hub / Add Input Device\n
    Category: Hub / Add Output Device


    Returns None
    """

    def __init__(self, mask:int) -> None:
        """
        This device provides support for using all 10 BB port pins as a combined digital input/output port. The initialization functions have an optional "mask" parameter that allows the use of the subset of the 10 pins.\n
        • read_port(): Reads the current values on the input pins of the BB port.\n
        • write_port(value): Sets the output pin values to the specified value, where value is between 0 and 1023. Note that the value is also adjusted against the mask value in the var=bbport(mask) operation, if a mask was provided.


        args:
            mask (int): The mask for the pins (-1 - 1024).
        """

        if cerr.type_error(int, "int", mask) == False: log("Argument 'mask' has to be type integer!", "ERROR", "TI Hub", "BB Port")
        if cerr.range_error(-1, 1024, mask) == False: log("Argument 'mask' has to be between the values -1 and 1024!", "ERROR", "TI Hub", "BB Port")

        err.type_error(int, "int", mask)
        err.range_error(-1, 1024, mask)


        log("Setting the mask for the input or output device set to bb port to '" + str(mask) + "'", "INFO", "TI Hub", "BB Port")
        print("Setting mask for input / output device 'bb_port' to '" + str(mask) + "'")
        return 


            

    def read_port(self):
        """
        Reads the current values on the input pins of the BB port.
        """
        log("Reading the ports of the device set to bb port", "INFO", "TI Hub", "BB Port")
        print("[bb_port] reading ports")
        return
    
    def write_port(self, value:int):
        """
        Sets the output pin values to the specified value, where value is between 0 and 1023. Note that the value is also adjusted against the mask value in the var=bbport(mask) operation, if a mask was provided.

        args:
            value (int): The output pin value (0 - 1023).

        Returns:
            list: a list containing the following data: [value]
        """
        if cerr.type_error(int, value) == False: log("Argument 'value' has to be type integer!", "ERROR", "TI Hub", "BB Port")
        if cerr.range_error(0, 1023, value) == False: log("Argument 'value' has to be between the values 0 and 1023!", "ERROR", "TI Hub", "BB Port")


        err.type_error(int, "int", value)
        err.range_error(0, 1023, value)

        log("Writing the port value of the device set to bb port to '" + str(value) + "'", "INFO", "TI Hub", "BB Port")
        print("[bb_port] writing value " + str(value))
        return [value]