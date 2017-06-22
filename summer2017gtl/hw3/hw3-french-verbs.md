---
layout: homework
title: Homework 3 - French Verbs
---

# Homework 3 - French Verbs

## Introduction

In this homework you will practice processing CSV, XML, and JSON data.

## General Instructions

**This is an individual assignment.**

Collaboration at a reasonable level will not result in substantially similar code. Students may only collaborate with fellow students currently taking Intro to Computing, the TA's and the lecturer. Collaboration means talking through problems, assisting with debugging, explaining a concept, etc. You should not exchange code or write code for others.

Notes:

- Include a comment with your name and GTID at the top of all Python files.
- *Do not wait until the last minute* to do this assignment in case you run into problems.
- Pay close attention to whether problems require you to print or return the results! Printing instead of returning or vice versa will result in a point deduction.
- Name all functions as specified in the instructions.
- Unless otherwise stated, you can assume inputs will be valid in this assignment (i.e. error checking is not required).
- In a Python module you must define a value (such as a function) before referencing it. So if you call function A from function B, the definition of function A must come before the definition of function B in the file.

## Problem Descrtiption

You are creating a web service that will provide data on french verbs -- given a french verb you will provide its senses with sample sentences and its conjugations. Your source data are partly in XML and partly in CSV files, but you want to provide data to clients in JSON format, as is common in web services. [dubois.xml](dubois.xml) is an XML file containing senses and sample sentences (among many other things) and [conjugations-0-2-0.csv](conjugations-0-2-0.csv) is a CSV file containing conjugations for some, but not all of the verbs in dubois.xml.

