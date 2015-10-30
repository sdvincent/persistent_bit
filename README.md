# persistent_bit

###How To?
sshCommands is a fabric file NOT a python file. To run, execute fab -f sshCommands.py <command_desired>
The hosts are currently specified in the env.hosts[] list and can be changed.


### TODO
* Pyinstaller for executable integration
* Fabric for ssh brute forcing.
    * change fabric to be based on a file of addresses.
* Flask for web server.

* Once we're in
    * sanitize logs of your presence 
    * Backdoors (trixdoor)


* Veil 
* Have writing to file from user shell for config stuff


### How we should implement commands
use <module> 
    * module would be the fabric ssh script (loading the module)
    * set can be defining variables (set ip = $IpYouWant)
