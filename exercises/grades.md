---
layout: exercise
title: Grades Module Exercise
---

# Grades Module

## Introduction

In this exercise you will practice

- writing functions,
- using control structures, and
- manipulating data structures.

## Problem Description

You need to process grades given as a list of lists, `list[list[str]]`, where the first list is a header, and subsequent lists have a name followed by grades. For example:

```Python
super_grades = [
    # First line is descriptive header. Subsequent lines hold data
    ['Student', 'Exam 1', 'Exam 2', 'Exam 3'],
    ['Thorny', '100', '90', '80'],
    ['Mac', '88', '99', '111'],
    ['Farva', '45', '56', '67'],
    ['Rabbit', '59', '61', '67'],
    ['Ursula', '73', '79', '83'],
    ['Foster', '89', '97', '101']
]
```

Write a module named `grades` with the following functions:

- `grades_lists(grades)`, which takes a grades list as specified above and creates a `dict[str, list[float]]` mapping names to lists of grades.

- `grades_dicts(grades)`, which takes a grades list as specified above and creates a `dict[str, dict[str, float]]` mapping names to dicitonaries of grades.

# `Averages(grades)`, which takes a `dict[str, list[float]]` mapping names to lists of grades and creates a dict mapping names to grade averages.

# `item_mean(grades, item)`, which takes a `dict[str, dict[str, float]]` and create a `dict[str, float]` mapping items to average for that `item` across all students.

# `rank(grades, item)` which takes a `dict[str, dict[str, float]]` mapping names to dicts of grades and returns a `list[tuple[str, float]]` of (student, grade) pairs sorted in descending order by the grades on `item`.

# Sort the students by their grade averages.

# Which student has the highest average?