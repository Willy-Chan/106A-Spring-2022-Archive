"""
File: data_analysis.py
----------------------
This program read in data on cumulative infections of a disease
in different locations, and computes the number of infections
per day at each location.
"""


def load_data(filename):
    """
    The function takes in the name of a datafile (string), which
    contains data on locations and their seven day cumulative number
    of infections.  The function returns a dictionary in which the
    keys are the locations in the data file, and the value associated
    with each key is a list of the (integer) values presenting the
    cumulative number of infections at that location.
    >>> load_data('data/disease1.txt')
    {'Evermore': [1, 1, 1, 1, 1, 1, 1], 'Vanguard City': [1, 2, 3, 4, 5, 6, 7], 'Excelsior': [1, 1, 2, 3, 5, 8, 13]}
    """
    data = {}

    list = [1]
    for elem in list:
        elem += 1

    with open(filename, 'r') as file:
        for line in file:
            start = 0
            name_end = line.find(',')
            city_name = line[start:name_end].strip()

            number_list = line[name_end + 1:len(line) + 1].split(',')        #creates a list of unparsed number strings
            for i in range(len(number_list)):
                number_list[i] = int(number_list[i].strip())                #strips list of number strings, then turns it into an int

            data[city_name] = number_list

    return data


def daily_cases(cumulative):
    """
    The function takes in a dictionary of the type produced by the load_data
    function (i.e., keys are locations and values are lists of seven values
    representing cumulative infection numbers).  The function returns a
    dictionary in which the keys are the same locations in the dictionary
    passed in, but the value associated with each key is a list of the
    seven values (integers) presenting the number of new infections each
    day at that location.
    >>> daily_cases({'Test': [1, 2, 3, 4, 4, 4, 4]})
    {'Test': [1, 1, 1, 1, 0, 0, 0]}
    >>> daily_cases({'Evermore': [1, 1, 1, 1, 1, 1, 1], 'Vanguard City': [1, 2, 3, 4, 5, 6, 7], 'Excelsior': [1, 1, 2, 3, 5, 8, 13]})
    {'Evermore': [1, 0, 0, 0, 0, 0, 0], 'Vanguard City': [1, 1, 1, 1, 1, 1, 1], 'Excelsior': [1, 0, 1, 1, 2, 3, 5]}
    """

    delta_cases = {}

    for key in cumulative:
        list = cumulative[key]

        differences = [list[0]]         # Always add the first element of cumulative as the first difference
        for i in range(1, len(list)):                  # keep appending all of the differences: this method DOES NOT MODIFY LIST/CUMULATIVE
            differences.append(list[i] - list[i-1])

        delta_cases[key] = differences



    # delta_cases = cumulative.copy()
    #
    # for key in delta_cases:
    #     for i in range(len(delta_cases[key])):
    #         if i != 0:
    #             x = cumulative[key][i] - cumulative[key][i-1]
    #             delta_cases[key][i] = cumulative[key][i] - cumulative[key][i-1]       ### WHY IS THIS MODIFYING CUMULATIVE?????



    return delta_cases

def main():
    filename = 'data/disease1.txt'

    data = load_data(filename)
    print(f"Loaded datafile {filename}:")
    print(data)

    print("Daily infections: ")
    print(daily_cases(data))


if __name__ == '__main__':
    main()
