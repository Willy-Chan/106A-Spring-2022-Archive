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
    To repair columns that are 4 avenues long, we need to fix an entire column of stones
    and transition columns exactly 4 times.
    """
    for i in range(4):
        fix_column_of_stones()
        move_columns()

def fix_column_of_stones():
    """
    Pre-condition:  Facing East at bottom row of a unfixed column
    Post-condition: Facing East at bottom row of a now-fixed column
    """
    ascend_and_fix_column()
    descend_column()



def ascend_and_fix_column():
    """
        Pre-condition:  Facing East at bottom row of a unfixed column
        Post-condition: Facing North at top row of a now-fixed column
    """
    turn_left()
    beeper_sweep()

def descend_column():
    """
    Pre-condition:  Facing North at top row of a now-fixed column
    Post-condition: Facing East at bottom row of a now-fixed column
    """
    turn_around()
    while front_is_clear():
        move()
    turn_left()


def beeper_sweep():
    """
        Karel will move forward, checking and picking up beepers along her path if they are
        present on the block that she (currently) stands on.
        If there is not a beeper present, she will continue moving forward in a straight path
        based on her orientation, which is assumed to be north in this case.

        Pre-condition:  Facing North at bottom row of a column.
        Post-condition: Facing North at top row of the same column.
    """
    while front_is_clear():
        if beepers_present():
            pick_beeper()
        else:
            move()
    if beepers_present():       # fence-post problem checker: ensures that Karel picks up any beepers
        pick_beeper()           # that are adjacent to a wall (which would break Karel out of her
                                # beeper-checking loop).

def move_columns():
    """
        Pre-condition:  Facing East at bottom row of a column.
        Post-condition: Facing East at bottom row of the column adjacent/to-the-right of
                        Karel's previous column.
    """
    for i in range(4):
        if front_is_clear():
            move()

def turn_right():
    """
    Pre-condition:  none
    Post-condition: Karel rotates 90-degrees counter-clockwise relative to whichever
                    direction Karel was facing previously
    """
    for i in range(3):
        turn_left()

def turn_around():
    """
        Pre-condition: none
        Post-condition: Karel makes a 180-degree turn from her initial position.
    """
    for i in range(2):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
