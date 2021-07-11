import os
import datetime


MODULES:list[str] = ["TI Hub", "TI Rover", "TI Draw", "TI System", "TI Plotlib"]
LOGTYPES:list[str] = ["WARNING", "ERROR", "INFO"]


SUBMODULES:list[str] = ["Clear Screen", "Window", "Auto Window", "Grid", "Axes", "Labels", "Title", "Show Plot", "Use Buffer", "Colour", "Scatter", "Plot", "Line", "Linear Regression", "Pen", "Text At", "Sleep", "Get Key", "Colour", "Light", "Sound", "Brightness", "DHT", "Ranger", "Light Level", "Temperature", "Moisture", "Magnetic", "Vernier", "Analog In", "Potentiometer", "Thermistor", "Loudness", "Colour Input", "Hub Time", "RGB Array", "LED", "RGB", "Speaker", "Power", "Continuous Servo", "Analog Out", "Vibration Motor", "Relay", "Servo", "Squarewave", "Digital", "BB Port", "Forward", "Backward", "Left", "Stop", "Stop Clear", "Resume", "Stay", "To", "Backward Time", "Forward Time", "Ranger Measurement", "Colour Measurement", "Red Measurement", "Green Measurement", "Blue Measurement", "Gray Measurement", "Encoders Gyroscope Measurement", "Gyroscope Measurement", "Colour RGB", "Blink", "Off", "Left Motor", "Right Motor", "Motors", "Waypoint Xythdrn", "Waypoint Previous", "Waypoint ETA", "Path Done", "Pathlist X", "Pathlist Y", "Pathlist Time", "Pathlist Heading", "Pathlist Distance", "Pathlist Revolutions", "Pathlist CMDNUM", "Waypoint X", "Waypoint Y", "Waypoint Time", "Waypoint Heading", "Waypoint Distance", "Waypoint Revolutions", "Recall Value", "Store Value", "Recall List", "Store List", "Evaluate Function", "Get Platform", "Get Mouse", "Clear History", "Get Time Milliseconds", "Draw Line", "Draw Rectangle", "Filled Rectangle", "Draw Circle", "Filled Circle", "Draw Text", "Draw Arc", "Filled Arc", "Draw Polygon", "Filled Polygon", "Plot XY", "Clear", "Set Colour", "Set Pen", "Set Window", "Get Screen Dimension", "Use Buffer", "Paint Buffer"]








def __check_log_file__():
    if os.path.exists("ti-python-log.log") == True:
        return
    else:
        with open("ti-python-log.log", "xt") as file:
            file.write("TI Python Module Log File\n")
            file.write("Format:\n")
            file.write("[Date - Time] [Logtype] [Module] [Function] log\n\n")
            file.write("You can delete this file to empty the log file, since a new one will be generated\n")
            file.write("-----" * 15)
            file.write("\n" * 4)
            file.close()

def __check_config__():
    if os.path.exists("ti-python-settings.cfg") == True:
        with open("ti-python-settings.cfg", "r") as file:
            settingslist = file.readlines()
            file.close()
            found = False
            for line in settingslist:
                if "log_file = " in line:
                    if line == "log_file = False":
                        return
                    elif line == "log_file = True":
                        __check_log_file__()
    else:
        print("======\nYou do not have a config file ('ti-python-settings.cfg') in your current directory.\nCall the function 'file_handler.generate_settings() once to generate the settings file.'\nWrite 'log_file = True' to enable a logfile or 'log_file = False' to disable a logfile and this message.\n\n")

def generate_settings():
    if os.path.exists("ti-python-settings.cfg") == True:
        return
    else:
        with open("ti-python-settings.cfg", "xt") as file:
            file.write("log_file = False")
            file.close()



def __date_and_time__(date_seperator:str = "-", date_time_seperator:str = " ", time_seperator:str = ":"):
        """
        Gets the current time and date for your location / timezone. Year, month and day are seperated by the 'date_seperator' value. Hour, minute and second are seperated by the 'time_seperator' value. Time and date are seperated by the 'date_time_seperator' value.

        Args:
            date_seperator (str, optional): The seperator between year, month and day. Defaults to "-".
            date_time_seperator (str, optional): The seperator between the date and time. Defaults to " ".
            time_seperator (str, optional): The seperator between hour, minute, second. Defaults to ":".

        Returns:
            list: A list containing the folowing data: [result, year, month, day, hour, minute, second]
        """
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        day = datetime.datetime.now().day
        hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute
        second = datetime.datetime.now().second

        year_str = str(year)
        month_str = str(month)
        day_str = str(day)
        hour_str = str(hour)
        minute_str = str(minute)
        second_str = str(second)

        year_str_len = year_str.__len__()
        month_str_len = month_str.__len__()
        day_str_len = day_str.__len__()
        hour_str_len = hour_str.__len__()
        minute_str_len = minute_str.__len__()
        second_str_len = second_str.__len__()

        if(year_str_len < 4):
            year_str = year_str + " "
        if(month_str_len < 2):
            month_str = "0" + month_str
        if(day_str_len < 2):
            day_str = "0" + day_str
        if(hour_str_len < 2):
            hour_str = "0" + hour_str
        if(minute_str_len < 2):
            minute_str = "0" + minute_str
        if(second_str_len < 2):
            second_str = "0" + second_str

        result = day_str + date_seperator + month_str + date_seperator + year_str + date_time_seperator + hour_str + time_seperator + minute_str + time_seperator + second_str
        return [result, year_str, month_str, day_str, hour_str, minute_str, second_str]


def create_log(log_context:str, log_type:str, module:str, submodule:str, available_modules:list[str] = MODULES, available_submodules:list[str] = SUBMODULES, available_log_types:list[str] = LOGTYPES):
    __check_config__()
    if os.path.exists("ti-python-log.log") == True:
        available_log_types.append(log_type)
        available_log_types.sort(key=len)
        max_len_log_type:int = available_log_types[available_log_types.__len__() - 1]
        max_len_log_type_char = max_len_log_type.__len__()

        max_len_log_type_char += 2

        len_log_type = log_type.__len__()

        len_diff:int = max_len_log_type_char - len_log_type
        time_and_date = __date_and_time__()[0]
        loggable_time = "[" + time_and_date + "]  "

        loggable_type = "[" + log_type.upper() + "]"
        for i in range(len_diff):
            loggable_type = loggable_type.__add__(" ")



        available_modules.append(module)
        available_modules.sort(key=len)
        max_len_module:int = available_modules[available_modules.__len__() - 1]
        max_len_module_char = max_len_module.__len__()

        max_len_module_char += 2

        len_module = module.__len__()

        len_diff:int = max_len_module_char - len_module

        loggable_module = "[" + module + "]"
        for i in range(len_diff):
            loggable_module = loggable_module.__add__(" ")


        available_submodules.append(submodule)
        available_submodules.sort(key=len)
        max_len_submodule:int = available_submodules[available_submodules.__len__() - 1]
        max_len_submodule_char = max_len_submodule.__len__()

        max_len_submodule_char += 2

        len_submodule = submodule.__len__()

        len_diff:int = max_len_submodule_char - len_submodule

        if submodule.isupper():
            loggable_submodule = "[" + submodule + "]"
            for i in range(len_diff):
                loggable_submodule = loggable_submodule.__add__(" ")
        else:
            loggable_submodule = "[" + submodule.title() + "]"
            for i in range(len_diff):
                loggable_submodule = loggable_submodule.__add__(" ")





        with open("ti-python-log.log", 'at') as file:
            file.write(loggable_time + loggable_type + loggable_module + loggable_submodule + log_context + "\n")