#!/bin/env python
import os
import sys

os.system("python starter.py '%s' & python detector.py" % str(sys.argv[1]))

os.system("clear")
