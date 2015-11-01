#!/usr/bin/env python
__author__ = 'Jared'

try:
    import sys 
    from datetime import datetime
    import logging
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

        self.logging(commandToEvaluate)
        if commandToEvaluate == "quit" or commandToEvaluate == "exit":
            sys.exit()

        elif commandToEvaluate == "help":
            print("""
                    help: launch this program.
                    quit: exit the program.
                  """)
        else:
            print("Invalid command. Try typing help")



    '''
        Function: timeStamp 
        Purpose: Used for logging method in order to associate a time stamp with command.
        Parameters: self
        Return: time stamp in format year month date hour month second
    '''
    def timeStamp(self):
        FORMAT = "%Y%m%d%H%M%S"
        return datetime.now().strftime(FORMAT)

    '''
        Function: logging
        Purpose: Useful for documentation purpose.
        Parameters: self, thingToLog
            thingToLog: Value being logged to a file. Could be a command or anything else.
        Return: Nothing            
    '''
    def logging(self, thingToLog):
        logging.basicConfig(filename='pbit.log', level=logging.DEBUG)
        command = str(self.timeStamp()) + " : " + str(thingToLog)
        logging.info(command)
