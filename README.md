# TI-Python-Module

## License

This repository is mainly about two files: `ti_hub.py` and `ti_rover.py`. These files are made by me, as a community member, which means, that TI-Nspire™ and I are both not responsible for any changes, deprecations or invalid content! Do not redistribute these files without my permission!

## How to install this feature / module
How to use these modules properly:
### Accessing the module

1. Download the file `ti_hub.py` and `ti_rover.py`
2. Copy both files into your workspace
3. Create an additional python file
4. Import both files (example shown in `example.py`)

### Putting the program on the calculator / rover

1. Check, if you have used any of the returned values from the methods. Since these are NOT implemented on the TI-CAS itself, these won't work. Just comment them out, so you will be able to use them again, when editing the program later again
2. Save the python file
3. Copy ONLY your python file to the calculator

## Known Problems / Issues

- The functions `digital` and `bb_port` are registered each two times in the calculator. If you enter these via the calculators menu, the software is able to differentiate between both of them. If you enter these commands via the keyboard, the system won't know, whether you are choosing the one from category "Add Output Device" or the one from "Add Input Device". Due to pythons programming, I am unable to add these functions two times with different arguments, processing ... with the same name. Therefore, only the ones from "Add Input Device" are currently registered.

- The module `cmath` dont exists. This is due to a module with the exact same name already exists build in to python. Since I am unable to change build-in classes, I can't add the proper functions. The same issue occurs for `time`. 




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


### What are the functions `errormsg_type` and `errormsg_range`?
These methods are just to simplify the writing of Error messages. They are not actually implemented in the software.

### The function I want to use requires an argument called `self`. What does that mean?
If a function requires an argument called `self`, then it is placed after a class (example, this is wrong btw: `hub.continuous_servo.set_cw(1, 1)`). Then, you have to check, if the class needs an argument aswell 
(example: `hub.continuous_servo("OUT 3").set_cw(1, 1)`). Then, you should no longer need a `self` argument.