---
layout: default
title: Text Editors
---

# Sublime Text

Visit the [Sublime Text web site](http://www.sublimetext.com/) and download the approprite installer for your computer. For almost everyone these days you'll want a 64-bit version. Sublime Text is not free, but you can use it in evaluation mode whcih simply means that the program will ask you if you'd like to buy a license every *n* saves (I think *n* is 10). If you decide to use Sublime Text I recommend that you buy a license, as I have (even though I use [The One True Editor](http://www.gnu.org/software/emacs/) as my primary editor).


## Customizing Sublime Text

### macOS

In Sublime Text's application menu, select the Preferences menu, then click Settings - User. An editor tabe will open with a blank JSON dictionary (curly braces). Replace the empy dictionary with the following and save with File -> Save, or Ctrl-S (Cmd-S on OS X).

```sh
{
    "tab_size": 4,
    "translate_tabs_to_spaces": true,
    "rulers": [80],
    "trim_trailing_white_space_on_save": true
}
```

### Linux and Windows

In Sublime Text's application menu, select the Preferences menu, then click Settings - User. An editor tabe will open with a blank JSON dictionary (curly braces). Replace the empy dictionary with the following and save with File -> Save, or Ctrl-S (Cmd-S on OS X).

```sh
{
    "tab_size": 4,
    "translate_tabs_to_spaces": true,
    "rulers": [80],
    "trim_trailing_white_space_on_save": true
}
```
