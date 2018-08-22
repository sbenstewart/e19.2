#!/bin/env python
import os
import sys

os.system("python new.py '%s' & python kit/new.py" % str(sys.argv[1]))

os.system("clear")
