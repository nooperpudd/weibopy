# encoding:utf-8
from __future__ import absolute_import

import requests
import json
import oauthlib




class WeiboClient(object):
    """
    """
    base_url = "https://api.weibo.com/"

    def __init__(self,username,password,token,):
        """
        
        """
        self.username = username
        self.password = password

        self.session = requests.Session()

    def error_handler(self):
        """
        :return: 
        """
        pass