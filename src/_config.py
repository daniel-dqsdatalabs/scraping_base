
# -*- coding: utf-8 -*-
#==============================================================================
# filename          : _config.py
# email             : daniel@dqsdatalabs.com
# date              : 29.12.2022
# version           : 0.01
#==============================================================================


import os
from pathlib import Path

BASE_PATH =  Path(__file__).parent.parent
LIB_PATH = os.path.join(BASE_PATH, "lib")

PROXY_CHECK_URL = "http://google.com"
VALIDATION_URL="https://www.nowsecure.nl"

CHROME_V1_PATH = os.path.join(LIB_PATH, "chromedriver/Linux/97/chromedriver")
CHROME_V2_PATH = os.path.join(LIB_PATH, "chromedriver/Linux/106/chromedriver")



