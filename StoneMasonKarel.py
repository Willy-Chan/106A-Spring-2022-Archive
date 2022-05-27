from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    for i in range(4):
        fix_stones()
        move_columns()



def turn_right():
    turn_left()
    turn_left()
    turn_left()

def fix_stones():
    turn_left()
    while front_is_clear():
        if beepers_present():
            pick_beeper()
        else:
            move()
    if beepers_present():
        pick_beeper()
    turn_left()
    turn_left()
    while front_is_clear():
        if beepers_present():
            pick_beeper()
        else:
            move()
    turn_left()

def move_columns():
    for i in range(4):
        if front_is_clear():
            move()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
