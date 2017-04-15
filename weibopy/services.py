# encoding:utf-8
from urllib.parse import urlencode

from .weibo import WeiboClient


class Services(WeiboClient):
    """
    weibo other info services
    """

    def search_topics(self, **kwargs):
        """
        访问级别：高级接口（需要授权）
        频次限制：是
        搜索某一话题下的微博
        
        request params:
                必选	    类型及范围	说明
        q	    true	string	    搜索的话题关键字，必须进行URLencode，utf-8编码。
        count	false	int	        单页返回的记录条数，默认为10，最大为50。
        page	false	int	        返回结果的页码，默认为1。
        
        注意事项
    
            关键词只能为两#间的话题，即只能搜索某话题下的微博
            只返回最新200条结果
            
        
        返回字段说明
        
        返回值字段	            字段类型	    字段说明
        created_at	            string	    微博创建时间
        id	                    int64	    微博ID
        mid	                    int64	    微博MID
        idstr	                string	    字符串型的微博ID
        text	                string	    微博信息内容
        source	                string	    微博来源
        favorited	            boolean	    是否已收藏，true：是，false：否
        truncated	            boolean	    是否被截断，true：是，false：否
        in_reply_to_status_id	string	    （暂未支持）回复ID
        in_reply_to_user_id	    string	    （暂未支持）回复人UID
        in_reply_to_screen_name	string	    （暂未支持）回复人昵称
        thumbnail_pic	        string	    缩略图片地址，没有时不返回此字段
        bmiddle_pic	            string	    中等尺寸图片地址，没有时不返回此字段
        original_pic	        string	    原始图片地址，没有时不返回此字段
        geo	                    object	    地理信息字段 详细
        user	                object	    微博作者的用户信息字段 详细
        retweeted_status	    object	    被转发的原微博信息字段，当该微博为转发微博时返回 详细
        reposts_count	        int	        转发数
        comments_count	        int	        评论数
        attitudes_count	        int	        表态数
        mlevel	                int	        暂未支持
        visible	                object	    微博的可见性及指定可见分组信息。该object中type取值，0：普通微博，1：私密微博，3：指定分组微博，4：密友微博；list_id为分组的组号
        pic_ids	                object	    微博配图ID。多图时返回多图ID，用来拼接图片url。用返回字段thumbnail_pic的地址配上该返回字段的图片ID，即可得到多个图片url。
        ad	                    object array	微博流内的推广微博ID
        
        
        {
            "statuses": [
                {
                    "created_at": "Fri Feb 24 15:18:31 +0800 2012",
                    "id": 3416614810943471,
                    "mid": "3416614810943471",
                    "idstr": "3416614810943471",
                    "text": "与大家分享我所喜爱的照片！#ABC晒新年# 。",
                    "source": "微活动</a>",
                    "favorited": false,
                    "truncated": false,
                    "in_reply_to_status_id": "",
                    "in_reply_to_user_id": "",
                    "in_reply_to_screen_name": "",
                    "thumbnail_pic": "http://ww3.sinaimg.cn/thumbnail/5f0eb04atw1dq4ir5bztkj.jpg",
                    "bmiddle_pic": "http://ww3.sinaimg.cn/bmiddle/5f0eb04atw1dq4ir5bztkj.jpg",
                    "original_pic": "http://ww3.sinaimg.cn/large/5f0eb04atw1dq4ir5bztkj.jpg",
                    "geo": null,
                    "user": {
                        "id": 1594798154,
                        "idstr": "1594798154",
                        "screen_name": "刘麦",
                        "name": "刘麦",
                        "province": "34",
                        "city": "16",
                        "location": "安徽 亳州",
                        "description": "新一代世界小童星。",
                        "url": "http://blog.sina.com.cn/liumaiduo",
                        "profile_image_url": "http://tp3.sinaimg.cn/1594798154/50/5614782838/1",
                        "profile_url": "liumaiduo",
                        "domain": "liumaiduo",
                        "weihao": "",
                        "gender": "m",
                        "followers_count": 314,
                        "friends_count": 555,
                        "statuses_count": 1913,
                        "favourites_count": 1,
                        "created_at": "Sat Jun 11 00:00:00 +0800 2011",
                        "following": false,
                        "allow_all_act_msg": false,
                        "geo_enabled": true,
                        "verified": false,
                        "verified_type": -1,
                        "allow_all_comment": false,
                        "avatar_large": "http://tp3.sinaimg.cn/1594798154/180/5614782838/1",
                        "verified_reason": "",
                        "follow_me": false,
                        "online_status": 1,
                        "bi_followers_count": 290,
                        "lang": "zh-cn"
                    },
                    "annotations": [...],
                    "reposts_count": 0,
                    "comments_count": 0,
                    "mlevel": 0,
                    "visible": {
                        "type": 0,
                        "list_id": 0
                    }
                },
                ...
            ],
            "total_number": 2543821
        }
        
        :param kwargs: 
        :return: 
        """
        return self.request("get", "search/topics.json", params=kwargs)

    def short_url_shorten(self, urls):
        """
        访问级别：普通接口
        频次限制：是
        将一个或多个长链接转换成短链接
        
        :param urls: list, 最多不超过20个
                
        :return:
        
        返回值字段	字段类型	字段说明
        url_short	string	短链接
        url_long	string	原始长链接
        type	    int	    链接的类型，0：普通网页、1：视频、2：音乐、3：活动、5、投票
        result	    boolean	短链的可用状态，true：可用、false：不可用。
        
       
        :return: 
        {
            "urls": [
                {
                    "url_short": "http://t.cn/h4DwT1",
                    "url_long": "http://finance.sina.com.cn/",
                    "type": 0,
                    "result": "true"
                },
                {
                    "url_short": "",
                    "url_long": "http://finance.sina.com.cn/",
                    "type": 0,
                    "result": "false"
                },
                ...
            ]
        }
        
        """
        group_urls = [("url_long", url) for url in urls]
        suffix = "short_url/shorten.json?{0}".format(urlencode(group_urls))
        return self.request("get", suffix, params={})

    def short_url_expand(self, urls):
        """
        访问级别：普通接口
        频次限制：是
        短链转长链
        
        返回字段说明
        返回值字段	字段类型	字段说明
        url_short	string	短链接
        url_long	string	原始长链接
        type	    int	    链接的类型，0：普通网页、1：视频、2：音乐、3：活动、5、投票
        result	    boolean	短链的可用状态，true：可用、false：不可用。

        :param urls: 最多不超过20个。 
        :return: 
        
        {
            "urls": [
                {
                    "url_short": "http://t.cn/h4DwT1",
                    "url_long": "http://finance.sina.com.cn/",
                    "type": 0,
                    "result": "true"
                },
                {
                    "url_short": "http://t.cn/h4DwT1",
                    "url_long": "",
                    "type": 0,
                    "result": "false"
                },
                ...
            ]
        }
        
        """
        group_urls = [("url_short", url) for url in urls]
        suffix = "short_url/expand.json?{0}".format(urlencode(group_urls))
        return self.request("get", suffix, params={})

    def short_url_share_counts(self, urls):
        """
        访问级别：普通接口
        频次限制：是
        获取短链接在微博上的微博分享数
        :param urls: 最多不超过20个。
        :return: 
                    {
                        "urls": [
                            {
                                "url_short": "http://t.cn/h4DwT1",
                                "url_long": "http://finance.sina.com.cn/",
                                "share_counts": "108"
                            },
                            ...
                        ]
                    }
        """
        group_urls = [("url_short", url) for url in urls]

        suffix = "short_url/share/counts.json?{0}".format(urlencode(group_urls))

        return self.request("get", suffix, params={})

    def short_url_comment_counts(self, urls):
        """
        访问级别：普通接口
        频次限制：是
        获取短链接在微博上的微博评论数
        :param urls: 最多不超过20个。
        :return: 
        
        {
            "urls": [
                {
                    "url_short": "http://t.cn/h4DwT1",
                    "url_long": "http://finance.sina.com.cn/",
                    "comment_counts": "108"
                },
                ...
            ]
        }
        
        """
        group_urls = [("url_short", url) for url in urls]

        suffix = "short_url/comment/counts.json?{0}".format(urlencode(group_urls))
        return self.request("get", suffix, params={})

    def get_timezone(self, **kwargs):
        """
        
        访问级别：普通接口
        频次限制：是
        获取时区配置表
        
        request params:
        
                        必选	    类型及范围	说明
        access_token	true	string	    采用OAuth授权方式为必填参数，OAuth授权后获得。
        language	    false	string	    返回的语言版本，zh-cn：简体中文、zh-tw：繁体中文、english：英文，默认为zh-cn。
            
        :return:
            {
                "268": "(GMT+08:00) 中国时间 - 北京",
                ...
            }
        
        """
        return self.request("get", "common/get_timezone.json", params=kwargs)

    def get_country(self, **kwargs):
        """
        
        访问级别：普通接口
        频次限制：是
        
        获取国家列表
        
        request params:
        
         	        必选	    类型及范围	说明
        province	true	string	    省份的省份代码。
        capital	    false	string	    城市的首字母，a-z，可为空代表返回全部，默认为全部。
        language	false	string	    返回的语言版本，zh-cn：简体中文、zh-tw：繁体中文、english：英文，默认为zh-cn。
        
        :return: [
                    {
                        "001011001": "东城"
                    },
                    ...
                ]

        """
        return self.request("get", "common/get_city.json", params=kwargs)

    def get_province(self, **kwargs):
        """
        
        访问级别：普通接口
        频次限制：是
        获取省份列表
        
        request params:
        
        	            必选	    类型及范围	说明
        country	        true	string	    国家的国家代码。
        capital	        false	string	    省份的首字母，a-z，可为空代表返回全部，默认为全部。
        language	    false	string	    返回的语言版本，zh-cn：简体中文、zh-tw：繁体中文、english：英文，默认为zh-cn。
        
        :return: [
                    {
                        "001011": "北京"
                    },
                    ...
                ]
        """
        return self.request("get", "common/get_province.json", params=kwargs)

    def code_to_location(self, **kwargs):
        """
        
        访问级别：普通接口
        频次限制：是
        通过地址编码获取地址名称
        
        request params:
                必选	    类型及范围	说明
        codes	true	string	    需要查询的地址编码，多个之间用逗号分隔。
  
        :return: [
                    {
                        "100": "卡塔尔"
                    },
                    ...
                ]
        """
        return self.request("get", "common/code_to_location.json", params=kwargs)

    def get_city(self, **kwargs):
        """
        访问级别：普通接口
        频次限制：是
        获取城市列表
        
        request params:
        
         	        必选	    类型及范围	说明
        province	true	string	    省份的省份代码。
        capital	    false	string	    城市的首字母，a-z，可为空代表返回全部，默认为全部。
        language	false	string	    返回的语言版本，zh-cn：简体中文、zh-tw：繁体中文、english：英文，默认为zh-cn。
        
        :return: [
                    {
                        "001011001": "东城"
                    },
                    ...
                ]
        """
        return self.request("get", "common/get_city.json", params=kwargs)

    def rate_limit_status(self):
        """
        
        访问级别：普通接口
        频次限制：否
        
        获取当前授权用户API访问频率限制
        
        :return: 
        {
            "ip_limit": 10000,
            "limit_time_unit": "HOURS",
            "remaining_ip_hits": 10000,
            "remaining_user_hits": 150,
            "reset_time": "2011-06-03 18:00:00",
            "reset_time_in_seconds": 1415,
            "user_limit": 150,
        }
       
        """
        return self.request("get", "account/rate_limit_status.json", params={})

    def get_uid(self):
        """
        访问级别：普通接口
        频次限制：否
        
        授权之后获取用户的UID
        :return:
        {
            "uid":"3456676543"
        }

        """
        return self.request("get", "account/get_uid.json", params={})

    def profile_email(self):
        """
        访问级别：高级接口（需要授权）
        频次限制：是
        
        授权之后获取用户的联系邮箱
       
        :return: 
        [
            {
                "email": "weibo_api_tech@sina.com"
            }
        ]
      
        """
        return self.request("get", "account/profile/email.json", params={})
