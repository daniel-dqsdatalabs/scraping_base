
# -*- coding: utf-8 -*-
#==============================================================================
# filename          : app.py
# email             : daniel@dqsdatalabs.com
# date              : 29.12.2022
# version           : 0.01
#==============================================================================

from time import sleep
from src import WebDriver, wait_page_loaded, fill_input, click_sync


def scrape(url):
    driver = WebDriver().init()
    
    input_txt = ""
    xpath_btn = ""
    
    try:
        driver.get(url)
        wait_page_loaded(driver)
        fill_input(driver, input_txt)
        click_sync(driver, xpath_btn)
    except Exception as e:
        print(e)
    finally:
        sleep(15)
        
    

if __name__ == "__main__":
    scrape(url="")
    
