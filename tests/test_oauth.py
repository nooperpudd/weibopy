# encoding:utf-8
import json
import unittest
from urllib import parse

import httpretty

from weibopy import WeiboOauth2, WeiboOauth2Error


@httpretty.activate
class Oauth2TestCase(unittest.TestCase):
    """
    """

    def setUp(self):
        self.access_token = "xxxxxx"
        self.client_id = "2802433140"
        self.client_secret = "987654321"
        self.redirect_url = "http://45.32.105.118:8000/weibo"
        self.oauth2_client = WeiboOauth2(client_id=self.client_id,
                                         client_secret=self.client_secret,
                                         redirect_url=self.redirect_url, force_login=False)

    def test_authorize_url(self):
        """
        :return:
        """
        request_params = {
            'client_id': self.client_id,
            'redirect_uri': self.redirect_url,
            "display": "default",
            "forcelogin": "false"
        }

        parse_result = parse.urlparse(self.oauth2_client.authorize_url)
        query_params = dict(parse.parse_qsl(parse_result.query))

        self.assertEqual(parse_result.hostname, "api.weibo.com")
        self.assertEqual(parse_result.path, "/oauth2/authorize")

        self.assertDictEqual(query_params, request_params)

    def test_authorize_url_mobile(self):
        """
        :return:
        """
        oauth2_client = WeiboOauth2(client_id=self.client_id,
                                    client_secret=self.client_secret,
                                    redirect_url=self.redirect_url, display="mobile")

        parse_result = parse.urlparse(oauth2_client.authorize_url)
        self.assertEqual(parse_result.hostname, "open.weibo.cn")

    def test_auth_access(self):
        """
        :return:
        """
        body = """
           {
               "access_token": "ACCESS_TOKEN",
               "expires_in": 1234,
               "remind_in":"798114",
               "uid":"12341234"
         }
        """
        httpretty.register_uri(httpretty.POST, "https://api.weibo.com/oauth2/",
                               body=body,
                               status=200,
                               content_type='text/json')
        response = self.oauth2_client.auth_access("abcde")

        self.assertDictEqual(response, json.loads(body))

    def test_revoke_auth_access(self):
        """
        :return:
        """
        body = "{'result':true}"
        httpretty.register_uri(httpretty.POST, "https://api.weibo.com/oauth2/revokeoauth2",
                               body=body,
                               status=200,
                               content_type='text/json')

        response = self.oauth2_client.revoke_auth_access(self.access_token)
        self.assertTrue(response)

    def test_refresh_token(self):
        """
        :return:
        """
        body = """
         {
            "access_token": "SlAV32hkKG",
            "expires_in": 3600
        }
        """
        httpretty.register_uri(httpretty.POST, "https://api.weibo.com/oauth2/access_token",
                               body=body,
                               status=200,
                               content_type='text/json')

        response = self.oauth2_client.refresh_token("xxxxxxxx")
        self.assertTrue(response, json.loads(body))

    def test_get_token_info(self):
        """
        :return:
        """
        body = """
          {
           "uid": 1073880650,
           "appkey": 1352222456,
           "scope": null,
           "create_at": 1352267591,
           "expire_in": 157679471
         }
        """
        httpretty.register_uri(httpretty.GET, "https://api.weibo.com/oauth2/get_token_info",
                               body=body,
                               status=200,
                               content_type='text/json')

        response = self.oauth2_client.get_token_info(self.access_token)

        self.assertDictEqual(response, json.loads(body))

    def test_assert_api_error(self):
        """
        :return:
        """
        body = """
        {
                "error": "unsupported_response_type",
                "error_code": 21329,
                "error_description": "不支持的ResponseType."
            }
        """

        httpretty.register_uri(httpretty.POST, "https://api.weibo.com/oauth2/get_token_info",
                               body=body,
                               status=200,
                               content_type='text/json')

        self.assertRaises(WeiboOauth2Error, self.oauth2_client.get_token_info("bdssds"))
