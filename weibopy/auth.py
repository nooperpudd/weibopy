# encoding:utf-8
from urllib.parse import urlencode

import requests


class WeiboAuth(object):
    """
    """
    site_url = "https://api.weibo.com/oauth2/"

    def __init__(self, client_id, client_secret, redirect_url, scope, state, display, language, force_login=False):
        """
        display:
            
        :param client_id: (required) str,
        :param client_secret: (required) str, 
        :param redirect_url: (required) str,
        :param scope: (optional) str,
        :param state: (optional) str,
        :param display:  (optional) str,  [default,mobile,wap,client,apponweibo]
        :param force_login: (optional) bool, default: false 
        :param language:  (optional) str
        """
        self.client_id = client_id
        self.redirect_url = redirect_url
        self.scope = scope
        self.state = state
        self.force_login = force_login
        self.display = display
        self.language = language
        self.client_secret = client_secret

    @property
    def authorize_url(self):
        """
        :return: 
        """
        auth_url = self.site_url + "authorize"

        params = {
            'client_id': self.client_id,
            'redirect_uri': self.redirect_url,
            "scope": self.scope,
            "state": self.state,
            "forcelogin": self.force_login,
            "language": self.language,
            "display": self.display
        }

        return "{auth_url}?{params}".format(auth_url=auth_url, params=urlencode(params))

    def auth_access(self, auth_code):
        """
        :return: 
        """
        access_url = self.site_url + "access_token"

        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'authorization_code',
            'code': auth_code,
            'redirect_uri': self.redirect_url
        }
        response = requests.post(access_url, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            # todo
            pass

    def get_token_info(self, access_token):
        """
        
         {
           "uid": 1073880650,
           "appkey": 1352222456,
           "scope": null,
           "create_at": 1352267591,
           "expire_in": 157679471
         }
        :param access_token: 
        :return: 
        """
        token_url = self.site_url + "get_token_info"
        data = {
            "access_token": access_token
        }
        response = requests.post(token_url, data=data)

        if response.status_code == 200:
            return response.json()
        else:
            # todo
            pass

    def revoke_auth_access(self, access_token):
        """
        :param access_token: 
        :return: bool
        """
        revoke_url = self.site_url + "revokeoauth2"

        data = {
            "access_token": access_token
        }
        response = requests.post(revoke_url, data=data)

        if response.status_code == 200:
            result = response.json()
            return result["result"]
        else:
            # todo
            pass

    def refresh_token(self, refresh_token):
        """
        :param refresh_token: 
        :return: 
        """
        access_url = self.site_url + "access_token"

        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "refresh_token",
            "redirect_url": self.redirect_url,
            "refresh_token": refresh_token
        }
        response = requests.post(access_url, data=data)

        if response.status_code == 200:
            return response.json()
        else:
            # todo
            pass
