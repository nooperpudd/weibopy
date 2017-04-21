# encoding:utf-8
import copy

import requests

from .exceptions import WeiboAPIError


def filter_params(params):
    """
    convert dict value if value is bool type, 
    False -> "false"
    True -> "true"
    """
    new_params = copy.deepcopy(params)
    for key, value in new_params.items():
        if isinstance(value, bool):
            new_params[key] = "true" if value else "false"
    return new_params


class WeiboClient(object):
    """
    weibo client base 
    """
    base = "https://api.weibo.com/2/"

    def __init__(self, access_token):
        """
        """
        self.access_token = access_token
        self.session = requests.Session()
        self.session.headers.update({"Authorization": "OAuth2 " + access_token})

    def request(self, method, suffix, params=None, data=None, files=None):
        """
        request weibo api 
        :param suffix: str,
        :param method: str,http method: GET,POST,PUT.etc
        :param params: dict, url query parameters 
        :param data: dict, 
        :return: 
        """
        url = self.base + suffix

        params = filter_params(params)

        response = self.session.request(method=method, url=url, params=params, data=data, files=files)
        json_obj = response.json()
        if isinstance(json_obj, dict) and json_obj.get("error_code"):
            # {
            #     "request": "/statuses/home_timeline.json",
            #     "error_code": "20502",
            #     "error": "Need you follow uid."
            # }

            raise WeiboAPIError(json_obj.get("request"), json_obj.get("error_code"), json_obj.get("error"))
        else:
            return json_obj
