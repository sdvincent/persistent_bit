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
        
        env = evalCmd()

        
        list = [ "a", 'b', 'c']
        with open('etc/ssh.conf').read() as f:
           # json.dump({'passwords' : list}, f)
            data = json.load(f)
        

        print data["passwords"]

        exit()
        
        #set target
        #Set's the remote host IP
        if args[0] == "target":
            i = 1
            
            
            print "setting target"
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
        print "Using SSH for persistence. For help type 'help.'"

        cmd  = raw_input("[ssh]>> ").rstrip()
        self.sshCommands(cmd)

    def quit(self, NULL):
        #Return to main menu
        return 0
    
    
