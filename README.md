# TI-Python-Module

## How to install this feature / module
How to use these modules properly:
### Accessing the module

- Install the package using `pip install ti-python-module`
- Import the modules (examples: `from ti_python_module.ti_hub import *` or `from ti_python_module import ti_rover as rv`)

### Putting the program on the calculator / rover

- Change the import so you don't habe the `ti_python_module` part

## Known Problems / Issues

- The module `cmath` dont exists. This is due to a module with the exact same name already exists build in to python. Since I am unable to change build-in classes, I can't add the proper functions. The same issue occurs for `time`. 

- The module `ti_image` does not exist. This is due to the method `new_image` requiring these parameters: `width, height, (red, green, blue)`. Since Python 3.x sub-list arguments (the part in brackets) are not supported (invalid). Due to the majority of people working with Python 3.x, I have decided *NOT* to implement the module, because if you can't create an image, you can't work with it later on.



If you know a way to solve one of these issues above, just open an issue tracker! Because clearly, I am not a computer, so i don't know everything ;-).


## Recommendated IDEs

As an IDE, I personally recommend you choosing between the following two IDEs depending on your use case.

 - Microsoft Visual Studio Code
   - Faster Use
   - Easier showing of function or class description


 - IntelliJ Idea
   - More Intense and deeper Use
   - Easier coding of complex programms


## FAQ

### I have used the `forward` or `backward` method, but when i copy my file to the calculator it won't work!
Make sure, that if you have specified the speed, that you have also specified the speed unit.


### I have used a method's returned value, but it won't work on my calculator!
The returned values of functions are just for your own use for debugging in your IDE. The methods on the calculator dont actually return anything, which is why you are unable to get the value from them.


### How do I see a functions / class description?
When using IntelliJ Idea, `Ctrl + Click` the statement.
When using Visual Studio Code, You will see a dialogue with autocomplete suggestions. Click the `>` sign to toggle the informations.



### What are the classes `err.py` and `file_handler.py`
These classes are just for simplifying the creation of the functions. 
**DO NOT USE THEM IN YOUR ACTUAL SCRIPT**

### The function I want to use requires an argument called `self`. What does that mean?
If a function requires an argument called `self`, then it is placed after a class (example, this is wrong btw: `hub.continuous_servo.set_cw(1, 1)`). Then, you have to check, if the class needs an argument aswell 
(example: `hub.continuous_servo("OUT 3").set_cw(1, 1)`). Then, you should no longer need a `self` argument.
