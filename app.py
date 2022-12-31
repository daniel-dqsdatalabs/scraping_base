
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
    
    query = "massa falida"
    xpath_btn = '/html/body/dev-root/dev-consulta/main/dev-filtros/div[3]/div/div/button[1]'
    
    try:
        driver.get(url)
        wait_page_loaded(driver)
        fill_input(driver, query)
        click_sync(driver, xpath_btn)
        print(driver)
    except Exception as e:
        print(e)
    finally:
        sleep(15)
        
    

if __name__ == "__main__":
    scrape(url="https://www.listadevedores.pgfn.gov.br")
    
