
# -*- coding: utf-8 -*-
#==============================================================================
# filename          : _config.py
# email             : daniel@dqsdatalabs.com
# date              : 29.12.2022
# version           : 0.01
#==============================================================================


import os
from pathlib import Path
from datetime import datetime

BASE_PATH =  Path(__file__).parent.parent
LIB_PATH = os.path.join(BASE_PATH, "lib")
REPO_PATH = os.path.join(LIB_PATH, "files")

DATABASE = "data.db"
TBL_DEBTORS = "tbl_debtors"
TBL_CREDITORS = "tbl_creditors"

PROXY_CHECK_URL = "http://google.com"
VALIDATION_URL="https://www.nowsecure.nl"
TARGET_URL="https://www.listadevedores.pgfn.gov.br/"

FILE_NAME = "Consulta_Lista_Devedores"
DATE = datetime.now().strftime("%Y_%m_%d")
ZIP_FILE_PATH = f"{REPO_PATH}/{FILE_NAME}_{DATE}.zip"
CSV_FILE_PATH = f"{REPO_PATH}/{FILE_NAME}_{DATE}.csv"

CHROME_V1_PATH = os.path.join(LIB_PATH, "chromedriver/Linux/97/chromedriver")
CHROME_V2_PATH = os.path.join(LIB_PATH, "chromedriver/Linux/106/chromedriver")
CHROME_PROFILE = "/Users/danielqueiroz/Library/Application Support/Google/Chrome/Profile 1"

PAGE_LOAD_XPATH = '/html/body'
TXT_QUERY_BY_NAME_XPATH = '//*[@id="nome"]'
TXT_QUERY_BY_CNPJ_XPATH = '//*[@id="identificacaoInput"]'
RESULTS_LABEL_XPATH = '/html/body/dev-root/dev-consulta/main/dev-resultados/p/span/strong'
BUTTON_SEARCH_XPATH = '/html/body/dev-root/dev-consulta/main/dev-filtros/div[3]/div/div/button[1]'
BUTTON_EXPORT_RESULTS_XPATH = '/html/body/dev-root/dev-consulta/main/dev-resultados/div[2]/div[2]/button[1]'
RESULTS_TABLE_SCROLL_XPATH = '/html/body/dev-root/dev-consulta/main/dev-resultados/cdk-virtual-scroll-viewport'
RESULTS_TABLE_XPATH = '/html/body/dev-root/dev-consulta/main/dev-resultados/cdk-virtual-scroll-viewport/div[1]/div/table/tbody'
RESULTS_TABLE_ROW_BUTTON_XPATH = f'/html/body/dev-root/dev-consulta/main/dev-resultados/cdk-virtual-scroll-viewport/div[1]/div/table/tbody/tr[{{row}}]/td[5]/a'

