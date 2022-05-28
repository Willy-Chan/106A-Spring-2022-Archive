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
    turn_left()
    if front_is_blocked():
        turn_right()
        ascend_while_staggering()
    else:
        turn_right()
        while front_is_clear():
            turn_left()
            ascend_while_staggering()
            descend_column()
            check_if_beeper()

        if front_is_blocked():
            turn_left()
            ascend_while_staggering()
            descend_column()








# todo: DEFINE ALL THESE HELPER FUNCTIONS
# todo: MAKE MORE HELPER FUNCTIONS FOR REPETITIVE CODE

def check_if_beeper():
    if front_is_clear():
        if beepers_present():       # This checks whether Karel's in an "odd" or "even" -numbered column.
                move()
                turn_left()
                if front_is_clear():
                    move()
                    turn_right()
                else:
                    turn_right()
                    if front_is_clear():
                        move()

        else:
            move()




def descend_column():
    '''
        precondition: facing north at the top of a column

        postcondition: facing east at the bottom of a column
    '''
    turn_around()
    move_to_wall()
    turn_left()         # back to original orientation

def ascend_while_staggering():
    '''
        precondition: facing north at the bottom of a column

        postcondition: facing north at the top of a column
    '''
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()


def check_move():
    if front_is_clear():
        move()



def turn_around():
    for i in range(2):
        turn_left()

def turn_right():
    for i in range(3):
        turn_left()

def move_to_wall():
    while front_is_clear():
        move()





# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
