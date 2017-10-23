---
layout: homework
title: HW4 - Company Database
---

# HW4 - Company Database

## Introduction

In this exercise you will practice

- creating dtabases,
- reading CSV files,
- writing data to relational databases, and
- writing SQL queries.

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

You need to answer questions about many different companies from many different sectors and these questions are awkward to answer using CSV files and Python code.

## Solution Description

Create a database to hold company data, write a Python script that reads CSV files containing various company data and inserts that data into a database, and write SQL queries that answer various questions about the data in your database.

### Part 1: Create Company Database

Write a database creation script named `company-schema.sql` with `create table` statements that create a database with the following tables:

- `company` with fields `ticker`, `name`, `sic`, `addr1`, `addr2`, `city`, `state`, and `zip`.
  - `ticker` should be the primary key.
  - `sic` should be a foreign key referencing the `sector` table.

- `sector` with fields `sic`, `name`.
  - `sic` should be the primary key.
  - `name` comes from the `Sector` field in the source CSV file.

- `stock_price` with fields `ticker`, `date`, `open`, `high`, `low`, `close`, `adj_close`, `volume`
  - (`ticker`, `date`) should be the (composite) primary key.

To develop and test your work on the remainder of this assignment you should run your `company-schema.sql` script to create an SQLite database stored in a file such as `company.db`.

### Part 2: Import CSV Data in to Company Database

Write a python script called `import_companies.py` that reads a CSV company data file such as the one you created in HW3 and stock price CSV files named after each company's ticker symbol -- such as the ones you used in HW2 -- and inserts the data from those files into a database created with the database creation script you wrote in Part 1.

Your script should take as its first command line argument the name of a CSV file containing compnay infomation with the following header line (from HW3):

  `Ticker,Name,SIC,Sector,Addr1,Addr2,City,State,Zip`

and the second command line argument to your script should be the name of an SQLite database file created from the database creation script you wrote in Part 1. For each record in the CSV file your script should:

- Insert the approriate information from the record into the `company` and `sector` tables of the database.
  - Note that many companies will have the same sector. There should be only one sector record for each sector in the `sector` table.

- Open the CSV file named for the company's ticker symbol. For each record in the stock data CSV file, insert an appropriate record in the `stock_price` table of the database.

Sample program run:

```sh
$ python import_companies.py company-data.csv company.db
```

### Part 3: Query Company Database

Write a file named `company-queries.sql` with SQL queries that answer the following questions:

- Which company has the highest stock price as of 1 September, 2017?
- Which company or companies have had the highest volume of trading during 2016?
- How may companies in the database are in each sector?
- What is the average stock price of companies in each sector as of 1 September, 2017?

## Tips and Considerations

- I'm not a finance expert, so if I've misconstrued some aspects of stocks, consider this assignment as practice in following specifications *as written* rather than using your own domain knowledge.

## Turn-in Procedure

Submit your `company_scraper.py` file on T-Square as an attachment.  When you're ready, double-check that you have submitted and not just saved a draft.

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
