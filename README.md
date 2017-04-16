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

    WeiboOauth2         # weibo Oauth2 
    WeiboComment        # weibo comment
    WeiboAPIError       # weibo api error
    WeiboOauth2Error    # weibo oath2 error
    WeiboRelation       # weibo friends relation
    WeiboServices       # weibo other services
    WeiboTweet          # weibo tweet 
    WeiboUser           # weibo user info
    WeiboQRCode         # weibo QR code

If we want to get the public tweets in recently hours.

```python
from weibopy import WeiboTweet

access_token = ""
tweet = WeiboTweet(access_token)


result =tweet.public_timeline()


a= {
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

## Contact

If you have any question about the weibo API, contact 365504029@qq.com


