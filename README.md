# Weibopy 

Weibopy is a weibo python3 sdk, support Python3 with requests packages.

[Weibo API doc](http://open.weibo.com/wiki/SDK)

## Install
Normal support Python3 version.

    pip3 install weibopy
    
## Prepare

1. First, need to register the weibo developer account, and build an app based  
   [Weibo Platform] (http://open.weibo.com/index.php).
2. Now we can get the `App Key` and `App Secret` in the weibo app info page.
3. Set the callback url in the weibo app settings.
4. Token authorization. 


```Python

from weibopy import WeiboOauth2

client_id="xxx",
client_secret="xxx"
redirect_url="http://"
client = WeiboOauth2(client_id,client_secret,redirect_url)

authorize_url = client.authorize_url

# 'https://api.weibo.com/oauth2/authorize?redirect_uri=http%3A%2F%2F127.0.0.1%2Fcallback&client_id=123456'
```

5. Open the authorize url in the browser, and send the code to get access token.

```Python

client.auth_access(auth_code)

{
   "access_token": "ACCESS_TOKEN",
   "expires_in": 1234,
    "remind_in":"798114",
    "uid":"12341234"
}


```

6. If the token is expired, we need to use `refresh_token` to get the access token.
 
**Note**: This refresh only provide official mobile app. 

## Usage

If we got the the `access_token`, now we can call api functions.

All the modules separated as the parts of the weibo api client to handler data .

    WeiboOauth2         # weibo Oauth2 authentication
    WeiboClient         # weibo Client API 
    WeiboAPIError       # weibo api error
    WeiboOauth2Error    # weibo oath2 error
    
If we want to get the public tweets in recently hours.

```python
from weibopy import WeiboClient

access_token = ""
client = WeiboClient(access_token)


result =client.get(suffix="statuses/public_timeline.json")


{
    "statuses": [{
                    "created_at": "Tue May 31 17:46:55 +0800 2011",
                    "id": 11488058246,
                    "text": "求关注。",
                    "source": "<a href='http://weibo.com' rel='nofollow'>新浪微博</a>",
                    "favorited": False,
                    "truncated": False,
                    "in_reply_to_status_id": "",
                    "in_reply_to_user_id": "",
                    "in_reply_to_screen_name": "",
                    "geo": None,
                    "mid": "5612814510546515491",
                    "reposts_count": 8,
                    "comments_count": 9,
                    "annotations": [],
                    "user": {
                        "id": 1404376560,
                        "screen_name": "zaku",
                        "name": "zaku",
                        "province": "11",
                        "city": "5",
                        "location": "北京 朝阳区",
                        "description": "人生五十年，乃如梦如幻；有生斯有死，壮士复何憾。",
                        "url": "http://blog.sina.com.cn/zaku",
                        "profile_image_url": "http://tp1.sinaimg.cn/1404376560/50/0/1",
                        "domain": "zaku",
                        "gender": "m",
                        "followers_count": 1204,
                        "friends_count": 447,
                        "statuses_count": 2908,
                        "favourites_count": 0,
                        "created_at": "Fri Aug 28 00:00:00 +0800 2009",
                        "following": False,
                        "allow_all_act_msg": False,
                        "remark": "",
                        "geo_enabled": False,
                        "verified": False,
                        "allow_all_comment": False,
                        "avatar_large": "http://tp1.sinaimg.cn/1404376560/180/0/1",
                        "verified_reason": "",
                        "follow_me": False,
                        "online_status": 0,
                        "bi_followers_count": 215
                    }
                },
                
            ],
            "previous_cursor": 0,
            "next_cursor": 11488013766,
            "total_number": 81655
        }
```

How to post a tweet with a picture?

```python

from weibopy import WeiboClient

access_token = ""
client = WeiboClient(access_token)

files = {'pic': open('a.png', 'rb')}
client.post("statuses/upload.json", data={"status":"nihao"}, files=files)
```
result:

     'biz_feature': 0,
     'bmiddle_pic': 'http://wx1.sinaimg.cn/bmiddle/70669a5dly1fescai5ggkj20gf0feq7e.jpg',
     'comments_count': 0,
     'created_at': 'Wed Apr 19 22:06:20 +0800 2017',
     'darwin_tags': [],
     'favorited': False,
     'geo': None,
     'gif_ids': None,
     'hasActionTypeCard': 0,
     'hot_weibo_tags': [],
     'id': 4098369015668443,
     'idstr': '4098369015668443',
     'in_reply_to_screen_name': '',
     'in_reply_to_status_id': '',
     'in_reply_to_user_id': '',
     'isLongText': False,
     'is_show_bulletin': 2,
     'mid': '4098369015668443',
     'mlevel': 0,
     'original_pic': 'http://wx1.sinaimg.cn/large/70669a5dly1fescai5ggkj20gf0feq7e.jpg',
     'pic_urls': [{'thumbnail_pic': 'http://wx1.sinaimg.cn/thumbnail/70669a5dly1fescai5ggkj20gf0feq7e.jpg'}],
     'positive_recom_flag': 0,
     'reposts_count': 0,
     'source': '<a href="http://open.weibo.com" rel="nofollow">未通过审核应用</a>',
     'source_allowclick': 0,
     'source_type': 1,
     'text': 'hhha \u200b',
     'textLength': 4,
     'text_tag_tips': [],
     'thumbnail_pic': 'http://wx1.sinaimg.cn/thumbnail/70669a5dly1fescai5ggkj20gf0feq7e.jpg',
     'truncated': False,
     'user': {'allow_all_act_msg': False,
              'allow_all_comment': True,
              'avatar_hd': 'http://tva4.sinaimg.cn/crop.320.120.960.960.1024/70669a5djw1eanuztfpewj218g0xcn9c.jpg',
              'avatar_large': 'http://tva4.sinaimg.cn/crop.320.120.960.960.180/70669a5djw1eanuztfpewj218g0xcn9c.jpg',
              'bi_followers_count': 9,
              'block_app': 0,
              'block_word': 0,
              'city': '2',
              'class': 1,
              'created_at': 'Tue Dec 07 21:44:06 +0800 2010',
              'credit_score': 80,
              'description': '',
              'domain': 'nooper',
              'favourites_count': 3,
              'follow_me': False,
              'followers_count': 48,
              'following': False,
              'friends_count': 140,
              'gender': 'm',
              'geo_enabled': True,
              'id': 1885772381,
              'idstr': '1885772381',
              'insecurity': {'sexual_content': False},
              'lang': 'zh-cn',
              'location': '北京 西城区',
              'mbrank': 0,
              'mbtype': 0,
              'name': '王小小小小小莫',
              'online_status': 0,
              'pagefriends_count': 0,
              'profile_image_url': 'http://tva4.sinaimg.cn/crop.320.120.960.960.50/70669a5djw1eanuztfpewj218g0xcn9c.jpg',
              'profile_url': 'nooper',
              'province': '11',
              'ptype': 0,
              'remark': '',
              'screen_name': '王小小小小小莫',
              'star': 0,
              'statuses_count': 168,
              'urank': 13,
              'url': '',
              'user_ability': 0,
              'verified': False,
              'verified_reason': '',
              'verified_reason_url': '',
              'verified_source': '',
              'verified_source_url': '',
              'verified_trade': '',
              'verified_type': -1,
              'weihao': ''},
     'userType': 590081,
     'visible': {'list_id': 0, 'type': 0}}
    
 

## Contact

If you have any question about the weibo API, contact 365504029@qq.com


