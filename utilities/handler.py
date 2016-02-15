#!/usr/bin/env python
__author__ = 'Scott'

try:
	import sys
	import os
	from utilities.logger import logger
	from utilities.colors import TermColors
	from utilities.test import Menu
	from persistence.ssh import ssh as s

except ImportError as err:
	print "2"
	print("Error, cannot find package " + str(err))
	sys.exit()

log = logger()
print menu()

exit()

class handler:

	def command(self, cmd, src):
		'''
		Name: inputHandle
		Description: Takes in the user input from the menu and splits it up to get the arguements.
			The first arg will be the command (use, help, etc.).
			The following args will be taken as a list. (Ex persistence/ssh)
		Parameters: input - string that contains the users input from the main menu
		Return: Returns a list of arguments
		'''
		#Create dictionary
		options = { 'exit':self.quit, 'use':self.use, 'exploit':"Future use" }
		print cmd
		#Split line based on white spaces
		inputList = cmd.split(' ')

		#Uncomment when we figure out the part below
		#return inputList

		#This part will go somewhere else but for testing just leaving it here

		
		try:
			cmd = inputList.pop(0)
			options[cmd](inputList, src)
		except Exception as err:
			print( TermColors.red + "[Error] " + str(err) + " does not exist.")
			log.log("Command not recognized. (" + str(err) + ")", "warn")

		else:
			log.log(str(options[cmd](inputList, src)), "info")


	def use(self, path, src):

		jumpTo = path[0]
		curPath = os.getcwd()
		jumpTo = curPath + "/" + jumpTo + ".py"
		
		#Because ssh is a class, I have to create an object before I can call
		#any methods in its class. I need to find a better way to do this or
		#else I will have to call every class when I don't have to
		ssh = s()

		#A dictionary of all of the current modules
		modules = {'persistence/ssh':ssh.ssh_menu
			}
		
		evaluate = handler()
		if os.path.isfile(jumpTo) is True:
			log.log("Calling " + path[0] + ".py", "info")
			modules[path[0]](evaluate)
		else:
			print( TermColors.red + "[Error] " + path[0] + " does not exist.")
			log.log(path[0] + ".py" + " does not exist", "warn")
			exit()


	def quit(self, path, src):


		if src == 'main_menu':
			log.log("Session ending.", "info")
			print(TermColors.blue + "Goodbye World")
			sys.exit()
			
		if src == 'ssh':
			print "Main Menu"
			mainMenu.main()
		

			print "In quit."
			print  src
			exit()










