"""
Class containing all TI-Hub commands. Used for debugging
"""


from typing import List


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


    Category: Hub / Miscellaneous


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
            print("Showing text '" + text + "' at line " + str(line) + " with alignement '" + align + "' !")
            return [text, line, align]
        else:
            raise ValueError(errormsg_range(1, 13, "line"))
            
    else:
        raise ValueError("ERROR: Paramteter <align> can only be 'left' or 'right' or 'center'!")
        

###########################################################################################

def sleep(seconds: float):
    """
    Waits for the given amount of time in seconds, until the script continues to run.


    Category: Hub / Miscellaneous


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
        raise ValueError("ERROR: Parameter <seconds> has to be greater then 0!")
        

###########################################################################################

def get_key():
    """
    Gets the pressed key.


    Category: Hub / Miscellaneous


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


        Category: Hub / Integrated / Colour Output


        Returns an array / list: [red, green, blue]
        """

        try:
            int(red)
        except ValueError:
            raise ValueError(errormsg_type("int", "red")) from None

        try:
            int(green)
        except ValueError:
            raise ValueError(errormsg_type("int", "green")) from None

        try:
            int(blue)
        except ValueError:
            raise ValueError(errormsg_type("int", "blue")) from None

        if(red > 255 or red < 0):
            raise ValueError(errormsg_range(0, 255, "red"))
            
        if(green > 255 or green < 0):
            raise ValueError(errormsg_range(0, 255, "green"))
            
        if(blue > 255 or blue < 0):
            raise ValueError(errormsg_range(0, 255, "blue"))
            

        print("Setting RGB-Led to Red: " + str(red) + ", Green: " + str(green) + ", Blue: " + str(blue))
        return [red, green, blue]


    ###########################################################################################


    def blink(frequency: float, time: float):
        """
        Blinks the RGB-LED at the given frequency (in Hertz) for the given time. The frequency ranges between 0.1 - 20 Hz and the time between 0.1 - 100 seconds.


        Category: Hub / Integrated / Colour Output


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


        Category: Hub / Integrated / Colour Output


        Returns None
        """

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


        Category: Hub / Integrated / Light-LED


        Returns None
        """

        print("Turning Light-LED off")
        return None

    ###########################################################################################

    def on():
        """
        Turns the Light-LED in.


        Category: Hub / Integrated / Light-LED


        Returns None
        """

        print("Turning Light-LED on")
        return None

    ###########################################################################################

    def blink(frequency: float, time: float):
        """
        Blinks the Light-LED at the given frequency (in Hertz) for the given time. The frequency ranges between 0.1 - 20 Hz and the time between 0.1 - 100 seconds.


        Category: Hub / Integrated / Colour Output


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


        Category: Hub / Integrated / Sound Output


        Returns an array / list: [frequency, time]
        """

        try:
            float(frequency)
        except ValueError:
            raise ValueError(errormsg_type("float", "frequency")) from None

        try:
            float(duration)
        except ValueError:
            raise ValueError(errormsg_type("float", "duration")) from None

        if(frequency > 8000 or frequency < 0):
            raise ValueError(errormsg_range(0.1, 20, "frequency"))
            
        if(duration > 100 or duration < 0.1):
            raise ValueError(errormsg_range(0.1, 100, "duration"))
            

        print("Setting the speakers frequency to " + str(frequency) + "Hz for " + str(duration) + " seconds")
        return [frequency, duration]

    ###########################################################################################

    def note(note :str, duration :float):
        """
        Plays the given note for the given duration. An example for the note is 'A4'. The duration ranges between 0.1 and 100 seconds.

        The note names are C, CS, D, DS, E, F, FS, G, GS, A, AS, and B.

        The octave numbers range from 1 to 9 (inclusive).


        Category: Hub / Integrated / Sound Output


        Returns an array / list: [note, time]
        """

        try:
            str(note)
        except ValueError:
            raise ValueError(errormsg_type("str", "note")) from None

        try:
            float(duration)
        except ValueError:
            raise ValueError(errormsg_type("float", "duration")) from None

        if(duration > 100 or duration < 0.1):
            raise ValueError(errormsg_range(0.1, 100, "duration"))
            

        print("Playing the note " + note + "for " + str(duration) + " seconds")
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
        Reads the built-in BRIGHTNESS (light level) sensor and returns a reading.
        The default range is 0 to 100. This can be changed using the 'range()' function.


        Category: Hub / Integrated / Brightness Input


        Returns None
        """

        print("Reading Brightness Sensor")
        return None

    ###########################################################################################

    def range(min:float, max:float):
        """
        Sets the range for mapping the readings from the light level sensor.


        Category: Hub / Integrated / Brightness Input


        Returns an array / list: [min, max]
        """

        try:
            float(min)
        except ValueError:
            raise ValueError(errormsg_type("float", "min")) from None

        try:
            float(max)
        except ValueError:
            raise ValueError(errormsg_type("float", "max")) from None        

        print("Setting the range of the brightness sensor to " + str(min) + " to " + str(max))
        return [min, max]

###########################################################################################

def dht(port:str):
    """
    This device outputs a list consisting of the current temperature, humidity, type of sensor, and last cached read status.

    Available Ports: 'IN 1', 'IN 2'


    Category: Hub / Add Input Device


    Returns an array / list: [port]
    """

    try:
        str(port)
    except ValueError:
        raise ValueError(errormsg_type("str", "port")) from None

    if(port == "IN 1" or port == "IN 2"):
        print("Setting port for input device 'dht' to '" + port + "'")
        return [port]
    else:
        raise ValueError("ERROR: This device only accepts these Ports: 'IN 1', 'IN 2'")
        

###########################################################################################

def ranger(port:str):
    """
    This device outputs the current distance measurement from the specified ultrasonic ranger.

    Available Ports: 'IN 1', 'IN 2'


    Category: Hub / Add Input Device


    Returns an array / list: [port]
    """

    try:
        str(port)
    except ValueError:
        raise ValueError(errormsg_type("str", "port")) from None

    if(port == "IN 1" or port == "IN 2"):
        print("Setting port for input device 'ranger' to '" + port + "'")
        return [port]
    else:
        raise ValueError("ERROR: This device only accepts these Ports: 'IN 1', 'IN 2'")
        

###########################################################################################

def light_level(port:str):
    """
    This device outputs the brightness level from the external light level (brightness) sensor.


    Available Ports: 'IN 1', 'IN 2', 'IN 3'


    Category: Hub / Add Input Device


    Returns an array / list: [port]
    """

    try:
        str(port)
    except ValueError:
        raise ValueError(errormsg_type("str", "port")) from None

    if(port == "IN 1" or port == "IN 2" or port == "IN 3"):
        print("Setting port for input device 'light_level' to '" + port + "'")
        return [port]
    else:
        raise ValueError("ERROR: This device only accepts these Ports: 'IN 1', 'IN 2', 'IN 3'")
        

###########################################################################################

def temperature(port:str):
    """
    This device outputs the temperature reading from the external temperature sensor. The default configuration is to support the Seeed temperature sensor in 'IN 1', 'IN 2' or 'IN 3' ports. To use the TI LM19 Temperature sensor from the TI-Innovator™ Hub breadboard pack, edit the port to the BB pin in use and use an optional argument Example: mylm19=temperature("BB 5","TIANALOG")
    
    Please Note, that this method will throw an ERROR with this library!


    Available Ports: 'IN 1', 'IN 2', 'IN 3'


    Category: Hub / Add Input Device


    Returns an array / list: [port]
    """

    try:
        str(port)
    except ValueError:
        raise ValueError(errormsg_type("str", "port")) from None

    if(port == "IN 1" or port == "IN 2" or port == "IN 3"):
        print("Setting port for input device 'temperature' to '" + port + "'")
        return [port]
    else:
        raise ValueError("ERROR: This device only accepts these Ports: 'IN 1', 'IN 2', 'IN 3'")
        

###########################################################################################

def moisture(port:str):
    """
    This device outputs the moisture sensor reading.


    Available Ports: 'IN 1', 'IN 2', 'IN 3'


    Category: Hub / Add Input Device


    Returns an array / list: [port]
    """

    try:
        str(port)
    except ValueError:
        raise ValueError(errormsg_type("str", "port")) from None

    if(port == "IN 1" or port == "IN 2" or port == "IN 3"):
        print("Setting port for input device 'moisture' to '" + port + "'")
        return [port]
    else:
        raise ValueError("ERROR: This device only accepts these Ports: 'IN 1', 'IN 2', 'IN 3'")
        

###########################################################################################

def magnetic(port:str):
    """
    This device detects the presence of a magnetic field. The threshold value to determine the presence of the field is set through the trigger() function. The default value of the threshold is 150.



    Available Ports: 'IN 1', 'IN 2', 'IN 3'


    Category: Hub / Add Input Device


    Returns an array / list: [port]
    """

    try:
        str(port)
    except ValueError:
        raise ValueError(errormsg_type("str", "port")) from None

    if(port == "IN 1" or port == "IN 2" or port == "IN 3"):
        print("Setting port for input device 'magnetic' to '" + port + "'")
        return [port]
    else:
        raise ValueError("ERROR: This device only accepts these Ports: 'IN 1', 'IN 2', 'IN 3'")
        

###########################################################################################

def vernier(port:str, sensor_type:str):
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

    try:
        str(port)
    except ValueError:
        raise ValueError(errormsg_type("str", "port")) from None

    if(port == "IN 1" or port == "IN 2" or port == "IN 3"):
        if(sensor_type == "temperature" or sensor_type == "lightlevel" or sensor_type == "pressure" or sensor_type == "pressure2" or sensor_type == "pH" or sensor_type == "force10" or sensor_type == "force50" or sensor_type == "accelerometer" or sensor_type == "generic"):
            print("Setting port for input device 'vernier' to '" + port + "' with sensor type '" + sensor_type + "'")
            return [port]
        else:
            raise ValueError("ERROR: Parameter <sensor_type> needs to be on of these: 'temperature', 'lightlevel', 'pressure', 'pressure2', 'pH', 'force10', 'force50', 'accelerometer', 'generic'")
            
    else:
        raise ValueError("ERROR: This device only accepts these Ports: 'IN 1', 'IN 2', 'IN 3'")
        

###########################################################################################

def analog_in(port:str):

    """
    This device supports the use of analog input generic devices.



    Available Ports: 'IN 1', 'IN 2', 'IN 3', 'BB 5', 'BB 6', 'BB 7'


    Category: Hub / Add Input Device


    Returns an array / list: [port]
    """

    try:
        str(port)
    except ValueError:
        raise ValueError(errormsg_type("str", "port")) from None

    if(port == "IN 1" or port == "IN 2" or port == "IN 3" or port == "BB 5" or port == "BB 6" or port == "BB 7"):
        print("Setting port for input device 'analog_in' to '" + port + "'")
        return [port]
    else:
        raise ValueError("ERROR: This device only accepts these Ports: 'IN 1', 'IN 2', 'IN 3', 'BB 5', 'BB 6', 'BB 7'")
        

###########################################################################################

def digital(port:str):
    """
    This device outputs the current state of the digital pin connected to the 'DIGITAL' object, or the cached state of the digital output value last 'SET' to the object.



    Available Ports: 'IN 1', 'IN 2', 'IN 3', 'BB 1', 'BB 2', 'BB 3', 'BB 4', 'BB 5', 'BB 6', 'BB 7', 'BB 8', 'BB 9', 'BB 10'


    Category: Hub / Add Input Device


    Returns an array / list: [port]
    """

    try:
        str(port)
    except ValueError:
        raise ValueError(errormsg_type("str", "port")) from None

    if(port == "IN 1" or port == "IN 2" or port == "IN 3" or port == "BB 1" or port == "BB 2" or port == "BB 3" or port == "BB 4" or port == "BB 5" or port == "BB 6" or port == "BB 7" or port == "BB 8" or port == "BB 9" or port == "BB 10"):
        print("Setting port for input device 'digital' to '" + port + "'")
        return [port]
    else:
        raise ValueError("ERROR: This device only accepts these Ports:  'IN 1', 'IN 2', 'IN 3', 'BB 1', 'BB 2', 'BB 3', 'BB 4', 'BB 5', 'BB 6', 'BB 7', 'BB 8', 'BB 9', 'BB 10'")
        

###########################################################################################

def potentiometer(port:str):
    """
    This device supports a potentiometer sensor. The range of the sensor can be changed by the range() function.



    Available Ports: 'IN 1', 'IN 2', 'IN 3', 'BB 5', 'BB 6', BB 7'


    Category: Hub / Add Input Device


    Returns an array / list: [port]
    """

    try:
        str(port)
    except ValueError:
        raise ValueError(errormsg_type("str", "port")) from None

    if(port == "IN 1" or port == "IN 2" or port == "IN 3" or port == "BB 5" or port == "BB 6" or port == "BB 7"):
        print("Setting port for input device 'potentiometer' to '" + port + "'")
        return [port]
    else:
        raise ValueError("ERROR: This device only accepts these Ports: 'IN 1', 'IN 2', 'IN 3', 'BB 5', 'BB 6', BB 7'")
        

###########################################################################################

def thermistor(port:str):
    """
    This device reads thermistor sensors. The default coefficients are designed to match the thermistor included in the Breadboard Pack of the TI-Innovator™ Hub, when used with a 10KΩ fixed resistor. A new set of calibration coefficients and reference resistance for the thermistor can be configured using the calibrate() function.



    Available Ports: 'IN 1', 'IN 2', 'IN 3', 'BB 5', 'BB 6', BB 7'


    Category: Hub / Add Input Device


    Returns an array / list: [port]
    """

    try:
        str(port)
    except ValueError:
        raise ValueError(errormsg_type("str", "port")) from None

    if(port == "IN 1" or port == "IN 2" or port == "IN 3" or port == "BB 5" or port == "BB 6" or port == "BB 7"):
        print("Setting port for input device 'thermistor' to '" + port + "'")
        return [port]
    else:
        raise ValueError("ERROR: This device only accepts these Ports: 'IN 1', 'IN 2', 'IN 3', 'BB 5', 'BB 6', BB 7'")
        

###########################################################################################

def loudness(port:str):
    """
    This device supports sound loudness sensors.


    Available Ports: 'IN 1', 'IN 2', 'IN 3'


    Category: Hub / Add Input Device


    Returns an array / list: [port]
    """

    try:
        str(port)
    except ValueError:
        raise ValueError(errormsg_type("str", "port")) from None

    if(port == "IN 1" or port == "IN 2" or port == "IN 3"):
        print("Setting port for input device 'loudness' to '" + port + "'")
        return [port]
    else:
        raise ValueError("ERROR: This device only accepts these Ports: 'IN 1', 'IN 2', 'IN 3'")
        

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



        Available Ports: 'BB 1', 'BB 2', 'BB 3', 'BB 4', 'BB 5', 'BB 6', 'BB 7', 'BB 8', 'BB 9', 'BB 10'


        Category: Hub / Add Input Device


        Returns None
        """
        
        try:
            str(port)
        except ValueError:
            raise ValueError(errormsg_type("str", "port")) from None

        if(port == "BB 1" or port == "BB 2" or port == "BB 3" or port == "BB 4" or port == "BB 5" or port == "BB 6" or port == "BB 7" or port == "BB 8" or port == "BB 9" or port == "BB 10"):
            print("Setting port for input device 'colour_input' to '" + port + "'")
        
            return #[port]
        else:
            raise ValueError("ERROR: This device only accepts these Ports: 'BB 1', 'BB 2', 'BB 3', 'BB 4', 'BB 5', 'BB 6', 'BB 7', 'BB 8', 'BB 9', 'BB 10'")
            
    

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
        print("[Colour_Input] fetching colour number")
        return None
    
    def red(self):
        """
        Returns a value from 0 to 255 that represents the intensity of the RED color level being detected.\n
        """
        print("[Colour_Input] fetching red value")
        return None
    
    def green(self):
        """
        Returns a value from 0 to 255 that represents the intensity of the GREEN color level being detected.\n
        """
        print("[Colour_Input] fetching green value")
        return None
    
    def blue(self):
        """
        Returns a value from 0 to 255 that represents the intensity of the BLUE color level being detected.\n
        """
        print("[Colour_Input] fetching blue value")
        return None

    def gray(self):
        """
        Returns a value from 0 to 255 that represents the gray level being detected, where 0 is black and 255 is white.\n
        """
        print("[Colour_Input] fetching gray value")
        return None

