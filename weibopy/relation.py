# encoding:utf-8
from .weibo import WeiboClient


class Relation(WeiboClient):
    """
    weibo relation api
    """

    def friends(self, **kwargs):
        """
        访问级别：普通接口
        频次限制：是
        获取用户的关注列表
        
        参数uid与screen_name二者必选其一，且只能选其一；
        接口升级后：uid与screen_name只能为当前授权用户；
        只返回同样授权本应用的用户，非授权用户将不返回；
        例如一次调用count是50，但其中授权本应用的用户只有10条，则实际只返回10条；
        使用官方移动SDK调用，多返回30%的非同样授权本应用的用户，总上限为500；
        
        请求参数:
                    必选	    类型及范围	说明
        uid	        false	int64	    需要查询的用户UID。
        screen_name	false	string	    需要查询的用户昵称。
        count	    false	int	        单页返回的记录条数，默认为50，最大不超过200。
        cursor	    false	int	        返回结果的游标，下一页用返回值里的next_cursor，上一页用previous_cursor，默认为0。
        trim_status	false	int	        返回值中user字段中的status字段开关，0：返回完整status字段、1：status字段仅返回status_id，默认为1。
        
        
        返回字段说明
        
            返回值字段	字段类型	字段说明
        id	int64	用户UID
        idstr	string	字符串型的用户UID
        screen_name	string	用户昵称
        name	string	友好显示名称
        province	int	用户所在省级ID
        city	int	用户所在城市ID
        location	string	用户所在地
        description	string	用户个人描述
        url	string	用户博客地址
        profile_image_url	string	用户头像地址（中图），50×50像素
        profile_url	string	用户的微博统一URL地址
        domain	string	用户的个性化域名
        weihao	string	用户的微号
        gender	string	性别，m：男、f：女、n：未知
        followers_count	int	粉丝数
        friends_count	int	关注数
        statuses_count	int	微博数
        favourites_count	int	收藏数
        created_at	string	用户创建（注册）时间
        following	boolean	暂未支持
        allow_all_act_msg	boolean	是否允许所有人给我发私信，true：是，false：否
        geo_enabled	boolean	是否允许标识用户的地理位置，true：是，false：否
        verified	boolean	是否是微博认证用户，即加V用户，true：是，false：否
        verified_type	int	暂未支持
        remark	string	用户备注信息，只有在查询用户关系时才返回此字段
        status	object	用户的最近一条微博信息字段 详细
        allow_all_comment	boolean	是否允许所有人对我的微博进行评论，true：是，false：否
        avatar_large	string	用户头像地址（大图），180×180像素
        avatar_hd	string	用户头像地址（高清），高清头像原图
        verified_reason	string	认证原因
        follow_me	boolean	该用户是否关注当前登录用户，true：是，false：否
        online_status	int	用户的在线状态，0：不在线、1：在线
        bi_followers_count	int	用户的互粉数
        lang	string	用户当前的语言版本，zh-cn：简体中文，zh-tw：繁体中文，en：英语
        
        :param kwargs: 
        :return: 
        
        {
            "users": [
                {
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
                    "status": {
                        "created_at": "Tue May 24 18:04:53 +0800 2011",
                        "id": 11142488790,
                        "text": "我的相机到了。",
                        "source": "<a href="http://weibo.com" rel="nofollow">新浪微博</a>",
                        "favorited": false,
                        "truncated": false,
                        "in_reply_to_status_id": "",
                        "in_reply_to_user_id": "",
                        "in_reply_to_screen_name": "",
                        "geo": null,
                        "mid": "5610221544300749636",
                        "annotations": [],
                        "reposts_count": 5,
                        "comments_count": 8
                    },
                    "allow_all_comment": true,
                    "avatar_large": "http://tp1.sinaimg.cn/1404376560/180/0/1",
                    "verified_reason": "",
                    "follow_me": false,
                    "online_status": 0,
                    "bi_followers_count": 215
                },
                ...
            ],
            "next_cursor": 5,
            "previous_cursor": 0,
            "total_number": 668
        }
        
        """
        return self.request("get", "friendships/friends.json", params=kwargs)

    def friends_ids(self, **kwargs):
        """
        访问级别：普通接口
        频次限制：是
        获取用户关注对象UID列表
        
        请求参数:
                        必选	    类型及范围	说明
        access_token	true	string	    采用OAuth授权方式为必填参数，OAuth授权后获得。
        uid	            false	int64	    需要查询的用户UID。
        screen_name	    false	string	    需要查询的用户昵称。
        count	        false	int	        单页返回的记录条数，默认为500，最大不超过5000。
        cursor	        false	int	        返回结果的游标，下一页用返回值里的next_cursor，上一页用previous_cursor，默认为0。
        
        参数uid与screen_name二者必选其一，且只能选其一；
        接口升级后：uid与screen_name只能为当前授权用户；
        只返回同样授权本应用的用户；
        使用官方移动SDK调用，多返回30%的非同样授权本应用的用户，总上限为500；
                
        :param kwargs: 
        :return: 
        
          {
            "ids": [
                1726475555,
                1404376560,
                1233616152,
                ...
            ],
            "next_cursor": 5,
            "previous_cursor": 0,
            "total_number": 668
        }
        """
        return self.request("get", "friendships/friends/ids.json", params=kwargs)

    def followers(self, **kwargs):
        """
        访问级别：普通接口
        频次限制：是
        获取用户粉丝列表
        
        参数uid与screen_name二者必选其一，且只能选其一；
        接口升级后：uid与screen_name只能为当前授权用户；
        只返回同样授权本应用的用户，非授权用户将不返回；
        例如一次调用count是50，但其中授权本应用的用户只有10条，则实际只返回10条；
        使用官方移动SDK调用，多返回30%的非同样授权本应用的用户，总上限为500；
        
        请求参数:
                    必选	    类型及范围	说明
        uid	        false	int64	    需要查询的用户UID。
        screen_name	false	string	    需要查询的用户昵称。
        count	    false	int	        单页返回的记录条数，默认为50，最大不超过200。
        cursor	    false	int	        返回结果的游标，下一页用返回值里的next_cursor，上一页用previous_cursor，默认为0。
        trim_status	false	int	        返回值中user字段中的status字段开关，0：返回完整status字段、1：status字段仅返回status_id，默认为1。
        
        
        返回字段说明
            返回值字段	字段类型	字段说明
        id	int64	用户UID
        idstr	string	字符串型的用户UID
        screen_name	string	用户昵称
        name	string	友好显示名称
        province	int	用户所在省级ID
        city	int	用户所在城市ID
        location	string	用户所在地
        description	string	用户个人描述
        url	string	用户博客地址
        profile_image_url	string	用户头像地址（中图），50×50像素
        profile_url	string	用户的微博统一URL地址
        domain	string	用户的个性化域名
        weihao	string	用户的微号
        gender	string	性别，m：男、f：女、n：未知
        followers_count	int	粉丝数
        friends_count	int	关注数
        statuses_count	int	微博数
        favourites_count	int	收藏数
        created_at	string	用户创建（注册）时间
        following	boolean	暂未支持
        allow_all_act_msg	boolean	是否允许所有人给我发私信，true：是，false：否
        geo_enabled	boolean	是否允许标识用户的地理位置，true：是，false：否
        verified	boolean	是否是微博认证用户，即加V用户，true：是，false：否
        verified_type	int	暂未支持
        remark	string	用户备注信息，只有在查询用户关系时才返回此字段
        status	object	用户的最近一条微博信息字段 详细
        allow_all_comment	boolean	是否允许所有人对我的微博进行评论，true：是，false：否
        avatar_large	string	用户头像地址（大图），180×180像素
        avatar_hd	string	用户头像地址（高清），高清头像原图
        verified_reason	string	认证原因
        follow_me	boolean	该用户是否关注当前登录用户，true：是，false：否
        online_status	int	用户的在线状态，0：不在线、1：在线
        bi_followers_count	int	用户的互粉数
        lang	string	用户当前的语言版本，zh-cn：简体中文，zh-tw：繁体中文，en：英语
        
        :param kwargs: 
        :return: 
        
        
        {
            "users": [
                {
                    "id": 321205008,
                    "idstr": "321205008",
                    "screen_name": "江湖社***",
                    "name": "江湖社***,
                    "province": "41",
                    "city": "1",
                    "location": "河南 郑州",
                    "description": "描述。。。",
                    "url": "http://www.weibo.com",
                    "profile_image_url": "http://tp2.sinaimg.cn/321205008/50/5652109562/1",
                    "profile_url": "523438876",
                    "domain": "laijianghu",
                    "weihao": "523438876",
                    "gender": "m",
                    "followers_count": 270,
                    "friends_count": 364,
                    "statuses_count": 23,
                    "favourites_count": 0,
                    "created_at": "Wed Jan 02 23:56:03 +0800 2013",
                    "following": false,
                    "allow_all_act_msg": true,
                    "geo_enabled": true,
                    "verified": false,
                    "verified_type": -1,
                    "remark": "",
                    "status_id": 3532859991713507,
                    "allow_all_comment": true,
                    "avatar_large": "http://tp2.sinaimg.cn/3212050081/180/5652109562/1",
                    "verified_reason": "",
                    "follow_me": false,
                    "online_status": 0,
                    "bi_followers_count": 204,
                    "lang": "zh-cn",
                    "star": 0,
                    "mbtype": 0,
                    "mbrank": 0,
                    "block_word": 0
                },
                ...
            ],
            "next_cursor": 1,
            "previous_cursor": 0,
            "total_number": 61550
        }
        
        """
        return self.request("get", "friendships/followers.json", params=kwargs)

    def followers_ids(self, **kwargs):
        """
        访问级别：普通接口
        频次限制：是
        获取用户粉丝UID列表
        
        参数uid与screen_name二者必选其一，且只能选其一；
        接口升级后：uid与screen_name只能为当前授权用户；
        只返回同样授权本应用的用户；
        使用官方移动SDK调用，多返回30%的非同样授权本应用的用户，总上限为500；

        请求参数:
                    必选	    类型及范围	说明
        uid	        false	int64	    需要查询的用户UID。
        screen_name	false	string	    需要查询的用户昵称。
        count	    false	int	        单页返回的记录条数，默认为500，最大不超过5000。
        cursor	    false	int	        返回结果的游标，下一页用返回值里的next_cursor，上一页用previous_cursor，默认为0。
        
        return:
        {
            "ids": [
                1726475555,
                1404376560,
                1233616152,
                ...
            ],
            "next_cursor": 5,
            "previous_cursor": 0,
            "total_number": 668
        }
        :param kwargs: 
        :return: 
        """
        return self.request("get", "friendships/followers/ids.json", params=kwargs)

    def show(self, **kwargs):
        """
        
        访问级别：普通接口
        频次限制：是
        获取两个用户关系的详细情况
        
        参数source_id与source_screen_name二者必选其一，且只能选其一
        参数target_id与target_screen_name二者必选其一，且只能选其一
        
        请求参数
                            必选	    类型及范围	说明
        access_token	    true	string	    采用OAuth授权方式为必填参数，OAuth授权后获得。
        source_id	        false	int64	    源用户的UID。
        source_screen_name	false	string	    源用户的微博昵称。
        target_id	        false	int64	    目标用户的UID。
        target_screen_name	false	string	    目标用户的微博昵称。
        
        
        :param kwargs: 
        :return: 
        {
            "target": {
                "id": 1418348195,
                "screen_name": "zaku",
                "followed_by": false,
                "following": false,
                "notifications_enabled": false
            },
            "source": {
                "id": 1734528095,
                "screen_name": "檀木幻想",
                "followed_by": false,
                "following": false,
                "notifications_enabled": false
            }
        }
        """
        return self.request("get", "friendships/show.json", params=kwargs)

    def create(self, **kwargs):
        """
        访问级别：高级接口（需要授权）
        频次限制：是
        关注某用户
        此接口仅针对微博类客户端开放，非微博类客户端应用不开放此接口权限。
        
        
        返回字段说明
        返回值字段	字段类型	字段说明
        id	int64	用户UID
        idstr	string	字符串型的用户UID
        screen_name	string	用户昵称
        name	string	友好显示名称
        province	int	用户所在省级ID
        city	int	用户所在城市ID
        location	string	用户所在地
        description	string	用户个人描述
        url	string	用户博客地址
        profile_image_url	string	用户头像地址（中图），50×50像素
        profile_url	string	用户的微博统一URL地址
        domain	string	用户的个性化域名
        weihao	string	用户的微号
        gender	string	性别，m：男、f：女、n：未知
        followers_count	int	粉丝数
        friends_count	int	关注数
        statuses_count	int	微博数
        favourites_count	int	收藏数
        created_at	string	用户创建（注册）时间
        following	boolean	暂未支持
        allow_all_act_msg	boolean	是否允许所有人给我发私信，true：是，false：否
        geo_enabled	boolean	是否允许标识用户的地理位置，true：是，false：否
        verified	boolean	是否是微博认证用户，即加V用户，true：是，false：否
        verified_type	int	暂未支持
        remark	string	用户备注信息，只有在查询用户关系时才返回此字段
        status	object	用户的最近一条微博信息字段 详细
        allow_all_comment	boolean	是否允许所有人对我的微博进行评论，true：是，false：否
        avatar_large	string	用户头像地址（大图），180×180像素
        avatar_hd	string	用户头像地址（高清），高清头像原图
        verified_reason	string	认证原因
        follow_me	boolean	该用户是否关注当前登录用户，true：是，false：否
        online_status	int	用户的在线状态，0：不在线、1：在线
        bi_followers_count	int	用户的互粉数
        lang	string	用户当前的语言版本，zh-cn：简体中文，zh-tw：繁体中文，en：英语
        
        请求参数
        	        必选	    类型及范围	说明
        uid	        false	int64	    需要关注的用户ID。
        screen_name	false	string	    需要关注的用户昵称。
        rip	        false	string	    开发者上报的操作用户真实IP，形如：211.156.0.1。
        :param kwargs: 
        :return: 
        
        {
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
            "geo_enabled": true,
            "verified": false,
            "status": {
                "created_at": "Tue May 24 18:04:53 +0800 2011",
                "id": 11142488790,
                "text": "我的相机到了。",
                "source": "<a href="http://weibo.com" rel="nofollow">新浪微博</a>",
                "favorited": false,
                "truncated": false,
                "in_reply_to_status_id": "",
                "in_reply_to_user_id": "",
                "in_reply_to_screen_name": "",
                "geo": null,
                "mid": "5610221544300749636",
                "annotations": [],
                "reposts_count": 5,
                "comments_count": 8
            },
            "allow_all_comment": true,
            "avatar_large": "http://tp1.sinaimg.cn/1404376560/180/0/1",
            "verified_reason": "",
            "follow_me": false,
            "online_status": 0,
            "bi_followers_count": 215
        }
        """
        return self.request("post", "friendships/create.json", params=kwargs)

    def destory(self, **kwargs):
        """
        访问级别：高级接口（需要授权）
        频次限制：是
        取消关注某用户 
        
        此接口仅针对微博类客户端开放，非微博类客户端应用不开放此接口权限。

        
        请求参数
 	                必选	    类型及范围	说明
        uid	        false	int64	    需要取消关注的用户ID。
        screen_name	false	string	    需要取消关注的用户昵称。
        
        返回字段说明
        返回值字段	字段类型	字段说明
        id	int64	用户UID
        idstr	string	字符串型的用户UID
        screen_name	string	用户昵称
        name	string	友好显示名称
        province	int	用户所在省级ID
        city	int	用户所在城市ID
        location	string	用户所在地
        description	string	用户个人描述
        url	string	用户博客地址
        profile_image_url	string	用户头像地址（中图），50×50像素
        profile_url	string	用户的微博统一URL地址
        domain	string	用户的个性化域名
        weihao	string	用户的微号
        gender	string	性别，m：男、f：女、n：未知
        followers_count	int	粉丝数
        friends_count	int	关注数
        statuses_count	int	微博数
        favourites_count	int	收藏数
        created_at	string	用户创建（注册）时间
        following	boolean	暂未支持
        allow_all_act_msg	boolean	是否允许所有人给我发私信，true：是，false：否
        geo_enabled	boolean	是否允许标识用户的地理位置，true：是，false：否
        verified	boolean	是否是微博认证用户，即加V用户，true：是，false：否
        verified_type	int	暂未支持
        remark	string	用户备注信息，只有在查询用户关系时才返回此字段
        status	object	用户的最近一条微博信息字段 详细
        allow_all_comment	boolean	是否允许所有人对我的微博进行评论，true：是，false：否
        avatar_large	string	用户头像地址（大图），180×180像素
        avatar_hd	string	用户头像地址（高清），高清头像原图
        verified_reason	string	认证原因
        follow_me	boolean	该用户是否关注当前登录用户，true：是，false：否
        online_status	int	用户的在线状态，0：不在线、1：在线
        bi_followers_count	int	用户的互粉数
        lang	string	用户当前的语言版本，zh-cn：简体中文，zh-tw：繁体中文，en：英语
        
        :param kwargs: 
        :return: 
        {
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
            "geo_enabled": true,
            "verified": false,
            "status": {
                "created_at": "Tue May 24 18:04:53 +0800 2011",
                "id": 11142488790,
                "text": "我的相机到了。",
                "source": "<a href="http://weibo.com" rel="nofollow">新浪微博</a>",
                "favorited": false,
                "truncated": false,
                "in_reply_to_status_id": "",
                "in_reply_to_user_id": "",
                "in_reply_to_screen_name": "",
                "geo": null,
                "mid": "5610221544300749636",
                "annotations": [],
                "reposts_count": 5,
                "comments_count": 8
            },
            "allow_all_comment": true,
            "avatar_large": "http://tp1.sinaimg.cn/1404376560/180/0/1",
            "verified_reason": "",
            "follow_me": false,
            "online_status": 0,
            "bi_followers_count": 215
        }
        """
        return self.request("post", "friendships/destroy.json", params=kwargs)
