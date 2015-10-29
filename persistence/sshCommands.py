#!/usr/bin/env python
'''
    Author: Jared Stroud
    Purpose: SSH Fabric file for dropping persistence scripts and running them on Linux machines.

'''
try:
    import sys
    from fabric.api import *
except ImportError as err:
    print("[Error] I don't have " + str(err))
    sys.exit()


# Specify hosts here
env.hosts = [
    "172.16.117.164"
]

#Specify credentials. I believe this can be a list.
env.user = 'root'
env.password = 'Password*'

def who(): # Executes whoami on remote machine.
    run('whoami')

def uptime(): # Executes uptime on the remote machine
    run('uptime')


if __name__ == "__main__":

    who() # Running test case
    uptime()
