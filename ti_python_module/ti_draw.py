from ti_python_module.err import withConsole as err
from ti_python_module.err import onlyCheck as cerr
from ti_python_module.file_handler import create_log as log


"""
Class containing all TI-Draw commands

    • The default configuration has (0,0) in the top left corner of the screen. The positive x-axis points to the right and the positive y-axis points to the bottom This can be modified by using the set_window() function.\n
    • The functions in ti_draw module are only available on the handheld and in handheld view on desktop
"""



###########################################################################################

def draw_line(x1:float, y1:float, x2:float, y2:float):
    """
    Draws a line starting from the specified x1,y1 coordinate to x2,y2.

    Args:
        x1 (float): The first x coordinate.
        y1 (float): The first y coordinate.
        x2 (float): The second x coordinate.
        y2 (float): The second y coordinate.

    Returns:
        list: a list containing the following data: [x1, y1, x2, y2]
    """
    if cerr.type_error(float, x1) == False: log("Argument 'x1' has to be type float!", "ERROR", "TI Draw", "Draw Line")
    if cerr.type_error(float, y1) == False: log("Argument 'y1' has to be type float!", "ERROR", "TI Draw", "Draw Line")
    if cerr.type_error(float, x2) == False: log("Argument 'x2' has to be type float!", "ERROR", "TI Draw", "Draw Line")
    if cerr.type_error(float, y2) == False: log("Argument 'y2' has to be type float!", "ERROR", "TI Draw", "Draw Line")

    err.type_error(float, "float", x1)
    err.type_error(float, "float", y1)
    err.type_error(float, "float", x2)
    err.type_error(float, "float", y2)
    
    log("Drawing line from ( " + str(x1) + " | " + str(y1) + " ) to ( " + str(x2) + " | " + str(y2) + " )", "INFO", "TI Draw", "Draw Line")
    print("Drawing line from ( " + str(x1) + " | " + str(y1) + " ) to ( " + str(x2) + " | " + str(y2) + " )")
    return [x1, y1, x2, y2]

###########################################################################################

def draw_rect(x_start:float, y_start:float, width:float, height:float):
    """
    Draws a rectangle starting at the specified x,y coordinate with the specified width and height.
    
    Args:
        x_start (float): The starting x coordinate.
        y_start (float): The starting y coordinate.
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.

    Returns:
        list: a list containing the following data: [x_start, y_start, width, height]
    """
    if cerr.type_error(float, x_start) == False: log("Argument 'x_start' has to be type float!", "ERROR", "TI Draw", "Draw Rectangle")
    if cerr.type_error(float, y_start) == False: log("Argument 'y_start' has to be type float!", "ERROR", "TI Draw", "Draw Rectangle")
    if cerr.type_error(float, width) == False: log("Argument 'width' has to be type float!", "ERROR", "TI Draw", "Draw Rectangle")
    if cerr.type_error(float, height) == False: log("Argument 'height' has to be type float!", "ERROR", "TI Draw", "Draw Rectangle")


    err.type_error(float, "float", x_start)
    err.type_error(float, "float", y_start)
    err.type_error(float, "float", width)
    err.type_error(float, "float", height)

    log("Drawing rectangle from starting point: ( " + str(x_start) + " | " + str(y_start) + " ) with a width of '" + str(width) + "' and a height of '" + str(height) + "'", "INFO", "TI Draw", "Draw Rectangle")
    print("Drawing rectangle from starting point: ( " + str(x_start) + " | " + str(y_start) + " ) with a width of '" + str(width) + "' and a height of '" + str(height) + "'")
    return [x_start, y_start, width, height]

###########################################################################################

