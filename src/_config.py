
# -*- coding: utf-8 -*-
#==============================================================================
# filename          : _config.py
# email             : daniel@dqsdatalabs.com
# date              : 29.12.2022
# version           : 0.01
#==============================================================================


import os
import logging
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv


load_dotenv()
logging.basicConfig(
    filename=f'./lib/logs/scraper_{int(round(datetime.now().timestamp()))}.log', 
    filemode='w', level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'
)
logger = logging.getLogger(__name__)
os.environ['PYDEVD_WARN_SLOW_RESOLVE_TIMEOUT'] = '180'

# read variables from the .env file
CSV_FILE_NAME = os.getenv('CSV_FILE_NAME')
DEFAULT_QUERY_STRING = os.getenv('DEFAULT_QUERY_STRING')

TARGET_URL = os.getenv('TARGET_URL')
VALIDATION_URL = os.getenv('VALIDATION_URL')
PROXY_CHECK_URL = os.getenv('PROXY_CHECK_URL')
PARQUET_MASTER_NAME = os.getenv('PARQUET_MASTER_NAME')
PARQUET_DETAILS_NAME = os.getenv('PARQUET_DETAILS_NAME')

PAGE_LOAD_XPATH = os.getenv('PAGE_LOAD_XPATH')
TXT_QUERY_BY_NAME_XPATH = os.getenv('TXT_QUERY_BY_NAME_XPATH')
TXT_QUERY_BY_UUID_XPATH = os.getenv('TXT_QUERY_BY_UUID_XPATH')
RESULTS_LABEL_XPATH = os.getenv('RESULTS_LABEL_XPATH')
BUTTON_SEARCH_XPATH = os.getenv('BUTTON_SEARCH_XPATH')
BUTTON_EXPORT_RESULTS_XPATH = os.getenv('BUTTON_EXPORT_RESULTS_XPATH')
RESULTS_TABLE_SCROLL_XPATH = os.getenv('RESULTS_TABLE_SCROLL_XPATH')
RESULTS_TABLE_XPATH = os.getenv('RESULTS_TABLE_XPATH')
RESULTS_TABLE_ROW_BUTTON_XPATH = os.getenv('RESULTS_TABLE_ROW_BUTTON_XPATH')

DETAILS_DATAFRAME_LABEL = os.getenv('DETAILS_DATAFRAME_LABEL')
DETAILS_FIELD_001_XPATH = os.getenv('DETAILS_FIELD_001_XPATH')
DETAILS_FIELD_002_XPATH = os.getenv('DETAILS_FIELD_002_XPATH')
DETAILS_FIELD_003_XPATH = os.getenv('DETAILS_FIELD_003_XPATH')
DETAILS_FIELD_004_XPATH = os.getenv('DETAILS_FIELD_004_XPATH')

DETAILS_FIELD_001_LABEL = os.getenv('DETAILS_FIELD_001_LABEL')
DETAILS_FIELD_002_LABEL = os.getenv('DETAILS_FIELD_002_LABEL')
DETAILS_FIELD_003_LABEL = os.getenv('DETAILS_FIELD_003_LABEL')
DETAILS_FIELD_004_LABEL = os.getenv('DETAILS_FIELD_004_LABEL')

UUID_COL = os.getenv('UUID_COL')
DATASET_COLUMNS = os.getenv('DATASET_COLUMNS').split(",")
DATASET_VISIBLE_COLUMNS = os.getenv('DATASET_VISIBLE_COLUMNS').split(",")


BUTTON_DETAIL = os.getenv('BUTTON_DETAIL')
BUTTON_EXPORT = os.getenv('BUTTON_EXPORT')

CSV_DT = datetime.now().strftime("%Y_%m_%d")
DIR_DT = datetime.now().strftime("%Y_%m_%d")

BASE_PATH =  Path(__file__).parent.parent
LIB_PATH = os.path.join(BASE_PATH, "lib")

FILE_PATH = os.path.join(LIB_PATH, "files")
DOWNLOAD_PATH = os.path.join(FILE_PATH, DIR_DT)
ZIP_FILE_PATH = f"{DOWNLOAD_PATH}/{CSV_FILE_NAME}_{CSV_DT}.zip"
CSV_FILE_PATH = f"{DOWNLOAD_PATH}/{CSV_FILE_NAME}_{CSV_DT}.csv"
PARQUET_MASTER_FILE_PATH = f"{FILE_PATH}/{PARQUET_MASTER_NAME}.parquet"
PARQUET_DETAIL_FILE_PATH = f"{FILE_PATH}/{PARQUET_DETAILS_NAME}.parquet"

CHROME_PROFILE = os.getenv('CHROME_PROFILE')
CHROME_DEFAULT_PATH = os.getenv('CHROME_DEFAULT_PATH')
CHROME_V1_PATH = os.path.join(LIB_PATH, "chromedriver/Linux/97/chromedriver")
CHROME_V2_PATH = os.path.join(LIB_PATH, "chromedriver/Linux/106/chromedriver")