###########################################################################################

class bb_port():
    """
    This device provides support for using all 10 BB port pins as a combined digital input/output port. The initialization functions have an optional "mask" parameter that allows the use of the subset of the 10 pins.\n
    • read_port(): Reads the current values on the input pins of the BB port.\n
    • write_port(value): Sets the output pin values to the specified value, where value is between 0 and 1023. Note that the value is also adjusted against the mask value in the var=bbport(mask) operation, if a mask was provided.


    Category: Hub / Add Input Device


    Returns None
    """

    def __init__(self, mask:int) -> None:
        """
        This device provides support for using all 10 BB port pins as a combined digital input/output port. The initialization functions have an optional "mask" parameter that allows the use of the subset of the 10 pins.\n
        • read_port(): Reads the current values on the input pins of the BB port.\n
        • write_port(value): Sets the output pin values to the specified value, where value is between 0 and 1023. Note that the value is also adjusted against the mask value in the var=bbport(mask) operation, if a mask was provided.


        Category: Hub / Add Input Device


        Returns None
        """

        try:
            int(mask)
        except ValueError:
            raise ValueError(errormsg_type("int", "mask")) from None

        if(mask > -1 or mask < 1024):
            print("Setting mask for input device 'bb_port' to '" + str(mask) + "'")
            return 
        else:
            raise ValueError("ERROR: This device only accepts mask values between 0 and 1023")
            

    def read_port(self):
        """
        Reads the current values on the input pins of the BB port.\n
        """
        print("[bb_port] reading ports")
        return
    
    def write_port(self ,value:int):
        """
        Sets the output pin values to the specified value, where value is between 0 and 1023. Note that the value is also adjusted against the mask value in the var=bbport(mask) operation, if a mask was provided.


        Returns an array / list: [value]
        """
        try:
            int(value)
        except ValueError:
            raise ValueError(errormsg_type("int", "value")) from None
        print("[bb_port] writing value " + str(value))
        return [value]

