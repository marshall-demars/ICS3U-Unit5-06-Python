#!/usr/bin/env python3

# Created by: Marshall Demars
# Created on: Dec 2022
# This program rounds numbers with user input


def decimal_rounding(decimal, user_number):
    # This function rounds numbers

    # process
    answer = user_number[0] * (10**decimal)
    answer = int(answer + 0.5)
    answer = answer / (10**decimal)

    user_number[0] = answer


def main():
    # main function

    # calling functions and inputs
    user_number = []

    number_as_string = input("Enter the number you want to round: ")
    decimal_as_string = input("Enter how many decimal places do you want to round by: ")

    try:
        number_as_int = float(number_as_string)
        decimal_as_int = int(decimal_as_string)

        user_number.append(number_as_int)

        decimal_rounding(decimal_as_int, user_number)

        print("\nThe rounded number is {0}".format(user_number[0]))

    except Exception:
        print("\nInvalid input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
