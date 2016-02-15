#!/usr/bin/env python
__author__ = 'Scott'

try:
	import sys
	import logging, logging.handlers
	from datetime import datetime

except ImportError as err:
	print "1"
	print("Error, cannot find package " + str(err))
	sys.exit()

class logger:

	def timeStamp(self):
		'''
	    Function: timeStamp 
	    Purpose: Used for logging method in order to associate a time stamp with command.
	    Parameters: self
	    Return: time stamp in format year month date hour month second
		  	'''
		FORMAT = "%Y-%m-%d (%H:%M:%S)"
		return datetime.now().strftime(FORMAT)

	def log(self, thingToLog, level):
		'''
		Function: logging
		Purpose: Useful for documentation purpose.
		Parameters: self, thingToLog
		    thingToLog: Value being logged to a file. Could be a command or anything else.
		Return: Nothing            
		'''
		logging.basicConfig(filename='pbit.log', level=logging.DEBUG)
		command = str(self.timeStamp()) + ": " + str(thingToLog)
		if level == "info":
			logging.info(command)
		elif level == "debug":
			logging.debug(command, exc_info=True)
		elif level == "warn":
			logging.warning(command, exc_info=True)
		elif level == "error":
			logging.error(command, exc_info=True)