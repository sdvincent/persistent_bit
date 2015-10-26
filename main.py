#!/usr/bin/env python

class TermColors:

        red = "\033[91m" 
        blue = "\033[94m"
        green = "\033[92m"

if __name__ == "__main__":

    print(TermColors.blue + "Goodbye World")
    while True:
        try:
            x = input(">> ")
        except NameError as cerr:
            print(TermColors.red + "Sorry, I didn't understand " + str(cerr))
            print(TermColors.blue) # Go back to blue as default terminal color.
