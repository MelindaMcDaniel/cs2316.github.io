---
layout: exercise
title: Dorms Query Exercise in SQLite
---

# Dorms Query Exercise in SQLite

## Introduction

In this exercise you will practice

- executing SQL scripts, and
- writing basic SQL queries.

## Problem Description

You work for the housing department of a major university and want to analyze information in your residency database.

## Solution Description

1. Download [dorms-sqlite.sql](dorms-sqlite.sql)
2. On the command line, go to the directory where you downloaded the dorms database script above.
3. Run the `dorms-sqlite.sql` script like this:

   ```sh
   $ sqlite3 dorms.db < dorms-sqlite.sql
   ```

### Running Queries on the Dorms Database

Use SQLite in interactive mode by starting `sqlite3` with the `dorms.db` database file.

    ```sh
    $ sqlite3 dorms.db
    SQLite version 3.13.0 2016-05-18 10:57:30
    Enter ".help" for usage hints.
    sqlite> .tables
    dorm     student
    ```

Tell SQLite to use headers and columns when displaying table data:

    ```sh
    sqlite> .headers on
    sqlite> .mode column
    ```

### Exploring the Database

Get a list of the tables:

```sql
sqlite> .tables
dorm     student
```

See the structure of a table:

```sql
sqlite> .schema dorm
CREATE TABLE dorm (
    dorm_id int primary key,
    name text,
    spaces integer
);
```

Run a simple query:

```sql
sqlite> select * from dorm;
dorm_id     name        spaces
----------  ----------  ----------
1           Armstrong   124
2           Brown       158
3           Caldwell    158
```

### Simple Queries on Dorms Database

- What are the names of all the dorms?
- Which students have GPAs greater than 3.0?
- Which students are in Armstrong?
- Rank students by GPA.
- Which student has the top GPA?
