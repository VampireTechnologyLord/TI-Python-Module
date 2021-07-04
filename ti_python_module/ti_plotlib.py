"""
Class containing all the TI Plotlib elements.
"""
from ti_python_module.file_handler import create_log as log
from ti_python_module.err import withConsole as err
from ti_python_module.err import onlyCheck as cerr


def cls():
    """
    Clears the plotting canvas.

    Returns:
        None: None
    """
    print("Clearing screen / display")
    log("Clearing the display / screen", "INFO", "TI Plotlib", "Clear Screen")
    return None

def window(x_min:int, x_max:int, y_min:int, y_max:int):
    """
    Defines the plotting window by mapping the the specified horizontal interval (xmin, xmax) and vertical interval (ymin, ymax) to the allotted plotting area (pixels).

    Args:
        x_min (int): The minimum x coordinate of the window.
        x_max (int): The maximum x coordinate of the window.
        y_min (int): The minimum y coordinate of the window.
        y_max (int): The maximum y coordinate of the window.

    Returns:
        list: a list containing the following data: [x_min, x_max, y_min, y_max]
    """


    if cerr.type_error(int, x_min) == False: log("Argument 'x_min' has to be type integer!", "ERROR", "TI Plotlib", "Window")
    if cerr.type_error(int, x_max) == False: log("Argument 'x_max' has to be type integer!", "ERROR", "TI Plotlib", "Window")
    if cerr.type_error(int, y_min) == False: log("Argument 'y_min' has to be type integer!", "ERROR", "TI Plotlib", "Window")
    if cerr.type_error(int, y_max) == False: log("Argument 'y_max' has to be type integer!", "ERROR", "TI Plotlib", "Window")

    if cerr.relation.smaller_error(x_min, x_max) == False: log("Argument 'x_min' has to be smaller then 'x_max'!", "ERROR", "TI Plotlib", "Window")
    if cerr.relation.smaller_error(y_min, y_max) == False: log("Argument 'y_min' has to be smaller then 'y_max'!", "ERROR", "TI Plotlib", "Window")

    err.type_error(int, "int", x_min)
    err.type_error(int, "int", x_max)
    err.type_error(int, "int", y_min)
    err.type_error(int, "int", y_max)

    err.relation.smaller_error(x_min, x_max)
    err.relation.smaller_error(y_min, y_max)

    print("Setting the horizontal interval to '" + str(x_max - x_min) + "' pixels and the vertical interval to '" + str(y_max - y_min) + "' pixels.")
    log("Setting the horizontal interval of the plotting window to '" + str(x_max - x_min) + "' pixels and the vertical interval to '" + str(y_max - y_min) + "' pixels.", "INFO", "TI Plotlib", "Window")
    return [x_min, x_max, y_min, y_max]

def auto_window(x_list:list[int], y_list:list[int]):
    """
    Autoscales the plotting window to fit the data ranges within x-list and y-list specified in the program prior to the auto_window().

    Args:
        x_list (list): The list of x values.
        y_list (list): The list of y values.

    Returns:
        list: a list containing the following data: [x_list, y_list]
    """
    if cerr.type_error(list[int], x_list) == False: log("Argument 'x_list' has to be type list!", "ERROR", "TI Plotlib", "Auto Window")
    if cerr.type_error(list[int], y_list) == False: log("Argument 'x_list' has to be type list!", "ERROR", "TI Plotlib", "Auto Window")

    err.type_error(list[int], "list", x_list)
    err.type_error(list[int], "list", y_list)

    print("Auto-scaling the window to fit the specified plotting data")
    log("Automatically scaling the plotting window to fit the given data range.", "INFO", "TI Plotlib", "Auto Window")
    return [x_list, y_list]

