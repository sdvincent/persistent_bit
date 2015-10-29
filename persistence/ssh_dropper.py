#!/usr/bin/env python


try:
    import sys
    from fabricapi import run, env
except ImportError as error:
    print("[Error] it appears I don't have " + str(error))
    sys.exit()

class SSHDropper:


    '''
        Name: __init__ (constructor)
        Paramaters: hostList, passwordDictionary
            hostList: Python list of username@ipAddress"
                Ex: hosts = [' root@192.168.1.1']

            passwordDictionary: dictionary of username@address : password
                Ex: passwords = {' root@192.168.1.1' : 'changeme'}
                    
        Return: Nothing.
    '''
    def __init__(self, hostList, passwordDictionary):
        self.hosts = hostList
        self.passwords = passwordDictionary

    '''
        Name: listHosts
        Description: Loops through host lists as specified in Init
        Parameters: None
        Return: Prints  list of hosts to ssh into.
    '''
    def listHosts(self):
        for host in self.hosts:
            print("[+] "+ str(host))

    '''
        Name: cmdExecution 
        Description: Commands to run against hosts
        Parameters: cmdToExecute
        Return: output of command executed.
    '''


    def cmdExecute(self, cmdToExecute):
        self.runCmd = cmdToExecute
        run(str(cmdToExecute)) # This will run said command against all hosts 

