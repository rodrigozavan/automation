import sys
import os
import json
from pathlib import Path

var_env = json.load(open(str(Path(__file__).parent.parent) + os.sep + 'config.json'))

if sys.platform == "linux" or sys.platform == "linux2":
    debug = False
    env = 'dev'
else:
    debug = False
    env = 'dev'