def fill_rect(x_start:float, y_start:float, width:float, height:float):
    """
    Draws a rectangle starting at the specified x,y coordinate with the specified width and height and filled with the specified color (using set_color or black if not defined).
    
    Args:
        x_start (float): The starting x coordinate.
        y_start (float): The starting y coordinate.
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.

    Returns:
        list: a list containing the following data: [x_start, y_start, width, height]
    """
    if cerr.type_error(float, x_start) == False: log("Argument 'x_start' has to be type float!", "ERROR", "TI Draw", "Filled Rectangle")
    if cerr.type_error(float, y_start) == False: log("Argument 'y_start' has to be type float!", "ERROR", "TI Draw", "Filled Rectangle")
    if cerr.type_error(float, width) == False: log("Argument 'width' has to be type float!", "ERROR", "TI Draw", "Filled Rectangle")
    if cerr.type_error(float, height) == False: log("Argument 'height' has to be type float!", "ERROR", "TI Draw", "Fill Rectangle")


    err.type_error(float, "float", x_start)
    err.type_error(float, "float", y_start)
    err.type_error(float, "float", width)
    err.type_error(float, "float", height)

    log("Drawing a filled rectangle from starting point: ( " + str(x_start) + " | " + str(y_start) + " ) with a width of '" + str(width) + "' and a height of '" + str(height) + "'", "INFO", "TI Draw", "Filled Rectangle")
    print("Drawing filled rectangle from starting point: ( " + str(x_start) + " | " + str(y_start) + " ) with a width of '" + str(width) + "' and a height of '" + str(height) + "'")
    return [x_start, y_start, width, height]

###########################################################################################

def draw_circle(x_start:float, y_start:float, radius:float):
    """
    Draws a circle starting at the specified x,y center coordinate with the specified radius.
    
    Args:
        x_start (float): The starting x coordinate.
        y_start (float): The starting y coordinate.
        radius (float): The radius of the circle.

    Returns:
        list: a list containing the following data: [x_start, y_start, radius]
    """

    if cerr.type_error(float, x_start) == False: log("Argument 'x_start' has to be type float!", "ERROR", "TI Draw", "Draw Circle")
    if cerr.type_error(float, y_start) == False: log("Argument 'y_start' has to be type float!", "ERROR", "TI Draw", "Draw Circle")
    if cerr.type_error(float, radius) == False: log("Argument 'radius' has to be type float!", "ERROR", "TI Draw", "Draw Circle")

    err.type_error(float, "float", x_start)
    err.type_error(float, "float", y_start)
    err.type_error(float, "float", radius)

    log("Drawing circle from starting point: ( " + str(x_start) + " | " + str(y_start) + " ) with a radius of '" + str(radius) + "'", "INFO", "TI Draw", "Draw Circle")
    print("Drawing circle from starting point: ( " + str(x_start) + " | " + str(y_start) + " ) with a radius of '" + str(radius) + "'")
    return [x_start, y_start, radius]

###########################################################################################

def fill_circle(x_start:float, y_start:float, radius:float):
    """
    Draws a circle starting at the specified x,y center coordinate with the specified radius and filled with the specified color (using set_color or black if not defined).
    
    Args:
        x_start (float): The starting x coordinate.
        y_start (float): The starting y coordinate.
        radius (float): The radius of the circle.

    Returns:
        list: a list containing the following data: [x_start, y_start, radius]
    """

    if cerr.type_error(float, x_start) == False: log("Argument 'x_start' has to be type float!", "ERROR", "TI Draw", "Filled Circle")
    if cerr.type_error(float, y_start) == False: log("Argument 'y_start' has to be type float!", "ERROR", "TI Draw", "Filled Circle")
    if cerr.type_error(float, radius) == False: log("Argument 'radius' has to be type float!", "ERROR", "TI Draw", "Filled Circle")

    err.type_error(float, "float", x_start)
    err.type_error(float, "float", y_start)
    err.type_error(float, "float", radius)

    log("Drawing a filled circle from starting point: ( " + str(x_start) + " | " + str(y_start) + " ) with a radius of '" + str(radius) + "'", "INFO", "TI Draw", "Filled Circle")
    print("Drawing filled circle from starting point: ( " + str(x_start) + " | " + str(y_start) + " ) with a radius of '" + str(radius) + "'")
    return [x_start, y_start, radius]

###########################################################################################

def draw_text(x_start:float, y_start:float, text:str):
    """
    Draws a text string at the specified x, y coordinate.
    
    Args:
        x_start (float): The starting x coordinate.
        y_start (float): The starting y coordinate.
        text (str): The text to draw.

    Returns:
        list: a list containing the following data: [x_start, y_start, text]
    """

    if cerr.type_error(float, x_start) == False: log("Argument 'x_start' has to be type float!", "ERROR", "TI Draw", "Draw Text")
    if cerr.type_error(float, y_start) == False: log("Argument 'y_start' has to be type float!", "ERROR", "TI Draw", "Draw Text")
    if cerr.type_error(str, text) == False: log("Argument 'text' has to be type string!", "ERROR", "TI Draw", "Draw Text")

    err.type_error(float, "float", x_start)
    err.type_error(float, "float", y_start)
    err.type_error(str, "str", text)
 
    log("Drawing text '" + text + "' from starting point: ( " + str(x_start) + " | " + str(y_start) + " )", "INFO", "TI Draw", "Draw Text")
    print("Drawing text '" + text + "' from starting point: ( " + str(x_start) + " | " + str(y_start) + " )")
    return [x_start, y_start, text]

