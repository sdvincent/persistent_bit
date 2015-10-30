#!/usr/bin/env python
'''
    Author: Jared Stroud
    Purpose: SSH Fabric file for dropping persistence scripts and running them on Linux machines.

'''

def set(args):
    '''
    Name: set
    Description: This function (or method if we end up putting this in a class) will be called when the user calls persistence/ssh then wishes to set settings
    Parameters: It takes a list of arguements that we will sort here
    Returns: Not sure at the moment.
    '''

    #set target
    #Set's the remote host IP
    if args[0] == "target"
        i = 1
        for i in args:
            #This allows adding of multiple hosts
            env.hosts.append(i)

    #set user
    #Specificy user that you will log in as
    if args[0] == "user":
        env.user = args[1]

    #set password
    #Allows user to set the password
    if args[0] == "password":
        env.password = args[1]



def main():
    try:
        import sys
        from fabric.api import *
    except ImportError as err:
        print("[Error] I don't have " + str(err))
        sys.exit()   
    
    
    cmd  = raw_input(">> ").rstrip()
    evaluate.cmdCheck(cmd)
    cmdList = cmd.split(' ')

    if cmdList[0] == "set":
        set()

#Thinking of doing a dict for this as well. Gotta ponder on it a bit more.
def who(): # Executes whoami on remote machine.
    run('whoami')

def uptime(): # Executes uptime on the remote machine
    run('uptime')





'''
# Specify hosts here
env.hosts = [
    "172.16.117.164"
]

#Specify credentials. I believe this can be a list.
env.user = 'root'
env.password = 'Password*'
'''

if __name__ == "__main__":
    main()
