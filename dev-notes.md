# Developer's notes
Anything I want to comment on without a long block at the top of the file goes here. List by folder and file.

## uncategorized

### backend
I should have a backend, but I really didn't think this through and sunk-cost goes harder than me falling when I finally decide to end it all.

This uses [beserk-downstream](https://github.com/dignissimus/berserk-downstream) as the actual API interface. Once I get around to rewriting
in C or C++, I'll probably use some other library. Unfortunately, I don't want to learn C and I'm too lazy to rewrite this tiny bit of code,
so that's not happening anytime soon.

## utils
Used to allow portability with the logging functions. That's about it.

## views
These are shared `GtkObject`s used in multiple places.

## windows
Anything that acts as a window goes here.

### development
Two windows in one file! Has a main debugging window with just a list of windows, a view tester, and some internal function tests.

### view_popout
A generic window that acts as a container for a view. It's used to allow for chat popouts, board popouts, etc.