###########################################################################################

def draw_arc(x_start:float, y_start:float, width:float, height:float, start_angle:float, arc_angle:float):
    """
    Draws an arc starting at the specified x,y coordinate with the specified width, height and angles.

    Args:
        x_start (float): The starting x coordinate.
        y_start (float): The starting y coordinate.
        width (float): The width of the arc.
        height (float): The height of the arc.
        start_angle (float): The starting angle of the arc.
        arc_angle (float): The arc angle.

    Returns:
        list: a list containing the following data: [x_start, y_start, width, height, start_angle, arc_angle]
    """
    if cerr.type_error(float, x_start) == False: log("Argument 'x_start' has to be type float!", "ERROR", "TI Draw", "Draw Arc")
    if cerr.type_error(float, y_start) == False: log("Argument 'y_start' has to be type float!", "ERROR", "TI Draw", "Draw Arc")
    if cerr.type_error(float, width) == False: log("Argument 'width' has to be type float!", "ERROR", "TI Draw", "Draw Arc")
    if cerr.type_error(float, height) == False: log("Argument 'height' has to be type float!", "ERROR", "TI Draw", "Draw Arc")
    if cerr.type_error(float, start_angle) == False: log("Argument 'start_angle' has to be type float!", "ERROR", "TI Draw", "Draw Arc")
    if cerr.type_error(float, arc_angle) == False: log("Argument 'arc_angle' has to be type float!", "ERROR", "TI Draw", "Draw Arc")

    err.type_error(float, "float", x_start)
    err.type_error(float, "float", y_start)
    err.type_error(float, "float", width)
    err.type_error(float, "float", height)
    err.type_error(float, "float", start_angle)
    err.type_error(float, "float", arc_angle)

    log("Drawing arc from starting point: ( " + str(x_start) + " | " + str(y_start) + " ) with start-angle '" + str(start_angle) + " degrees' and arc-angle '" + str(arc_angle) + " degrees' with a height of '" + str(height) + "' and a width of '" + str(width) + "'", "INFO", "TI Draw", "Draw Arc")
    print("Drawing arc from starting point: ( " + str(x_start) + " | " + str(y_start) + " ) with start-angle '" + str(start_angle) + " degrees' and arc-angle '" + str(arc_angle) + " degrees' with a height of '" + str(height) + "' and a width of '" + str(width) + "'")
    return [x_start, y_start, width, height, start_angle, arc_angle]

###########################################################################################

def fill_arc(x_start:float, y_start:float, width:float, height:float, start_angle:float, arc_angle:float):
    """
    Draws an arc starting at the specified x,y coordinate with the specified width, height and angles filled with the specified color (using set_color or black if not defined). 

    Args:
        x_start (float): The starting x coordinate.
        y_start (float): The starting y coordinate.
        width (float): The width of the arc.
        height (float): The height of the arc.
        start_angle (float): The starting angle of the arc.
        arc_angle (float): The arc angle.

    Returns:
        list: a list containing the following data: [x_start, y_start, width, height, start_angle, arc_angle]
    """
    if cerr.type_error(float, x_start) == False: log("Argument 'x_start' has to be type float!", "ERROR", "TI Draw", "Filled Arc")
    if cerr.type_error(float, y_start) == False: log("Argument 'y_start' has to be type float!", "ERROR", "TI Draw", "Filled Arc")
    if cerr.type_error(float, width) == False: log("Argument 'width' has to be type float!", "ERROR", "TI Draw", "Filled Arc")
    if cerr.type_error(float, height) == False: log("Argument 'height' has to be type float!", "ERROR", "TI Draw", "Filled Arc")
    if cerr.type_error(float, start_angle) == False: log("Argument 'start_angle' has to be type float!", "ERROR", "TI Draw", "Filled Arc")
    if cerr.type_error(float, arc_angle) == False: log("Argument 'arc_angle' has to be type float!", "ERROR", "TI Draw", "Filled Arc")

    err.type_error(float, "float", x_start)
    err.type_error(float, "float", y_start)
    err.type_error(float, "float", width)
    err.type_error(float, "float", height)
    err.type_error(float, "float", start_angle)
    err.type_error(float, "float", arc_angle)

    log("Drawing a filled arc from starting point: ( " + str(x_start) + " | " + str(y_start) + " ) with start-angle '" + str(start_angle) + " degrees' and arc-angle '" + str(arc_angle) + " degrees' with a height of '" + str(height) + "' and a width of '" + str(width) + "'", "INFO", "TI Draw", "Filled Arc")
    print("Drawing filled arc from starting point: ( " + str(x_start) + " | " + str(y_start) + " ) with start-angle '" + str(start_angle) + " degrees' and arc-angle '" + str(arc_angle) + " degrees' with a height of '" + str(height) + "' and a width of '" + str(width) + "'")
    return [x_start, y_start, width, height, start_angle, arc_angle]

