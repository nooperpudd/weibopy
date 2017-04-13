# encoding:utf-8
from __future__ import absolute_import

import requests
import json
import oauthlib
from .exceptions import WeiboAPIError


class WeiboClient(object):
    """
    """
    base = "https://api.weibo.com/2/"

    def __init__(self,access_token,):
        """
        
        """
        self.access_token = access_token
        self.session = requests.Session()

    def request(self,method,url, params,data=None):
        """
        :param url: 
        :param method: 
        :param params: 
        :param data: 
        :return: 
        """
        params.update({
            "access_token": self.access_token
        })
        response = self.session.request(method=method,url=url,params=params,data=data)

        return self._error_handler(response.json())


    def _error_handler(self,data):
        """
        :return: 
        """
        if data.get("error_code"):
            raise WeiboAPIError(data["error_code"], data["error"])
        else:
            return data