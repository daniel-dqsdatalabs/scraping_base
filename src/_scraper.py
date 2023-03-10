# -*- coding: utf-8 -*-
# ==============================================================================
# filename          : scraper.py
# email             : daniel@dqsdatalabs.com
# date              : 29.12.2022
# version           : 0.01
# ==============================================================================


import re
import time
import pandas as pd
from typing import Any
from lxml import etree
from random import randint
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from ._config import *
from ._utils import *
from ._driver import WebDriver

class Scraper:
    
    @log_execution 
    def __init__(self, url: str, query: str = None, uuid: str = None):
        """ initialize the scraper object """
        
        self._url: str = url   
        self._uuid: str = uuid     
        self._query: str = query
        self._datasets: List = []
        self._details_html: str = None
        self._driver: Any = WebDriver().init()
        
    @property
    def dataset(self) -> List:
        return pd.concat(self._datasets)
        
    @log_execution 
    def _wait_page_load(self):
        """
        wait up to 20 seconds for the page elements 
        identified by the PAGE_LOAD_XPATH to become visible
        """
        
        WebDriverWait(self._driver, timeout=20).until(
            EC.visibility_of_all_elements_located(
                (By.XPATH, PAGE_LOAD_XPATH)
            )
        )
        
    @log_execution 
    def _wait_page_details_load(self):
        """
        wait up to 120 seconds for the page elements 
        identified by the RESULTS_LABEL_XPATH to become visible
        """
        
        WebDriverWait(self._driver, timeout=120).until(
            EC.presence_of_element_located(
                (By.XPATH, RESULTS_LABEL_XPATH)
            )
        )
        
    @log_execution 
    def _scroll_to_middle(self, value: int = 2):
        
        # get scroll position
        scroll_position = self._driver.execute_script("return window.pageYOffset;")
        
        # find scroll element
        wait((3.1, 4.6))
        body = self._driver.find_element(
            By.XPATH, PAGE_LOAD_XPATH
        )
        # scroll to middle
        target = scroll_position + (body.size["height"] / value)
        self._driver.execute_script("window.scrollTo(0, {});".format(target))
        

        
    @log_execution 
    def _execute_query(self):
        """"
        This function is used to run a query on the main page. 
        It validates the input type, finds the input query element, 
        fills the query, scrolls down and finds the search button before finally clicking it.
        """
        
        # validate input type
        self._wait_page_load()
        INPUT_XPATH = (
            TXT_QUERY_BY_NAME_XPATH
            if self._query else TXT_QUERY_BY_UUID_XPATH
        )
        
        # find query element
        txt_query = self._driver.find_element(
            By.XPATH, INPUT_XPATH
        )
        
        # fill query
        (ActionChains(self._driver)
            .move_to_element(txt_query)
            .click(txt_query)
            .pause(2)
            .send_keys(f"{self._uuid if self._uuid else self._query}\n")
            .perform()
        )
        
        # scroll down page
        self._scroll_to_middle(2)
        
        btn = WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, BUTTON_SEARCH_XPATH))
        )
        
        wait((3.1, 3.5))
        # scroll element into view and click it
        ActionChains(self._driver).move_to_element(btn).perform()
        self._driver.execute_script("arguments[0].click();", btn)
        
        wait((6.1, 7.1))
        
    @log_execution 
    def _download_csv(self):
        """ download csv file from main page """
        
        # wait for element to become visible
        self._wait_page_load()
        self._wait_page_details_load()
        
        # scroll down page
        self._scroll_to_middle(4)
        
        btn = WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, BUTTON_EXPORT))
        )
        
        wait((3.1, 3.5))
        # scroll element into view and click it
        ActionChains(self._driver).move_to_element(btn).perform()
        self._driver.execute_script("arguments[0].click();", btn)
        
        # wait download to complete
        wait((30, 32))
        
    @log_execution 
    def _load_details_page(self):
        """ load details page and fill details_html attribute """
        
        self._wait_page_details_load()
        btn = self._driver.find_element(
            By.XPATH, BUTTON_DETAIL
        )
        
        # click details button
        (ActionChains(self._driver)
            .move_to_element(btn)
            .click(btn)
            .perform())
        
        wait((7.8, 9.9))
        self._details_html = self._driver.page_source
        
    @log_execution 
    def _parse_html(self):
        """ data parser """
        
        self._load_details_page()
        
        if not self._details_html:
            raise Exception("No details page info found.")
        
        soup = BeautifulSoup(
            self._details_html, "html.parser"
        )
        dom = etree.HTML(str(soup))
        for h6 in soup.select("h6"):
            table = h6.find_next("table")
            if not table:
                continue
            
            dataset = pd.read_html(str(table), header=0)[0]
            dataset[DETAILS_DATAFRAME_LABEL] = h6.get_text()
            dataset[DETAILS_FIELD_001_LABEL] = dom.xpath(DETAILS_FIELD_001_XPATH)[0].text
            dataset[DETAILS_FIELD_002_LABEL] = dom.xpath(DETAILS_FIELD_002_XPATH)[0].text
            dataset[DETAILS_FIELD_003_LABEL] = dom.xpath(DETAILS_FIELD_003_XPATH)[0].text
            dataset[DETAILS_FIELD_003_LABEL] = dom.xpath(DETAILS_FIELD_004_XPATH)[0].text
            self._datasets.append(dataset)
            
    @log_execution 
    def scrape_main_page_data(self):
        """ main page """
        
        if not self._query:
            return None
        
        self._driver.get(self._url)
        self._execute_query()
        self._download_csv()
        self._driver.quit()

    @log_execution 
    def scrape_details_page_data(self):
        """ details page """
        
        if not self._uuid:
            return None
        
        self._driver.get(self._url)
        self._execute_query()
        self._parse_html()
        self._driver.quit()