###########################################################################################

def draw_poly(x_list:list[float], y_list:list[float]):
    """
    Draws a polygon using the specified x-list,y-list values.

    Args:
        x_list (list): The list of values with the x coordinates.
        y_list (list): The list of values with the y coordinates.

    Returns:
        list: a list containing the following data: [x_list, y_list]
    """
    if cerr.type_error(list, x_list) == False: log("Argument 'x_list' has to be type list!", "ERROR", "TI Draw", "Draw Polygon")
    if cerr.type_error(list, y_list) == False: log("Argument 'y_list' has to be type list!", "ERROR", "TI Draw", "Draw Polygon")

    err.type_error(list, "list", x_list)
    err.type_error(list, "list", y_list)
    
    log("Drawing a polygon from the given x and y list", "INFO", "TI Draw", "Draw Polygon")
    print("Drawing Polygon from x-list and y-list")
    return [x_list, y_list]

###########################################################################################

def fill_poly(x_list:list, y_list:list):
    """
    Draws a polygon using the specified x-list,y-list values filled with the specified colour (using set_colour or black if not defined).

    Args:
        x_list (list): The list of values with the x coordinates.
        y_list (list): The list of values with the y coordinates.

    Returns:
        list: a list containing the following data: [x_list, y_list]
    """
    if cerr.type_error(list, x_list) == False: log("Argument 'x_list' has to be type list!", "ERROR", "TI Draw", "Filled Polygon")
    if cerr.type_error(list, y_list) == False: log("Argument 'y_list' has to be type list!", "ERROR", "TI Draw", "Filled Polygon")

    err.type_error(list, "list", x_list)
    err.type_error(list, "list", y_list)
    
    log("Drawing a filled polygon from the given x and y list", "INFO", "TI Draw", "Filled Polygon")
    print("Drawing filled Polygon from x-list and y-list")
    return [x_list, y_list]

###########################################################################################

def plot_xy(x_start:float, y_start:float, form_id:int):
    """
    Draws a shape using the specified x,y coordinate and specified number from 1-13 representing different shapes and symbols.
    
    Args:
        x_start (float): The x coordinate to draw at.
        y_start (float): The y coordinate to draw at.
        form_id (int): The id of which form to draw.

    Returns:
        list: a list containing the following data: [x_start, y_start, form_id]
    """

    if cerr.type_error(float, x_start) == False: log("Argument 'x_start' has to be type float!", "ERROR", "TI Draw", "Plot XY")
    if cerr.type_error(float, y_start) == False: log("Argument 'y_start' has to be type float!", "ERROR", "TI Draw", "Plot XY")
    if cerr.type_error(int, form_id) == False: log("Argument 'form_id' has to be type integer!", "ERROR", "TI Draw", "Plot XY")
    if cerr.range_error(1, 13, form_id) == False: log("Argument 'form_id' has to be between the values 1 and 13 (inclusive)!", "ERROR", "TI Draw", "Plot XY")

    err.type_error(float, "float", x_start)
    err.type_error(float, "float", y_start)
    err.type_error(int, "int", form_id)

    err.range_error(1, 13, form_id)
    
    log("Drawing form with id '" + str(form_id) + "' at ( " + str(x_start) + " | " + str(y_start) + " )", "INFO", "TI Draw", "Plot XY")
    print("Drawing form '" + str(form_id) + "' at ( " + str(x_start) + " | " + str(y_start) + " )")
    return [x_start, y_start, form_id]

###########################################################################################

