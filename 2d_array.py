#!/usr/bin/env python3

# Created by: Cameron Carter
# Created on June 2021
# This program finds the average of a 2d array

import random


def find_average(the_list, amount_of_rows, amount_of_columns):
    # This function determines the average

    # total
    total = 0

    # Loop through "array" to find average
    for row_counter in the_list:
        for column_counter in row_counter:
            total += column_counter
    average = total / (amount_of_rows * amount_of_columns)

    return average


def main():
    # This function generates random numbers

    # List declaration
    two_dimensional_list = []

    # Input
    rows_as_string = str(input("How many rows do you want? "))
    columns_as_string = str(input("How many columns do you want? "))

    # Process and output
    try:
        rows = int(rows_as_string)
        columns = int(columns_as_string)
        for loop_counter in range(0, rows):
            temp = []
            for loop_counter in range(0, columns):
                generated_number = random.randint(1, 50)
                temp.append(generated_number)
                print("{0} ".format(generated_number), end="")
            two_dimensional_list.append(temp)
            print("")
            # Call find_average
        average = find_average(two_dimensional_list, rows, columns)
        print("\nThe average is {}.".format(average))
        print("\nDone.")
    except Exception:
        print("Invalid input")


if __name__ == "__main__":
    main()
