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
import functools
import traceback
import pandas as pd
from typing import List
import concurrent.futures
from typing import Callable
from fake_user_agent import user_agent
from ._config import *


def log_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Executing function {func.__name__} with args: {args} and kwargs: {kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Function {func.__name__} executed successfully with result: {result}")
            return result
        except Exception as e:
            logger.error(f"Function {func.__name__} raised an exception: {str(e)}")
            traceback.print_exc()
            raise
    return wrapper


def random_chrome_driver():
    return random.choice([
        CHROME_V1_PATH, 
        CHROME_V2_PATH
    ])
    
@log_execution 
def random_user_agent():
    return user_agent("chrome", use_cache=False)

@log_execution 
def random_http_headers():
    return {
        'User-Agent': '{0}'.format(random_user_agent()),
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Accept-Language': 'en-US,zh;q=0.8'
    }
    
@log_execution 
def remove_special_characters(text: str):
    return text.replace(".", "").replace("-", "").replace("/", "")

@log_execution 
def file_exists(path: str):
    return os.path.isfile(path)

@log_execution 
def extract_file():

    if not file_exists(ZIP_FILE_PATH):
        raise FileNotFoundError("ZIP File not found")
    
    # extract file 
    with zipfile.ZipFile(ZIP_FILE_PATH, 'r') as zip_ref:
        zip_ref.extractall(DOWNLOAD_PATH)
        
    # # remove zip file
    time.sleep(5)
    if file_exists(ZIP_FILE_PATH):
        os.remove(ZIP_FILE_PATH)

@log_execution 
def create_dataset() -> pd.DataFrame:
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
        names=DATASET_COLUMNS, 
        usecols=DATASET_VISIBLE_COLUMNS
    )
    
@log_execution 
def load_dataset(path: str):
    return pd.read_parquet(path, engine="pyarrow")

@log_execution 
def combine_datasets(datasets: List):
    """ merge datasets """

    return pd.concat([
        ds for ds in datasets  
        if ds is not None
    ])
    
@log_execution 
def wait(delay: float = (2, 4)):
    time.sleep(random.uniform(*delay))

@log_execution 
def parallel_process_rows(df: pd.DataFrame, function: Callable, delay: float = (1, 3)):
    with concurrent.futures.ProcessPoolExecutor(5) as executor:
        results = list(executor.map(function, df.iterrows()))
        for _ in results:
            yield _
            
