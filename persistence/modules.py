#!/usr/bin/env python
'''
    Author: Jared Stroud, Scott Vincent
    Purpose: Stores modules that will be used for persistence
    #Purpose: SSH Fabric file for dropping persistence scripts and running them on Linux machines.

'''

class Modules:

    try:
        import json
    except ImportError as err:
        print("Error, cannot find package " + str(err))
        exit()

    def set(self, args):
        '''
        Name: set
        Description: This function (or method if we end up putting this in a class) will be called when the user calls persistence/ssh then wishes to set settings
        Parameters: It takes a list of arguements that we will sort here
        Returns: Not sure at the moment.
        '''
        try:
            from utilities.commands import evalCmd
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
            for i in args:
                print( i + " has been set as a target")
        
        #set user
        #Specificy user that you will log in as
        if cmd  == "user":
            print("Setting users...")
            data['users'] = args
            f = open('etc/ssh.conf', 'w')  
            json.dump(data, f) 
            f.close()
            for i in args:
                print( i + " has been set as a user")

        #set password
        #Allows user to set the password
        if cmd  == "password":
            print("Setting password...")
            data['passwords'] = args
            f = open('etc/ssh.conf', 'w')  
            json.dump(data, f) 
            f.close()
            for i in args:
                print( i + " has been set as a password")


        #Return to ssh prompt
        self.ssh()

    def who(self):
        run('whoami')

    def uptime(self): # Executes uptime on the remote machine
        run('uptime')


    def sshCommands(self, cmd):
        args = cmd.split(' ')
        cmd = args.pop(0)

        commands = { 
                'set':self.set,
                'who':self.who,
                'uptime':self.uptime,
                'exit':self.quit
                }
                     
        #Run the command
        try:
            commands[cmd](args)
        except KeyError:
            print("[Error]" + cmd + " is not a valid command. Type 'help' for more information")
            self.ssh()

    def ssh(self):
        '''
        I don't know how this is going to work yet but we will see
        '''
        print( "Using SSH for persistence. For help type 'help.'")

        cmd  = raw_input("[ssh]>> ").rstrip()
        self.sshCommands(cmd)

    def quit(self, NULL):
        #Return to main menu
        return 0
    
    