def grid(x_scale:float, y_scale:float, style:str):
    """
    Displays a grid using specified scale for x and y axes.

    Args:
        x_scale (float): x axis scale
        y_scale (float): y axis scale
        style (str): the style of the grid lines. Options: 'solid', 'dotted', 'dashed'.

    Returns:
        list: a list containing the followig data: [x_scale, y_scale, style]
    """
    if cerr.type_error(float, x_scale) == False: log("Argument 'x_scale' has to be type float!", "ERROR", "TI Plotlib", "Grid")
    if cerr.type_error(float, y_scale) == False: log("Argument 'y_scale' has to be type float!", "ERROR", "TI Plotlib", "Grid")
    if cerr.type_error(str, style) == False: log("Argument 'style' has to be type string!", "ERROR", "TI Plotlib", "Grid")
    err.type_error(float, "float", x_scale)
    err.type_error(float, "float", y_scale)
    err.type_error(str, "str", style)

    if cerr.argument_error(style, "solid", "dotted", "dashed") == False: log("Argument 'style' can only be on of these: 'solid', 'dotted', 'dashed'!", "ERROR", "TI Plotlib", "Grid")
    err.argument_error(style, "solid", "dotted", "dashed")

    print("Setting the grid scale to '" + str(x_scale) + ", " + str(y_scale) + "' with the style '" + style + "'")
    log("Setting the grid scale to '" + str(x_scale) + " x' and '" + str(y_scale) + " y' with style '" + style + "'", "INFO", "TI Plotlib", "Grid")
    return [x_scale, y_scale, style]

def axes(mode:str):
    """
    Displays axes on specified window in the plotting area.

    Args:
        mode (str): The mode of the axes. Options: 'off', 'on', 'axes', 'window'.

    Returns:
        list: a list containing the following data: [mode]
    """
    if cerr.type_error(str, mode) == False: log("Argument 'mode' has to be type string!", "ERROR", "TI Plotlib", "Axes")
    err.type_error(str, "str", mode)

    if cerr.argument_error(mode, "off", "on", "axes", "window") == False: log("Argument 'mode' can only be one of these: 'off', 'on', 'axes', 'window'!", "ERROR", "TI Plotlib", "Axes")
    err.argument_error(mode, "off", "on", "axes", "window")
    print("Setting axes mode to '" + mode + "'")
    log("Setting the axes mode to '" + mode + "'", "INFO", "TI Plotlib", "Axes")
    return [mode]

def labels(x_name:str, y_name:str, x_row:int, y_row:int):
    """
    Displays "x-label" and "y-label" labels on the plot axes at row positions x and y.

    Args:
        x_name (str): The label of the x axis.
        y_name (str): The label of the y axis.
        x_row (int): The row for the x label.
        y_row (int): The row for the y label.

    Returns:
    list: a list containing the following data: [x_name, y_name, x_row, y_row]
    """
    if cerr.type_error(str, x_name) == False: log("Argument 'x_name' has to be type string!", "ERROR", "TI Plotlib", "Labels")
    if cerr.type_error(str, y_name) == False: log("Argument 'y_name' has to be type string!", "ERROR", "TI Plotlib", "Labels")
    if cerr.type_error(int, x_row) == False: log("Argument 'x_row' has to be type integer!", "ERROR", "TI Plotlib", "Labels")
    if cerr.type_error(int, y_row) == False: log("Argument 'y_row' has to be type integer!", "ERROR", "TI Plotlib", "Labels")
    err.type_error(str, "str", x_name)
    err.type_error(str, "str", y_name)
    err.type_error(int, "int", x_row)
    err.type_error(int, "int", y_row)

    print("Displaying '" + x_name + "' at row '" + str(x_row) + "' for the x axis. Displaying '" + y_name + "' at row '" + str(y_row) + "' for the y axis.")
    log("Displaying '" + x_name + "' at row '" + str(x_row) + "' for the x axis. Displaying '" + y_name + "' at row '" + str(y_row) + "' for the y axis.", "INFO", "TI Plotlib", "Screen")
    return[x_name, y_name, x_row, y_row]

def title(title:str):
    """
    Displays the title centered on top line of window.

    Args:
        title (str): The displayed title.

    Returns:
        list: a list containing the following data: [title]
    """
    if cerr.type_error(str, title) == False: log("Argument 'title' has to be type string!", "ERROR", "TI Plotlib", "Title")
    err.type_error(str, "str", title)

    log("Setting the title of the plotting window to '" + title + "'", "INFO", "TI Plotlib", "Title")
    print("Setting the title of the window to '" + title + "'")
    return [title]

