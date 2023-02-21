# -*- coding: utf-8 -*-
# ==============================================================================
# filename          : app.py
# email             : daniel@dqsdatalabs.com
# date              : 29.12.2022
# version           : 0.01
# ==============================================================================

import concurrent.futures
import time
import pandas as pd
from typing import Callable
from src import *


def main_page(query: str = DEFAULT_QUERY_STRING):
    
    if file_exists(CSV_FILE_PATH):
        print("File already exists")
        return
    
    # Run Scraper
    scraper = Scraper(url=TARGET_URL, query=query)
    scraper.scrape_main_page_data() 
    
    # Process CSV
    extract_file()
    dataset = create_dataset()
    dataset.to_parquet(PARQUET_MASTER_FILE_PATH, engine="pyarrow", overwrite=True)

    
def details_page():
    
    datasets = []
    cnpj_list = load_dataset(PARQUET_MASTER_FILE_PATH)["cnpj"].values.tolist()
    
    # TODO: use concurrent.futures
    for cnpj in cnpj_list:
        if len(datasets) == 2:
            break
        scraper = Scraper(url=TARGET_URL, cnpj=cnpj)
        dataset = scraper.scrape_details_page_data() 
        datasets.append = dataset if dataset else None
        
    dataset = combine_datasets(datasets)
    dataset.to_parquet(PARQUET_DETAIL_FILE_PATH, engine="pyarrow", overwrite=True)
    
if __name__ == "__main__":
    main_page()
    details_page()



