#!/bin/env python
import os
import sys
import subprocess


os.system("open -a 'Microsoft PowerPoint.app' '%s'" % str(sys.argv[1]))

number = os.popen('ps aux | pgrep "Microsoft PowerPoint" | wc -l')
print number


while number[0]-0 != 0:
    number = os.popen('ps aux | pgrep "Microsoft PowerPoint" | wc -l').readline()
    print number[0]

os.system("python killer.py")