def show_plot():
    """
    Displays the buffered drawing output. The use_buffer() and show_plot() functions are useful in cases where displaying multiple objects on the screen could cause delays (not necessary in most cases).

    Returns:
        None: None
    """
    log("Displaying the buffered drawing output", "INFO", "TI Plotlib", "Show Plot")
    print("Displaying buffered drawing output")
    return None

def use_buffer():
    """
    Enables an off-screen buffer to speed up drawing.

    Returns:
        None: None
    """
    log("Enabling the use of the offscreen buffer for faster plotting", "INFO", "TI Plotlib", "Use Buffer")
    print("Enabling offscreen buffer")
    return None

def colour(red:float, green:float, blue:float):
    """
    Sets the color for all following graphics/plotting.

    Args:
        red (float): The red part of the colour. Ranges from 0 to 255.
        green (float): The green part of the colour. Ranges from 0 to 255.
        blue (float): The blue part of the colour. Ranges from 0 to 255.

    Returns:
        list: a list containing the following data: [red, green, blue]
    """
    if cerr.type_error(float, red) == False: log("Argument 'red' has to be type float!", "ERROR", "TI Plotlib", "Colour")
    if cerr.type_error(float, green) == False: log("Argument 'green' has to be type float!", "ERROR", "TI Plotlib", "Colour")
    if cerr.type_error(float, blue) == False: log("Argument 'blue' has to be type float!", "ERROR", "TI Plotlib", "Colour")

    if cerr.range_error(0, 255, red) == False: log("Argument 'red' has to be between the values 0 and 255 (included)!", "ERROR", "TI Plotlib", "Colour")
    if cerr.range_error(0, 255, green) == False: log("Argument 'green' has to be between the values 0 and 255 (included)!", "ERROR", "TI Plotlib", "Colour")
    if cerr.range_error(0, 255, blue) == False: log("Argument 'blue' has to be between the values 0 and 255 (included)!", "ERROR", "TI Plotlib", "Colour")


    err.type_error(float, "float", red)
    err.type_error(float, "float", green)
    err.type_error(float, "float", blue)

    err.range_error(0, 255, red)
    err.range_error(0, 255, green)
    err.range_error(0, 255, blue)
    
    log("Setting the plotting colout to '" + str(red) + " red', '"+ str(green) + " green', '" + str(blue) + " blue'", "INFO", "TI Plotlib", "Colour")
    print("Setting the colour to '" + str(red) + " red', '"+ str(green) + " green', '" + str(blue) + " blue'")
    return [red, green, blue]

def scatter(x_list:list, y_list:list, mark:str):
    """
    Plots a sequence of ordered pair from (x-list,y-list) with the specified mark style.

    Args:
        x_list (list): The list of the possible x values.
        y_list (list): The list of the possible y values.
        mark (str): The mark to scatter. Possible Options: 'o', '+', 'x', '.'.

    Returns:
        list: a list containing the following data: [x_list, y_list, mark]
    """
    if cerr.type_error(list, x_list) == False: log("Argument 'x_list' has to be type list!", "ERROR", "TI Plotlib", "Scatter")
    if cerr.type_error(list, y_list) == False: log("Argument 'y_list' has to be type list!", "ERROR", "TI Plotlib", "Scatter")
    if cerr.type_error(str, mark) == False: log("Argument 'mark' has to be type string!", "ERROR", "TI Plotlib", "Scatter")

    if cerr.argument_error(mark, "o", "+", "x", ".") == False: log("Argument 'mark' can only be one of these: 'o', '+', 'x', '.'!", "ERROR", "TI Plotlib", "Scatter")

    err.type_error(list, "list", x_list)
    err.type_error(list, "list", y_list)
    err.type_error(str, "str", mark)

    err.argument_error(mark, "o", "+", "x", ".")

    log("Scattering mark '" + mark + "' at the values from the given lists", "INFO", "TI Plotlib", "Scatter")
    print("Scattering mark '" + mark + "' in between the given lists")
    return [x_list, y_list, mark]


