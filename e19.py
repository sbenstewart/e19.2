#!/bin/env python

./new.command $1 &
python kit/new.py

os.system("new.command" % str(sys.argv[1]))
os.system("python kit/new.py ")

os.system("clear")