def clear():
    """
    Clears the entire screen. Use 'clear_rect' to clear only a rectangular area.
    
    Returns:
        None: None
    """
    log("Clearing all drawings from the screen / display", "INFO", "TI Draw", "Clear")
    print("Clearing Drawings from Screen")
    return None

###########################################################################################

def clear_rect(x_start:float, y_start:float, width:float, height:float):
    """
    Clears a rectangular area from the screen, specified with the x, y, width, height.
    
    Args:
        x_start (float): The starting x coordinate.
        y_start (float): The starting y coordinate.
        width (float): The width of the rectangle to clear.
        height (float): The height of the rectangle to clear.

    Returns:
        list: a list containing the following data: [x_start, y_start, width, height]
    """
    if cerr.type_error(float, x_start) == False: log("Argument 'x_start' has to be type float!", "ERROR", "TI Draw", "Clear Rectangle")
    if cerr.type_error(float, y_start) == False: log("Argument 'y_start' has to be type float!", "ERROR", "TI Draw", "Clear Rectangle")
    if cerr.type_error(float, width) == False: log("Argument 'width' has to be type float!", "ERROR", "TI Draw", "Clear Rectangle")
    if cerr.type_error(float, height) == False: log("Argument 'height' has to be type float!", "ERROR", "TI Draw", "Clear Rectangle")


    err.type_error(float, "float", x_start)
    err.type_error(float, "float", y_start)
    err.type_error(float, "float", width)
    err.type_error(float, "float", height)

    log("Clearing a rectangular area from starting point: ( " + str(x_start) + " | " + str(y_start) + " ) with a width of '" + str(width) + "' and a height of '" + str(height) + "'", "INFO", "TI Draw", "Clear Rectangle")
    print("Clearing a rectangular area from starting point: ( " + str(x_start) + " | " + str(y_start) + " ) with a width of '" + str(width) + "' and a height of '" + str(height) + "'")
    return [x_start, y_start, width, height]

###########################################################################################

def set_colour(red:int, green:int, blue:int):
    """
    Sets the color of the shape(s) that follow in the program until another color is set. 

    Args:
        red (int): The amount of red. Ranges from 0 to 255.
        green (int): The amount of green. Ranges from 0 to 255.
        blue (int): The amount of blue. Ranges from 0 to 255.

    Returns:
        list: a list containing the following data: [red, green, blue]
    """
    if cerr.type_error(int, red) == False: log("Argument 'red' has to be type integer!", "ERROR", "TI Draw", "Set Colour")
    if cerr.type_error(int, green) == False: log("Argument 'green' has to be type integer!", "ERROR", "TI Draw", "Set Colour")
    if cerr.type_error(int, blue) == False: log("Argument 'blue' has to be type integer!", "ERROR", "TI Draw", "Set Colour")

    if cerr.range_error(0, 255, red) == False: log("Argument 'red' has to be between the values 0 and 255!", "ERROR", "TI Draw", "Set Colour")
    if cerr.range_error(0, 255, green) == False: log("Argument 'green' has to be between the values 0 and 255!", "ERROR", "TI Draw", "Set Colour")
    if cerr.range_error(0, 255, blue) == False: log("Argument 'blue' has to be between the values 0 and 255!", "ERROR", "TI Draw", "Set Colour")


    err.type_error(int, "int", red)
    err.type_error(int, "int", green)
    err.type_error(int, "int", blue)

    err.range_error(0, 255, red)
    err.range_error(0, 255, green)
    err.range_error(0, 255, blue)
    
    
    log("Setting drawing colour to red '" +str(red) + "', green '" + str(green) + "', blue '" + str(blue) + "'", "INFO", "TI Draw", "Set Colour")
    print("Setting drawing colour to red '" +str(red) + "', green '" + str(green) + "', blue '" + str(blue) + "'")
    return [red, green, blue]
    
###########################################################################################

