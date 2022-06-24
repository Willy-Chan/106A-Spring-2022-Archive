"""
File: word_guess.py
-------------------
Fill in this comment.
"""


import random


LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with


def play_game(secret_word):
    """
    Add your code (remember to delete the "pass" below)
    """

    # Initial hidden word (100% hidden)
    hidden_word = ''
    for i in range(len(secret_word)):
        hidden_word += '-'


    # Guesses left starts with the initial number of given guesses
    guesses_left = INITIAL_GUESSES


    # Main game that plays until the number of guesses left == 0
    while guesses_left > 0 and hidden_word != secret_word:
        print_current_conditions(hidden_word, guesses_left)

        player_guess = input('Type a single letter here, then press enter: ')

        if len(player_guess) > 1:
            print('Your guess should only be a single character.')

        elif player_guess.lower() in secret_word.lower():
            guesses_left -= 1
            hidden_word = replace_hidden_letter(hidden_word, secret_word, player_guess)
            print('That guess is correct.')

        else:
            guesses_left -= 1
            print('There are no ' + player_guess.upper() + "'s in this word.")


    if hidden_word == secret_word:
        print('Congrats! The word is: ' + secret_word.upper())
    else:
        print('Sorry, you lost. The secret word was: '+ secret_word.upper())




def print_current_conditions(hidden_word, guesses_left):
    print('The word now looks like this: ' + hidden_word + '\n' + \
          'You have ' + str(guesses_left) + ' guesses left')

def replace_hidden_letter(hidden_word, secret_word, player_guess):
    replaced_word = ''
    replaced_word_list = []

    for char in hidden_word:
        replaced_word_list += char      # turn the string into a list of chars (allows us to use indexing)

    for i in range(len(secret_word)):       # Find every index where player guess is present and replace that element in the list
        if secret_word[i].lower() == player_guess.lower():
            replaced_word_list[i] = player_guess.upper()

    for elem in replaced_word_list:     # Turn the now correct list back into a string
        replaced_word += elem

    return replaced_word


def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """

    """OLD CODE"""
    # index = random.randrange(3)
    # if index == 0:
    #     return 'HAPPY'
    # elif index == 1:
    #     return 'PYTHON'
    # else:
    #     return 'COMPUTER'

    """NEW CODE HERE"""
    words = []
    with open(LEXICON_FILE, 'r') as file:
        for line in file:
            words.append(line)

    selected_word = words[random.randint(1, len(words))]
    return selected_word



def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()