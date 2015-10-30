#!/usr/bin/env python

__authors__ = "Jared E. Stroud aka The Doc"

'''
The MIT License (MIT)

Copyright (c) 2015 sdvincent

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

from utilities.colors import TermColors
from utilities.commands import evalCmd

evaluate = evalCmd()

def menu():
    '''
    Name: menu
    Description: Calls the Main Menu
    Parameters: None
    Returns: Users input as a string
    '''
    cmd = ""

    try:
        #Changes color of output
        print(TermColors.blue)
        
        #takes in user input
        cmd  = raw_input(">> ").rstrip()
        
        #Verify command legit
        evaluate.cmdCheck(cmd)
        return cmd

    except NameError as cerr:
        #Something went wrong (does not cause program to quit)
        print(TermColors.red + "Sorry, I didn't understand " + str(cerr))
        print(TermColors.blue) # Go back to blue as default terminal color.

def inputHandle(input):
    '''
    Name: inputHandle
    Description: Takes in the user input and splits it up to get the arguements.
                 The first arg will be the command (use, help).
                 The following args will be taken as a list. (Ex persistence/ssh)
    Parameters: input - string that contains the users input from the main menu
    Return: Returns a list of arguments
    '''

    #Split line based on white spaces
    inputList = input.split(' ')
    
    #Uncomment when we figure out the part below
    #return inputList
    
    #This part will go somewhere else but for testing just leaving it here
    cmd = inputList.pop(0)
    print("We want to use: " + cmd)

    #Instead of using IFs and ELIFs we should use dicts. (This is what pythong typically uses instead of switch statements
    if cmd == "use": #Would call the a use module (will build next)
        #This would go in the use module
        module = inputList.pop(0)

        if module == "persistence/ssh":
            #call the ssh shit
            print "call this"


def main():
    '''
    Main Function
    '''
    while True: 
        input  = menu()
        inputHandle(input)
        if input == "exit" or input == "quit":
            print(TermColors.blue + "Goodbye World")
            exit()
    
if __name__ == "__main__":
    main()

   
