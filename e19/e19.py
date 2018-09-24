#!/bin/env python
import os
import sys

os.system("python checker.py '%s' & python detector.py" % str(sys.argv[1]))

os.system("clear")
