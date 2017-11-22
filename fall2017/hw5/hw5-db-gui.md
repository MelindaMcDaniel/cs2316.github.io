---
layout: homework
title: HW5 - Company Database GUI
---

# HW5 - Company Database GUI

## Introduction

In this exercise you will practice:

- writing GUI applications with PyQt, and
- writing Python code to interact with an SQL database.

## General Instructions

**This is an individual assignment.**

Collaboration at a reasonable level will not result in substantially similar code. Students may only collaborate with fellow students currently taking CS 2316, the TA's and the professor. Collaboration means talking through problems, assisting with debugging, explaining a concept, etc. You should not exchange code or write code for others.

Notes:

- Include a comment with your name, T-Square login ID, and GTID at the top of all Python files.
- *Do not wait until the last minute* to do this assignment in case you run into problems.
- Pay close attention to whether problems require you to print or return the results! Printing instead of returning or vice versa will result in a point deduction.
- Name all modules, classes methods, and functions as specified in the instructions.
- Unless otherwise stated, you can assume inputs will be valid in this assignment (i.e. error checking is not required).
- In a Python module you must define a value (such as a function) before referencing it. So if you call function A from function B, the definition of function A must come before the definition of function B in the file.

## Problem Description

You need to share your company database with users who don't know SQL.

## Solution Description

Create a GUI application in a Python source file named `company_gui.py` that displays the table data in the company database you created in the previous homework.

### Main Screen

Your application may assume that there is an SQLite3 database stored in a file named `company.db` in the same directory as your `company_gui.py` program. When the user runs `company_gui.py` the program should display a main screen (25 points). The main screen should show three buttons labeled:

- (25 points) "Companies" which, when clicked, displays a dialog box that displays a table with the contents of the `company` table,

- (25 points) "Sectors" which, when clicked, displays a dialog box that displays a table with the contents of the `sector` table, and

- (25 points) "Stock Prices" which, when clicked, displays a dialog box that displays a table with the contents of the `stock_price` table.

Each dialog box should have a button labled "Ok" which, when clicked, returns the user to the main screen.

You may be reading this and thinking, "this is too easy; it can't be all there is!" You're right, it is easy. And it's all you need for a 100.

### Extra Credit

You may do any number of these you wish. You'll need to join tables for most of these.

- (10 points) Instead of a button for Companies, have a drop-down list with all the company names and a button next to it labeled "Show". The "Show" button should be disabled if there is no company selected in the drop-down list. When the "Show" button is clicked, show a dialog box displaying the company information in the format of a form, e.g.:

  ```
   Company name: Apple, Inc.
  Ticker Symbol: AAPL
         Sector: ELECTRONIC COMPUTERS (3571)
        Address: ONE INFINITE LOOP,CUPERTINO,CA,95014
  ```



- (10 points) On the dialog above showing a company profile, have a list (with scroll bars, of course) showing all the stock proces for that company in the database.

- (10 points) On the dialog above showing a company profile, allow the user to edit the company information and have the user's changes reflected in the database. In addition to an "Ok" button, this dialog should have a "Cancel" button that discards the user's changes.

- (10 points) In addition to the "Show" button for companies, have a "New..." button. When the "New..." button is clicked, display a dialog that allows the user to create a new company to add to the database. This dialog should include a drop-down menu for the sector with sector names from the database. In addition to an "Ok" button, this dialog should have a "Cancel" button that discards the user's changes.

- (10 points) Instead of a button for Sectors, have a drop-down list with all the sector names and a button next to it labeled "Show". The "Show" button should be disabled if there is no sector selected in the drop-down list. When the "Show" button is clicked, show a dialog box displaying a list of all the companies -- names and ticker symbols -- that are in that sector.

## Tips and Considerations

- Example code is your friend: [https://github.com/cs2316/cs2316.github.io/tree/master/code/gui](https://github.com/cs2316/cs2316.github.io/tree/master/code/gui)
- There's an example of a dialog box in this (incomplete) MySql example: [https://github.com/cs2316/cs2316.github.io/blob/master/code/gui/mysql_browser.py](https://github.com/cs2316/cs2316.github.io/blob/master/code/gui/mysql_browser.py)

## Turn-in Procedure

Submit your `company_gui.py` file on T-Square as an attachment.  When you're ready, double-check that you have submitted and not just saved a draft.

## Verify the Success of Your Submission to T-Square

Practice safe submission! Verify that your HW files were truly submitted correctly, the upload was successful, and that your program runs with no syntax or runtime errors. It is solely your responsibility to turn in your homework and practice this safe submission safeguard.

- After uploading the files to T-Square you should receive an email from T-Square listing the names of the files that were uploaded and received. If you do not get the confirmation email almost immediately, something is wrong with your HW submission and/or your email. Even receiving the email does not guarantee that you turned in exactly what you intended.
- After submitting the files to T-Square, return to the Assignment menu option and this homework. It should show the submitted files.
- Download copies of your submitted files from the T-Square Assignment page placing them in a new folder.
- Re-run and test the files you downloaded from T-Square to make sure it's what you expect.
- This procedure helps guard against a few things.

    - It helps insure that you turn in the correct files.
    - It helps you realize if you omit a file or files. Missing files will not be given any credit, and non-compiling homework solutions will receive few to zero points. Also recall that late homework will not be accepted regardless of excuse. Treat the due date with respect.  Do not wait until the last minute!
(If you do discover that you omitted a file, submit all of your files again, not just the missing one.)
    - Helps find syntax errors or runtime errors that you may have added after you last tested your code.
