---
layout: homework
title: Homework 1
---

# Homework 1

## Introduction

In this assignment you'll practice

- writing functions and modules,
- doing arithmetic calculations,
- simple text processing,
- manipulating data structures and
- testing modules with doctest.

## General Instructions

**This is an individual assignment.**

Collaboration at a reasonable level will not result in substantially similar code. Students may only collaborate with fellow students currently taking CS 2316, the TA's and the lecturer. Collaboration means talking through problems, assisting with debugging, explaining a concept, etc. You should not exchange code or write code for others.

Notes:

- Include a comment with your name, T-Square login ID, and GTID at the top of all Python files.
- *Do not wait until the last minute* to do this assignment in case you run into problems.
- Pay close attention to whether problems require you to print or return the results! Printing instead of returning or vice versa will result in a point deduction.
- Name all functions as specified in the instructions.
- Unless otherwise stated, you can assume inputs will be valid in this assignment (i.e. error checking is not required).
- In a Python module you must define a value (such as a function) before referencing it. So if you call function A from function B, the definition of function A must come before the definition of function B in the file.


## Problem Description

You need to do some text processing and decide to write a few utility functions to get started.

## Solution Description

Write a module named `hw1` with the functions specified below.

### `doctest`

The specification for each function is given as a [docstring](https://www.python.org/dev/peps/pep-0257/) -- which you should include in your code -- and the types of arguments and return values are given using type hints documented in [PEP 484 -- Type Hints](https://www.python.org/dev/peps/pep-0484/).

Because each function will have a docstring that includes usage examples formatted as Python interactive sessions, you can use [doctest](https://docs.python.org/3/library/doctest.html) to test your code using this command line invocation:

```sh
python -m doctest -v fit.py
```

If all the tests pass, then you'll probably (but not defnitely) get a 100 on this homework.

### Required Functions

**IMPORTANT**: Do not modify the provided docstrings!


```Python
def long_words(text, n):
    """Return the words in text that are longer than n.

    Parameters:
    text: str -- the text of interest

    Return: Sequence[int] -- words in text that are longer than n

    Usage Examples:
    >>> long_words('I do not write good', 3)
    ['write', 'good']
    """

def num_long_words(text, n):
    """Return the number of words in text that are longer than n.

    Parameters:
    text: str -- the text of interest

    Return: int -- the number of words in text that are longer than n

    Usage Examples:
    >>> num_long_words('I do not write good', 3)
    2
    """

def count_if(sequence, predicate):
    """Count the number of elements in sequence that satisfy predicate function.

    Parameters:
    sequence: Sequence -- a sequence of elements of any type
    predicate: Function: Any -> bool -- a function that takes a single parameter and returns a
    bool

    Usage Examples:
    >>> count_if([0, 1, 2, 3, 4], lambda x: x % 2 == 0)
    3
    >>> count_if(['fe', 'fi', 'fo', 'fum'], lambda s: len(s) > 2)
    1
    """

def palindrome(text):
    """Tests whether a string is a palindrome, ignoring case, puntuation,
    and spaces.

    Parameters:
    text: str -- the text of interest

    Return: True if sequence of letters in text is a palindrome, false otherwise

    Usage Examples:
    >>> palindrome('Borrow or rob')
    True
    >>> palindrome('This is a palindrome')
    False
    """

def make_tups(seq1, seq2):
    """Convert seq1 and seq2 to a list of tuples with corresponding elements of
    seq1 and seq2.

    Parameters:
    seq1: Sequence[Any] -- a sequence of elements of any type
    seq2: Sequence[Any] -- a sequence of elements of any type

    Return: Sequence[(Any, Any)] - a sequence of 2-tuples where the ith tuples
    contain the ith elements of seq1 and seq2. Length of returned list is
    length of shortest input seq

    Usage Examples:
    >>> make_tups(['a', 'b', 'c', 'd'], [1, 2, 3])
    [('a', 1), ('b', 2), ('c', 3)]
    """
```

### Testing Your Module Interactively

In addition to running the doctests as described above, you can import your `hw1` module in the Python REPL to test your functions as you write and modify them. For example, ssuming you're in the same directory as your `hw1.py` file:

```Python
Python 3.6.1 |Continuum Analytics, Inc.| (default, Jul  2 2016, 17:53:06)
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import hw1
>>> hw1.palindrome("a but tuba")
True
```

After you modify your module you'll need to restart your Python REPL, or reload it using the `importlib` module:

```Python
>>> import importlib as imp
>>> imp.reload(hw1)
```

## Grading

- 50 points for having all required functions that can be called with the right parameters l returning values of the correct type but not necessarily correct values
- 10 points for each correctly implemented function named exactly as listed above with docstrings as provided (40 points total)
- 10 points for following instructions, e.g., including your name, T-Square and GTID, indenting with four spaces, correctly naming your module and file

## Turn-in Procedure

Submit your `hw1.py` file on T-Square as an attachment.  When you're ready, double-check that you have submitted and not just saved a draft.

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
