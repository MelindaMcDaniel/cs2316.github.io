---
layout: exercise
title: Company Scraper
---

# C

## Introduction

In this exercise you will practice

- web scraping, and
- writing CSV files.


## Problem Description

You need to process general information about many different companies from many different sectors. The only place you can consitently find this information is on the web.

## Solution Description

Write a module called `company_data.py` that scrapes data from SEC.gov's Edgar search engine to extract the name and address of each company in a list of companies contained in a text file, and saves the data in a single CSV file.

- The Edgar search results are in URLs such as `https://www.sec.gov/cgi-bin/browse-edgar?CIK={ticker}`, where `{ticker}` is a company's ticker symbol.
- Use a list of ticker symbols contained in a file such as [tickers.txt](tickers.txt)
- Write the comapny's name, sector, address line 1, address line 2, city, state, and zip to a CSV file with a header line like:

  `Name,Addr1,Addr2,City,State,Zip`

Your program should take the name of the tickers file as the first command line argument and the name for the CSV output file as its second command line argument. For example, if you have a list of tickers in the file named `tickers.txt`, then running your script would look like this:

```sh
$ python company_data.py tickers.txt company-data.csv
$ cat company-data.csv
Name,Addr1,Addr2,City,State,Zip
APPLE INC,ONE INFINITE LOOP,,CUPERTINO,CA,95014
BANK OF AMERICA CORP /DE/,BANK OF AMERICA CORPORATE CENTER,100 N TRYON ST,CHARLOTTE,NC,28255
CITIGROUP INC,388 GREENWICH STREET,,NEW YORK,NY,10013
"CISCO SYSTEMS, INC.",170 WEST TASMAN DR,,SAN JOSE,CA,95134-1706
FORD MOTOR CO,ONE AMERICAN RD,,DEARBORN,MI,48126
Facebook Inc,1601 WILLOW ROAD,,MENLO PARK,CA,94025
Fiat Chrysler Automobiles N.V.,25 ST. JAMES? STREET,,LONDON X0,SW1A,1HA
General Motors Co,300 RENAISSANCE CENTER,,DETROIT,MI,48265-3000
Alphabet Inc.,1600 AMPHITHEATRE PARKWAY,,MOUNTAIN VIEW,CA,94043
JPMORGAN CHASE & CO,270 PARK AVENUE,,NEW YORK,NY,10017
ORACLE CORP,500 ORACLE PARKWAY,MAIL STOP 5 OP 7,REDWOOD CITY,CA,94065
WELLS FARGO & COMPANY/MN,420 MONTGOMERY STREET,,SAN FRANCISCO,CA,94163
```

## Tips and Considerations

- I'm not a finance expert, so if I've misconstrued some aspects of stocks, consider this assignment as practice in following specifications *as written* rather than using your own domain knowledge.
- You'll want to use [Python's datetime module](https://docs.python.org/3/library/datetime.html), in particular you'll find [datetime.strptime](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime) useful.

## Turn-in Procedure

Submit your Python module source file on T-Square as an attachment.  When you're ready, double-check that you have submitted and not just saved a draft.

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
