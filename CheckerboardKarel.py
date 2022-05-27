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
    todo: Delete this comment and replace it with a better, more descriptive one.
    """

    turn_left()                 # Orients Karel so she can check whether the first column is more than 1-block tall

    while front_is_clear():     # If it is, she starts to ascend: staggering beepers along the way
        stagger()
        turn_right()                # After detecting a wall, she stops and prepares to switch rows.

        if beepers_present():       # This checks whether Karel's in an "odd" or "even" -numbered column.
                                    # If a beeper is present, there must be an odd number of rows.

            if front_is_blocked():  # This checks whether there's more than 1 column.
                turn_left()         # Turning left returns it to blocked position, and breaks the loop
            else:
                move()
                turn_right()        # If there's more than 1 column, it moves to the second column
                move()              # and begins staggering beepers.

                stagger()           # Because this is an "odd" row scenario,
                                    # Karel must make an extra move() before staggering beepers to achieve
                                    # a checkerboard pattern.

                turn_left()         # Karel is on the lowest row, so she must make a "U-Turn" onto the
                check_move()        # next column: orienting herself so she's in the exact same position as where
                turn_left()         # she started. todo:(DEFINE WHAT CHECK-MOVE IS AND HOW IT WORKS!)

        else:                       # If beeper isn't present at the top, there are an even number of rows
            if front_is_blocked():  # Again, this ends the loop if there's only one column
                turn_left()
            else:
                move()              # Exact same code as the odd-column, except it's has one
                turn_right()        # less move() command because there is no need for it.

                stagger()

                turn_left()
                check_move()            # U-Turn
                turn_left()


    if right_is_clear():     # The following bits of code are activated if Karel is blocked in her starting position.
        turn_right()         # This indicates that there is only one row.
        stagger()            # In this case, because the right is clear, Karel knows to stagger horizontally.

    if right_is_blocked():              # Here, Karel checks if she is surrounded on all sides.
        if left_is_blocked():           # If she is, she places a beeper and the run is finished.
            if front_is_blocked():
                turn_left()
                turn_left()
                if front_is_blocked():
                    put_beeper()



# todo: DEFINE ALL THESE HELPER FUNCTIONS
# todo: MAKE MORE HELPER FUNCTIONS FOR REPETITIVE CODE

def stagger():
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()


def check_move():
    if front_is_clear():
        move()
    else:
        # turn_right()
        if left_is_clear():     #at the bottom
            turn_right()


def turn_right():
    turn_left()
    turn_left()
    turn_left()





# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
