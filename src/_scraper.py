# -*- coding: utf-8 -*-
# ==============================================================================
# filename          : scraper.py
# email             : daniel@dqsdatalabs.com
# date              : 29.12.2022
# version           : 0.01
# ==============================================================================


import time
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from ._driver import WebDriver
from ._utils import validate_cnpj

from ._config import REPO_PATH
from ._config import PAGE_LOAD_XPATH
from ._config import RESULTS_LABEL_XPATH
from ._config import RESULTS_TABLE_XPATH
from ._config import BUTTON_SEARCH_XPATH
from ._config import TXT_QUERY_BY_NAME_XPATH
from ._config import TXT_QUERY_BY_CNPJ_XPATH
from ._config import RESULTS_TABLE_SCROLL_XPATH
from ._config import BUTTON_EXPORT_RESULTS_XPATH
from ._config import RESULTS_TABLE_ROW_BUTTON_XPATH

class Scraper:
    
    
    def __init__(self, url: str, query: str = None, cnpj: str = None):
        """ initialize the scraper object """
        
        self.url = url
        self.cnpj = cnpj        
        self.query = query
        self.driver = WebDriver().init()
        

    def _wait_load(self):
        """
        wait up to 20 seconds for the page elements 
        identified by the PAGE_LOAD_XPATH to become visible
        """
        
        WebDriverWait(self.driver, timeout=20).until(
            EC.visibility_of_all_elements_located(
                (By.XPATH, PAGE_LOAD_XPATH)
            )
        )
        
    def _run_query(self):
        """"
        This function is used to run a query on the main page. 
        It validates the input type, finds the input query element, 
        fills the query, scrolls down and finds the search button before finally clicking it.
        """
        
        # validate input type
        INPUT_XPATH = (
            TXT_QUERY_BY_NAME_XPATH
            if not validate_cnpj(self.query)
            else TXT_QUERY_BY_CNPJ_XPATH
        )
        
        # find query element
        qry_elem = self.driver.find_element(
            By.XPATH, INPUT_XPATH
        )
        
        # fill query
        (ActionChains(self.driver)
         .move_to_element(qry_elem)
         .click(qry_elem)
         .pause(randint(1,2))
         .send_keys(f"{self.query}\n")
         .perform())
        
        # find scroll element
        body = self.driver.find_element(
            By.XPATH, PAGE_LOAD_XPATH
        )
        
        # scroll down once
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(randint(1,2))
        
        # find search button
        btn_elem = self.driver.find_element(
            By.XPATH, BUTTON_SEARCH_XPATH
        )
        
        # click search button
        (ActionChains(self.driver)
         .move_to_element(btn_elem)
         .click(btn_elem)
         .pause(randint(3, 5))
         .perform())


    def _download_csv(self):
        """
        This function is used to extract the information from the details page.
        """
        
        # wait up to 2 min until element become visible
        WebDriverWait(self.driver, timeout=120).until(
            EC.presence_of_element_located(
                (By.XPATH, RESULTS_LABEL_XPATH)
            )
        )
        
        # wait up to 2 min until element become visible
        WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(
                (By.XPATH, RESULTS_LABEL_XPATH)
            )
        )
        
        # find export button
        btn = self.driver.find_element(
            By.XPATH, '/html/body/dev-root/dev-consulta/main/dev-resultados/div[3]/div/div/button[1]'
        )
        
        # click export button
        (ActionChains(self.driver)
         .move_to_element(btn)
         .click(btn)
         .perform())
        
        # wait 5s
        time.sleep(20)
        
    def download_file(self):
        """ 
        Method responsible for downloading a file from the given URL. 
        It uses Selenium webdriver to open the URL, wait for the page to load and run the query. 
        """

        # Open the URL
        self.driver.get(self.url)
        
        # Page 1
        self._wait_load()
        self._run_query()
        
        # Page 2
        self._wait_load()
        self._download_csv()
        
        # Close the browser
        self.driver.quit()
        







