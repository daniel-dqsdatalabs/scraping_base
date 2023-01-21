
# -*- coding: utf-8 -*-
#==============================================================================
# filename          : _driver.py
# email             : daniel@dqsdatalabs.com
# date              : 29.12.2022
# version           : 0.01
#==============================================================================


import undetected_chromedriver.v2 as uc
from undetected_chromedriver import ChromeOptions
from selenium.webdriver.chrome.service import Service

from ._config import CHROME_PROFILE, REPO_PATH
from ._utils import random_user_agent, random_chrome_driver


class WebDriver:
    
    
    def _get_driver_options(self):
        """
        Set up Chrome options to prevent download dialog and set download directory
        """
        _agent = random_user_agent()
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--ignore-ssl-errors")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument('--user-agent={0}'.format(_agent))
        chrome_options.add_argument('--user-data-dir={0}'.format(CHROME_PROFILE))      
        
        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": REPO_PATH,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })
          	
        return chrome_options
    

    def init(self) -> uc.Chrome:
        path = random_chrome_driver()
        options = self._get_driver_options()
        service = Service(
            executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        )
        
        return uc.Chrome(
            service=service, 
            options=options, 
            use_subprocess=True,
        )