###########################################################################################

def hub_time():
    """
    This device provides access to the internal millisecond timer of the HUB.


    Category: Hub / Add Input Device


    Returns None
    """
    print("Fetching millisecond timer of HUB")
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
    def set(self, position:int, red:int, green:int, blue:int):
        """
        Sets a specific led_position (0-15) to the specified r,g,b value, where r,g,b are values from 0 to 255.

        
        Returns an array / list: [position, red, green, blue]
        """

        try:
            int(position)
        except ValueError:
            raise ValueError(errormsg_type("int", "position")) from None
        try:
            int(red)
        except ValueError:
            raise ValueError(errormsg_type("int", "red")) from None
        try:
            int(green)
        except ValueError:
            raise ValueError(errormsg_type("int", "green")) from None
        try:
            int(blue)
        except ValueError:
            raise ValueError(errormsg_type("int", "blue")) from None

        if(position > 15 or position < 0):
            raise ValueError(errormsg_range(0, 15, "position"))
            

        if(red > 255 or red < 0):
            raise ValueError(errormsg_range(0, 255, "red"))
            
        
        if(green > 255 or green < 0):
            raise ValueError(errormsg_range(0, 255, "green"))
            return
        
        if(blue > 255 or blue < 0):
            raise ValueError(errormsg_range(0, 255, "blue"))
            

        print("[RGB-Array] Setting the LED-Position to '" + str(position) + "' with the RGB-Values '" + str(red) + " red', '"+ str(green) + " green', '" + str(blue) + " blue'")
        return [position, red, green, blue]


    def set_all(self, red:int, green:int, blue:int):
        """
        Sets all RGB LEDs in the array to the same r,g,b value.


        
        Returns an array / list: [red, green, blue]
        """

        try:
            int(red)
        except ValueError:
            raise ValueError(errormsg_type("int", "red")) from None
        try:
            int(green)
        except ValueError:
            raise ValueError(errormsg_type("int", "green")) from None
        try:
            int(blue)
        except ValueError:
            raise ValueError(errormsg_type("int", "blue")) from None


        if(red > 255 or red < 0):
            raise ValueError(errormsg_range(0, 255, "red"))
            
        
        if(green > 255 or green < 0):
            raise ValueError(errormsg_range(0, 255, "green"))
            return
        
        if(blue > 255 or blue < 0):
            raise ValueError(errormsg_range(0, 255, "blue"))
            

        print("[RGB-Array] Setting all LEDs to the RGB-Values '" + str(red) + " red', '"+ str(green) + " green', '" + str(blue) + " blue'")
        return [red, green, blue]


    def all_off(self):
        """
        Turns off all RGB LEDs in the array


        Returns None
        """
        print("[RGB-Array] Turning off all RGB LEDs")
        return None

    def measurement(self):
        """
        Returns the approximate current draw that the RGB array is using from the TI-Innovator™ in milliAmps.


        Returns None
        """
        print("[RGB-Array] measuring current draw of the HUB")
        return None

    def pattern(self, value:int):
        """
        Using the value of the argument as a binary value in the range 0 to 65535, turns on pixels where a 1 value in the representation would be. LEDs are turned on as RED with pwm level value of 255.


        Returns [value]
        """

        try:
            int(value)
        except ValueError:
            raise ValueError(errormsg_type("int", "value")) from None

        if(value > 65536 or value < 0):
            raise ValueError(errormsg_range(0, 65536, "value"))
            
        
        print("[RGB-Array] Turning on pixels from binary value '" + value + "' (1 => on ; 0 => off)")
        return [value]

