---
layout: sabic-homework
title: Homework 1 - BMI
---

# Homework 1 - `bmi` Module

## Introduction

In this assignment you'll practice

- writing functions and modules,
- manipulating strings,
- converting values to different data types,
- doing arithmetic calculations, and
- testing modules with doctest.

## General Instructions

**This is an individual assignment.**

Collaboration at a reasonable level will not result in substantially similar code. Students may only collaborate with fellow students currently taking Intro to Computing, the TA's and the lecturer. Collaboration means talking through problems, assisting with debugging, explaining a concept, etc. You should not exchange code or write code for others.

Notes:

- Include a comment with your name, T-Square login ID, and GTID at the top of all Python files.
- *Do not wait until the last minute* to do this assignment in case you run into problems.
- Pay close attention to whether problems require you to print or return the results! Printing instead of returning or vice versa will result in a point deduction.
- Name all functions as specified in the instructions.
- Unless otherwise stated, you can assume inputs will be valid in this assignment (i.e. error checking is not required).
- In a Python module you must define a value (such as a function) before referencing it. So if you call function A from function B, the definition of function A must come before the definition of function B in the file.


## Problem Description

You want to live a healthy life and use your computer to help you analyze your fitness and health.

## Solution Description

Create a module that provides convenience functions for converting imperial measures to metric equivalents, a function to calculate BMI, and two functions that tell you whether you are overweight or underweight according to government [BMI standards](https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmicalc.htm). Your module will be named `bmi` and contain the functions listed below.

### `doctest`

The specification for each function is given as a [docstring](https://www.python.org/dev/peps/pep-0257/) -- which you should include in your code -- and the types of arguments and return values are given using type hints documented in [PEP 484 -- Type Hints](https://www.python.org/dev/peps/pep-0484/).

Because each function will have a docstring that includes usage examples formatted as Python interactive sessions, you can use [doctest](https://docs.python.org/3/library/doctest.html) to test your code using this command line invocation:

```sh
python -m doctest -v bmi.py
```

If all the tests pass, then you'll probably (but not defnitely) get a 100 on this homework.

### Required Functions

Implement the following functions in your `bmi.py` file. For convenience you can simply copy the code below.

**IMPORTANT**: Do not modify the provided docstrings!

```Python
def in2m(inches):
    """Convert inches to meters according to convsersion rule 1m == 39.3701in

    Parameters:
    inches: float

    Return:
    float

    Usage examples:
    >>> abs(in2m(39.3701) - 1) < .01
    True
    """

def lb2kg(pounds):
    """Convert pounds to kilograms according to convsersion rule 1kg == 2.2lb

    Parameters:
    pounds: float

    Usage examples:
    >>> abs(lb2kg(2.2) - 1) < .01
    1
    """

def bmi(weight, height):
    """Calculate body mass index (BMI) for given weight and height.

    Paramters:
    weight: float -- weight in kilograms
    height: float -- height in meters

    Return:
    float -- BMI calculated by weight / (height **2)

    Usage examples:
    >>> abs(bmi(66, 1.72) - 22.309) < .01
    True
    """

def is_overwieght(weight, height):
    """Answer whether the given weight and height is considered overweight
    by government standards (BMI > 25).

    Paramters:
    weight: float -- weight in kilograms
    height: float -- height in meters

    Return:
    bool: True if BMI for weight and height is greater than 25, False otherwise

    Usage examples:
    >>> is_overwieght(74, 1.72)
    True
    >>> is_overwieght(73, 1.72)
    False
    """

def is_underweight(weight, height):
    """Answer whether the given weight and height is considered overweight
    by government standards (BMI < 18.5).

    Paramters:
    weight: float -- weight in kilograms
    height: float -- height in meters

    Return:
    bool: True if BMI for weight and height is greater than 25, False otherwise

    Usage examples:
    >>> is_underweight(54, 1.72)
    True
    >>> is_underweight(55, 1.72)
    False
    """
```

### Testing Your Module Interactively

In addition to running the doctests as described above, you can import your `bmi` module in the Python REPL to test your functions as you write and modify them. For example, ssuming you're in the same directory as your `bmi.py` file:

```Python
Python 3.5.2 |Continuum Analytics, Inc.| (default, Jul  2 2016, 17:53:06)
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import bmi
>>> bmi.bmi(bmi.lb2kg(114), bmi.in2m(65))
19.010279100284023
```

After you modify your module you'll need to restart your Python REPL, or reload it using the `importlib` module:

```Python
>>> import importlib as imp
>>> imp.reload(fit)
```

## Grading

- 50 points for having all required functions that can be called with the right parameters but not necessarily returning correct values
- 10 points for each correctly implemented function named exactly as listed above with docstrings as provided (40 points total)
- 10 points for following instructions, e.g., including your name, T-Square ID, and GTID, indenting with four spaces, correctly naming your module and file.

## Turn-in Procedure

Submit your `bmi.py` file on T-Square as an attachment.  When you're ready, double-check that you have submitted and not just saved a draft.

## Verify the Success of Your Submission to T-Square

Practice safe submission! Verify that your HW files were truly submitted correctly, the upload was successful, and that your program runs with no syntax or runtime errors. It is solely your responsibility to turn in your homework and practice this safe submission safeguard.

- After uploading the files to T-Square you should receive an email from T-Square listing the names of the files that were uploaded and received. If you do not get the confirmation email almost immediately, something is wrong with your HW submission and/or your email. Even receiving the email does not guarantee that you turned in exactly what you intended.
- After submitting the files to T-Square, return to the Assignment menu option and this homework. It should show the submitted files.
- Download copies of your submitted files from the T-Square Assignment page placing them in a new folder.
- Re-run and test the files you downloaded from T-Square to make sure it's what you expect.
- This procedure helps guard against a few things.

    - It helps insure that you turn in the correct files.
    - It helps you realize if you omit a file or files.\footnote{Missing files will not be given any credit, and non-compiling homework solutions will receive few to zero points. Also recall that late homework will not be accepted regardless of excuse. Treat the due date with respect.  Do not wait until the last minute!}
(If you do discover that you omitted a file, submit all of your files again, not just the missing one.)
    - Helps find syntax errors or runtime errors that you may have added after you last tested your code.
