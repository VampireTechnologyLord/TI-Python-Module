# TI-Python-Module

> [Texas Instruments](https://education.ti.com/en/products/calculators/graphing-calculators/ti-nspire-cx-ii-cx-ii-cas/programming-in-python) Python Debugging and Programming Support

##### Installation:

```shell
# Installation:
pip install ti-python-module
# Update:
pip install ti-python-module --upgrade
```

## How to install this feature / module

How to use these modules properly:

#### Accessing the module

-   Install the package using `pip install ti-python-module`
-   Import the modules (examples: `from ti_python_module.ti_hub import *` or `from ti_python_module import ti_rover as rv`)

#### Putting the program on the calculator / rover

-   Change the import so you don't have the `ti_python_module` part

## Known Problems / Issues

-   The module `cmath` don't exists. This is due to a module with the exact same name already exists build in to python. Since I am unable to change build-in classes, I can't add the proper functions. The same issue occurs for `time`.

-   The module `ti_image` does not exist. This is due to the method `new_image` requiring these parameters: `width, height, (red, green, blue)`. Since Python 3.x sub-list arguments (the part in brackets) are not supported (invalid). Due to the majority of people working with Python 3.x, I have decided _NOT_ to implement the module, because if you can't create an image, you can't work with it later on.

## Recommended IDEs

As an IDE, I personally recommend you choosing between the following two IDEs depending on your use case.

-   Microsoft Visual Studio Code

    -   Faster Use
    -   Easier showing of function or class description

-   IntelliJ Idea
    -   More Intense and deeper Use
    -   Easier coding of complex programs

## FAQ

### Why don't the `forward` or `backward` method work?

Make sure, that if you have specified the speed, that you have also specified the speed unit.
There are three usecases of the functions, like listed below. It is not possible to set the speed parameter, but not the speed unit.

```py
from ti_python_module import ti_rover as rv  # import

# RIGHT USE
# forward
rv.forward(1)
rv.forward(1, "m")
rv.forward(1, "m", 1, "m/s")
#backward
rv.backward(1)
rv.backward(1, "m")
rv.backward(1, "m", 1, "m/s")

# WRONG USE
# forward
# rv.forward(1, "m", 1)
# backward
# rv.backward(1, "m", 1)
```

### What are the return values of a function?

As you might have guessed, the functions do not actually measure any values, but they rather return calculated or random values.

### How do I see a functions / class description?

When using IntelliJ Idea, `Ctrl + Click` the statement.
When using Visual Studio Code, You will see a dialogue with autocomplete suggestions. Click the `>` sign to toggle the information.

### What are the classes `err.py` and `file_handler.py`

These classes are just for simplifying the creation of the functions.
**DO NOT USE THEM IN YOUR ACTUAL SCRIPT**

### The function I want to use requires an argument called `self`. What does that mean?

If a function requires an argument called `self`, then it is placed after a class. Some classes need an argument, whilst some just need the brackets `()`

```python
from ti_python_module.ti_hub import continuous_servo, hub_time
continuous_servo.set_cw(1, 1)               # WRONG
continuous_servo("OUT 3").set_cw(1, 1)      # RIGHT

hub_time.measurement()                      # WRONG
hub_time().measurement()                    # RIGHT
```