###########################################################################################

def led(port:str):
    """
    This device manages functions for controlling externally connected LEDs.


    Available Ports: 'OUT 1', 'OUT 2', 'OUT 3'
    
    
    Category: Hub / Add Output Device
    
    
    Returns an array / list: [port]
    """
    try:
        str(port)
    except ValueError:
        raise ValueError(errormsg_type("str", "port")) from None

    if(port == "OUT 1" or port == "OUT 2" or port == "OUT 3"):
        print("Setting port for output device 'led' to '" + port + "'")
        return [port]
    else:
        raise ValueError("ERROR: This device only accepts these Ports: 'OUT 1', 'OUT 2', 'OUT 3'")
        

###########################################################################################

def rgb(port:str):
    """
    Description


    Available Ports: 'OUT 1', 'OUT 2', 'OUT 3'
    
    
    Category: Hub / Add Output Device
    
    
    Returns an array / list [port]
    """
    try:
        str(port)
    except ValueError:
        raise ValueError(errormsg_type("str", "port")) from None

    if(port == "OUT 1" or port == "OUT 2" or port == "OUT 3"):
        print("Setting port for output device 'rgb' to '" + port + "'")
        return [port]
    else:
        raise ValueError("ERROR: This device only accepts these Ports: 'OUT 1', 'OUT 2', 'OUT 3'")
        

