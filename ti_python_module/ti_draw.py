import err


"""
Class containing all TI-Draw commands

    • The default configuration has (0,0) in the top left corner of the screen. The positive x-axis points to the right and the positive y-axis points to the bottom This can be modified by using the set_window() function.\n
    • The functions in ti_draw module are only available on the handheld and in handheld view on desktop
"""



###########################################################################################

def draw_line(x1:float, y1:float, x2:float, y2:float):
    """
    Draws a line starting from the specified x1,y1 coordinate to x2,y2.
    
    
    Category: TI Draw / Shape
    
    
    Returns an array / list: [x1, y1, x2, y2]
    """
    err.type_error(float, "float", x1)
    err.type_error(float, "float", y1)
    err.type_error(float, "float", x2)
    err.type_error(float, "float", y2)
    
    print("Drawing line from ( " + str(x1) + " | " + str(y1) + " ) to ( " + str(x2), + " | " + str(y2) + " )")
    return [x1, y1, x2, y2]

###########################################################################################

def draw_rect(x_start:float, y_start:float, width:float, height:float):
    """
    Draws a rectangle starting at the specified x,y coordinate with the specified width and height.
    
    
    Category: TI Draw / Shape
    
    
    Returns an array / list: [x_start, y_start, width, height]
    """
    err.type_error(float, "float", x_start)
    err.type_error(float, "float", y_start)
    err.type_error(float, "float", width)
    err.type_error(float, "float", height)

    print("Drawing rectangle from starting point: ( " + str(x_start) + " | " + str(y_start) + " ) with a width of '" + str(width) + "' and a height of '" + str(height) + "'")
    return [x_start, y_start, width, height]

###########################################################################################

def fill_rect(x_start:float, y_start:float, width:float, height:float):
    """
    Draws a rectangle starting at the specified x,y coordinate with the specified width and height and filled with the specified color (using set_color or black if not defined).
    
    
    Category: TI Draw / Shape
    
    
    Returns an array / list: [x_start, y_start, width, height]
    """
    err.type_error(float, "float", x_start)
    err.type_error(float, "float", y_start)
    err.type_error(float, "float", width)
    err.type_error(float, "float", height)

    print("Drawing filled rectangle from starting point: ( " + str(x_start) + " | " + str(y_start) + " ) with a width of '" + str(width) + "' and a height of '" + str(height) + "'")
    return [x_start, y_start, width, height]

###########################################################################################

def draw_circle(x_start:float, y_start:float, radius:float):
    """
    Draws a circle starting at the specified x,y center coordinate with the specified radius.
    
    
    Category: TI Draw / Shape
    
    
    Returns an array / list: [x_start, y_start, radius]
    """
    err.type_error(float, "float", x_start)
    err.type_error(float, "float", y_start)
    err.type_error(float, "float", radius)

    print("Drawing circle from starting point: ( " + str(x_start) + " | " + str(y_start) + " ) with a radius of '" + str(radius) + "'")
    return [x_start, y_start, radius]

###########################################################################################

def fill_circle(x_start:float, y_start:float, radius:float):
    """
    Draws a circle starting at the specified x,y center coordinate with the specified radius and filled with the specified color (using set_color or black if not defined).
    
    
    Category: TI Draw / Shape
    
    
    Returns an array / list: [x_start, y_start, radius]
    """
    err.type_error(float, "float", x_start)
    err.type_error(float, "float", y_start)
    err.type_error(float, "float", radius)

    print("Drawing filled circle from starting point: ( " + str(x_start) + " | " + str(y_start) + " ) with a radius of '" + str(radius) + "'")
    return [x_start, y_start, radius]

###########################################################################################

def draw_text(x_start:float, y_start:float, text:str):
    """
    Draws a text string at the specified x, y coordinate.
    
    
    Category: TI Draw / Shape
    
    
    Returns an array / list: [x_start, y_start, text]
    """
    err.type_error(float, "float", x_start)
    err.type_error(float, "float", y_start)
    err.type_error(str, "str", text)
 
    print("Drawing text '" + text + "' from starting point: ( " + str(x_start) + " | " + str(y_start) + " )")
    return [x_start, y_start, text]

###########################################################################################

def draw_arc(x_start:float, y_start:float, width:float, height:float, start_angle:float, arc_angle:float):
    """
    Draws an arc starting at the specified x,y coordinate with the specified width, height and angles. 
    
    
    Category: TI Draw / Shape
    
    
    Returns an array / list: [x_start, y_start, width, height, start_angle, arc_angle]
    """
    err.type_error(float, "float", x_start)
    err.type_error(float, "float", y_start)
    err.type_error(float, "float", width)
    err.type_error(float, "float", height)
    err.type_error(float, "float", start_angle)
    err.type_error(float, "float", arc_angle)

    print("Drawing arc from starting point: ( " + str(x_start) + " | " + str(y_start) + " ) with start-angle '" + str(start_angle) + " degrees' and arc-angle '" + str(arc_angle) + " degrees' with a height of '" + str(height) + "' and a width of '" + str(width) + "'")
    return [x_start, y_start, width, height, start_angle, arc_angle]

