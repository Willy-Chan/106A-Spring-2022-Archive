"""
File: searchengine.py
---------------------
You fill in this comment
"""


import os
import sys
import string


def create_index(filenames, index, file_titles):
    """
    This function is passed:
        filenames:      a list of file names (strings)

        index:          a dictionary mapping from terms to file names (i.e., inverted index)
                        (term -> list of file names that contain that term)

        file_titles:    a dictionary mapping from a file names to the title of the article
                        in a given file
                        (file name -> title of article in that file)

    The function will update the index passed in to include the terms in the files
    in the list filenames.  Also, the file_titles dictionary will be updated to
    include files in the list of filenames.

    >>> index = {}
    >>> file_titles = {}
    >>> create_index(['test1.txt'], index, file_titles)
    >>> index
    {'file': ['test1.txt'], '1': ['test1.txt'], 'title': ['test1.txt'], 'apple': ['test1.txt'], 'ball': ['test1.txt'], 'carrot': ['test1.txt']}
    >>> file_titles
    {'test1.txt': 'File 1 Title'}
    >>> index = {}
    >>> file_titles = {}
    >>> create_index(['test2.txt'], index, file_titles)
    >>> index
    {'file': ['test2.txt'], '2': ['test2.txt'], 'title': ['test2.txt'], 'ball': ['test2.txt'], 'carrot': ['test2.txt'], 'dog': ['test2.txt']}
    >>> file_titles
    {'test2.txt': 'File 2 Title'}
    >>> index = {}
    >>> file_titles = {}
    >>> create_index(['test1.txt', 'test2.txt'], index, file_titles)
    >>> index
    {'file': ['test1.txt', 'test2.txt'], '1': ['test1.txt'], 'title': ['test1.txt', 'test2.txt'], 'apple': ['test1.txt'], 'ball': ['test1.txt', 'test2.txt'], 'carrot': ['test1.txt', 'test2.txt'], '2': ['test2.txt'], 'dog': ['test2.txt']}
    >>> index = {}
    >>> file_titles = {}
    >>> create_index(['test1.txt', 'test2.txt', 'test2.txt'], index, file_titles)
    >>> index
    {'file': ['test1.txt', 'test2.txt'], '1': ['test1.txt'], 'title': ['test1.txt', 'test2.txt'], 'apple': ['test1.txt'], 'ball': ['test1.txt', 'test2.txt'], 'carrot': ['test1.txt', 'test2.txt'], '2': ['test2.txt'], 'dog': ['test2.txt']}
    >>> file_titles
    {'test1.txt': 'File 1 Title', 'test2.txt': 'File 2 Title'}
    >>> index = {'file': ['test1.txt'], '1': ['test1.txt'], 'title': ['test1.txt'], 'apple': ['test1.txt'], 'ball': ['test1.txt'], 'carrot': ['test1.txt']}
    >>> file_titles = {'test1.txt': 'File 1 Title'}
    >>> create_index([], index, file_titles)
    >>> index
    {'file': ['test1.txt'], '1': ['test1.txt'], 'title': ['test1.txt'], 'apple': ['test1.txt'], 'ball': ['test1.txt'], 'carrot': ['test1.txt']}
    >>> file_titles
    {'test1.txt': 'File 1 Title'}
    """

    # Create file title list
    for filename in filenames:
        with open(filename, 'r') as file:
            first_line = next(file).strip().strip(string.punctuation)       #next() returns one line from the file in order, so this will give the first line

            if filename not in file_titles.keys():          # if filename title not already included, add it in!
                file_titles[filename] = first_line


    # Create Index
    for filename in filenames:      # Loop through each file

        word_list = []    # Set an empty word list to append terms into

        with open(filename, 'r') as file:           # Open the file

            for line in file:

                # Parse all the words in each file into a list

                data_list = line.split()                    # Parses the line by putting ALL words into a list
                for i in range(len(data_list)):
                    data_list[i] = data_list[i].strip(string.punctuation)  # Strips punctuation from every word in the list

                for elem in data_list:              # Append all elems from data_list into bigger word_list
                    if elem not in word_list:       # Checks to make sure duplicates are not appended
                        word_list.append(elem.lower())

        # Assign the list (value) to each word (key)
        for word in word_list:
            if word not in index.keys():    # If key isn't in the dict yet, assign the new key:value pair
                index[word] = [filename]
            else:
                if filename not in index[word]: # Check for duplicate filenames in the list! index[word] gives you the list of the relevant filenames, make sure that it doesn't repeat
                    index[word] += [filename]   # If key IS in the dict, EXTEND the list



