#!/usr/bin/env python3
# Created by: Jonathan Kene
# Created on: May 10 2021
# This program asks the user to guess a number between 0 to 9
# and tells the user if the guess is right or wrong

import constants


def main():

    # this function checks if there is over 30 students

    # get the user's guess
    user_guess = int(input("Enter the number between 0 and 9: "))
    print("")

    # check to see if the user guess is correct or wrong
    if user_guess == constants.CORRECT_GUESS:
        print("You are correct!")

    # check to see if the user guess is correct or wrong
    if user_guess != constants.CORRECT_GUESS:
        print("You are wrong!")


if __name__ == "__main__":
    main()