###########################################################################################

def speaker(port:str):
    """
    This device manages functions for supporting an external speaker with the TIInnovator™ Hub. The functions are the same as the ones for "tone".

    
    
    Available Ports: 'OUT 1', 'OUT 2', 'OUT 3', 'BB 1', 'BB 2', 'BB 3', 'BB 4', 'BB 5', 'BB 6', 'BB 7', 'BB 8', 'BB 9', 'BB 10'


    Category: Hub / Add Output Device


    Returns an array / list: [port]
    """

    try:
        str(port)
    except ValueError:
        raise ValueError(errormsg_type("str", "port")) from None

    if(port == "OUT 1" or port == "OUT 2" or port == "OUT 3" or port == "BB 1" or port == "BB 2" or port == "BB 3" or port == "BB 4" or port == "BB 5" or port == "BB 6" or port == "BB 7" or port == "BB 8" or port == "BB 9" or port == "BB 10"):
        print("Setting port for output device 'speaker' to '" + port + "'")
        return [port]
    else:
        raise ValueError("ERROR: This device only accepts these Ports:  'OUT 1', 'OUT 2', 'OUT 3', 'BB 1', 'BB 2', 'BB 3', 'BB 4', 'BB 5', 'BB 6', 'BB 7', 'BB 8', 'BB 9', 'BB 10'")
        

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



        Available Ports: 'OUT 1', 'OUT 2', 'OUT 3'


        Category: Hub / Add Output Device


        Returns None
        """
        try:
            str(port)
        except ValueError:
            raise ValueError(errormsg_type("str", "port")) from None

        if(port == "OUT 1" or port == "OUT 2" or port == "OUT 3"):
            print("Setting port for output device 'power' to '" + port + "'")
            return
        else:
            raise ValueError("ERROR: This device only accepts these Ports:  'OUT 1', 'OUT 2', 'OUT 3'")
            

    def set(self, value:int):
        """
        Sets the Power level to the specified value, between 0 and 100.


        Returns an array / list [value]
        """
        
        try:
            int(value)
        except ValueError:
            raise ValueError(errormsg_type("int", "value")) from None

        if(value > 100 or value < 0):
            raise ValueError(errormsg_range(0, 100, "value"))
            

        print("[Power] Setting the powerlevel to '" + str(value) + "'")
        return [value]

    def on(self):
        """
        Sets the powerlevel to 100


        Returns None
        """
        print("[Power] Setting the powerlevel to '100'")
        return None

    def off(self):
        """
        Sets the powerlevel to 0


        Returns None
        """
        print("[Power] Setting the powerlevel to '0'")
        return

###########################################################################################

class continous_servo():

    """
    Manages functions for controlling continuous servo motors.\n
    • set_cw(speed,time): The servo will spin in the clockwise direction at the specified speed (0-255) and for the specific duration in seconds.\n
    • set_ccw(speed,time): The servo will spin in the counterclockwise direction at the specified speed (0-255) and for the specific duration in seconds.\n
    • stop(): Stops the continuous servo.


    Available Ports: 'OUT 3'
   
    
    Category: Hub / Add Output Device
  
    
    Returns None
    """

    def __init__(self, port:str) -> None:
        
        """
        Manages functions for controlling continuous servo motors.\n
        • set_cw(speed,time): The servo will spin in the clockwise direction at the specified speed (0-255) and for the specific duration in seconds.\n
        • set_ccw(speed,time): The servo will spin in the counterclockwise direction at the specified speed (0-255) and for the specific duration in seconds.\n
        • stop(): Stops the continuous servo.


        Available Ports: 'OUT 3'
    
    
        Category: Hub / Add Output Device
    
    
        Returns None
        """
        try:
            str(port)
        except ValueError:
            raise ValueError(errormsg_type("str", "port")) from None

        if(port == "OUT 3"):
            print("Setting port for output device 'continous_servo' to '" + port + "'")
            return
        else:
            raise ValueError("ERROR: This device only accepts these Ports:  'OUT 3'")
            


    def set_cw(self, speed:int, time:float):
        """
        The servo will spin in the clockwise direction at the specified speed (0-255) and for the specific duration in seconds.


        Returns an array / list: [speed, time]
        """

        try:
            int(speed)
        except ValueError:
            raise ValueError(errormsg_type("int", "speed")) from None
        try:
            float(time)
        except ValueError:
            raise ValueError(errormsg_type("float", "time")) from None
        
        if(speed > 255 or speed < 0):
            raise ValueError(errormsg_range(0, 255, "speed"))
            
        if(time > 100 or time < 0.1):
            raise ValueError(errormsg_range(0.1, 100, "time"))
            
        
        print("[Continuous Servo] Spinning the servo clockwise for '" + str(time) + "' seconds with speed '" + str(speed) + "'")
        return [speed, time]

    def set_cw(self, speed:int, time:float):
        """
        The servo will spin in the anti-clockwise direction at the specified speed (0-255) and for the specific duration in seconds.


        Returns an array / list: [speed, time]
        """

        try:
            int(speed)
        except ValueError:
            raise ValueError(errormsg_type("int", "speed")) from None
        try:
            float(time)
        except ValueError:
            raise ValueError(errormsg_type("float", "time")) from None
        
        if(speed > 255 or speed < 0):
            raise ValueError(errormsg_range(0, 255, "speed"))
            
        if(time > 100 or time < 0.1):
            raise ValueError(errormsg_range(0.1, 100, "time"))
            
        
        print("[Continuous Servo] Spinning the servo anti-clockwise for '" + str(time) + "' seconds with speed '" + str(speed) + "'")
        return [speed, time]

    def stop(self):
        """
        Stops the continuous servo.


        Returns None
        """
        print("[Continuous Servo] Stopping the continuous servo")
        return None

###########################################################################################

def analog_out(port:str):
    """
    Functions for the use of analog input generic devices.
    
    
    Available Ports: 'OUT 1', 'OUT 2', 'OUT 3', 'BB 1', 'BB 2', 'BB 3', 'BB 4', 'BB 5', 'BB 6', 'BB 7', 'BB 8', 'BB 9', 'BB 10'
    
    
    Category: Hub / Add Output Device
    
    
    Returns an array / list: [port]
    """
    try:
        str(port)
    except ValueError:
        raise ValueError(errormsg_type("str", "port")) from None
    
    if(port == "OUT 1" or port == "OUT 2" or port == "OUT 3" or port == "BB 1" or port == "BB 2" or port == "BB 3" or port == "BB 4" or port == "BB 5" or port == "BB 6" or port == "BB 7" or port == "BB 8" or port == "BB 9" or port == "BB 10"):
        print("Setting port for output device 'analog_out' to '" + port + "'")
        return [port]
    else:
        raise ValueError("ERROR: This device only accepts these Ports:  'OUT 1', 'OUT 2', 'OUT 3', 'BB 1', 'BB 2', 'BB 3', 'BB 4', 'BB 5', 'BB 6', 'BB 7', 'BB 8', 'BB 9', 'BB 10'")
        

class vibration_monitor():
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


        Available Ports: 'OUT 3'
   
    
        Category: Hub / Add Output Device
  
    
        Returns None
        """

        try:
            str(port)
        except ValueError:
            raise ValueError(errormsg_type("str", "port")) from None

        if(port == "OUT 3"):
            print("Setting port for output device 'vibration_motor' to '" + port + "'")
            return
        else:
            raise ValueError("ERROR: This device only accepts these Ports:  'OUT 3'")
            

    def set(self, value:int):
        """
        Sets the vibration motor intensity to "val" (0-255).


        Returns an array / list: [value]
        """
        try:
            int(value)
        except ValueError:
            raise ValueError(errormsg_type("int", "value")) from None
        
        if(value > 255 or value < 0):
            raise ValueError(errormsg_range(0, 255, "value"))
            

        print("[Vibration Motor] Setting the intensity of the vibration motor to '" + str(value) + "'")
        return [value]

    def off(self):
        """
        Turns the vibration motor off (intensity: 0).


        Returns None
        """
        print("[Vibration Motor] Setting the intensity of the vibration motor to '0'")
        return None

    def on(self):
        """
        Turns the vibration motor on (intensity: 255).


        Returns None
        """
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


        Available Ports: 'OUT 3'
   
    
        Category: Hub / Add Output Device
  
    
        Returns None
        """

        try:
            str(port)
        except ValueError:
            raise ValueError(errormsg_type("str", "port")) from None

        if(port == "OUT 3"):
            print("Setting port for output device 'relay' to '" + port + "'")
            return
        else:
            raise ValueError("ERROR: This device only accepts these Ports:  'OUT 3'")
            

    def on(self):
        """
        Sets the relay state to the ON state


        Returns None
        """
        print("[Relay] Setting realy state to 'ON'")
        return None

    def off(self):
        """
        Sets the relay state to the OFF state


        Returns None
        """
        print("[Relay] Setting realy state to 'OFF'")
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


        Available Ports: 'OUT 3'
   
    
        Category: Hub / Add Output Device
  
    
        Returns None
        """

        try:
            str(port)
        except ValueError:
            raise ValueError(errormsg_type("str", "port")) from None

        if(port == "OUT 3"):
            print("Setting port for output device 'servo' to '" + port + "'")
            return
        else:
            raise ValueError("ERROR: This device only accepts these Ports:  'OUT 3'")
            

    def set_position(self, pos:int):
        """
        Sets the sweep servo position within a range of -90 to +90.\n


        Returns an array / list: [pos]
        """
        try:
            int(pos)
        except ValueError:
            raise ValueError(errormsg_type("int", "pos")) from None
        
        if(pos > 90 or pos < -90):
            raise ValueError(errormsg_range(-90, 90, "pos"))
            
        
        print("[Servo] Setting the servo position to '" + str(pos) + "'")
        return [pos]

    def zero(self):
        """
        Sets the sweep servo position to 0\n


        Returns None
        """
        print("[Servo] Setting the servo position to '0'")
        return None

