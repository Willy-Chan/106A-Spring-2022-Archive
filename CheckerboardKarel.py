from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    """
    Karel is facing East and must create a checkerboard pattern in her environment with beepers, starting with
    one beeper on her initial position. She begins the simulation with an empty environment facing east, on the
    1st avenue and 1st street.

    Karel first checks if her environment is 1-block tall, in which case she knows to move forward while staggering
    beepers (placing one, and then moving 2 spaces to place another) until reaching a wall. If it is not, she ascends
    a column while staggering beepers before descending the column and checking if there is a beeper on the lowest
    position. Depending on whether there is a beeper on the lowest row, Karel knows whether there should be a beeper
    horizontally adjacent to it, and either skips or places a beeper on the lowest row of the next column depending on
    the presence of a beeper on the lowest row of her current column. This process repeats until she reaches the
    rightmost wall, to which she simply ascends the final column while staggering beepers along the way.
    """
    turn_left()                         # Karel repositions to check if the environment is more than one block tall.
    if front_is_blocked():              # This if-statement checks if the environment is 1-block tall.
        turn_right()                    # In such a scenario, it's much more efficient to turn East
        straight_stagger()              # and horizontally-stagger beepers rather than checking each individual column.
    else:
        turn_right()
        while front_is_clear():         # As long as there are clear spaces when Karel's facing East,
            turn_left()                 # she knows to turn left (facing North)
            straight_stagger()          # ascend while vertically-staggering beepers
            descend_column()            # descend the column
            check_if_beeper()           # check if there is a beeper at the bottom of a column, which
                                        # indicates whether this is an "odd" or "even" column. This way,
                                        # Karel can reset her position so that this while loop continuously
                                        # Generates a checkerboard pattern.

        if front_is_blocked():         # This if-statement effectively checks if Karel is in the last/final column.
            turn_left()                # If this is the case, she knows to simply turn left (facing North) and
            straight_stagger()         # vertically stagger beepers.
            descend_column()





def check_if_beeper():
    '''
            precondition: facing East at the bottom of a column.
            postcondition: facing East at the lowest or second-lowest row of an adjacent column.

            If a beeper is present, Karel knows to move in an "L-shape" to intentionally
            'skip' past a space on the next column of the lowest row. This way, she can tell
            whether she's in an odd or even-numbered row, and knows to skip the bottom beeper
            for an even-numbered row, while not skipping for an odd-numbered row.
    '''

    if front_is_clear():
        if beepers_present():           # This checks whether Karel's in an "odd" or "even"-numbered column
                move()                  # depending on the presence of a beeper.
                turn_left()
                move()
                turn_right()            # At the end of this sequence, Karel is facing East whilst
                                        # having/skipping an empty space that's directly below her
                                        # (even-numbered column)
        else:
            move()                      # If there is no beeper present, Karel can simply
                                        # transition columns and continue.



def descend_column():
    '''
        precondition: facing North at the top of a column
        postcondition: facing East at the bottom of a column

        Assuming Karel is facing upwards at the top of a column, she will reverse
        direction and descend that same column, before returning to her default orientation (East).
    '''
    turn_around()           # Changes her orientation from North to South
    move_to_wall()
    turn_left()             # From South to original orientation (East)

def straight_stagger():
    '''
        precondition: facing North at the bottom of a column
        postcondition: facing North at the top of a column

        Karel will move forward while placing beepers in a staggered pattern, starting
        with the space she is on initially.
    '''
    put_beeper()                    # Will always place a beeper on her current block.
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()

def turn_around():
    """
            Pre-condition: none
            Post-condition: Karel makes a 180-degree turn from her initial position.
    """
    for i in range(2):
        turn_left()

def turn_right():
    """
        Pre-condition:  none
        Post-condition: Karel rotates 90-degrees counter-clockwise relative to whichever
                        direction Karel was facing previously
    """
    for i in range(3):
        turn_left()

def move_to_wall():
    """
        Karel will move forward until she reaches a wall.
    """
    while front_is_clear():
        move()





# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
