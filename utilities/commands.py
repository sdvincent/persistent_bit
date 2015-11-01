#!/usr/bin/env python
__author__ = 'Jared'

try:
    import sys 
except ImportError as err:
    print("Error, cannot find package " + str(err))
    sys.exit()


class evalCmd:

    '''
        Function: cmdCheck
        Parameters:self, commandToEvaluate
            self: Required by the class.
            commandToEvaluate: User input that then compares it to available commands and launches
                               additional methods.

        Return: Nothing, prints status of current funcionality, and (TODO) calls other method.
    '''

    def cmdCheck(self, commandToEvaluate):

        if commandToEvaluate == "quit" or commandToEvaluate == "exit":
            sys.exit()

        elif commandToEvaluate == "help":
            print("""
                    help: launch this program.
                    quit: exit the program.
                  """)
        else:
            print("Invalid command. Try typing help")
