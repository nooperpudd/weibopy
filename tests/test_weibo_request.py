import json
import unittest

import httpretty

from weibopy import WeiboClient, WeiboAPIError


@httpretty.activate
class WeiboRequestTestCase(unittest.TestCase):
    """
    """

    def setUp(self):
        """
        :return:
        """
        self.token = "1qaz3edc"
        self.client = WeiboClient(self.token)

    def test_weibo_request(self):
        """
        :return:
        """

        body = """
        {"next_cursor": 4098746105417334, "hasvisible": false, "uve_blank": -1, "statuses": ["4098748692646689",
        "4098748689403910", "4098748688918202", "4098747640117551", "4098747434341769", "4098747430814353",
        "4098747430145399", "4098747052681634", "4098746357066702", "4098746322855226", "4098746297959121",
        "4098746251989195", "4098746226771596", "4098746205413046", "4098746180805829", "4098746175979920",
         "4098746172045575", "4098746172045403", "4098746160243131", "4098746139219122"], "ad": [],
         "advertises": [], "interval": 0, "previous_cursor": 0, "total_number": 1322}
        """
        httpretty.register_uri(httpretty.GET, "https://api.weibo.com/2/statuses/friends_timeline/ids.json",
                               body=body,
                               status=200,
                               content_type='text/json')

        self.assertDictEqual(self.client.get("statuses/friends_timeline/ids.json"), json.loads(body))

    def test_weibo_post(self):
        """
        :return:
        """
        body = """
              {
          "attitudes_count": 0,
          "biz_feature": 0,
          "comments_count": 0,
          "created_at": "Thu Apr 20 23:18:30 +0800 2017",
          "darwin_tags": [],
          "favorited": false,
          "geo": null,
          "gif_ids": null,
          "hasActionTypeCard": 0,
          "hot_weibo_tags": [],
          "id": 4098749565013950,
          "idstr": "4098749565013950",
          "in_reply_to_screen_name": "",
          "in_reply_to_status_id": "",
          "in_reply_to_user_id": "",
          "isLongText": false,
          "is_show_bulletin": 2,
          "mid": "4098749565013950",
          "mlevel": 0,
          "pic_urls": [],
          "positive_recom_flag": 0,
          "reposts_count": 0,
          "source": "<a href='http://open.weibo.com' rel='nofollow'>app</a>",
          "source_allowclick": 0,
          "source_type": 1,
          "text": "haha",
          "textLength": 4,
          "text_tag_tips": [],
          "truncated": false,
          "user": {
            "allow_all_act_msg": false,
            "allow_all_comment": true,
            "avatar_hd": "http://tva4.sinaimg.cn/crop.320.120.960.960.1024/70669a5djw1eanuztfpewj218g0xcn9c.jpg",
            "avatar_large": "http://tva4.sinaimg.cn/crop.320.120.960.960.180/70669a5djw1eanuztfpewj218g0xcn9c.jpg",
            "bi_followers_count": 9,
            "block_app": 0,
            "block_word": 0,
            "city": "2",
            "class": 1,
            "created_at": "Tue Dec 07 21:44:06 +0800 2010",
            "credit_score": 80,
            "description": "",
            "domain": "nooper",
            "favourites_count": 3,
            "follow_me": false,
            "followers_count": 48,
            "following": false,
            "friends_count": 140,
            "gender": "m",
            "geo_enabled": true,
            "id": 1885772381,
            "idstr": "1885772381",
            "insecurity": {
              "sexual_content": false
            },
            "lang": "zh-cn",
            "online_status": 0,
            "pagefriends_count": 0,
            "profile_image_url": "http://tva4.sinaimg.cn/crop.320.120.960.960.50/70669a5djw1eanuztfpewj218g0xcn9c.jpg",
            "profile_url": "nooper",
            "province": "11",
            "ptype": 0,
            "remark": "",
            "screen_name": "nooper",
            "star": 0,
            "statuses_count": 168,
            "urank": 13,
            "url": "",
            "user_ability": 0,
            "verified": false,
            "verified_reason": "",
            "verified_reason_url": "",
            "verified_source": "",
            "verified_source_url": "",
            "verified_trade": "",
            "verified_type": -1,
            "weihao": ""
          },
          "userType": 590081,
          "visible": {
            "list_id": 0,
            "type": 0
          }
        }
        """
        httpretty.register_uri(httpretty.POST, "https://api.weibo.com/2/statuses/update.json",
                               body=body,
                               status=200,
                               content_type='text/json')

        self.assertDictEqual(self.client.post("statuses/update.json"), json.loads(body))

    def test_weibo_api_error(self):
        """
        :return:
        """
        body = """
                {
                        "request": "/statuses/home_timeline.json",
                        "error_code": "20502",
                        "error": "Need you follow uid."
                }
                """
        httpretty.register_uri(httpretty.GET, "https://api.weibo.com/2/statuses/home_timeline.json",
                               body=body,
                               status=200,
                               content_type='text/json')

        self.assertRaises(WeiboAPIError, self.client.get, "statuses/home_timeline.json")
