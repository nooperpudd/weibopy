# encoding:utf-8
from .weibo import WeiboClient


class WeiboUser(WeiboClient):
    """
    weibo user info
    """

    def show(self, **kwargs):
        """
        
        访问级别：普通接口
        频次限制：是
        获取用户信息
        
        请求参数
                        必选	    类型及范围	说明
        uid	            false	int64	需要查询的用户ID。
        screen_name	    false	string	需要查询的用户昵称。
        
        参数uid与screen_name二者必选其一，且只能选其一；
        接口升级后，对未授权本应用的uid，将无法获取其个人简介、认证原因、粉丝数、关注数、微博数及最近一条微博内容。
        
        
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
        return self.request("get", "users/show.json", params=kwargs)

    def domain_show(self, **kwargs):
        """
        
        访问级别：普通接口
        频次限制：是
        通过个性域名获取用户信息
        
        接口升级后，对未授权本应用的uid，将无法获取其个人简介、认证原因、粉丝数、关注数、微博数及最近一条微博内容。
        
        
        请求参数
                        必选	    类型及范围	说明
        domain	        true	string	    需要查询的个性化域名。
        
        
        
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
        return self.request("get", "users/domain_show.json", params=kwargs)

    def counts(self, **kwargs):
        """
        访问级别：普通接口
        频次限制：是
        批量获取用户的粉丝数、关注数、微博数
        
        接口升级后，对未授权本应用的uid，将无法获取其粉丝数、关注数及微博数。
        
        请求参数
                        必选      类型及范围	说明
        uids	        true	string	    需要获取数据的用户UID，多个之间用逗号分隔，最多不超过100个。
           
        
        返回字段说明
        返回值字段	字段类型	字段说明
        id	int64	微博ID
        followers_count	int	粉丝数
        friends_count	int	关注数
        statuses_count	int	微博数
        private_friends_count	int	暂未支持
        :param kwargs: 
        :return: 
        
        [
            {
                "id": "1404376560",
                "followers_count": "1369",
                "friends_count": "526",
                "statuses_count": "2908"
            },
            ...
        ]
        """

        return self.request("get", "users/counts.json", params=kwargs)
