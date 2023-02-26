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


@log_execution 
def main_page(query: str = DEFAULT_QUERY_STRING):
    
    # Run Scraper
    scraper = Scraper(url=TARGET_URL, query=query)
    scraper.scrape_main_page_data() 
    
    # Process CSV
    extract_file()
    dataset = create_dataset()
    dataset.to_parquet(PARQUET_MASTER_FILE_PATH, engine="pyarrow")

    
@log_execution 
def details_page():
    
    datasets = []
    uuid_values = load_dataset(PARQUET_MASTER_FILE_PATH)[UUID_COL].values.tolist()
    
    # TODO: use concurrent.futures
    for uuid in uuid_values:
        if len(datasets) == 2:
            break
        scraper = Scraper(url=TARGET_URL, uuid=uuid)
        dataset = scraper.scrape_details_page_data() 
        datasets.append = dataset if dataset else None
        
    dataset = combine_datasets(datasets)
    dataset.to_parquet(PARQUET_DETAIL_FILE_PATH, engine="pyarrow")
    
if __name__ == "__main__":
    #main_page()
    details_page()