def set_pen(thickness:str, stile:str):
    """
    Sets the specified thickness and style of the border when drawing shapes (not applicable when using fill commands). 
    
    Args:
        thickness (str): The thickness of the pen. Possible Options: 'thin', 'medium', 'thick'.
        stile (str): The stile of the pen. Possible Options: 'solid', 'dotted', 'dashed'.

    Returns:
        list: a list containing the following data: [thickness, stile]
    """
    if cerr.type_error(str, thickness) == False: log("Argument 'thickness' has to be type string!", "ERROR", "TI Draw", "Set Pen")
    if cerr.type_error(str, stile) == False: log("Argument 'stile' has to be type string!", "ERROR", "TI Draw", "Set Pen")

    if cerr.argument_error(thickness, "thin", "medium", "thick") == False: log("Argument 'thickness' can only be one of these: 'thin', 'medium', 'thick'!", "ERROR", "TI Draw", "Set Pen")
    if cerr.argument_error(stile, "solid", "dotted", "dashed") == False: log("Argument 'stile' can only be one of these: 'solid', 'dotted', 'dashed'!", "ERROR", "TI Draw", "Set Pen")

    err.type_error(str, "str", thickness)
    err.type_error(str, "str", stile)

    err.argument_error(thickness, "thin", "medium", "thick")
    err.argument_error(stile, "solid", "dotted", "dashed")

    log("Setting Drawing Pen thickness to '" + thickness + "' and pen stile to '" + stile + "'", "INFO", "TI Draw", "Set Pen")
    print("Setting Drawing Pen thickness to '" + thickness + "' and pen stile to '" + stile + "'")
    return [thickness, stile]

###########################################################################################

def set_window(x_min:int, x_max:int, y_min:int, y_max:int):
    """
    Sets the size of the window in which any shapes will be drawn. This function is useful to resize the window to match the data or to change the origin (0,0) of the drawing canvas.

    Args:
        x_min (int): The minimum x coordinate.
        x_max (int): The minimum y coordinate.
        y_min (int): The maximum x coordinate.
        y_max (int): The maximum y corrdinate.

    Raises:
        ValueError: If x_min is greater or equal to x_max.
        ValueError: If y_min is greater or equal to y_max.

    Returns:
        list: a list containing the following data: [x_min, x_max, y_min, y_max]
    """
    if cerr.type_error(int, x_min) == False: log("Argument 'x_min' has to be type integer!", "ERROR", "TI Draw", "Set Window")
    if cerr.type_error(int, x_max) == False: log("Argument 'x_max' has to be type integer!", "ERROR", "TI Draw", "Set Window")
    if cerr.type_error(int, y_min) == False: log("Argument 'y_min' has to be type integer!", "ERROR", "TI Draw", "Set Window")
    if cerr.type_error(int, y_max) == False: log("Argument 'y_max' has to be type integer!", "ERROR", "TI Draw", "Set Window")

    if cerr.relation.larger_equal_error(x_min, x_max) == False: log("Argument 'x_min' has to be smaller then argument 'x_max'!", "ERROR", "TI Draw", "Set Window")
    if cerr.relation.larger_equal_error(y_min, y_max) == False: log("Argument 'y_min' has to be smaller then argument 'y_max'!", "ERROR", "TI Draw", "Set Window")


    err.type_error(int, "int", x_min)
    err.type_error(int, "int", x_max)
    err.type_error(int, "int", y_min)
    err.type_error(int, "int", y_max)

    err.relation.larger_equal_error(x_min, x_max)
    err.relation.larger_equal_error(y_min, y_max)

    log("Setting Drawing window from (" + str(x_min) + " | " + str(y_min) + " ) to (" + str(x_max) + " | " + str(y_max) + " )", "INFO", "TI Draw", "Set Window")
    print("Setting Drawing window from (" + str(x_min) + " | " + str(y_min) + " ) to (" + str(x_max) + " | " + str(y_max) + " )")
    return [x_min, x_max, y_min, y_max]

###########################################################################################

def get_screen_dim():
    """
    Returns the x_max and y_max of the screen dimensions.
    
    Returns:
        None: None
    """
    log("Getting the max coordinates of the screen / window", "INFO", "TI Draw", "Get Screen Dimension")
    print("Getting max coordinates of screen / window")
    return None

###########################################################################################

def use_buffer():
    """
    Enables an off-screen buffer to speed up drawing.
    
    Returns:
        None: None
    """
    log("Enabling the use of the off-screen buffer for faster drawing", "INFO", "TI Draw", "Use Buffer")
    print("Enabled off-screen buffer")
    return None

###########################################################################################

def paint_buffer():
    """
    Displays the buffered drawing output. The 'use_buffer()' and 'paint_buffer()' functions are useful in cases where displaying multiple objects on the screen could cause delays.
    
    Returns:
        None: None
    """
    log("Displaying the buffered content", "INFO", "TI Draw", "Paint Buffer")
    print("Displaying buffered output")