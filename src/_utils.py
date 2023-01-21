# -*- coding: utf-8 -*-
#==============================================================================
# filename          : _utils.py
# email             : daniel@dqsdatalabs.com
# date              : 29.12.2022
# version           : 0.01
#==============================================================================

import os
import random
import time 
import zipfile
import pandas as pd
from typing import Union
from validate_docbr import CNPJ
from fake_user_agent import user_agent
from ._config import CHROME_V1_PATH, CHROME_V2_PATH, ZIP_FILE_PATH, CSV_FILE_PATH, REPO_PATH



def random_chrome_driver():
    return random.choice([
        CHROME_V1_PATH, 
        CHROME_V2_PATH
    ])
    

def random_user_agent():
    return user_agent("chrome", use_cache=False)


def random_http_headers():
    return {
        'User-Agent': '{0}'.format(random_user_agent()),
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Accept-Language': 'en-US,zh;q=0.8'
    }

def validate_cnpj(cnpj: str):
    return CNPJ().validate(cnpj)


def file_exists(path: str):
    """ 
    Check if a file exist in a directory
    :return: boolean value, True if file exist and False otherwise
    """
    return os.path.isfile(path)


def extract_file():
    """
    This function extracts a zip file from the repository path to the given file path. 
    It first checks if the file is present in the repository path, and if it is not present, it waits for one second and checks again. 
    Once the file is present, it unzips it to the given file path.
    """

    # file exists
    if not file_exists(ZIP_FILE_PATH):
        raise FileNotFoundError("ZIP File not found")

    # extract file 
    with zipfile.ZipFile(ZIP_FILE_PATH, 'r') as zip_ref:
        zip_ref.extractall(REPO_PATH)
        
    # # remove zip file
    time.sleep(5)
    if file_exists(ZIP_FILE_PATH):
        os.remove(ZIP_FILE_PATH)


def create_dataset():
    """
    This function reads a csv file for the given date. 
    It takes in the current date as a string and returns a pandas dataframe. 
    The file is located in the path provided by the filepath function and is encoded in utf-8 with 12 header rows.
    """
    
    # file exists
    if not file_exists(CSV_FILE_PATH):
        raise FileNotFoundError("CSV File not found")
    
    # create dataframe
    return pd.read_csv(
        CSV_FILE_PATH, 
        sep=";", 
        skiprows=range(0, 12),
        header=None,
        engine="python", 
        encoding="iso-8859-1",
        names=[
            "cnpj", "nome", "nome_fantasia", "valor_total_debito", "VTDS"
        ], 
        usecols=[
            "cnpj", "nome", "nome_fantasia", "valor_total_debito"
        ]
    )
