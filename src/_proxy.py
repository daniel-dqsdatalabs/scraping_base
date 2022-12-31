

# -*- coding: utf-8 -*-
#==============================================================================
# filename          : _proxy.py
# email             : daniel@dqsdatalabs.com
# date              : 29.12.2022
# version           : 0.01
#==============================================================================

import json
import random
import requests
import functools
from src._req import WebRequest
from src._config import PROXY_CHECK_URL
from src._utils import random_http_headers


class Proxy:

    def _srv_001(self):
        url = "http://proxylist.fatezero.org/proxy.list"
        try:
            r = WebRequest().get(url).text
            for each in r.split("\n"):
                if each:
                    json_info = json.loads(each)
                    if json_info.get("country") == "BR":
                        yield "%s:%s" % (json_info.get("host", ""), json_info.get("port", ""))
        except Exception as e:
            print(e)
            
    
    def _check_proxy(self, proxy):
        try:
            session = requests.Session()
            session.max_redirects = 300
            session.headers = random_http_headers()
            session.get(PROXY_CHECK_URL, proxies={'http':'http://' + proxy}, timeout=3, allow_redirects=True)
        except:
           return False
       
        return True 
    
    
    @functools.cached_property
    def proxies(self):
        _p = filter(
            lambda p: self._check_proxy(p) is True,
            self._srv_001()
        )
        return list(set(_p))
        

    @property
    def proxy(self):
        return random.choice(self.proxies)
        