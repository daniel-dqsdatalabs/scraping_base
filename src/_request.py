
# -*- coding: utf-8 -*-
#==============================================================================
# filename          : _req.py
# email             : daniel@dqsdatalabs.com
# date              : 29.12.2022
# version           : 0.01
#==============================================================================

import time
import requests
import requests_cache
from lxml import etree
from requests.models import Response
from ._utils import random_http_headers

requests.packages.urllib3.disable_warnings()
requests_cache.install_cache('root_cache', backend='sqlite', expire_after=28800)


class WebRequest:

    def __init__(self, proxy=None):
        self.response = Response()
        self.proxy = proxy 

    def get(self, url, header=None, retry_time=3, retry_interval=5, timeout=5, *args, **kwargs):
        headers = random_http_headers()
        if header and isinstance(header, dict):
            headers.update(header)    
        while True:
            try:
                self.response = requests.get(
                    url=url, 
                    headers=headers, 
                    proxies=self.proxy, 
                    timeout=timeout, 
                    *args, **kwargs
                )
                return self 
            except Exception as e:
                retry_time -= 1
                if retry_time <= 0:
                    resp = Response()
                    resp.status_code = 200
                    return self
                time.sleep(retry_interval)

    @property
    def tree(self):
        return etree.HTML(self.response.content)

    @property
    def text(self):
        return self.response.text

    @property
    def json(self):
        try:
            return self.response.json()
        except Exception as e:
            return {}

