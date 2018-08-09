#!/bin/env python
import os
import sys
import subprocess


os.system("open -a 'Microsoft PowerPoint.app' '%s'" % str(sys.argv[1]))


command = ["ps","aux","|","pgrep","Microsoft PowerPoint","|","wc","-l"]
command = 'ps aux | pgrep "Microsoft PowerPoint" | wc -l'
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)

#Launch the shell command:
output = process.communicate()

#print output[0]




while int(output[0]) != 0:
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
    output = process.communicate()
    #print output[0]

os.system("python killer.py")
