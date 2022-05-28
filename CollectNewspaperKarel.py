from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


def main():
    """
    Karel moves to the newspaper, picks it up without changing position or orientation,
    and then proceeds to return to his(/her?) initial position.

    *IMPORTANT NOTE: For sake of consistency, my Karel uses "she/her" pronouns.
    """
    move_to_newspaper()
    pick_up_newspaper()
    return_home()



def move_to_newspaper():
    """
        Karel moves forward until meeting a wall, to which she will make the necessary turns
        to reach her doorway and the beeper that resides near it.
    """
    while front_is_clear():
        move()
    turn_right()
    move()
    turn_left()
    while no_beepers_present():
        move()

def pick_up_newspaper():
    """
        Karel picks up the beeper if there is one on the block she's standing on.
    """
    if beepers_present():
        pick_beeper()

def return_home():
    """
        Karel turns around and moves until reaching a wall. At this point, because we know the layout
        of Karel's house, she turns and moves to her initial position before making one final right
        turn to return to her starting orientation.
    """
    turn_around()
    while front_is_clear():
        move()
    turn_right()
    move()
    turn_right()

def turn_right():
    """
    Pre-condition:  none
    Post-condition: Karel has turned right/90-degrees counter-clockwise
                    relative to her initial orientation.
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
