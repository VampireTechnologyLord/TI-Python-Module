"""
Class containing all the TI Plotlib elements.
"""
from typing import overload
from ti_python_module import err as err


def cls():
    """
    Clears the plotting canvas.

    Returns:
        None: None
    """
    print("Clearing screen / display")
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
    err.type_error(int, "int", x_min)
    err.type_error(int, "int", x_max)
    err.type_error(int, "int", y_min)
    err.type_error(int, "int", y_max)

    err.relation.smaller_error(x_min, x_max)
    err.relation.smaller_error(y_min, y_max)

    print("Setting the horizontal interval to '" + str(x_max - x_min) + "' pixels and the vertical interval to '" + str(y_max - y_min) + "' pixels.")
    return [x_min, x_max, y_min, y_max]

def auto_window(x_list:list, y_list:list):
    """
    Autoscales the plotting window to fit the data ranges within x-list and y-list specified in the program prior to the auto_window().

    Args:
        x_list (list): The list of x values.
        y_list (list): The list of y values.

    Returns:
        list: a list containing the following data: [x_list, y_list]
    """
    err.type_error(list, "list", x_list)
    err.type_error(list, "list", y_list)

    print("Auto-scaling the window to fit the specified plotting data")
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
    err.type_error(float, "float", x_scale)
    err.type_error(float, "float", y_scale)
    err.type_error(str, "str", style)

    err.argument_error(style, "solid", "dotted", "dashed")

    print("Setting the grid scale to '" + str(x_scale) + ", " + str(y_scale) + "' with the style '" + style + "'")
    return [x_scale, y_scale, style]

def axes(mode:str):
    """
    Displays axes on specified window in the plotting area.

    Args:
        mode (str): The mode of the axes. Options: 'off', 'on', 'axes', 'window'.

    Returns:
        list: a list containing the following data: [mode]
    """
    err.type_error(str, "str", mode)

    err.argument_error(mode, "off", "on", "axes", "window")
    print("Setting axes mode to '" + mode + "'")
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
    err.type_error(str, "str", x_name)
    err.type_error(str, "str", y_name)
    err.type_error(int, "int", x_row)
    err.type_error(int, "int", y_row)

    print("Displaying '" + x_name + "' at row '" + str(x_row) + "' for the x axis. Displaying '" + y_name + "' at row '" + str(y_row) + "' for the y axis.")
    return[x_name, y_name, x_row, y_row]

def title(title:str):
    """
    Displays the title centered on top line of window.

    Args:
        title (str): The displayed title.

    Returns:
        list: a list containing the following data: [title]
    """
    err.type_error(str, "str", title)

    print("Setting the title of the window to '" + title + "'")
    return [title]

def show_plot():
    """
    Displays the buffered drawing output. The use_buffer() and show_plot() functions are useful in cases where displaying multiple objects on the screen could cause delays (not necessary in most cases).

    Returns:
        None: None
    """
    print("Displaying buffered drawing output")
    return None

def use_buffer():
    """
    Enables an off-screen buffer to speed up drawing.

    Returns:
        None: None
    """
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
    err.type_error(float, "float", red)
    err.type_error(float, "float", green)
    err.type_error(float, "float", blue)

    err.range_error(0, 255, red)
    err.range_error(0, 255, green)
    err.range_error(0, 255, blue)
    
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
    err.type_error(list, "list", x_list)
    err.type_error(list, "list", y_list)
    err.type_error(str, "str", mark)

    err.argument_error(mark, "o", "+", "x", ".")

    print("Scattering mark '" + mark + "' in between the given lists")
    return [x_list, y_list, mark]


def plot(x_list:list, y_list:list, mark:str):
    """
    Plots a line using ordered pairs from specified x-list and y-list.


    Args:
        x_list (list): The list of the possible x values.
        y_list (list): The list of the possible y values.
        mark (str): The mark to scatter. Possible Options: 'o', '+', 'x', '.'.

    Returns:
        list: a list containing the following data: [x_list, y_list, mark]
    """
    err.type_error(list, "list", x_list)
    err.type_error(list, "list", y_list)
    err.type_error(str, "str", mark)

    err.argument_error(mark, "o", "+", "x", ".")

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
    err.type_error(float, "float", x1)
    err.type_error(float, "float", y1)
    err.type_error(float, "float", x2)
    err.type_error(float, "float", y2)
    err.type_error(str, "str", mode)

    err.relation.smaller_error(x1, x2)
    err.relation.smaller_error(y1, y2)

    err.argument_error(mode, "default", "arrow")

    print("Drawing line of type '" + mode + "' from '(" + str(x1) + "|" + str(y1) + ")' to '(" + str(x2) + "|" + str(y2) + ")'")
    return [x1, y1, x2, y2, mode]

def line_reg(x_list:list, y_list:list, display:str):
    """
    Calculates and draws the linear regression model, ax+b, of x-list,y-list.


    Args:
        x_list (list): The list of the possible x values.
        y_list (list): The list of the possible y values.
        display (str): The display alignment. Possible Options: 'left', 'center', 'right'.

    Returns:
        list: a list containing the following data: [x_list, y_list, display]
    """
    err.type_error(list, "list", x_list)
    err.type_error(list, "list", y_list)
    err.type_error(str, "str", display)

    err.argument_error(display, "left", "center", "right")

    print("Drawing linear regression model with display alignment '" + display + "'")
    return [x_list, y_list, display]

def pen(thickness:str, style:str):
    """
    Sets the appearance of all following lines until the next pen() is executed.

    Args:
        thickness (str): The thickness of the pen. Possible Options: 'thin', 'medium', 'thick'.
        style (str): The style of the pens line. Possible Options: 'solid', 'dotted', 'dashed'.

    Returns:
        list: list: a list containing the following data: [thickness, style]
    """
    err.type_error(str, "str", thickness)
    err.type_error(str, "str", style)

    err.argument_error(thickness, "thin", "medium", "thick")
    err.argument_error(style, "solid", "dotted", "dashed")

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
        list: list: list: a list containing the following data: [line, text, align]
    """
    err.type_error(int, "int", line)
    err.type_error(str, "str", text)
    err.type_error(str, "str", align)
    err.argument_error(align, "left", "center", "right")
    err.range_error(1, 13, line)

    print("Showing text '" + text + "' at line " + str(line) + " with alignement '" + align + "' !")
    return [text, line, align]