"""
Class containing all TI-Draw commands
"""


def errormsg_type(requiredDataType: str, parameter: str):
    msg = "ERROR: Parameter <" + parameter + \
        "> has to be data-type " + requiredDataType + "!"
    return msg


def errormsg_range(rangeMin: float, rangeMax: float, parameter: str):
    msg = "ERROR: Parameter <" + parameter + \
        "> has to be in range between " + str(rangeMin) + " and " + str(rangeMax) + "!"
    return msg


###########################################################################################

def draw_line(x1:float, y1:float, x2:float, y2:float):
    """
    Draws a line starting from the specified x1,y1 coordinate to x2,y2.
    
    
    Category: TI Draw / Shape
    
    
    Returns an array / list: [x1, y1, x2, y2]
    """
    try:
        float(x1)
    except ValueError:
        raise ValueError(errormsg_type("float", "x1")) from None
    try:
        float(y1)
    except ValueError:
        raise ValueError(errormsg_type("float", "y1")) from None
    try:
        float(x2)
    except ValueError:
        raise ValueError(errormsg_type("float", "x2")) from None
    try:
        float(y2)
    except ValueError:
        raise ValueError(errormsg_type("float", "y2")) from None
    
    print("Drawing line from ( " + str(x1) + " | " + str(y1) + " ) to ( " + str(x2), + " | " + str(y2) + " )")
    return [x1, y1, x2, y2]

###########################################################################################

def draw_rect(x_start:float, y_start:float, width:float, height:float):
    """
    Draws a rectangle starting at the specified x,y coordinate with the specified width and height.
    
    
    Category: TI Draw / Shape
    
    
    Returns an array / list: [x_start, y_start, width, height]
    """
    try:
        float(x_start)
    except ValueError:
        raise ValueError(errormsg_type("float", "x_start")) from None
    try:
        float(y_start)
    except ValueError:
        raise ValueError(errormsg_type("float", "y_start")) from None
    try:
        float(width)
    except ValueError:
        raise ValueError(errormsg_type("float", "width")) from None
    try:
        float(height)
    except ValueError:
        raise ValueError(errormsg_type("float", "height")) from None

    print("Drawing rectangle from starting point: ( " + str(x_start) + " | " + str(y_start) + " ) with a width of '" + str(width) + "' and a height of '" + str(height) + "'")
    return [x_start, y_start, width, height]

###########################################################################################

def fill_rect(x_start:float, y_start:float, width:float, height:float):
    """
    Draws a rectangle starting at the specified x,y coordinate with the specified width and height and filled with the specified color (using set_color or black if not defined).
    
    
    Category: TI Draw / Shape
    
    
    Returns an array / list: [x_start, y_start, width, height]
    """
    try:
        float(x_start)
    except ValueError:
        raise ValueError(errormsg_type("float", "x_start")) from None
    try:
        float(y_start)
    except ValueError:
        raise ValueError(errormsg_type("float", "y_start")) from None
    try:
        float(width)
    except ValueError:
        raise ValueError(errormsg_type("float", "width")) from None
    try:
        float(height)
    except ValueError:
        raise ValueError(errormsg_type("float", "height")) from None

    print("Drawing filled rectangle from starting point: ( " + str(x_start) + " | " + str(y_start) + " ) with a width of '" + str(width) + "' and a height of '" + str(height) + "'")
    return [x_start, y_start, width, height]

###########################################################################################

def draw_circle(x_start:float, y_start:float, radius:float):
    """
    Draws a circle starting at the specified x,y center coordinate with the specified radius.
    
    
    Category: TI Draw / Shape
    
    
    Returns an array / list: [x_start, y_start, radius]
    """
    try:
        float(x_start)
    except ValueError:
        raise ValueError(errormsg_type("float", "x_start")) from None
    try:
        float(y_start)
    except ValueError:
        raise ValueError(errormsg_type("float", "y_start")) from None
    try:
        float(radius)
    except ValueError:
        raise ValueError(errormsg_type("float", "radius")) from None
    print("Drawing circle from starting point: ( " + str(x_start) + " | " + str(y_start) + " ) with a radius of '" + str(radius) + "'")
    return [x_start, y_start, radius]

###########################################################################################

def fill_circle(x_start:float, y_start:float, radius:float):
    """
    Draws a circle starting at the specified x,y center coordinate with the specified radius and filled with the specified color (using set_color or black if not defined).
    
    
    Category: TI Draw / Shape
    
    
    Returns an array / list: [x_start, y_start, radius]
    """
    try:
        float(x_start)
    except ValueError:
        raise ValueError(errormsg_type("float", "x_start")) from None
    try:
        float(y_start)
    except ValueError:
        raise ValueError(errormsg_type("float", "y_start")) from None
    try:
        float(radius)
    except ValueError:
        raise ValueError(errormsg_type("float", "radius")) from None
    print("Drawing filled circle from starting point: ( " + str(x_start) + " | " + str(y_start) + " ) with a radius of '" + str(radius) + "'")
    return [x_start, y_start, radius]

###########################################################################################

def draw_text(x_start:float, y_start:float, text:str):
    """
    Draws a text string at the specified x, y coordinate.
    
    
    Category: TI Draw / Shape
    
    
    Returns an array / list: [x_start, y_start, text]
    """
    try:
        float(x_start)
    except ValueError:
        raise ValueError(errormsg_type("float", "x_start")) from None
    try:
        float(y_start)
    except ValueError:
        raise ValueError(errormsg_type("float", "y_start")) from None
    try:
        str(text)
    except ValueError:
        raise ValueError(errormsg_type("str", "text")) from None
    print("Drawing text '" + text + "' from starting point: ( " + str(x_start) + " | " + str(y_start) + " )")
    return [x_start, y_start, text]

###########################################################################################

def draw_arc(x_start:float, y_start:float, width:float, height:float, start_angle:float, arc_angle:float):
    """
    Description
    
    
    Category: TI Draw / Shape
    
    
    Returns an array / list: [x_start, y_start, width, height, start_angle, arc_angle]
    """
    try:
        float(x_start)
    except ValueError:
        raise ValueError(errormsg_type("float", "x_start")) from None
    try:
        float(y_start)
    except ValueError:
        raise ValueError(errormsg_type("float", "y_start")) from None
    try:
        float(width)
    except ValueError:
        raise ValueError(errormsg_type("float", "width")) from None
    try:
        float(height)
    except ValueError:
        raise ValueError(errormsg_type("float", "height")) from None
    try:
        float(start_angle)
    except ValueError:
        raise ValueError(errormsg_type("float", "start_angle")) from None
    try:
        float(arc_angle)
    except ValueError:
        raise ValueError(errormsg_type("float", "arc_angle")) from None
    print("Drawing arc from starting point: ( " + str(x_start) + " | " + str(y_start) + " ) with start-angle '" + str(start_angle) + " degrees' and arc-angle '" + str(arc_angle) + " degrees' with a hieght of '" + str(height) + "cm' and a width of '" + str(width) + "cm'")
    return [x_start, y_start, width, height, start_angle, arc_angle]