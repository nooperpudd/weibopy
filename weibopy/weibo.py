# encoding:utf-8
import copy

import requests

from .exceptions import WeiboAPIError, WeiboRequestError


def filter_params(params):
    """
    convert dict value if value is bool type,
    False -> "false"
    True -> "true"
    """
    if params is not None:
        new_params = copy.deepcopy(params)
        new_params = dict((k, v) for k, v in new_params.items() if v is not None)
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

    def _handler_response(self, response, data=None):
        """
        error code response:
        {
            "request": "/statuses/home_timeline.json",
            "error_code": "20502",
            "error": "Need you follow uid."
        }
        :param response:
        :return:
        """
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, dict) and data.get("error_code"):

                raise WeiboAPIError(data.get("request"), data.get("error_code"), data.get("error"))
            else:
                return data
        else:
            raise WeiboRequestError(
                "Weibo API request error: status code: {code} url:{url} ->"
                " method:{method}: data={data}".format(
                    code=response.status_code,
                    url=response.url,
                    method=response.request.method,
                    data=data
                )
            )

    def get(self, suffix, params=None):
        """
        request weibo api
        :param suffix: str,
        :param params: dict, url query parameters
        :return:

        """

        url = self.base + suffix
        params = filter_params(params)

        response = self.session.get(url=url, params=params)

        return self._handler_response(response)

    def post(self, suffix, params=None, data=None, files=None):
        """
        :return:
        """

        url = self.base + suffix
        params = filter_params(params)

        response = self.session.post(url=url, params=params, data=data, files=files)

        return self._handler_response(response, data=data)
