# -*- coding: utf-8 -*-
#==============================================================================
# filename          : _utils.py
# email             : daniel@dqsdatalabs.com
# date              : 29.12.2022
# version           : 0.01
#==============================================================================

import random 
from fake_user_agent import user_agent
from selenium.webdriver.common.by import By
from src._config import CHROME_V1_PATH, CHROME_V2_PATH
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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


def wait_page_loaded(web_driver):
    wait = WebDriverWait(web_driver, 20)
    wait.until(EC.visibility_of_all_elements_located((By.XPATH, '/html/body')))
    

def click_sync(web_driver, xpath):
    web_driver.find_elements(By.XPATH, xpath)[-1].click() 
    
    
def fill_input(web_driver, input):
    obj = web_driver.find_element(By.XPATH, '//*[@id="nome"]')
    obj.clear()
    obj.send_keys(f"{input}\n") 
   