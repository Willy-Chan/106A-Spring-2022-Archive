"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """

    mastery_threshold = 3
    num_correct = 0

    while num_correct <= (mastery_threshold - 1):
        num_1 = random.randint(10, 99)
        num_2 = random.randint(10, 99)
        print("What is " + str(num_1) + " + " + str(num_2) + " ?")

        key = num_1 + num_2
        user_answer = int(input("Your answer: "))

        if key != user_answer:
            num_correct = 0  # EQUALITY OPERATOR
            print("Incorrect. The expected answer is " + str(key) + ".")

        elif key == user_answer:
            num_correct += 1
            print("Correct! You've gotten " + str(num_correct) + " correct in a row.")

    if num_correct >= (mastery_threshold - 1):
        print("Congratulations! You mastered addition.")




# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
