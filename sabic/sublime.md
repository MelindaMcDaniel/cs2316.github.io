---
layout: sabic
title: Text Editors
---

# Sublime Text

Visit the [Sublime Text web site](http://www.sublimetext.com/) and download the approprite installer for your computer. For almost everyone these days you'll want a 64-bit version. Sublime Text is not free, but you can use it in evaluation mode whcih simply means that the program will ask you if you'd like to buy a license every *n* saves (I think *n* is 10). If you decide to use Sublime Text I recommend that you buy a license, as I have (even though I use [The One True Editor](http://www.gnu.org/software/emacs/) as my primary editor).


## Customizing Sublime Text

Customizing your text editor will save you time and ensure that your source files are consistently formatted. In some cases customizations will save you hours of frustration. For example, Python uses whitespace for indentation and requires that all whitespace in a file is consistent -- either tabs or spaces but not both. Since they look the same, beginning Python programmers are often frustrated by syntax errors in code that looks correct but contains both tabs and spaces. Setting your text editors to indent with spaces exclusively will save you from this frustration.

### macOS

In Sublime Text's application menu, select the Preferences menu, then click Settings - User. Two editor tabs will open side by side. The left contains the default settings, the right tab contains your cusomizations. The first time you open your settings the custom settings tab will contain a blank JSON dictionary (curly braces). Replace the empty dictionary with the following and save with File -> Save, or Cmd-S.

```sh
{
    "tab_size": 4,
    "translate_tabs_to_spaces": true,
    "rulers": [80],
    "trim_trailing_white_space_on_save": true
}
```

### Linux and Windows

In the main menu, select the Preferences menu, then Settings. Two editor tabs will open side by side. The left contains the default settings, the right tab contains your cusomizations. The first time you open your settings the custom settings tab will contain a blank JSON dictionary (curly braces). Replace the empty dictionary with the following and save with File -> Save or Ctrl-S.

```sh
{
    "tab_size": 4,
    "translate_tabs_to_spaces": true,
    "rulers": [80],
    "trim_trailing_white_space_on_save": true
}
```
