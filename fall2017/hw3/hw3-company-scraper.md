---
layout: homework
title: HW3 - Company Scraper
---

# HW3 - Company Scraper

## Introduction

In this exercise you will practice

- web scraping, and
- writing CSV files.

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

You need to process general information about many different companies from many different sectors. The only place you can consitently find this information is on the web.

## Solution Description

Write a module called `company_scraper.py` that scrapes data from SEC.gov's Edgar search engine to extract the name and address of each company in a list of companies contained in a text file, and saves the data in a single CSV file.

- The Edgar search results are in URLs such as `https://www.sec.gov/cgi-bin/browse-edgar?CIK={ticker}`, where `{ticker}` is a company's ticker symbol.
- Use a list of ticker symbols contained in a file such as [tickers.txt](tickers.txt) or [dow-jones.txt](dow-jones.txt)
- Write the company's ticker, name, sector inductrial code (SIC), sector name, address line 1, address line 2, city, state, and zip to a CSV file with a header line like:

  `Ticker,Name,SIC,Sector,Addr1,Addr2,City,State,Zip`

Your program should take the name of the tickers file as the first command line argument and the name for the CSV output file as its second command line argument. For example, if you have a list of tickers in the file named `tickers.txt`, then running your script would look like this:

```sh
$ python company_scraper.py tickers.txt company-data.csv
```

would produce a CSV file with these contents:

```
Ticker,Name,SIC,Sector,Addr1,Addr2,City,State,Zip
AAPL,APPLE INC,3571,ELECTRONIC COMPUTERS,ONE INFINITE LOOP,,CUPERTINO,CA,95014
BAC,BANK OF AMERICA CORP /DE/,6021,NATIONAL COMMERCIAL BANKS,BANK OF AMERICA CORPORATE CENTER,100 N TRYON ST,CHARLOTTE,NC,28255
C,CITIGROUP INC,6021,NATIONAL COMMERCIAL BANKS,388 GREENWICH STREET,,NEW YORK,NY,10013
CSCO,"CISCO SYSTEMS, INC.",3576,COMPUTER COMMUNICATIONS EQUIPMENT,170 WEST TASMAN DR,,SAN JOSE,CA,95134-1706
F,FORD MOTOR CO,3711,MOTOR VEHICLES & PASSENGER CAR BODIES,ONE AMERICAN RD,,DEARBORN,MI,48126
FB,Facebook Inc,7370,"SERVICES-COMPUTER PROGRAMMING, DATA PROCESSING, ETC.",1601 WILLOW ROAD,,MENLO PARK,CA,94025
FCAU,Fiat Chrysler Automobiles N.V.,3711,MOTOR VEHICLES & PASSENGER CAR BODIES,25 ST. JAMES? STREET,,LONDON X0,SW1A,1HA
GM,General Motors Co,3711,MOTOR VEHICLES & PASSENGER CAR BODIES,300 RENAISSANCE CENTER,,DETROIT,MI,48265-3000
GOOG,Alphabet Inc.,7370,"SERVICES-COMPUTER PROGRAMMING, DATA PROCESSING, ETC.",1600 AMPHITHEATRE PARKWAY,,MOUNTAIN VIEW,CA,94043
JPM,JPMORGAN CHASE & CO,6021,NATIONAL COMMERCIAL BANKS,270 PARK AVENUE,,NEW YORK,NY,10017
ORCL,ORACLE CORP,7372,SERVICES-PREPACKAGED SOFTWARE,500 ORACLE PARKWAY,MAIL STOP 5 OP 7,REDWOOD CITY,CA,94065
WFC,WELLS FARGO & COMPANY/MN,6021,NATIONAL COMMERCIAL BANKS,420 MONTGOMERY STREET,,SAN FRANCISCO,CA,94163
```

## Tips and Considerations

- I'm not a finance expert, so if I've misconstrued some aspects of stocks, consider this assignment as practice in following specifications *as written* rather than using your own domain knowledge.
- Use Chrome's Developer Tools or Firefox's Firebug to help you find the HTML elements that contain the data.
- Most of the elements that contain the data have distinct class attribute values, so you can easily extract their text content with [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) (note that BeautifulSoup refers to elements as `tag`s).
- You'll need to use a regular expression to extract the sector name.

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