def plot(x_list:list, y_list:list, mark:str):
    """
    Plots a line using ordered pairs from specified x-list and y-list. To use just one value, put this one value in a list.


    Args:
        x_list (list): The list of the possible x values.
        y_list (list): The list of the possible y values.
        mark (str): The mark to plot. Possible Options: 'o', '+', 'x', '.'.

    Returns:
        list: a list containing the following data: [x_list, y_list, mark]
    """
    if cerr.type_error(list, x_list) == False: log("Argument 'x_list' has to be type list!", "ERROR", "TI Plotlib", "Plot")
    if cerr.type_error(list, y_list) == False: log("Argument 'y_list' has to be type list!", "ERROR", "TI Plotlib", "Plot")
    if cerr.type_error(str, mark) == False: log("Argument 'mark' has to be type string!", "ERROR", "TI Plotlib", "Plot")

    if cerr.argument_error(mark, "o", "+", "x", ".") == False: log("Argument 'mark' can only be one of these: 'o', '+', 'x', '.'!", "ERROR", "TI Plotlib", "Plot")

    err.type_error(list, "list", x_list)
    err.type_error(list, "list", y_list)
    err.type_error(str, "str", mark)

    err.argument_error(mark, "o", "+", "x", ".")

    log("Plotting a line with the mark '" + mark + "' in between the range of the specifed lists", "INFO", "TI Plotlib", "Plot")
    print("Plotting line with mark '" + mark + "' in between the given lists")
    return [x_list, y_list, mark]

def line(x1:float, y1:float, x2:float, y2:float, mode:str):
    """
    Plots a line segment from (x1,y1) to (x2,y2).

    Args:
        x1 (float): Start coordinate (x).
        y1 (float): Start coordinate (y).
        x2 (float): End coordinate (x).
        y2 (float): End coordinate (y).
        mode (str): The line mode. Possible Options: 'default', 'arrow'.

    Returns:
        list: a list containing the following data: [x1, y1, x2, y2, mode]
    """
    if cerr.type_error(float, x1) == False: log("Argument 'x1' has to be type float!", "ERROR", "TI Plotlib", "Line")
    if cerr.type_error(float, y1) == False: log("Argument 'y1' has to be type float!", "ERROR", "TI Plotlib", "Line")
    if cerr.type_error(float, x2) == False: log("Argument 'x2' has to be type float!", "ERROR", "TI Plotlib", "Line")
    if cerr.type_error(float, y2) == False: log("Argument 'y2' has to be type float!", "ERROR", "TI Plotlib", "Line")
    if cerr.type_error(str, mode) == False: log("Argument 'mode' has to be type string!", "ERROR", "TI Plotlib", "Line")


    if cerr.argument_error(mode, "default", "arrow") == False: log("Argument 'mode' can only be one of these: 'default', 'arrow'!", "ERROR", "TI Plotlib", "Line")


    err.type_error(float, "float", x1)
    err.type_error(float, "float", y1)
    err.type_error(float, "float", x2)
    err.type_error(float, "float", y2)
    err.type_error(str, "str", mode)


    err.argument_error(mode, "default", "arrow")

    log("Drawing a line of type '" + mode + "' from '(" + str(x1) + "|" + str(y1) + ")' to '(" + str(x2) + "|" + str(y2) + ")'", "INFO", "TI Plotlib", "Line")
    print("Drawing line of type '" + mode + "' from '(" + str(x1) + "|" + str(y1) + ")' to '(" + str(x2) + "|" + str(y2) + ")'")
    return [x1, y1, x2, y2, mode]

