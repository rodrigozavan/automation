import sys
import os
import secrets
import json
from pathlib import Path

var_env = json.load(open(str(Path(__file__).parent.parent) + os.sep + 'config.json'))

if sys.platform == "linux" or sys.platform == "linux2":
    debug = False
    Chrome = str(Path(__file__).parent.parent) + os.sep + 'webdriver' + os.sep + 'chromedriver_linux_' + var_env[
        'chrome_version']
    Firefox = str(Path(__file__).parent.parent) + os.sep + 'webdriver' + os.sep + 'geckodriver'
    env = 'dev'
else:
    debug = False
    Chrome = str(Path(__file__).parent.parent) + os.sep + 'webdriver' + os.sep + 'chromedriver.exe'
    Firefox = str(Path(__file__).parent.parent) + os.sep + 'webdriver' + os.sep + 'geckodriver'
    env = 'dev'

secret_key = str(secrets.token_hex(16))
