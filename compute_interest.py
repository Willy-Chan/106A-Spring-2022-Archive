"""
File: compute_interest.py
-------------------------
Add your comments here.
"""

initial_balance = float(input("Initial Balance: "))
start_year = int(input("Start Year: "))
start_month = int(input("Start Month: "))
end_year = int(input("End Year: "))
end_month = int(input("End Month: "))

monthly_time_frame = (end_year - start_year) * 12 + (end_month - start_month)






def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    validate_time()

    interest_rate = float(input("Interest Rate (0 to quit): "))
    if interest_rate <= 0.0:
        quit()

    current_balance = initial_balance
    current_year = start_year
    current_month = start_month

    for i in range(monthly_time_frame + 1):
        print("Year " + str(current_year) + ", month " + str(current_month) + " balance: " + str(current_balance))

        current_balance *= (1 + interest_rate)

        current_month += 1
        if current_month > 12:
            current_year += 1
            current_month = 1







def validate_time():
    if start_year > end_year:
        print("Starting date needs to be before the ending date.")
    elif start_year == end_year and start_month > end_month:
        print("Starting date needs to be before the ending date.")



# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
