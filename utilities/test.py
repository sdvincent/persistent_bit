#!/usr/bin/env python
__author__ = 'Scott'

try:
	import sys
	from utilities.logger import logger
	from utilities.colors import TermColors
	from utilities.handler import handler

except ImportError as err:
	print("Error, cannot find package: " + str(err))
	sys.exit()

class Menu:

	log = logger()

	def main(self):
		'''
		Name: menu
		Description: Calls the Main Menu
		Parameters: None
		Returns: Users input as a string
		'''
		evaluate = handler()

		cmd = ""

		try:
		    #Changes color of output
		    print(TermColors.blue)
		    
		    #takes in user input
		    cmd  = raw_input(">> ").rstrip()
		    
		    #Tells the handler where the command is coming from
		    src = "main_menu"

		    #Verify command legit
		    evaluate.command(cmd, src)
		    

		except NameError as cerr:
		    #Something went wrong (does not cause program to quit)
		    log.log("Command not recognized. (" + str(cerr) + ")", "error")
		    print(TermColors.red + "Sorry, I didn't understand " + str(cerr))
		    sys.exit()



