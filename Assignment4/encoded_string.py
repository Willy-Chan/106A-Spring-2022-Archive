"""
File: encoded_string.py
-----------------------
This program expands strings encoded with run-length encoding.
"""


def expand_encoded_string(encoded):
    """
    This function is passed a run-length encoded string and
    returns the expanded version of that string.
    >>> expand_encoded_string('B4')
    'BBBB'
    >>> expand_encoded_string('m1e2t1')
    'meet'
    >>> expand_encoded_string('B1o2k2e2p1e1r1!3')
    'Bookkeeper!!!'
    """
    expanded_message = ''
    letters = encoded[::2]
    numbers = encoded[1::2]

    for i in range(len(letters)):
        expanded_message += letters[i] * int(numbers[i])

    return expanded_message

def main():
    result = expand_encoded_string('B4')
    print(result)      # should print: BBBB

    result = expand_encoded_string('m1e2t1')
    print(result)      # should print: meet

    result = expand_encoded_string('B1o2k2e2p1e1r1!3')
    print(result)      # should print: Bookkeeper!!!


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
