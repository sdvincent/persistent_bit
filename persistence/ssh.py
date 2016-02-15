#!/usr/bin/env python
'''
    Author: Scott Vincent
    Purpose: Stores modules that will be used for persistence
    #Purpose: SSH Fabric file for dropping persistence scripts and running them on Linux machines.

'''

class ssh:

    #from utilities.handler import handler
    try:
        import json
        import sys
    except ImportError as err:
        print("Error, cannot find package " + str(err))
        sys.exit()

    def set(self, args):
        '''
        Name: set
        Description: This function (or method if we end up putting this in a class) will be called when the user calls persistence/ssh then wishes to set settings
        Parameters: It takes a list of arguements that we will sort here
        Returns: Not sure at the moment.
        '''
        try:
            from utilities.colors import TermColors
            import json
        except ImportError as err:
            print("Error, cannot find package " + str(err))
            return 0
        

        cmd = args.pop(0)
        
        #Open ssh config file for writing
        f = open('etc/ssh.conf', 'r')
        data = json.load(f)
        f.close

        #set target
        #Set's the remote host IP
        if cmd  == "target":

            print("Setting targets...")
            data['targets'] = args
            #This can probably go into a method but for now w/e
            f = open('etc/ssh.conf', 'w')  
            json.dump(data, f) 
            f.close()
            print(TermColors.green)
            for i in args:
                print( i + " has been set as a target")
            print(TermColors.blue)
        
        #set user
        #Specificy user that you will log in as
        if cmd  == "user":
            print("Setting users...")
            data['users'] = args
            f = open('etc/ssh.conf', 'w')  
            json.dump(data, f) 
            f.close()
            print(TermColors.green)
            for i in args:
                print( i + " has been set as a user")
            print(TermColors.blue)

        #set password
        #Allows user to set the password
        if cmd  == "password":
            print("Setting password...")
            data['passwords'] = args
            f = open('etc/ssh.conf', 'w')  
            json.dump(data, f) 
            f.close()
            print(TermColors.green)
            for i in args:
                print( i + " has been set as a password")
            print(TermColors.blue)

        #Return to ssh prompt
        self.ssh()

    def check(self, val):
        #Will be used to see what is in config file
        import json

        f = open('etc/ssh.conf', 'r')
        data = json.load(f)
        f.close
        if val[0] == "target" or val[0] == "targets":
            print("Tagets loaded:")
            for i in  data["targets"]:
                print("\t" + i)
        
        if val[0] == "user" or val[0] == "users":
            print("Usersnames loaded:")
            for i in  data["users"]:
                print("\t" + i)

        if val[0] == "password" or val[0] == "passwords":
            print("Passwords loaded:")
            for i in  data["passwords"]:
                print("\t" + i)

        self.ssh()

    def connect(self, NULL):
        '''
        Name: connect
        Description: This creates and maintains ssh connection with the use of paramiko, a python module for SSH. For more information on paramiko, check out: http://www.paramiko.org/index.html.
        All commands will be executed from this method. User may exit this method and return to ssh method by typing "exit"
        Parameters: None
        Returns: None
        '''
        
        try:
            import json
            import paramiko
            from utilities.colors import TermColors
        except ImportError as err:
            print("Error, cannot find package " + str(err))
            self.ssh()

        #Read in our targets and place into list
        f = open('etc/ssh.conf','r')
        data = json.load(f)
        f.close()

        #Set values
        targets = data["targets"]
        users = data["users"]
        passwords = data["passwords"]

        #Create paramiko object
        ssh = paramiko.SSHClient()

        #Allow hosts automatically without manually saying 'yes'
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        #Connect to hosts
        #How this is done right now is temporary. We will have to put this in a for loop for multiple hosts.
        #Should also put in a try/except for succes easy success messages
        try:
            ssh.connect(targets[0], username=users[0],password=passwords[0])
            print(TermColors.green + "Success connection established on: " + targets[0] + ". Happy hunting!") 
            print(TermColors.blue)

            input = ""
            while True:
                input = raw_input("["+TermColors.cyan+"ssh"+TermColors.blue+"]>> ").rstrip()
                if input == "exit":
                    #Maybe try a break instead so we can return 0 (good practice?)
                    ssh.close()
                    self.ssh()
                
                #These next couple lines combine the stdout and stderr and places in correct order
                tran = ssh.get_transport()
                chan = tran.open_session()
                chan.get_pty()
                f = chan.makefile()
                chan.exec_command(input)
                print(TermColors.white)
                print f.read(), #Cannot put into print function b/c output was weird. Will look into later
                print(TermColors.blue)

        except Exception, e:
            print(TermColors.red)
            print("[Error] " + str(e))
            print(TermColors.blue)


    def sshCommands(self, cmd):
        args = cmd.split(' ')
        cmd = args.pop(0)

        commands = { 
                'set':self.set,
                'check':self.check,
                'charge!':self.connect,
                'exit':self.quit
                }
                     
        #Run the command
        try:
            commands[cmd](args)
        except KeyError:
            print("[Error]" + cmd + " is not a valid command. Type 'help' for more information")
            self.ssh()

    def ssh_menu(self, evaluate):
        '''
        I don't know how this is going to work yet but we will see
        '''
        
        src = "ssh"

        print( "Using SSH for persistence. For help type 'help.'")

        cmd  = raw_input("[ssh]>> ").rstrip()
        evaluate.command(cmd, src)





