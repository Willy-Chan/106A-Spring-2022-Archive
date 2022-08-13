"""
File: common_elements.py
------------------------
File to implement a function that is passed two lists and returns a new list
containing those elements that appear in both of the lists passed in.

ERRORS ENCOUNTERED
- .pop() takes in an INDEX, while .remove() removes the first ELEM with the specified value
- NEVER ITERATE OVER SOMETHING THAT IS ACTIVELY BEING MODIFIED

    EXAMPLE OF BAD CODE:
        for elem in list:
            list.remove(elem)  <---- ASKING for errors! the value corresponding to the current 'elem' or 'index' has now CHANGED!

"""


def common(list1, list2):
    """
    This function is passed two lists and returns a new list containing
    those elements that appear in both of the lists passed in.
    >>> common(['a'], ['a'])
    ['a']
    >>> common(['a', 'b', 'c'], ['x', 'a', 'z', 'c'])
    ['a', 'c']
    >>> common(['a', 'a', 'b'], ['a', 'a', 'x'])
    ['a']
    >>> common(['a', 'b', 'c'], ['x', 'y', 'z'])
    []
    """
    common_list = []

    for elem in list1:
        if elem not in common_list:     # This "if-not in" line prevents duplicates from appearing in common_list
            common_list.append(elem)    # Appends every element from list 1 into the common list

    for elem in list1:            # Now we check elems in the common_list against elems in list 2
        if elem not in list2:
            common_list.remove(elem)    # Delete any elements that are not in common with list 2

    return common_list





def main():
    print(common(['a'], ['a']))                             # should print ['a']
    print(common(['a', 'b', 'c'], ['x', 'a', 'z', 'c']))    # should print ['a', 'c']
    print(common(['a', 'b', 'c'], ['x', 'y', 'z']))         # should print []
    print(common(['a', 'a', 'b'], ['a', 'a', 'x']))         # should print ['a']


if __name__ == '__main__':
    main()
