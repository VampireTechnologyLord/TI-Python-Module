# TI-Python-Module

## Info

This repository is mainly about two files: `ti_hub.py` and `ti_rover.py`. These files are made by me, as a community member, which means, that TI-Nspire™ and I are both not responsible for any changes, deprecations or invalid content!

## How to use this

Using this feature is very simple. You just download both files into your workspace. Then you just have to import both files like shown in `example.py`. Then, you can just start writing code. Please note, that many functions return an array / a list or values. You can use these for internal debugging purposes, but they will NOT work, when you copy your file to the Calculator itself, since these are just from the moduels and not integrated in the actual function itself.

## Known Problems / Issues

- The functions `digital` and `bb_port` are registered each two times in the calculator. If you enter these via the calculators menu, the software is able to differentiate between both of them. If you enter these commands via the keyboard, the system won't know, whether you are choosing the one from category "Add Output Device" or the one from "Add Input Device". Due to pythons programming, I am unable to add these functions two times with different arguments, processing ... with the same name. Therefore, only the ones from "Add Inout Device" are currently registered.

## Recommendated IDEs

As an IDE, I personally recommend you choosing between the following two IDEs depending on your use case.
 - Faster Use:
    - Microsoft Visual Studio Code

 - More Intense and deeper Use
    - IntelliJ Idea