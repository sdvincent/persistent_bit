#!/usr/bin/env python
'''
    Author: Jared Stroud, Scott Vincent
    Purpose: Stores modules that will be used for persistence
    #Purpose: SSH Fabric file for dropping persistence scripts and running them on Linux machines.

'''

class Modules:

    def set(self, args):
        '''
        Name: set
        Description: This function (or method if we end up putting this in a class) will be called when the user calls persistence/ssh then wishes to set settings
        Parameters: It takes a list of arguements that we will sort here
        Returns: Not sure at the moment.
        '''

        #set target
        #Set's the remote host IP
        if args[0] == "target":
            i = 1
            for i in args:
                #This allows adding of multiple hosts
                env.hosts.append(i)
                print("Target has been set to: " + env.hosts[i])

        #set user
        #Specificy user that you will log in as
        if args[0] == "user":
            env.user = args[1]
            print("User set to: " + env.user)

        #set password
        #Allows user to set the password
        if args[0] == "password":
            env.password = args[1]
            print("Password set to: " + env.password)

    def who(self):
        run('whoami')

    def uptime(self): # Executes uptime on the remote machine
        run('uptime')


    def sshCommands(self, cmd):
        commands = { 
                'set':set,
                'who':who,
                'uptime':uptime,
                'exit':exit
                }
                     
        #Run the command
        commands[cmd]
        ssh("f")

    def test(self):
        print "hope this works"

    def ssh(self,f):
        '''
        I don't know how this is going to work yet but we will see
        For some reason, I don't pass any args when I call it 
        '''
        print "Using SSH for persistence. For help type 'help.'"

        self.test()
        exit()
        cmd  = raw_input(">> ").rstrip()
        
        print cmd
        sshCommands(cmd)
        print cmd

        #Dictionary for possible commands user can do
        #Might put these somewhere else, but for now, they are here as well
        

    #def main():
    #    try:
    #        import sys
    #        from fabric.api import *
    #    except ImportError as err:
    #        print("[Error] I don't have " + str(err))
    #        sys.exit()   
        
        
    #    cmd  = raw_input(">> ").rstrip()
    #    evaluate.cmdCheck(cmd)
    #    cmdList = cmd.split(' ')

     #   if cmdList[0] == "set":
     #       set()

    #Thinking of doing a dict for this as well. Gotta ponder on it a bit more.
    



'''
# Specify hosts here
env.hosts = [
    "172.16.117.164"
]

#Specify credentials. I believe this can be a list.
env.user = 'root'
env.password = 'Password*'
'''