def lin_reg(x_list:list, y_list:list, display:str):
    """
    Calculates and draws the linear regression model, ax+b, of x-list,y-list.


    Args:
        x_list (list): The list of the possible x values.
        y_list (list): The list of the possible y values.
        display (str): The display alignment. Possible Options: 'left', 'center', 'right'.

    Returns:
        list: a list containing the following data: [x_list, y_list, display]
    """
    if cerr.type_error(list, x_list) == False: log("Argument 'x_list' has to be type list!", "ERROR", "TI Plotlib", "Linear Regression")
    if cerr.type_error(list, y_list) == False: log("Argument 'y_list' has to be type list!", "ERROR", "TI Plotlib", "Linear Regression")
    if cerr.type_error(str, display) == False: log("Argument 'dsiplay' has to be type string!", "ERROR", "TI Plotlib", "Linear Regression  ")

    if cerr.argument_error(display, "left", "center", "right") == False: log("Argument 'display' can only be one of these: 'left', 'center', 'right'!", "ERROR", "TI Plotlib", "Linear Regression")


    err.type_error(list, "list", x_list)
    err.type_error(list, "list", y_list)
    err.type_error(str, "str", display)

    err.argument_error(display, "left", "center", "right")

    log("Drawing linear regression model ax+b using the given lists with the alignment '" + display + "'", "INFO", "TI Plotlib", "Linear Regressio")
    print("Drawing linear regression model with display alignment '" + display + "'")
    return [x_list, y_list, display]

def pen(thickness:str, style:str):
    """
    Sets the appearance of all following lines until the next pen() is executed.

    Args:
        thickness (str): The thickness of the pen. Possible Options: 'thin', 'medium', 'thick'.
        style (str): The style of the pens line. Possible Options: 'solid', 'dotted', 'dashed'.

    Returns:
        list: a list containing the following data: [thickness, style]
    """
    if cerr.type_error(str, thickness) == False: log("Argument 'thickness' has to be type string!", "ERROR", "TI Plotlib", "Pen")
    if cerr.type_error(str, style) == False: log("Argument 'style' has to be type string!", "ERROR", "TI Plotlib", "Pen")

    if cerr.argument_error(thickness, "thin", "medium", "thick") == False: log("Argument 'thickness' can only be one of these: 'thin', 'medium', 'thick'!", "ERROR", "TI Plotlib", "Pen")
    if cerr.argument_error(style, "solid", "dotted", "dashed") == False: log("Argument 'style' can only be one of these: 'solid', 'dotted', 'dashed'!", "ERROR", "TI Plotlib", "Pen")


    err.type_error(str, "str", thickness)
    err.type_error(str, "str", style)

    err.argument_error(thickness, "thin", "medium", "thick")
    err.argument_error(style, "solid", "dotted", "dashed")

    log("Setting the thickness of the plotting pen to '" + thickness + "' and the line style to '" + style + "'", "INFO", "TI Plotlib", "Pen")
    print("Setting pen thickness to '" + thickness + "' and line style to '" + style + "'")
    return [thickness, style]

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

    if cerr.type_error(int, line) == False: log("Argument 'line' has to be type integer!", "ERROR", "TI Plotlib", "Text At")
    if cerr.type_error(str, text) == False: log("Argument 'text' has to be type string!", "ERROR", "TI Plotlib", "Text At")
    if cerr.type_error(str, align) == False: log("Argument 'align' has to be type string!", "ERROR", "TI Plotlib", "Text At")
    if cerr.argument_error(align, "left", "center", "right") == False: log("Argument 'align' can only be one of these: 'left', 'center', 'right'!", "ERROR", "TI Plotlib", "Text At")
    if cerr.range_error(1, 13, line) == False: log("Argument 'line' has to be between the values 1 and 13 (included)!", "ERROR", "TI Plotlib", "Text At")


    err.type_error(int, "int", line)
    err.type_error(str, "str", text)
    err.type_error(str, "str", align)
    err.argument_error(align, "left", "center", "right")
    err.range_error(1, 13, line)

    log("Showing text '" + text + "' at line " + str(line) + " with alignement '" + align + "'", "INFO", "TI Plotlib", "Text At")
    print("Showing text '" + text + "' at line " + str(line) + " with alignement '" + align + "'")
    return [text, line, align]