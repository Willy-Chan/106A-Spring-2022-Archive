from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should leave
a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """
    To place exactly one beeper at the midpoint of the lowest row of the environment.
    If there are an even number of columns in the environment, Karel can place a single beeper
    on either of the two center-most spaces.
    """

    create_boundary()
    place_an_extra_beeper_on_the_midpoint()
    move_to_wall()
    reverse()
    pick_up_every_beeper()


def move_to_wall():
    """
        Karel will move forward until she reaches a wall.
    """
    while front_is_clear():
        safe_move()

def pick_up_every_beeper():
    """
    precondition: Karel is at the rightmost or leftmost point, and is facing west or east respectively.
    postcondition: Karel is at the opposite position to which she started in the same orientation.

    If Karel detects a beeper present, she picks it up and moves forward: checking whether there is a
    beeper on the next block.
    """
    while beepers_present():
        pick_beeper()
        safe_move()

def place_an_extra_beeper_on_the_midpoint():
    """
        precondition: Karel is on the space directly to the left of the midpoint.
        postcondition: Karel is at the midpoint, which now has 2 beepers placed on it.
    """
    reverse()
    safe_move()                 # Fence-post problem: will always initially "overshoot" the
    put_beeper()                # midpoint due to constrict_boundary's safe_move after putting a beeper down.


def create_boundary():
    """
        precondition: Karel is facing east at (1,1).
        postcondition: Karel is on the space directly to the left of the midpoint, having placed
                        beepers on every space on the lowest row.
    """
    while no_beepers_present():
        safe_move()
        if beepers_present():           # This if-statement MUST come first, since
            constrict_boundary()        # the presence of a beeper must overshadow
        if front_is_blocked():          # the presence of a wall.
            set_initial_boundary()


def set_initial_boundary():
    """
        precondition: Karel is at the rightmost column & lowest row facing east.
        postcondition: Karel is at the (empty) space left to the rightmost column & lowest row
    """
    put_beeper()
    reverse()
    safe_move()

def constrict_boundary():
    """
        precondition: Karel is on a space containing a beeper.
        postcondition: Karel is 2 spaces from her initial position, having placed 1 beeper adjacent
                        to her initial position.
    """
    reverse()
    safe_move()
    put_beeper()
    safe_move()



def reverse():
    """
       Karel makes a 180-degree turn in place.
    """
    turn_left()
    turn_left()

def safe_move():
    """
    Karel moves forward if there is no wall in front of her.
    """
    if front_is_clear():
        move()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