###########################################################################################

class squarewave():
    """
    Manages functions for generating a square wave.\n
    • set(frequency,duty,time): Sets the output squarewave with a default duty cycle of 50% (if duty is not specified) and an output frequency specified by "frequence". The frequency may be from 1 to 500 Hz. The duty cycle, if specified, may be from 0 to 100%.\n
    • off(): Turns the squarewave off.\n
    
    
    Available Ports: 'OUT 1', 'OUT 2', 'OUT 3', 'BB 1', 'BB 2', 'BB 3', 'BB 4', 'BB 5', 'BB 6', 'BB 7', 'BB 8', 'BB 9', 'BB 10'
    
    
    Category: Hub / Add Output Device
    
    
    Returns None
    """
    def __init__(self, port:str) -> None:
        """
        Manages functions for generating a square wave.\n
        • set(frequency,duty,time): Sets the output squarewave with a default duty cycle of 50% (if duty is not specified) and an output frequency specified by "frequence". The frequency may be from 1 to 500 Hz. The duty cycle, if specified, may be from 0 to 100%.\n
        • off(): Turns the squarewave off.\n
    
    
        Available Ports: 'OUT 1', 'OUT 2', 'OUT 3', 'BB 1', 'BB 2', 'BB 3', 'BB 4', 'BB 5', 'BB 6', 'BB 7', 'BB 8', 'BB 9', 'BB 10'
    
    
        Category: Hub / Add Output Device
    
    
        Returns None
        """
        try:
            str(port)
        except ValueError:
            raise ValueError(errormsg_type("str", "port")) from None
    
        if(port == "OUT 1" or port == "OUT 2" or port == "OUT 3" or port == "BB 1" or port == "BB 2" or port == "BB 3" or port == "BB 4" or port == "BB 5" or port == "BB 6" or port == "BB 7" or port == "BB 8" or port == "BB 9" or port == "BB 10"):
            print("Setting port for output device 'squarewave' to '" + port + "'")
            return 
        else:
            raise ValueError("ERROR: This device only accepts these Ports:  'OUT 1', 'OUT 2', 'OUT 3', 'BB 1', 'BB 2', 'BB 3', 'BB 4', 'BB 5', 'BB 6', 'BB 7', 'BB 8', 'BB 9', 'BB 10'")
            

    def set(self, frequency:int, duty:int, time:float):
        """
        Sets the output squarewave with a default duty cycle of 50% (if duty is Null) and an output frequency specified by "frequence". The frequency may be from 1 to 500 Hz. The duty cycle, if specified, may be from 0 to 100%.\n


        Returns an array / list: [frequency, duty, time]
        """
        if(duty == None):
            duty = 50
        
        try:
            int(frequency)
        except ValueError:
            raise ValueError(errormsg_type("int", "frequency")) from None
        try:
            int(duty)
        except ValueError:
            raise ValueError(errormsg_type("int", "duty")) from None
        try:
            float(time)
        except ValueError:
            raise ValueError(errormsg_type("float", "time")) from None
        if(frequency > 500 or frequency < 1):
            raise ValueError(errormsg_range(1, 500, "frequency"))
            
        if(duty > 100 or duty < 0):
            raise ValueError(errormsg_range(0, 100, "duty"))
            
        if(time > 100 or time < 0.1):
            raise ValueError(errormsg_range(0.1, 100, "time"))
            
        print("[Square Wave] Setting the frequency to '" + str(frequency) + "Hz', the duty to '" + str(duty) + "%' and the duration to '" + str(time) + "' seconds")
        return [frequency, duty, time]

    def off(self):
        """
        Turns the squarewave off


        Returns None
        """
        print("[Square Wave] Turning squarewave off")
        return None

##digital - out
##bb_port - out
