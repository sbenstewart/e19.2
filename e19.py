#!/bin/env python
import os
import sys

os.system("./new.command '%s' & python kit/new.py" % str(sys.argv[1]))


os.system("clear")