def search(index, query):
    """
    This function is passed:
        index:      a dictionary mapping from terms to file names (inverted index)
                    (term -> list of file names that contain that term)

        query  :    a query (string), where any letters will be lowercase. you can just assume for the basic version of the program that the user will not enter any punctuation characters in their query.

    The function returns a list of the names of all the files that contain *all* of the
    terms in the query (using the index passed in).

    >>> index = {}
    >>> create_index(['test1.txt', 'test2.txt'], index, {})
    >>> search(index, 'apple')
    ['test1.txt']
    >>> search(index, 'ball')
    ['test1.txt', 'test2.txt']
    >>> search(index, 'file')
    ['test1.txt', 'test2.txt']
    >>> search(index, '2')
    ['test2.txt']
    >>> search(index, 'carrot')
    ['test1.txt', 'test2.txt']
    >>> search(index, 'dog')
    ['test2.txt']
    >>> search(index, 'nope')
    []
    >>> search(index, 'apple carrot')
    ['test1.txt']
    >>> search(index, 'apple ball file')
    ['test1.txt']
    >>> search(index, 'apple ball nope')
    []
    """

    relevant_files = []     # List of the names of the files that contain all of the terms in the given query.

    # Process and parse every word in the query
    words = query.split()       # words = list containing all of the relevant words in the query
    for i in range(len(words)):
        words[i].strip().strip(string.punctuation) # Split and Strip the query (remove spaces and punctuation)


    # Append the name of every file that contains *ALL* the words in the relevant_files list

    for word in words:   # Loop through each word being searched
        # If a searched word is not the index, there will be no relevant files
        if word not in index:
            relevant_files = []     # the relevant files list MUST be empty if a word is not in the index
            break                   # regardless of the other words

        # Append all the files relevant to the first word to the relevant_files list.
        # Future words will be compared to this initially created list, which constantly updates and
        # filters out files that do not contain every word searched.
        elif word in index and relevant_files == []:

            # Append every filename in the index list corresponding to the searched word to relevant_files
            for elem in index[word]:
                relevant_files.append(elem)

        # Compare the relevant_files to the index list containing the 2nd/3rd/... word
        elif word in index:

            # Comparing the filename lists in relevant_files and index[word], remove any NON-duplicate elements

            for filename in relevant_files:     # !!! - Use for-each loop here to avoid indexing errors
                if filename not in index[word]:
                    relevant_files.remove(filename) # .remove(value) takes in a value argument, and since we
                                                    # guaranteed no filename duplicates, it will always remove the
                                                    # correct filename from the list.


    return relevant_files




##### YOU SHOULD NOT NEED TO MODIFY ANY CODE BELOW THIS LINE (UNLESS YOU'RE ADDING EXTENSIONS) #####


def do_searches(index, file_titles):
    """
    This function is given an inverted index and a dictionary mapping from
    file names to the titles of articles in those files.  It allows the user
    to run searches against the data in that index.
    """
    while True:
        query = input("Query (empty query to stop): ")
        query = query.lower()                   # convert query to lowercase
        if query == '':
            break
        results = search(index, query)

        # display query results
        print("Results for query '" + query + "':")
        if results:                             # check for non-empty results list
            for i in range(len(results)):
                title = file_titles[results[i]]
                print(str(i + 1) + ".  Title: " + title + ",  File: " + results[i])
        else:
            print("No results match that query.")


def textfiles_in_dir(directory):
    """
    DO NOT MODIFY
    Given the name of a valid directory, returns a list of the .txt
    file names within it.

    Input:
        directory (string): name of directory
    Returns:
        list of (string) names of .txt files in directory
    """
    filenames = []

    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filenames.append(os.path.join(directory, filename))

    return filenames


def main():
    """
    Usage: searchengine.py <file directory> -s
    The first argument specified should be the directory of text files that
    will be indexed/searched.  If the parameter -s is provided, then the
    user can interactively search (using the index).  Otherwise (if -s is
    not included), the index and the dictionary mapping file names to article
    titles are just printed on the console.
    """
    # Get command line arguments
    args = sys.argv[1:]

    num_args = len(args)
    if num_args < 1 or num_args > 2:
        print('Please specify directory of files to index as first argument.')
        print('Add -s to also search (otherwise, index and file titles will just be printed).')
    else:
        # args[0] should be the folder containing all the files to index/search.
        directory = args[0]
        if os.path.exists(directory):
            # Build index from files in the given directory
            files = textfiles_in_dir(directory)
            index = {}          # index is empty to start
            file_titles = {}    # mapping of file names to article titles is empty to start
            create_index(files, index, file_titles)

            # Either allow the user to search using the index, or just print the index
            if num_args == 2 and args[1] == '-s':
                do_searches(index, file_titles)
            else:
                print('Index:')
                print(index)
                print('File names -> document titles:')
                print(file_titles)
        else:
            print('Directory "' + directory + '" does not exist.')


if __name__ == '__main__':
    main()