Sources:
- [Les verbes français](http://rali.iro.umontreal.ca/rali/?q=en/node/1238)
- [French Verb Conjugation Rules](https://sourceforge.net/projects/fvcr/)

## Solution Description

As a first step you decide to write a Python program to consolidate your XML and CSV data and produce JSON data that will be provided by your french verb service.

1. Write a module named `french_verb` with a function called `info` that takes a string argument containing the infinitive form of a verb and returns a JSON string with the following structure:

```
{"verbe": infinitive,
 "sens": { sense1: [sentence1-1, sentence1-2, ..., sentence1-N],
           sense2: [sentence2-1, sentence2-2, ..., sentence2-N],
           ...
           senseM: [sentenceM-1, sentenceM-2, ..., sentenceM-N]},
 "conjugaisons":
   {"Présent": ["je ...", "tu ...", "il ...", "nous ...", "vous ...", "ils ..."],
   "Passé Composé": ["je ...", "tu ...", "il ...", "nous ...", "vous ...", "ils ..."],
   "Imparfait": ["je ...", "tu ...", "il ...", "nous ...", "vous ...", "ils ..."],
   "Plus-que-parfait": ["je ...", "tu ...", "il ...", "nous ...", "vous ...", "ils ..."],
   "Futur": ["je ...", "tu ...", "il ...", "nous ...", "vous ...", "ils ..."],
   "Futur Antérieur": ["je ...", "tu ...", "il ...", "nous ...", "vous ...", "ils ..."],
   "Conditionnel Présent": ["je ...", "tu ...", "il ...", "nous ...", "vous ...", "ils ..."],
   "Conditionnel Passé": ["je ...", "tu ...", "il ...", "nous ...", "vous ...", "ils ..."],
   "Subjonctif Présent": ["je ...", "tu ...", "il ...", "nous ...", "vous ...", "ils ..."],
   "Subjonctif Passé": ["je ...", "tu ...", "il ...", "nous ...", "vous ...", "ils ..."],
   "Subjonctif Imparfait": ["je ...", "tu ...", "il ...", "nous ...", "vous ...", "ils ..."],
   "Subjonctif Plus-que-parfait": ["je ...", "tu ...", "il ...", "nous ...", "vous ...", "ils ..."],
   "Passé simple": ["je ...", "tu ...", "il ...", "nous ...", "vous ...", "ils ..."],
   "Passé Antérieur": ["je ...", "tu ...", "il ...", "nous ...", "vous ...", "ils ..."],
   "Impératif Présent": ["je ...", "tu ...", "il ...", "nous ...", "vous ...", "ils ..."],
   "Infinitif Présent": ["je ...", "tu ...", "il ...", "nous ...", "vous ...", "ils ..."],
   "Participe Présent": ["je ...", "tu ...", "il ...", "nous ...", "vous ...", "ils ..."],
   "Participe Passé": ["je ...", "tu ...", "il ...", "nous ...", "vous ...", "ils ..."],
```

2. Make your `french_verb` module executable so that when run from the command line the first command line argument to the script is the verb for which to get info, whcih is then printed to the console.

Your `french_verb` module may assume that the two source data files are located in the same directory as the module.


### Sample Output



```sh
$ python french_verb.py avoir
{"verbe": "avoir", "sens": {"posséder": ["On a~ une grande propriété dans le midi, de l'argent."], "accompli": ["On a~ mangé."], "devoir +infinitive": ["On a~ à travailler."], "se trouver": ["Il y a~ des gens dans la cour, des pommes au four."], "duper, baiser, posséder": ["On a~ ce naïf.", "On a été a~."], "obtenir de": ["On a~ de P un ordinateur."], "avoir comme raisons": ["On a~ que P est malade, que sa femme est partie."]}, "conjugaisons": {"Présent": ["j'ai", "tu as", "il a", "nous avons", "vous avez", "ils ont"], "Passé": ["j'eus eu", "tu eus eu", "il eut eu", "nous eûmes eu", "vous eûtes eu", "ils eurent eu"], "Imparfait": ["j'avais", "tu avais", "il avait", "nous avions", "vous aviez", "ils avaient"], "Plus-que-parfait": ["j'avais eu", "tu avais eu", "il avait eu", "nous avions eu", "vous aviez eu", "ils avaient eu"], "Futur": ["j'aurai eu", "tu auras eu", "il aura eu", "nous aurons eu", "vous aurez eu", "ils auront eu"], "Conditionnel": ["j'aurais eu", "tu aurais eu", "il aurait eu", "nous aurions eu", "vous auriez eu", "ils auraient eu"], "Subjonctif": ["que j'eusse eu", "que tu eusses eu", "qu'il eût eu", "que nous eussions eu", "que vous eussiez eu", "qu'ils eussent eu"], "Impératif": ["", "tu aie", "", "nous ayons", "vous ayez", ""], "Infinitif": ["j'avoir", "tu avoir", "il avoir", "nous avoir", "vous avoir", "ils avoir"], "Participe": ["j'eu", "tu eu", "il eu", "nous eu", "vous eu", "ils eu"]}}
$ python french_verb.py être
{"verbe": "être", "sens": {"copule": ["On e~ pauvre, stupide, en retard, absent."], "verbe auxiliaire passif, intransitif, pronominal": ["On a e~ blessé.", "On s'e~ absenté.", "On e~ venu à Paris."], "devoir être": ["On e~ sans cesse à taquiner P.", "Ceci e~ à faire pour demain."], "aller": ["On a déjà e~ à Paris."], "exister": ["Le monde e~ et cela suffit."]}, "conjugaisons": {"Présent": ["je suis", "tu es", "il est", "nous sommes", "vous êtes", "ils sont"], "Passé": ["j'eus été", "tu eus été", "il eut été", "nous eûmes été", "vous eûtes été", "ils eurent été"], "Imparfait": ["j'étais", "tu étais", "il était", "nous étions", "vous étiez", "ils étaient"], "Plus-que-parfait": ["j'avais été", "tu avais été", "il avait été", "nous avions été", "vous aviez été", "ils avaient été"], "Futur": ["j'aurai été", "tu auras été", "il aura été", "nous aurons été", "vous aurez été", "ils auront été"], "Conditionnel": ["j'aurais été", "tu aurais été", "il aurait été", "nous aurions été", "vous auriez été", "ils auraient été"], "Subjonctif": ["que j'eusse été", "que tu eusses été", "qu'il eût été", "que nous eussions été", "que vous eussiez été", "qu'ils eussent été"], "Impératif": ["", "tu sois", "", "nous soyons", "vous soyez", ""], "Infinitif": ["j'être", "tu être", "il être", "nous être", "vous être", "ils être"], "Participe": ["j'été", "tu été", "il été", "nous été", "vous été", "ils été"]}}
$ python french_verb.py abaisser
{"verbe": "abaisser", "sens": {"baisser": ["On a~ les prix, les revenus de dix pour cent.", "Les prix s'a~ de beaucoup."], "incliner, pencher": ["On a~ la manette, le levier.", "La manette s'a~ vers le bas."], "faire descendre": ["Le malade a~ la fièvre avec l'aspirine.", "La fièvre s'a~."], "avilir, humilier": ["On a~ P, son orgueil en le blâmant.", "On s'a~ en public."], "s'humilier à": ["On s'a~ à demander une faveur, à cette demande."], "descendre vers": ["La route s'a~ vers la rivière."], "s'avilir, tomber jusqu'à": ["On s'a~ au niveau de cet escroc."]}, "conjugaisons": {}}
```

Notice that some verbs don't have conjugations in the conjugations file. For verbs without conjugations it's fine to return an empty `dict`, as in the example above for abaisser.

## Submission Instructions

Attach your `verb-consolidator.py` file to your T-Square HW2 assignment submission.

## Verify Your T-Square Submission!

Practice safe submission! Verify that your HW files were truly submitted correctly, the upload was successful, and that your program runs with no syntax or runtime errors. It is solely your responsibility to turn in your homework and practice this safe submission safeguard.

- After uploading the files to T-Square you should receive an email from T-Square listing the names of the files that were uploaded and received. If you do not get the confirmation email almost immediately, something is wrong with your HW submission and/or your email. Even receiving the email does not guarantee that you turned in exactly what you intended.
- After submitting the files to T-Square, return to the Assignment menu option and this homework. It should show the submitted files.
- Download copies of your submitted files from the T-Square Assignment page placing them in a new folder.
- Re-run and test the files you downloaded from T-Square to make sure it's what you expect.
- This procedure helps guard against a few things.

    - It helps insure that you turn in the correct files.
    - It helps you realize if you omit a file or files. Missing files will not be given any credit, and non-compiling homework solutions will receive few to zero points. Also recall that late homework will not be accepted regardless of excuse. Treat the due date with respect.  Do not wait until the last minute! (If you do discover that you omitted a file, submit all of your files again, not just the missing one.)
    - Helps find syntax errors or runtime errors that you may have added after you last tested your code.
