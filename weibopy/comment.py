# encoding:utf-8
from .weibo import WeiboClient


class WeiboComments(WeiboClient):
    """
    """

    def show(self, **kwargs):
        """
        访问级别：普通接口
        频次限制：是
        获取某条微博的评论列表
            
        	            必选	    类型及范围	说明
        id	            true	int64	需要查询的微博ID。
        since_id	    false	int64	若指定此参数，则返回ID比since_id大的评论（即比since_id时间晚的评论），默认为0。
        max_id	        false	int64	若指定此参数，则返回ID小于或等于max_id的评论，默认为0。
        count	        false	int	    单页返回的记录条数，默认为50。
        page	        false	int	    返回结果的页码，默认为1。
        filter_by_author	false	int	作者筛选类型，0：全部、1：我关注的人、2：陌生人，默认为0。
        
        
        返回字段说明
        返回值字段	字段类型	字段说明
        created_at	string	评论创建时间
        id	int64	评论的ID
        text	string	评论的内容
        source	string	评论的来源
        user	object	评论作者的用户信息字段 详细
        mid	string	评论的MID
        idstr	string	字符串型的评论ID
        status	object	评论的微博信息字段 详细
        reply_comment	object	评论来源评论，当本评论属于对另一评论的回复时返回此字段
          
        :return: 
        
          {
            "comments": [
                {
                    "created_at": "Wed Jun 01 00:50:25 +0800 2011",
                    "id": 12438492184,
                    "text": "love your work.......",
                    "source": "<a href="http://weibo.com" rel="nofollow">新浪微博</a>",
                    "mid": "202110601896455629",
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
                        "following": false,
                        "allow_all_act_msg": false,
                        "remark": "",
                        "geo_enabled": true,
                        "verified": false,
                        "allow_all_comment": true,
                        "avatar_large": "http://tp1.sinaimg.cn/1404376560/180/0/1",
                        "verified_reason": "",
                        "follow_me": false,
                        "online_status": 0,
                        "bi_followers_count": 215
                    },
                    "status": {
                        "created_at": "Tue May 31 17:46:55 +0800 2011",
                        "id": 11488058246,
                        "text": "求关注。"，
                        "source": "<a href="http://weibo.com" rel="nofollow">新浪微博</a>",
                        "favorited": false,
                        "truncated": false,
                        "in_reply_to_status_id": "",
                        "in_reply_to_user_id": "",
                        "in_reply_to_screen_name": "",
                        "geo": null,
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
                            "following": false,
                            "allow_all_act_msg": false,
                            "remark": "",
                            "geo_enabled": true,
                            "verified": false,
                            "allow_all_comment": true,
                            "avatar_large": "http://tp1.sinaimg.cn/1404376560/180/0/1",
                            "verified_reason": "",
                            "follow_me": false,
                            "online_status": 0,
                            "bi_followers_count": 215
                        }
                    }
                },
                ...
            ],
            "previous_cursor": 0,
            "next_cursor": 0,
            "total_number": 7
        }
        """
        return self.request("get", "comments/show.json", params=kwargs)

    def by_me(self, **kwargs):
        """
        访问级别：普通接口
        频次限制：是
        获取当前登录用户所发出的评论列表
        
        请求参数
 	    必选	类型及范围	说明
        access_token	true	string	采用OAuth授权方式为必填参数，OAuth授权后获得。
        since_id	false	int64	若指定此参数，则返回ID比since_id大的评论（即比since_id时间晚的评论），默认为0。
        max_id	false	int64	若指定此参数，则返回ID小于或等于max_id的评论，默认为0。
        count	false	int	单页返回的记录条数，默认为50。
        page	false	int	返回结果的页码，默认为1。
        filter_by_source	false	int	来源筛选类型，0：全部、1：来自微博的评论、2：来自微群的评论，默认为0。
        
        
        返回字段说明
        返回值字段	字段类型	字段说明
        created_at	string	评论创建时间
        id	int64	评论的ID
        text	string	评论的内容
        source	string	评论的来源
        user	object	评论作者的用户信息字段 详细
        mid	string	评论的MID
        idstr	string	字符串型的评论ID
        status	object	评论的微博信息字段 详细
        reply_comment	object	评论来源评论，当本评论属于对另一评论的回复时返回此字段
        
        
        
        
        :param kwargs: 
        :return: 
        {
            "comments": [
                {
                    "created_at": "Wed Jun 01 00:50:25 +0800 2011",
                    "id": 12438492184,
                    "text": "love your work.......",
                    "source": "<a href="http://weibo.com" rel="nofollow">新浪微博</a>",
                    "mid": "202110601896455629",
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
                        "following": false,
                        "allow_all_act_msg": false,
                        "remark": "",
                        "geo_enabled": true,
                        "verified": false,
                        "allow_all_comment": true,
                        "avatar_large": "http://tp1.sinaimg.cn/1404376560/180/0/1",
                        "verified_reason": "",
                        "follow_me": false,
                        "online_status": 0,
                        "bi_followers_count": 215
                    },
                    "status": {
                        "created_at": "Tue May 31 17:46:55 +0800 2011",
                        "id": 11488058246,
                        "text": "求关注。"，
                        "source": "<a href="http://weibo.com" rel="nofollow">新浪微博</a>",
                        "favorited": false,
                        "truncated": false,
                        "in_reply_to_status_id": "",
                        "in_reply_to_user_id": "",
                        "in_reply_to_screen_name": "",
                        "geo": null,
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
                            "following": false,
                            "allow_all_act_msg": false,
                            "remark": "",
                            "geo_enabled": true,
                            "verified": false,
                            "allow_all_comment": true,
                            "avatar_large": "http://tp1.sinaimg.cn/1404376560/180/0/1",
                            "verified_reason": "",
                            "follow_me": false,
                            "online_status": 0,
                            "bi_followers_count": 215
                        }
                    }
                },
                ...
            ],
            "previous_cursor": 0,
            "next_cursor": 0,
            "total_number": 7
        }
        
        """
        return self.request("get", "comments/by_me.json", params=kwargs)

    def to_me(self, **kwargs):
        """
        访问级别：普通接口
        频次限制：是
        获取当前登录用户所接收到的评论列表
        
        只返回授权用户的评论，非授权用户的评论将不返回；
        使用官方移动SDK调用，可多返回30%的非授权用户的评论；
        
        请求参数
                        必选	        类型及范围	    说明
        access_token	true	    string	    采用OAuth授权方式为必填参数，OAuth授权后获得。
        since_id	    false	    int64	    若指定此参数，则返回ID比since_id大的评论（即比since_id时间晚的评论），默认为0。
        max_id	        false	    int64	    若指定此参数，则返回ID小于或等于max_id的评论，默认为0。
        count	        false	    int	        单页返回的记录条数，默认为50。
        page	        false	    int	        返回结果的页码，默认为1。
        filter_by_author	false	int	    作者筛选类型，0：全部、1：我关注的人、2：陌生人，默认为0。
        filter_by_source	false	int	    来源筛选类型，0：全部、1：来自微博的评论、2：来自微群的评论，默认为0。

        返回字段说明
        返回值字段	字段类型	字段说明
        created_at	string	评论创建时间
        id	        int64	评论的ID
        text	    string	评论的内容
        source	    string	评论的来源
        user	    object	评论作者的用户信息字段 详细
        mid	        string	评论的MID
        idstr	    string	字符串型的评论ID
        status	    object	评论的微博信息字段 详细
        reply_comment	object	评论来源评论，当本评论属于对另一评论的回复时返回此字段
        
        :param kwargs: 
        :return: 
        {
            "comments": [
                {
                    "created_at": "Wed Jun 01 00:50:25 +0800 2011",
                    "id": 12438492184,
                    "text": "love your work.......",
                    "source": "<a href="http://weibo.com" rel="nofollow">新浪微博</a>",
                    "mid": "202110601896455629",
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
                        "following": false,
                        "allow_all_act_msg": false,
                        "remark": "",
                        "geo_enabled": true,
                        "verified": false,
                        "allow_all_comment": true,
                        "avatar_large": "http://tp1.sinaimg.cn/1404376560/180/0/1",
                        "verified_reason": "",
                        "follow_me": false,
                        "online_status": 0,
                        "bi_followers_count": 215
                    },
                    "status": {
                        "created_at": "Tue May 31 17:46:55 +0800 2011",
                        "id": 11488058246,
                        "text": "求关注。"，
                        "source": "<a href="http://weibo.com" rel="nofollow">新浪微博</a>",
                        "favorited": false,
                        "truncated": false,
                        "in_reply_to_status_id": "",
                        "in_reply_to_user_id": "",
                        "in_reply_to_screen_name": "",
                        "geo": null,
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
                            "following": false,
                            "allow_all_act_msg": false,
                            "remark": "",
                            "geo_enabled": true,
                            "verified": false,
                            "allow_all_comment": true,
                            "avatar_large": "http://tp1.sinaimg.cn/1404376560/180/0/1",
                            "verified_reason": "",
                            "follow_me": false,
                            "online_status": 0,
                            "bi_followers_count": 215
                        }
                    }
                },
                ...
            ],
            "previous_cursor": 0,
            "next_cursor": 0,
            "total_number": 7
        }
        """
        return self.request("get", "comments/to_me.json", params=kwargs)

    def timeline(self, **kwargs):
        """
        访问级别：普通接口
        频次限制：是
        
        录用户的最新评论包括接收到的与发出的
        
        请求参数
            必选	类型及范围	说明
        access_token	true	string	采用OAuth授权方式为必填参数，OAuth授权后获得。
        since_id	false	int64	若指定此参数，则返回ID比since_id大的评论（即比since_id时间晚的评论），默认为0。
        max_id	false	int64	若指定此参数，则返回ID小于或等于max_id的评论，默认为0。
        count	false	int	单页返回的记录条数，默认为50。
        page	false	int	返回结果的页码，默认为1。
        trim_user	false	int	返回值中user字段开关，0：返回完整user字段、1：user字段仅返回user_id，默认为0。
        
        
        获取用户发送及收到的评论列表
        
        返回字段说明
        返回值字段	字段类型	字段说明
        created_at	string	评论创建时间
        id	int64	评论的ID
        text	string	评论的内容
        source	string	评论的来源
        user	object	评论作者的用户信息字段 详细
        mid	string	评论的MID
        idstr	string	字符串型的评论ID
        status	object	评论的微博信息字段 详细
        reply_comment	object	评论来源评论，当本评论属于对另一评论的回复时返回此字段
        
        :param kwargs:
        :return: 
        
        {
            "comments": [
                {
                    "created_at": "Wed Jun 01 00:50:25 +0800 2011",
                    "id": 12438492184,
                    "text": "love your work.......",
                    "source": "<a href="http://weibo.com" rel="nofollow">新浪微博</a>",
                    "mid": "202110601896455629",
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
                        "following": false,
                        "allow_all_act_msg": false,
                        "remark": "",
                        "geo_enabled": true,
                        "verified": false,
                        "allow_all_comment": true,
                        "avatar_large": "http://tp1.sinaimg.cn/1404376560/180/0/1",
                        "verified_reason": "",
                        "follow_me": false,
                        "online_status": 0,
                        "bi_followers_count": 215
                    },
                    "status": {
                        "created_at": "Tue May 31 17:46:55 +0800 2011",
                        "id": 11488058246,
                        "text": "求关注。"，
                        "source": "<a href="http://weibo.com" rel="nofollow">新浪微博</a>",
                        "favorited": false,
                        "truncated": false,
                        "in_reply_to_status_id": "",
                        "in_reply_to_user_id": "",
                        "in_reply_to_screen_name": "",
                        "geo": null,
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
                            "following": false,
                            "allow_all_act_msg": false,
                            "remark": "",
                            "geo_enabled": true,
                            "verified": false,
                            "allow_all_comment": true,
                            "avatar_large": "http://tp1.sinaimg.cn/1404376560/180/0/1",
                            "verified_reason": "",
                            "follow_me": false,
                            "online_status": 0,
                            "bi_followers_count": 215
                        }
                    }
                },
                ...
            ],
            "previous_cursor": 0,
            "next_cursor": 0,
            "total_number": 7
        }
        
        """
        return self.request("get", "comments/timeline.json", params=kwargs)

    def mentions(self, **kwargs):
        """
        访问级别：普通接口
        频次限制：是
        获取@到我的评论
        
        请求参数
        必选	类型及范围	说明
        access_token	true	string	采用OAuth授权方式为必填参数，OAuth授权后获得。
        since_id	false	int64	若指定此参数，则返回ID比since_id大的评论（即比since_id时间晚的评论），默认为0。
        max_id	false	int64	若指定此参数，则返回ID小于或等于max_id的评论，默认为0。
        count	false	int	单页返回的记录条数，默认为50。
        page	false	int	返回结果的页码，默认为1。
        filter_by_author	false	int	作者筛选类型，0：全部、1：我关注的人、2：陌生人，默认为0。
        filter_by_source	false	int	来源筛选类型，0：全部、1：来自微博的评论、2：来自微群的评论，默认为0。
        
        
        返回字段说明
        返回值字段	字段类型	字段说明
        created_at	string	评论创建时间
        id	int64	评论的ID
        text	string	评论的内容
        source	string	评论的来源
        user	object	评论作者的用户信息字段 详细
        mid	string	评论的MID
        idstr	string	字符串型的评论ID
        status	object	评论的微博信息字段 详细
        reply_comment	object	评论来源评论，当本评论属于对另一评论的回复时返回此字段
        
        :param kwargs:
        :return: 
        
        {
            "comments": [
                {
                    "created_at": "Wed Jun 01 00:50:25 +0800 2011",
                    "id": 12438492184,
                    "text": "love your work.......",
                    "source": "<a href="http://weibo.com" rel="nofollow">新浪微博</a>",
                    "mid": "202110601896455629",
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
                        "following": false,
                        "allow_all_act_msg": false,
                        "remark": "",
                        "geo_enabled": true,
                        "verified": false,
                        "allow_all_comment": true,
                        "avatar_large": "http://tp1.sinaimg.cn/1404376560/180/0/1",
                        "verified_reason": "",
                        "follow_me": false,
                        "online_status": 0,
                        "bi_followers_count": 215
                    },
                    "status": {
                        "created_at": "Tue May 31 17:46:55 +0800 2011",
                        "id": 11488058246,
                        "text": "求关注。"，
                        "source": "<a href="http://weibo.com" rel="nofollow">新浪微博</a>",
                        "favorited": false,
                        "truncated": false,
                        "in_reply_to_status_id": "",
                        "in_reply_to_user_id": "",
                        "in_reply_to_screen_name": "",
                        "geo": null,
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
                            "following": false,
                            "allow_all_act_msg": false,
                            "remark": "",
                            "geo_enabled": true,
                            "verified": false,
                            "allow_all_comment": true,
                            "avatar_large": "http://tp1.sinaimg.cn/1404376560/180/0/1",
                            "verified_reason": "",
                            "follow_me": false,
                            "online_status": 0,
                            "bi_followers_count": 215
                        }
                    }
                },
                ...
            ],
            "previous_cursor": 0,
            "next_cursor": 0,
            "total_number": 7
        }
        """
        return self.request("get", "comments/mentions.json", params=kwargs)

    def show_batch(self, **kwargs):
        """
        
        访问级别：普通接口
        频次限制：是
        
        请求参数
                必选	    类型及范围	说明
        cids	true	int64	    需要查询的批量评论ID，用半角逗号分隔，最大50。
        
        
        返回字段说明
        返回值字段	字段类型	字段说明
        created_at	string	评论创建时间
        id	int64	评论的ID
        text	string	评论的内容
        source	string	评论的来源
        user	object	评论作者的用户信息字段 详细
        mid	string	评论的MID
        idstr	string	字符串型的评论ID
        status	object	评论的微博信息字段 详细
        reply_comment	object	评论来源评论，当本评论属于对另一评论的回复时返回此字段
        
        
        批量获取评论内容
        :param kwargs: 
        :return: 
        [
            {
                "created_at": "Wed Jun 01 00:50:25 +0800 2011",
                "id": 12438492184,
                "text": "love your work.......",
                "source": "<a href="http://weibo.com" rel="nofollow">新浪微博</a>",
                "mid": "202110601896455629",
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
                    "following": false,
                    "allow_all_act_msg": false,
                    "remark": "",
                    "geo_enabled": true,
                    "verified": false,
                    "allow_all_comment": true,
                    "avatar_large": "http://tp1.sinaimg.cn/1404376560/180/0/1",
                    "verified_reason": "",
                    "follow_me": false,
                    "online_status": 0,
                    "bi_followers_count": 215
                },
                "status": {
                    "created_at": "Tue May 31 17:46:55 +0800 2011",
                    "id": 11488058246,
                    "text": "求关注。"，
                    "source": "<a href="http://weibo.com" rel="nofollow">新浪微博</a>",
                    "favorited": false,
                    "truncated": false,
                    "in_reply_to_status_id": "",
                    "in_reply_to_user_id": "",
                    "in_reply_to_screen_name": "",
                    "geo": null,
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
                        "following": false,
                        "allow_all_act_msg": false,
                        "remark": "",
                        "geo_enabled": true,
                        "verified": false,
                        "allow_all_comment": true,
                        "avatar_large": "http://tp1.sinaimg.cn/1404376560/180/0/1",
                        "verified_reason": "",
                        "follow_me": false,
                        "online_status": 0,
                        "bi_followers_count": 215
                    }
                }
            },
            ...
        ]
        
        """
        return self.request("get", "comments/show_batch.json", params=kwargs)

    def create(self, **kwargs):
        """
        访问级别：普通接口
        频次限制：是
        评论一条微博
        
        请求参数
                        必选	    类型及范围	说明
        access_token	true	string	    采用OAuth授权方式为必填参数，OAuth授权后获得。
        comment	        true	string	    评论内容，必须做URLencode，内容不超过140个汉字。
        id	            true	int64	    需要评论的微博ID。
        comment_ori	    false	int	        当评论转发微博时，是否评论给原微博，0：否、1：是，默认为0。
        rip	            false	string	    开发者上报的操作用户真实IP，形如：211.156.0.1。
        
    
        返回值字段	字段类型	字段说明
        created_at	string	评论创建时间
        id	int64	评论的ID
        text	string	评论的内容
        source	string	评论的来源
        user	object	评论作者的用户信息字段 详细
        mid	string	评论的MID
        idstr	string	字符串型的评论ID
        status	object	评论的微博信息字段 详细
        reply_comment	object	评论来源评论，当本评论属于对另一评论的回复时返回此字段
        
        :param kwargs: 
        :return: 
        {
            "created_at": "Wed Jun 01 00:50:25 +0800 2011",
            "id": 12438492184,
            "text": "love your work.......",
            "source": "<a href="http://weibo.com" rel="nofollow">新浪微博</a>",
            "mid": "202110601896455629",
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
                "following": false,
                "allow_all_act_msg": false,
                "remark": "",
                "geo_enabled": true,
                "verified": false,
                "allow_all_comment": true,
                "avatar_large": "http://tp1.sinaimg.cn/1404376560/180/0/1",
                "verified_reason": "",
                "follow_me": false,
                "online_status": 0,
                "bi_followers_count": 215
            },
            "status": {
                "created_at": "Tue May 31 17:46:55 +0800 2011",
                "id": 11488058246,
                "text": "求关注。"，
                "source": "<a href="http://weibo.com" rel="nofollow">新浪微博</a>",
                "favorited": false,
                "truncated": false,
                "in_reply_to_status_id": "",
                "in_reply_to_user_id": "",
                "in_reply_to_screen_name": "",
                "geo": null,
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
                    "following": false,
                    "allow_all_act_msg": false,
                    "remark": "",
                    "geo_enabled": true,
                    "verified": false,
                    "allow_all_comment": true,
                    "avatar_large": "http://tp1.sinaimg.cn/1404376560/180/0/1",
                    "verified_reason": "",
                    "follow_me": false,
                    "online_status": 0,
                    "bi_followers_count": 215
                }
            }
        }
                
        """
        return self.request("post", "comments/create.json", data=kwargs)

    def destroy(self, **kwargs):
        """
        访问级别：普通接口
        频次限制：是
        删除一条我的评论
        
        
        请求参数
                        必选	类型及范围	说明
        cid	true	    int64	要删除的评论ID，只能删除登录用户自己发布的评论。
        
        返回字段说明
        返回值字段	字段类型	字段说明
        created_at	string	评论创建时间
        id	int64	评论的ID
        text	string	评论的内容
        source	string	评论的来源
        user	object	评论作者的用户信息字段 详细
        mid	string	评论的MID
        idstr	string	字符串型的评论ID
        status	object	评论的微博信息字段 详细
        reply_comment	object	评论来源评论，当本评论属于对另一评论的回复时返回此字段
        
        :param kwargs: 
        :return: 
        
        {
            "created_at": "Wed Jun 01 00:50:25 +0800 2011",
            "id": 12438492184,
            "text": "love your work.......",
            "source": "<a href="http://weibo.com" rel="nofollow">新浪微博</a>",
            "mid": "202110601896455629",
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
                "following": false,
                "allow_all_act_msg": false,
                "remark": "",
                "geo_enabled": true,
                "verified": false,
                "allow_all_comment": true,
                "avatar_large": "http://tp1.sinaimg.cn/1404376560/180/0/1",
                "verified_reason": "",
                "follow_me": false,
                "online_status": 0,
                "bi_followers_count": 215
            },
            "status": {
                "created_at": "Tue May 31 17:46:55 +0800 2011",
                "id": 11488058246,
                "text": "求关注。"，
                "source": "<a href="http://weibo.com" rel="nofollow">新浪微博</a>",
                "favorited": false,
                "truncated": false,
                "in_reply_to_status_id": "",
                "in_reply_to_user_id": "",
                "in_reply_to_screen_name": "",
                "geo": null,
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
                    "following": false,
                    "allow_all_act_msg": false,
                    "remark": "",
                    "geo_enabled": true,
                    "verified": false,
                    "allow_all_comment": true,
                    "avatar_large": "http://tp1.sinaimg.cn/1404376560/180/0/1",
                    "verified_reason": "",
                    "follow_me": false,
                    "online_status": 0,
                    "bi_followers_count": 215
                }
            }
        }
        """
        return self.request("post", "comments/destroy.json", data=kwargs)

    def destroy_batch(self, **kwargs):
        """
        访问级别：普通接口
        频次限制：是
        批量删除我的评论
        
        请求参数
                        必选	    类型及范围	说明
        cids	        true	int64	    需要删除的评论ID，用半角逗号隔开，最多20个。
        
                
        返回值字段	字段类型	字段说明
        created_at	string	评论创建时间
        id	int64	评论的ID
        text	string	评论的内容
        source	string	评论的来源
        user	object	评论作者的用户信息字段 详细
        mid	string	评论的MID
        idstr	string	字符串型的评论ID
        status	object	评论的微博信息字段 详细
        reply_comment	object	评论来源评论，当本评论属于对另一评论的回复时返回此字段
        
      
        :param kwargs: 
        :return: 
        
          [
            {
                "created_at": "Wed Jun 01 00:50:25 +0800 2011",
                "id": 12438492184,
                "text": "love your work.......",
                "source": "<a href="http://weibo.com" rel="nofollow">新浪微博</a>",
                "mid": "202110601896455629",
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
                    "following": false,
                    "allow_all_act_msg": false,
                    "remark": "",
                    "geo_enabled": true,
                    "verified": false,
                    "allow_all_comment": true,
                    "avatar_large": "http://tp1.sinaimg.cn/1404376560/180/0/1",
                    "verified_reason": "",
                    "follow_me": false,
                    "online_status": 0,
                    "bi_followers_count": 215
                },
                "status": {
                    "created_at": "Tue May 31 17:46:55 +0800 2011",
                    "id": 11488058246,
                    "text": "求关注。"，
                    "source": "<a href="http://weibo.com" rel="nofollow">新浪微博</a>",
                    "favorited": false,
                    "truncated": false,
                    "in_reply_to_status_id": "",
                    "in_reply_to_user_id": "",
                    "in_reply_to_screen_name": "",
                    "geo": null,
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
                        "following": false,
                        "allow_all_act_msg": false,
                        "remark": "",
                        "geo_enabled": true,
                        "verified": false,
                        "allow_all_comment": true,
                        "avatar_large": "http://tp1.sinaimg.cn/1404376560/180/0/1",
                        "verified_reason": "",
                        "follow_me": false,
                        "online_status": 0,
                        "bi_followers_count": 215
                    }
                }
            },
            ...
        ]
        """
        return self.request("post", "comments/destroy_batch.json", data=kwargs)

    def reply(self, **kwargs):
        """
        
        访问级别：普通接口
        频次限制：是
        回复一条我收到的评论
        
        
        请求参数
                        必选	    类型及范围	说明
        access_token	true	string	采用OAuth授权方式为必填参数，OAuth授权后获得。
        cid	            true	int64	需要回复的评论ID。
        id	            true	int64	需要评论的微博ID。
        comment	        true	string	回复评论内容，必须做URLencode，内容不超过140个汉字。
        without_mention	false	int	    回复中是否自动加入“回复@用户名”，0：是、1：否，默认为0。
        comment_ori	    false	int	    当评论转发微博时，是否评论给原微博，0：否、1：是，默认为0。
        rip	            false	string	开发者上报的操作用户真实IP，形如：211.156.0.1。
        
        
        返回字段说明
        返回值字段	字段类型	字段说明
        created_at	string	评论创建时间
        id	int64	评论的ID
        text	string	评论的内容
        source	string	评论的来源
        user	object	评论作者的用户信息字段 详细
        mid	string	评论的MID
        idstr	string	字符串型的评论ID
        status	object	评论的微博信息字段 详细
        reply_comment	object	评论来源评论，当本评论属于对另一评论的回复时返回此字段
        
        
        :param kwargs: 
        :return: 

        {
            "created_at": "Wed Jun 01 00:50:25 +0800 2011",
            "id": 12438492184,
            "text": "love your work.......",
            "source": "<a href="http://weibo.com" rel="nofollow">新浪微博</a>",
            "mid": "202110601896455629",
            "reply_comment": {
                "created_at": "Wed Jun 01 00:50:25 +0800 2011",
                "id": 4949855625,
                "text": "小新小新",
                "source": "<a href="http://weibo.com" rel="nofollow">新浪微博</a>",
                "mid": "202110601896455629",
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
                    "following": false,
                    "allow_all_act_msg": false,
                    "remark": "",
                    "geo_enabled": true,
                    "verified": false,
                    "allow_all_comment": true,
                    "avatar_large": "http://tp1.sinaimg.cn/1404376560/180/0/1",
                    "verified_reason": "",
                    "follow_me": false,
                    "online_status": 0,
                    "bi_followers_count": 215
                }
            },
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
                "following": false,
                "allow_all_act_msg": false,
                "remark": "",
                "geo_enabled": true,
                "verified": false,
                "allow_all_comment": true,
                "avatar_large": "http://tp1.sinaimg.cn/1404376560/180/0/1",
                "verified_reason": "",
                "follow_me": false,
                "online_status": 0,
                "bi_followers_count": 215
            },
            "status": {
                "created_at": "Tue May 31 17:46:55 +0800 2011",
                "id": 11488058246,
                "text": "求关注。"，
                "source": "<a href="http://weibo.com" rel="nofollow">新浪微博</a>",
                "favorited": false,
                "truncated": false,
                "in_reply_to_status_id": "",
                "in_reply_to_user_id": "",
                "in_reply_to_screen_name": "",
                "geo": null,
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
                    "following": false,
                    "allow_all_act_msg": false,
                    "remark": "",
                    "geo_enabled": true,
                    "verified": false,
                    "allow_all_comment": true,
                    "avatar_large": "http://tp1.sinaimg.cn/1404376560/180/0/1",
                    "verified_reason": "",
                    "follow_me": false,
                    "online_status": 0,
                    "bi_followers_count": 215
                }
            }
        }
        """
        return self.request("post", "comments/reply.json", data=kwargs)
