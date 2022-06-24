"""
File: credit_card_total.py
--------------------------
This program totals up a credit card bill based on
how much was spent at each store on the bill.
"""


INPUT_FILE = 'bill2.txt'

def main():
    """
    Add your code (remember to delete the "pass" below)
    """

    credit_statement = {}

    with open(INPUT_FILE, 'r') as file:
        for line in file:

            # Data Parse
            store_name = line[line.find('[') + 1 : line.find(']')]
            charge_value = int(line[line.find('$') + 1::].strip())


            # Checks if store name is already in dict, then adds the new charge
            if store_name in credit_statement:
                credit_statement[store_name] += charge_value
            else:
                credit_statement[store_name] = charge_value

    for key in credit_statement:
        print(key + ": " + '$' + str(credit_statement[key]))




# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
