"""
File: rating_stats.py
----------------------
This file defines a program that allows a user to calculate
baseline summary statistics about a datafile of professor review
data. 
"""


def calculate_rating_stats(filename):
    """
    This function analyzes the professor review data in the given
    file to calculate the percentage of reviews for both men and
    women that fall in the "high rating" bucket, which is a numerical
    rating that is greater than 3.5.

    The resulting information is printed to the console.
    """
    num_women = 0
    num_women_high = 0

    num_men = 0
    num_men_high = 0

    with open(filename, 'r') as file:
        for line in file:
            data_line = line.split(',')
            sex = data_line[1]
            rating = data_line[0]
            if sex == 'W':
                num_women += 1
                if float(rating) > 3.5:
                    num_women_high += 1

            elif sex == 'M':
                num_men += 1
                if float(rating) > 3.5:
                    num_men_high += 1

    percent_women = round((num_women_high / num_women) * 100)
    percent_men = round((num_men_high / num_men) * 100)

    print(str(percent_men) + '% of reviews for men in the dataset are high')
    print(str(percent_women) + '% of reviews for women in the dataset are high')


def main():
    # Ask the user to input the name of a file
    filename = input("Which data file would you like to load? ")

    # Calculate review distribution statistics by gender for
    # that file. This function should print out the results of
    # the analysis to the console.
    calculate_rating_stats(filename)


if __name__ == '__main__':
    main()