###########################################################################################

def draw_arc(x_start:float, y_start:float, width:float, height:float, start_angle:float, arc_angle:float):
    """
    Draws an arc starting at the specified x,y coordinate with the specified width, height and angles filled with the specified color (using set_color or black if not defined). 
    
    
    Category: TI Draw / Shape
    
    
    Returns an array / list: [x_start, y_start, width, height, start_angle, arc_angle]
    """
    err.type_error(float, "float", x_start)
    err.type_error(float, "float", y_start)
    err.type_error(float, "float", width)
    err.type_error(float, "float", height)
    err.type_error(float, "float", start_angle)
    err.type_error(float, "float", arc_angle)
    
    print("Drawing filled arc from starting point: ( " + str(x_start) + " | " + str(y_start) + " ) with start-angle '" + str(start_angle) + " degrees' and arc-angle '" + str(arc_angle) + " degrees' with a height of '" + str(height) + "' and a width of '" + str(width) + "'")
    return [x_start, y_start, width, height, start_angle, arc_angle]

###########################################################################################

def draw_poly(x_list:list, y_list:list):
    """
    Draws a polygon using the specified x-list,y-list values.
    
    
    Category: TI Draw / Shape
    
    
    Returns an array / list: [x_list, y_list]
    """
    err.type_error(list, "list", x_list)
    err.type_error(list, "list", y_list)
    
    print("Drawing Polygon from x-list and y-list")
    return [x_list, y_list]

###########################################################################################

def fill_poly(x_list:list, y_list:list):
    """
    Draws a polygon using the specified x-list,y-list values filled with the specified colour (using set_colour or black if not defined).
    
    
    Category: TI Draw / Shape
    
    
    Returns an array / list: [x_list, y_list]
    """
    err.type_error(list, "list", x_list)
    err.type_error(list, "list", y_list)
    
    print("Drawing filled Polygon from x-list and y-list")
    return [x_list, y_list]

###########################################################################################

def plot_xy(x:float, y:float, form_id:int):
    """
    Description
    
    
    Category: TI Draw / Shape
    
    
    Returns an array / list: [x, y, form_id]
    """
    err.type_error(float, "float", x)
    err.type_error(float, "float", y)
    err.type_error(int, "int", y)
        
    print("Drawing form '" + str(form_id) + "' at ( " + str(x) + " | " + str(y) + " )")
    return [x, y, form_id]

###########################################################################################

def clear():
    """
    Clears the entire screen. Can be used with x,y,width,height parameters to clear an existing rectangle.
    
    
    Category: TI Draw / Control
    
    
    Returns None
    """
    print("Clearing Drawings from Screen")
    return None

###########################################################################################

def clear_rect(x_start:float, y_start:float, width:float, height:float):
    """
    Clears a rectangular area from the screen, specified with the x, y, width, height.
    
    
    Category: TI Draw / Control
    
    
    Returns an array / list: [x_start, y_start, width, height]
    """
    print("Clearing rectangular space from starting point: ( " + str(x_start) + " | " + str(y_start) + " ) with a height of '" + str(height) + "' and a width of '" + str(width) + "'")
    return [x_start, y_start, width, height]

###########################################################################################

def set_colour(red:int, green:int, blue:int):
    """
    Sets the color of the shape(s) that follow in the program until another color is set. 
    
    
    Category: TI Draw / Control
    
    
    Returns an array / list: [red, green, blue]
    """
    err.type_error(int, "int", red)
    err.type_error(int, "int", green)
    err.type_error(int, "int", blue)

    err.range_error(0, 255, red)
    err.range_error(0, 255, green)
    err.range_error(0, 255, blue)
    
    

    print("Setting drawing colour to red '" +str(red) + "', green '" + str(green) + "', blue '" + str(blue) + "'")
    return [red, green, blue]
    
###########################################################################################

def set_pen(thickness:str, stil:str):
    """
    Sets the specified thickness and style of the border when drawing shapes (not applicable when using fill commands). 
    
    
    Category: TI Draw / Control
    
    
    Returns an array / list: [thickness, stil]
    """
    err.type_error(str, "str", thickness)
    err.type_error(str, "str", stil)

    err.argument_error(thickness, "thin", "medium", "thick")
    err.argument_error(stil, "solid", "dotted", "dashed")

    print("Setting Drawing Pen thickness to '" + thickness + "' and pen stil to '" + stil + "'")
    return [thickness, stil]