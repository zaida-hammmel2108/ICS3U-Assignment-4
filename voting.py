#!/usr/bin/env python3

# Created by: Zaida Hammel
# Created on: Nov 2022
# This program determines if you're eligible to vote


def main():
    # this function uses compound boolean statements

    # input
    user_age = input("Enter your age: ")
    print("")

    # process & output
    try:
        user_age = int(user_age)
        if user_age >= 18:
            print("You are eligible to vote in Canada.")
        else:
            print("Sorry, you are not eligible to vote in Canada.")
    except ValueError:
        print("That is not a valid input.")
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
