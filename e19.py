#!/bin/env python
import os
import sys

os.system("python new.py '%s' & python detector.py" % str(sys.argv[1]))

os.system("clear")
