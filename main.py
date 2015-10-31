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
from persistence.modules import Modules

evaluate = evalCmd()
mod = Modules()

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
        #evaluate.cmdCheck(cmd)
        return cmd

    except NameError as cerr:
        #Something went wrong (does not cause program to quit)
        print(TermColors.red + "Sorry, I didn't understand " + str(cerr))
        print(TermColors.blue) # Go back to blue as default terminal color.

def inputHandle(userInput):
    '''
    Name: inputHandle
    Description: Takes in the user input and splits it up to get the arguements.
                 The first arg will be the command (use, help).
                 The following args will be taken as a list. (Ex persistence/ssh)
    Parameters: input - string that contains the users input from the main menu
    Return: Returns a list of arguments
    '''
    cmd = ""

    #Create dictionary
    options = { 'use':use, 'exploit':"Future use" }

    #Split line based on white spaces
    inputList = userInput.split(' ')
   
    #Uncomment when we figure out the part below
    #return inputList
    
    #This part will go somewhere else but for testing just leaving it here
    cmd = inputList.pop(0)
    print("We want to use: " + cmd)
    
    print options[cmd](inputList[0])


def use(str):
    '''
    Name: use
    Description: Contains dict that points the user to the correct module when the 'use' arg is used
    Parameters: Second arg as a string (should this be a list? Will need to be if we allow more than one arg)
    Return: None
    '''
    
    print "in use"
    
    #Split string up until first slash to pull out 
    try:
        index = str.index('/')
        package = str[0:index]
        print("package: " + package)
        modVar = str[index+1:]
        print("module: " + modVar)

    except:
        print "Module not found. Type 'help' for more information."
        main()
    
    #Dict for the possible modules we will have
    packages = { 'persistence':module }

    print packages[package](modVar)

def module(str):
    '''
    Name: module
    Description: Calls module (ie ssh)
    Parameters: The module 
    Return: None
    '''
    print "in module"

    #Spliting for now incase we want to go deeper in the future. For now we only go as deep as package/module (persistence/ssh)
    try:
        index = str.index('/')
        module = str[0:index]
        print("package: " + package)
        #As of right now, nothing goes 3 deep but future use idk
        future = str[index+1:]
        print("Future thing: " + future)

    except ValueError:
        #Comes in here if no slash is found meaning this is the module
        module = str
    except:
        print "Module not found. Type 'help' for more information."
        main()
    
    #Declare dictionary with all modules
    modules = { 'ssh':ssh }

    #Call module from dict
    modules[module]()


def ssh():
    mod.ssh()
    print "here"


def main():
    '''
    Main Function
    '''
    while True: 
        userInput = menu()
        inputHandle(userInput)
        if userInput == "exit" or userInput == "quit":
            print(TermColors.blue + "Goodbye World")
            exit()
    
if __name__ == "__main__":
    main()

   
