# -*- coding: utf-8 -*-
# ==============================================================================
# filename          : app.py
# email             : daniel@dqsdatalabs.com
# date              : 29.12.2022
# version           : 0.01
# ==============================================================================


from src import Scraper, Storage
from src import TARGET_URL, CSV_FILE_PATH 
from src import create_dataset, extract_file, file_exists

def generate_data_service():
    
    if file_exists(CSV_FILE_PATH):
        print("File already exists")
        return
    
    # download file
    page = Scraper(url=TARGET_URL, query="massa falida")
    page.download_file()
    
    # process file
    extract_file()
    dataset = create_dataset()
    
    # store results
    storage = Storage()
    storage.save_debtors(dataset)
 
    
def acquisition_data_service():
        
    # query results
    storage = Storage()
    dataset = storage.get_debtors()
    
    print(dataset.head(10))


if __name__ == "__main__":
    acquisition_data_service()
