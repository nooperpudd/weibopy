# encoding:utf-8
from .weibo import WeiboClient


class WeiboTweet(WeiboClient):
    """
    """

    def public_timeline(self, **kwargs):
        """
        访问级别：普通接口
        频次限制：是
        返回最新的公共微博

        请求参数
 	                必选	    类型及范围	说明
        count	    false	int	    单页返回的记录条数，默认为50。
        page	    false	int	    返回结果的页码，默认为1。
        base_app	false	int	    是否只获取当前应用的数据。0为否（所有数据），1为是（仅当前应用），默认为0。
        
        
        返回值字段	字段类型	字段说明
        created_at	string	微博创建时间
        id	int64	微博ID
        mid	int64	微博MID
        idstr	string	字符串型的微博ID
        text	string	微博信息内容
        source	string	微博来源
        favorited	boolean	是否已收藏，true：是，false：否
        truncated	boolean	是否被截断，true：是，false：否
        in_reply_to_status_id	string	（暂未支持）回复ID
        in_reply_to_user_id	string	（暂未支持）回复人UID
        in_reply_to_screen_name	string	（暂未支持）回复人昵称
        thumbnail_pic	string	缩略图片地址，没有时不返回此字段
        bmiddle_pic	string	中等尺寸图片地址，没有时不返回此字段
        original_pic	string	原始图片地址，没有时不返回此字段
        geo	object	地理信息字段 详细
        user	object	微博作者的用户信息字段 详细
        retweeted_status	object	被转发的原微博信息字段，当该微博为转发微博时返回 详细
        reposts_count	int	转发数
        comments_count	int	评论数
        attitudes_count	int	表态数
        mlevel	int	暂未支持
        visible	object	微博的可见性及指定可见分组信息。该object中type取值，0：普通微博，1：私密微博，3：指定分组微博，4：密友微博；list_id为分组的组号
        pic_ids	object	微博配图ID。多图时返回多图ID，用来拼接图片url。用返回字段thumbnail_pic的地址配上该返回字段的图片ID，即可得到多个图片url。
        ad	object array	微博流内的推广微博ID
        
        :return:
         {
            "statuses": [
                {
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
                },
                ..
            ],
            "previous_cursor": 0,
            "next_cursor": 11488013766,
            "total_number": 81655
        }
        """
        return self.request("get", "statuses/public_timeline.json", params=kwargs)

    def home_timeline(self, **kwargs):
        """
        
        访问级别：普通接口
        频次限制：是
        获取当前登录用户及其所关注（授权）用户的最新微博
        
        只返回授权用户的微博，非授权用户的微博将不返回；
        例如一次调用total_number是50，但其中授权用户发的只有10条，则实际只返回10条微博；
        使用官方移动SDK调用，可多返回30%的非授权用户的微博；
        
        请求参数

                    必选	    类型及范围	说明
        since_id	false	int64	若指定此参数，则返回ID比since_id大的微博（即比since_id时间晚的微博），默认为0。
        max_id	    false	int64	若指定此参数，则返回ID小于或等于max_id的微博，默认为0。
        count	    false	int	    单页返回的记录条数，最大不超过100，默认为20。
        page	    false	int	    返回结果的页码，默认为1。
        base_app	false	int	    是否只获取当前应用的数据。0为否（所有数据），1为是（仅当前应用），默认为0。
        feature	    false	int	    过滤类型ID，0：全部、1：原创、2：图片、3：视频、4：音乐，默认为0。
        trim_user	false	int	    返回值中user字段开关，0：返回完整user字段、1：user字段仅返回user_id，默认为0。
        
                
        返回字段说明
        
        返回值字段	字段类型	字段说明
        created_at	string	微博创建时间
        id	int64	微博ID
        mid	int64	微博MID
        idstr	string	字符串型的微博ID
        text	string	微博信息内容
        source	string	微博来源
        favorited	boolean	是否已收藏，true：是，false：否
        truncated	boolean	是否被截断，true：是，false：否
        in_reply_to_status_id	string	（暂未支持）回复ID
        in_reply_to_user_id	string	（暂未支持）回复人UID
        in_reply_to_screen_name	string	（暂未支持）回复人昵称
        thumbnail_pic	string	缩略图片地址，没有时不返回此字段
        bmiddle_pic	string	中等尺寸图片地址，没有时不返回此字段
        original_pic	string	原始图片地址，没有时不返回此字段
        geo	object	地理信息字段 详细
        user	object	微博作者的用户信息字段 详细
        retweeted_status	object	被转发的原微博信息字段，当该微博为转发微博时返回 详细
        reposts_count	int	转发数
        comments_count	int	评论数
        attitudes_count	int	表态数
        mlevel	int	暂未支持
        visible	object	微博的可见性及指定可见分组信息。该object中type取值，0：普通微博，1：私密微博，3：指定分组微博，4：密友微博；list_id为分组的组号
        pic_ids	object	微博配图ID。多图时返回多图ID，用来拼接图片url。用返回字段thumbnail_pic的地址配上该返回字段的图片ID，即可得到多个图片url。
        ad	object array	微博流内的推广微博ID
        
        :return: 
        
        {
            "statuses": [
                {
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
                },
                ...
            ],
            "ad": [
                {
                    "id": 3366614911586452,
                    "mark": "AB21321XDFJJK"
                },
                ...
            ],
            "previous_cursor": 0,                   // 暂未支持
            "next_cursor": 11488013766,    // 暂未支持
            "total_number": 81655
        }
        """

        return self.request("get", "statuses/home_timeline.json", params=kwargs)

    def friends_timeline_ids(self, **kwargs):
        """
        
        访问级别：普通接口
        频次限制：是
        获取当前登录用户及其所关注用户的最新微博的ID
        
        请求参数
 	                必选	    类型及范围	说明
        since_id	false	int64	若指定此参数，则返回ID比since_id大的微博（即比since_id时间晚的微博），默认为0。
        max_id	    false	int64	若指定此参数，则返回ID小于或等于max_id的微博，默认为0。
        count	    false	int	    单页返回的记录条数，最大不超过100，默认为20。
        page	    false	int	    返回结果的页码，默认为1。
        base_app	false	int	    是否只获取当前应用的数据。0为否（所有数据），1为是（仅当前应用），默认为0。
        feature	    false	int	    过滤类型ID，0：全部、1：原创、2：图片、3：视频、4：音乐，默认为0
        
        :param kwargs: 
        :return: 
        
        {
            "statuses": [
                "3382905382185354",
                "3382905252160340",
                "3382905235630562",
                ...
            ],
            "previous_cursor": 0,   // 暂未支持
            "next_cursor": 0,           // 暂未支持
            "total_number": 16
        }
        """
        return self.request("get", "statuses/friends_timeline/ids.json", params=kwargs)

    def user_timeline(self, **kwargs):
        """
        
        访问级别：普通接口
        频次限制：是
        获取某个用户最新发表的微博列表
        
        获取自己的微博，参数uid与screen_name可以不填，则自动获取当前登录用户的微博；
        指定获取他人的微博，参数uid与screen_name二者必选其一，且只能选其一；
        接口升级后：uid与screen_name只能为当前授权用户；
        读取当前授权用户所有关注人最新微博列表，请使用：获取当前授权用户及其所关注用户的最新微博接口（statuses/home_timeline）；
        此接口最多只返回最新的5条数据，官方移动SDK调用可返回10条；
        
        
        请求参数
 	                必选	    类型及范围	说明  
        uid	        false	int64	需要查询的用户ID。
        screen_name	false	string	需要查询的用户昵称。
        since_id	false	int64	若指定此参数，则返回ID比since_id大的微博（即比since_id时间晚的微博），默认为0。
        max_id	    false	int64	若指定此参数，则返回ID小于或等于max_id的微博，默认为0。
        count	    false	int	    单页返回的记录条数，最大不超过100，超过100以100处理，默认为20。
        page	    false	int	    返回结果的页码，默认为1。
        base_app	false	int	    是否只获取当前应用的数据。0为否（所有数据），1为是（仅当前应用），默认为0。
        feature	    false	int	    过滤类型ID，0：全部、1：原创、2：图片、3：视频、4：音乐，默认为0。
        trim_user	false	int	    返回值中user字段开关，0：返回完整user字段、1：user字段仅返回user_id，默认为0。
        
        
        返回值字段	字段类型	字段说明
        created_at	string	微博创建时间
        id	int64	微博ID
        mid	int64	微博MID
        idstr	string	字符串型的微博ID
        text	string	微博信息内容
        source	string	微博来源
        favorited	boolean	是否已收藏，true：是，false：否
        truncated	boolean	是否被截断，true：是，false：否
        in_reply_to_status_id	string	（暂未支持）回复ID
        in_reply_to_user_id	string	（暂未支持）回复人UID
        in_reply_to_screen_name	string	（暂未支持）回复人昵称
        thumbnail_pic	string	缩略图片地址，没有时不返回此字段
        bmiddle_pic	string	中等尺寸图片地址，没有时不返回此字段
        original_pic	string	原始图片地址，没有时不返回此字段
        geo	object	地理信息字段 详细
        user	object	微博作者的用户信息字段 详细
        retweeted_status	object	被转发的原微博信息字段，当该微博为转发微博时返回 详细
        reposts_count	int	转发数
        comments_count	int	评论数
        attitudes_count	int	表态数
        mlevel	int	暂未支持
        visible	object	微博的可见性及指定可见分组信息。该object中type取值，0：普通微博，1：私密微博，3：指定分组微博，4：密友微博；list_id为分组的组号
        pic_ids	object	微博配图ID。多图时返回多图ID，用来拼接图片url。用返回字段thumbnail_pic的地址配上该返回字段的图片ID，即可得到多个图片url。
        ad	object array	微博流内的推广微博ID
        
        :param kwargs: 
        :return: 
        
        {
            "statuses": [
                {
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
                },
                ...
            ],
            "previous_cursor": 0,                     // 暂未支持
            "next_cursor": 11488013766,      // 暂未支持
            "total_number": 81655
        }
        """
        return self.request("get", "statuses/user_timeline.json", params=kwargs)

    def user_timeline_ids(self, **kwargs):
        """
        
        访问级别：普通接口
        频次限制：是
        获取用户发布的微博的ID
        
        
        参数uid与screen_name二者必选其一，且只能选其一，uid优先
        接口升级后：uid与screen_name只能为当前授权用户；
        读取当前授权用户所有关注人最新微博列表，请使用：获取当前授权用户及其所关注用户的最新微博接口（statuses/home_timeline）；
        此接口最多只返回最新的5条数据，官方移动SDK调用可返回10条；
        
        请求参数:
        
                        必选	类型及范围	说明
        access_token	true	string	采用OAuth授权方式为必填参数，OAuth授权后获得。
        uid	            false	int64	需要查询的用户ID。
        screen_name	    false	string	需要查询的用户昵称。
        since_id	    false	int64	若指定此参数，则返回ID比since_id大的微博（即比since_id时间晚的微博），默认为0。
        max_id	        false	int64	若指定此参数，则返回ID小于或等于max_id的微博，默认为0。
        count	        false	int	    单页返回的记录条数，最大不超过100，默认为20。
        page	        false	int	    返回结果的页码，默认为1。
        base_app	    false	int	    是否只获取当前应用的数据。0为否（所有数据），1为是（仅当前应用），默认为0。
        feature	        false	int	    过滤类型ID，0：全部、1：原创、2：图片、3：视频、4：音乐，默认为0。
        

        
        :param kwargs: 
        :return: 
        
                {
            "statuses": [
                "3382905382185354",
                "3382905252160340",
                "3382905235630562",
                ...
            ],
            "previous_cursor": 0, // 暂未支持
            "next_cursor": 0,         //  暂未支持
            "total_number": 16
        }
        """
        return self.request("get", "statuses/user_timeline/ids.json", params=kwargs)

    def timeline_batch(self, **kwargs):
        """
        访问级别：高级接口（需要授权）
        频次限制：是
        批量获取指定的一批用户的微博列表
        
        注意事项
        参数uids与screen_name二者必选其一，且只能选其一；
        查询的用户必须是调用应用的授权用户，非授权用户的微博将不返回；
        使用官方移动SDK调用，可多返回30%的非授权用户的微博；
        
                        必选	    类型及范围	说明
        uids	        false	string	需要查询的用户ID，用半角逗号分隔，一次最多20个。
        screen_names	false	string	需要查询的用户昵称，用半角逗号分隔，一次最多20个。
        count	        false	int	    单页返回的记录条数，默认为20。
        page	        false	int	    返回结果的页码，默认为1。
        base_app	    false	int	    是否只获取当前应用的数据。0为否（所有数据），1为是（仅当前应用），默认为0。
        feature	        false	int	    过滤类型ID，0：全部、1：原创、2：图片、3：视频、4：音乐，默认为0。
                
        返回值字段	字段类型	字段说明
        created_at	string	微博创建时间
        id	int64	微博ID
        mid	int64	微博MID
        idstr	string	字符串型的微博ID
        text	string	微博信息内容
        source	string	微博来源
        favorited	boolean	是否已收藏，true：是，false：否
        truncated	boolean	是否被截断，true：是，false：否
        in_reply_to_status_id	string	（暂未支持）回复ID
        in_reply_to_user_id	string	（暂未支持）回复人UID
        in_reply_to_screen_name	string	（暂未支持）回复人昵称
        thumbnail_pic	string	缩略图片地址，没有时不返回此字段
        bmiddle_pic	string	中等尺寸图片地址，没有时不返回此字段
        original_pic	string	原始图片地址，没有时不返回此字段
        geo	object	地理信息字段 详细
        user	object	微博作者的用户信息字段 详细
        retweeted_status	object	被转发的原微博信息字段，当该微博为转发微博时返回 详细
        reposts_count	int	转发数
        comments_count	int	评论数
        attitudes_count	int	表态数
        mlevel	int	暂未支持
        visible	object	微博的可见性及指定可见分组信息。该object中type取值，0：普通微博，1：私密微博，3：指定分组微博，4：密友微博；list_id为分组的组号
        pic_ids	object	微博配图ID。多图时返回多图ID，用来拼接图片url。用返回字段thumbnail_pic的地址配上该返回字段的图片ID，即可得到多个图片url。
        ad	object array	微博流内的推广微博ID
        
        :param kwargs: 
        :return: 
        {
            "statuses": [
                {
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
                },
                ...
            ],
            "previous_cursor": 0,
            "next_cursor": 11488013766,
            "total_number": 81655
        }

        """
        return self.request("get", "statuses/timeline_batch.json", params=kwargs)

    def repost_timeline(self, **kwargs):
        """
        访问级别：普通接口
        频次限制：是
        获取指定微博的转发微博列表
        
                            必选	    类型及范围	说明
        id	                true	int64	需要查询的微博ID。
        since_id	        false	int64	若指定此参数，则返回ID比since_id大的微博（即比since_id时间晚的微博），默认为0。
        max_id	            false	int64	若指定此参数，则返回ID小于或等于max_id的微博，默认为0。
        count	            false	int	    单页返回的记录条数，最大不超过200，默认为20。
        page	            false	int	    返回结果的页码，默认为1。
        filter_by_author	false	int	    作者筛选类型，0：全部、1：我关注的人、2：陌生人，默认为0。
        
        
        
        返回值字段	字段类型	字段说明
        idstr	string	字符串型的微博ID
        created_at	string	创建时间
        id	int64	微博ID
        text	string	微博信息内容
        source	string	微博来源
        favorited	boolean	是否已收藏
        truncated	boolean	是否被截断
        in_reply_to_status_id	int64	（暂未支持）回复ID
        in_reply_to_user_id	int64	（暂未支持）回复人UID
        in_reply_to_screen_name	string	（暂未支持）回复人昵称
        mid	int64	微博MID
        bmiddle_pic	string	中等尺寸图片地址
        original_pic	string	原始图片地址
        thumbnail_pic	string	缩略图片地址
        reposts_count	int	转发数
        comments_count	int	评论数
        annotations	array	微博附加注释信息
        geo	object	地理信息字段
        user	object	微博作者的用户信息字段
        retweeted_status	object	转发的微博信息字段
        
        :param kwargs: 
        :return: 
        {
            "reposts": [
                {
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
                    },
                    "retweeted_status": {
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
                        "comments_count": 8,
                        "user": {
                            "id": 1073880650,
                            "screen_name": "檀木幻想",
                            "name": "檀木幻想",
                            "province": "11",
                            "city": "5",
                            "location": "北京 朝阳区",
                            "description": "请访问微博分析家。",
                            "url": "http://www.weibo007.com/",
                            "profile_image_url": "http://tp3.sinaimg.cn/1073880650/50/1285051202/1",
                            "domain": "woodfantasy",
                            "gender": "m",
                            "followers_count": 723,
                            "friends_count": 415,
                            "statuses_count": 587,
                            "favourites_count": 107,
                            "created_at": "Sat Nov 14 00:00:00 +0800 2009",
                            "following": true,
                            "allow_all_act_msg": true,
                            "remark": "",
                            "geo_enabled": true,
                            "verified": false,
                            "allow_all_comment": true,
                            "avatar_large": "http://tp3.sinaimg.cn/1073880650/180/1285051202/1",
                            "verified_reason": "",
                            "follow_me": true,
                            "online_status": 0,
                            "bi_followers_count": 199
                        }
                    }
                },
                ...
            ],
            "previous_cursor": 0,  // 暂未支持
            "next_cursor": 0,           // 暂未支持
            "total_number": 3
        }
        """
        return self.request("get", "statuses/repost_timeline.json", params=kwargs)

    def report_timeline_ids(self, **kwargs):
        """
        原创微博的最新转发微博的ID

        只返回授权用户的微博，非授权用户的微博将不返回；
        使用官方移动SDK调用，可多返回30%的非授权用户的微博
        
        	                必选	类型及范围	说明
        access_token	    true	string	采用OAuth授权方式为必填参数，OAuth授权后获得。
        id	                true	int64	需要查询的微博ID。
        since_id	        false	int64	若指定此参数，则返回ID比since_id大的微博（即比since_id时间晚的微博），默认为0。
        max_id	            false	int64	若指定此参数，则返回ID小于或等于max_id的微博，默认为0。
        count	            false	int	    单页返回的记录条数，最大不超过200，默认为20。
        page	            false	int	    返回结果的页码，默认为1。
        filter_by_author	false	int	    作者筛选类型，0：全部、1：我关注的人、2：陌生人，默认为0。
        
        
        :param kwargs: 
        :return: 
             {
                "statuses": [
                    "3382905382185354",
                    "3382905252160340",
                    "3382905235630562",
                    ...
                ],
                "previous_cursor": 0,  // 暂未支持
                "next_cursor": 0,          // 暂未支持
                "total_number": 16
            }
        """
        return self.request("get", "statuses/repost_timeline/ids.json", params=kwargs)

    def mentions(self, **kwargs):
        """
        
        访问级别：普通接口
        频次限制：是
        获取最新的提到登录用户的微博列表，即@我的微博
        
        注意事项:
        只返回授权用户的微博，非授权用户的微博将不返回；
        使用官方移动SDK调用，可多返回30%的非授权用户的微博；
        
                            必选	    类型及范围	说明
        ccess_token	        true	string	采用OAuth授权方式为必填参数，OAuth授权后获得。
        since_id	        false	int64	若指定此参数，则返回ID比since_id大的微博（即比since_id时间晚的微博），默认为0。
        max_id	            false	int64	若指定此参数，则返回ID小于或等于max_id的微博，默认为0。
        count	            false	int	    单页返回的记录条数，最大不超过200，默认为20。
        page	            false	int	    返回结果的页码，默认为1。
        filter_by_author	false	int	    作者筛选类型，0：全部、1：我关注的人、2：陌生人，默认为0。
        filter_by_source	false	int	    来源筛选类型，0：全部、1：来自微博、2：来自微群，默认为0。
        filter_by_type	    false	int	    原创筛选类型，0：全部微博、1：原创的微博，默认为0。
        
          
        返回值字段	字段类型	字段说明
        created_at	string	微博创建时间
        id	int64	微博ID
        mid	int64	微博MID
        idstr	string	字符串型的微博ID
        text	string	微博信息内容
        source	string	微博来源
        favorited	boolean	是否已收藏，true：是，false：否
        truncated	boolean	是否被截断，true：是，false：否
        in_reply_to_status_id	string	（暂未支持）回复ID
        in_reply_to_user_id	string	（暂未支持）回复人UID
        in_reply_to_screen_name	string	（暂未支持）回复人昵称
        thumbnail_pic	string	缩略图片地址，没有时不返回此字段
        bmiddle_pic	string	中等尺寸图片地址，没有时不返回此字段
        original_pic	string	原始图片地址，没有时不返回此字段
        geo	object	地理信息字段 详细
        user	object	微博作者的用户信息字段 详细
        retweeted_status	object	被转发的原微博信息字段，当该微博为转发微博时返回 详细
        reposts_count	int	转发数
        comments_count	int	评论数
        attitudes_count	int	表态数
        mlevel	int	暂未支持
        visible	object	微博的可见性及指定可见分组信息。该object中type取值，0：普通微博，1：私密微博，3：指定分组微博，4：密友微博；list_id为分组的组号
        pic_ids	object	微博配图ID。多图时返回多图ID，用来拼接图片url。用返回字段thumbnail_pic的地址配上该返回字段的图片ID，即可得到多个图片url。
        ad	object array	微博流内的推广微博ID
        
        :param kwargs: 
        :return: 
        {
            "statuses": [
                {
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
                },
                ...
            ],
            "previous_cursor": 0,                // 暂未支持
            "next_cursor": 11488013766, // 暂未支持
            "total_number": 81655
        }
        """
        return self.request("get", "statuses/mentions.json", params=kwargs)

    def mentions_ids(self, **kwargs):
        """
        访问级别：普通接口
        频次限制：是
        获取@当前用户的最新微博的ID
        
        只返回授权用户的微博，非授权用户的微博将不返回；
        使用官方移动SDK调用，可多返回30%的非授权用户的微博；
        
        
        请求参数
                            必选	    类型及范围	说明
        access_token	    true	string	采用OAuth授权方式为必填参数，OAuth授权后获得。
        since_id	        false	int64	若指定此参数，则返回ID比since_id大的微博（即比since_id时间晚的微博），默认为0。
        max_id	            false	int64	若指定此参数，则返回ID小于或等于max_id的微博，默认为0。
        count	            false	int	    单页返回的记录条数，最大不超过200，默认为20。
        page	            false	int	    返回结果的页码，默认为1。
        filter_by_author	false	int	    作者筛选类型，0：全部、1：我关注的人、2：陌生人，默认为0。
        filter_by_source	false	int	    来源筛选类型，0：全部、1：来自微博、2：来自微群，默认为0。
        filter_by_type	    false	int	    原创筛选类型，0：全部微博、1：原创的微博，默认为0。
        
        :param kwargs: 
        :return: 
        
        {
            "statuses": [
                "3382905382185354",
                "3382905252160340",
                "3382905235630562",
                ...
            ],
            "previous_cursor": 0,    // 暂未支持
            "next_cursor": 0,             // 暂未支持
            "total_number": 16
        }
        """
        return self.request("get", "statuses/mentions/ids.json", params=kwargs)

    def bilateral_timeline(self, **kwargs):
        """
        访问级别：普通接口
        频次限制：是
        获取双向关注用户的最新微博
        
        请求参数
                        必选	    类型及范围	说明
        access_token	true	string	采用OAuth授权方式为必填参数，OAuth授权后获得。
        since_id	    false	int64	若指定此参数，则返回ID比since_id大的微博（即比since_id时间晚的微博），默认为0。
        max_id	        false	int64	若指定此参数，则返回ID小于或等于max_id的微博，默认为0。
        count	        false	int	    单页返回的记录条数，最大不超过100，默认为20。
        page	        false	int	    返回结果的页码，默认为1。
        base_app	    false	int	    是否只获取当前应用的数据。0为否（所有数据），1为是（仅当前应用），默认为0。
        feature	        false	int	    过滤类型ID，0：全部、1：原创、2：图片、3：视频、4：音乐，默认为0。
        trim_user	    false	int	    返回值中user字段开关，0：返回完整user字段、1：user字段仅返回user_id，默认为0。
        
        
        返回字段说明
        返回值字段	字段类型	字段说明
        created_at	string	微博创建时间
        id	int64	微博ID
        mid	int64	微博MID
        idstr	string	字符串型的微博ID
        text	string	微博信息内容
        source	string	微博来源
        favorited	boolean	是否已收藏，true：是，false：否
        truncated	boolean	是否被截断，true：是，false：否
        in_reply_to_status_id	string	（暂未支持）回复ID
        in_reply_to_user_id	string	（暂未支持）回复人UID
        in_reply_to_screen_name	string	（暂未支持）回复人昵称
        thumbnail_pic	string	缩略图片地址，没有时不返回此字段
        bmiddle_pic	string	中等尺寸图片地址，没有时不返回此字段
        original_pic	string	原始图片地址，没有时不返回此字段
        geo	object	地理信息字段 详细
        user	object	微博作者的用户信息字段 详细
        retweeted_status	object	被转发的原微博信息字段，当该微博为转发微博时返回 详细
        reposts_count	int	转发数
        comments_count	int	评论数
        attitudes_count	int	表态数
        mlevel	int	暂未支持
        visible	object	微博的可见性及指定可见分组信息。该object中type取值，0：普通微博，1：私密微博，3：指定分组微博，4：密友微博；list_id为分组的组号
        pic_ids	object	微博配图ID。多图时返回多图ID，用来拼接图片url。用返回字段thumbnail_pic的地址配上该返回字段的图片ID，即可得到多个图片url。
        ad	object array	微博流内的推广微博ID
        
        :param kwargs: 
        :return: 
        {
            "statuses": [
                {
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
                },
                ...
            ],
            "previous_cursor": 0, // 暂未支持
            "next_cursor": 0,          // 暂未支持
            "total_number": 16
        }
        """
        return self.request("get", "statuses/bilateral_timeline.json", params=kwargs)

    def show(self, **kwargs):
        """
        访问级别：普通接口
        频次限制：是
        根据ID获取单条微博信息
        
        请求参数
 	                    必选	    类型及范围	说明
        access_token	true	string	采用OAuth授权方式为必填参数，OAuth授权后获得。
        id	            true	int64	需要获取的微博ID。
        
        返回字段说明
        返回值字段	字段类型	字段说明
        created_at	string	微博创建时间
        id	int64	微博ID
        mid	int64	微博MID
        idstr	string	字符串型的微博ID
        text	string	微博信息内容
        source	string	微博来源
        favorited	boolean	是否已收藏，true：是，false：否
        truncated	boolean	是否被截断，true：是，false：否
        in_reply_to_status_id	string	（暂未支持）回复ID
        in_reply_to_user_id	string	（暂未支持）回复人UID
        in_reply_to_screen_name	string	（暂未支持）回复人昵称
        thumbnail_pic	string	缩略图片地址，没有时不返回此字段
        bmiddle_pic	string	中等尺寸图片地址，没有时不返回此字段
        original_pic	string	原始图片地址，没有时不返回此字段
        geo	object	地理信息字段 详细
        user	object	微博作者的用户信息字段 详细
        retweeted_status	object	被转发的原微博信息字段，当该微博为转发微博时返回 详细
        reposts_count	int	转发数
        comments_count	int	评论数
        attitudes_count	int	表态数
        mlevel	int	暂未支持
        visible	object	微博的可见性及指定可见分组信息。该object中type取值，0：普通微博，1：私密微博，3：指定分组微博，4：密友微博；list_id为分组的组号
        pic_ids	object	微博配图ID。多图时返回多图ID，用来拼接图片url。用返回字段thumbnail_pic的地址配上该返回字段的图片ID，即可得到多个图片url。
        ad	object array	微博流内的推广微博ID
        :param kwargs: 
        :return: 
        {
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
        """
        return self.request("get", "statuses/show.json", params=kwargs)

    def show_batch(self, **kwargs):
        """
        访问级别：高级接口（需要授权）
        频次限制：是
        根据微博ID批量获取微博信息 
        
        当微博已经被删除时，返回的微博ID以及text字段，text字段值为：“此微博已被原作者删除。”其余字段置为空值；
        部分微博ID出错时，仅返回成功获取的微博，全部微博ID出错，则返回错误信息；
        查询的微博必须是授权用户发出的，非授权用户发出的将不返回数据；
        
        
        请求参数
                        必选	    类型及范围	说明
        access_token	true	string	    采用OAuth授权方式为必填参数，OAuth授权后获得。
        ids	            true	string	    需要查询的微博ID，用半角逗号分隔，最多不超过50个。
        trim_user	    false	int	        返回值中user字段开关，0：返回完整user字段、1：user字段仅返回user_id，默认为0。
        
        
        返回字段说明
        返回值字段	字段类型	字段说明
        created_at	string	微博创建时间
        id	int64	微博ID
        mid	int64	微博MID
        idstr	string	字符串型的微博ID
        text	string	微博信息内容
        source	string	微博来源
        favorited	boolean	是否已收藏，true：是，false：否
        truncated	boolean	是否被截断，true：是，false：否
        in_reply_to_status_id	string	（暂未支持）回复ID
        in_reply_to_user_id	string	（暂未支持）回复人UID
        in_reply_to_screen_name	string	（暂未支持）回复人昵称
        thumbnail_pic	string	缩略图片地址，没有时不返回此字段
        bmiddle_pic	string	中等尺寸图片地址，没有时不返回此字段
        original_pic	string	原始图片地址，没有时不返回此字段
        geo	object	地理信息字段 详细
        user	object	微博作者的用户信息字段 详细
        retweeted_status	object	被转发的原微博信息字段，当该微博为转发微博时返回 详细
        reposts_count	int	转发数
        comments_count	int	评论数
        attitudes_count	int	表态数
        mlevel	int	暂未支持
        visible	object	微博的可见性及指定可见分组信息。该object中type取值，0：普通微博，1：私密微博，3：指定分组微博，4：密友微博；list_id为分组的组号
        pic_ids	object	微博配图ID。多图时返回多图ID，用来拼接图片url。用返回字段thumbnail_pic的地址配上该返回字段的图片ID，即可得到多个图片url。
        ad	object array	微博流内的推广微博ID
        
        
        :param kwargs: 
        :return: 
        {
            "statuses": [
                {
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
                },
                ...
            ],
            "previous_cursor": 0,
            "next_cursor": 0,
            "total_number": 16,
            "states": [
                {
                    "id": 11488058246,
                    "state": 0
                },
                ...
            ]
        }
        """
        return self.request("get", "statuses/show_batch.json", params=kwargs)

    def querymid(self, **kwargs):
        """
        
        访问级别：普通接口
        频次限制：是
        通过id获取mid
        
        请求参数
                        必选	    类型及范围	说明
        id	            true	int64	需要查询的微博（评论、私信）ID，批量模式下，用半角逗号分隔，最多不超过20个。
        type	        true	int	    获取类型，1：微博、2：评论、3：私信，默认为1。
        is_batch	    false	int	    是否使用批量模式，0：否、1：是，默认为0。
        :param kwargs: 
        :return: 
        {
            "mid": "8Ras3qlz"
        }
        """
        return self.request("get", "statuses/querymid.json", params=kwargs)

    def queryid(self, **kwargs):
        """
        访问级别：普通接口
        频次限制：是
        
        通过mid获取id
        

        形如“3z4efAo4lk”的MID即为经过base62转换的MID
        
        请求参数
                        必选	    类型及范围	说明
        access_token	true	string	采用OAuth授权方式为必填参数，OAuth授权后获得。
        mid	            true	string	需要查询的微博（评论、私信）MID，批量模式下，用半角逗号分隔，最多不超过20个。
        type	        true	int	    获取类型，1：微博、2：评论、3：私信，默认为1。
        is_batch	    false	int	    是否使用批量模式，0：否、1：是，默认为0。
        inbox	        false	int	    仅对私信有效，当MID类型为私信时用此参数，0：发件箱、1：收件箱，默认为0 。
        isBase62	    false	int	    MID是否是base62编码，0：否、1：是，默认为0。
        :param kwargs: 
        :return: 
        {
            "id": "7987885345"
        }
        """
        return self.request("get", "statuses/queryid.json", params=kwargs)

    def count(self, **kwargs):
        """
        访问级别：普通接口
        频次限制：是
        批量获取指定微博的转发数评论数
        
        
        请求参数
                        必选	    类型及范围	说明
        access_token	true	string	采用OAuth授权方式为必填参数，OAuth授权后获得。
        ids	            true	string	需要获取数据的微博ID，多个之间用逗号分隔，最多不超过100个。
        
        返回字段说明
        返回值字段	字段类型	字段说明
        id	int64	微博ID
        comments	int	评论数
        reposts	int	转发数
        attitudes	int	暂未支持
        
        :param kwargs: 
        :return: 
        [
            {
                "id": "32817222",
                "comments": "16",
                "reposts": "38"
            },
           ...
        ]
        """
        return self.request("get", "statuses/count.json", params=kwargs)

    def go(self, **kwargs):
        """
        访问级别：普通接口
        频次限制：是
        根据ID跳转到单条微博页
        
        
            必选	类型及范围	说明
        source	false	string	采用OAuth授权方式不需要此参数，其他授权方式为必填参数，数值为应用的AppKey。
        access_token	false	string	采用OAuth授权方式为必填参数，其他授权方式不需要此参数，OAuth授权后获得。
        uid	true	int64	需要跳转的用户ID。
        id	true	int64	需要跳转的微博ID。
        
        //成功返回
        无，跳转到指定的单条微博页
        
        //失败返回
        无，跳转到微博首页
        
        :param kwargs: 
        :return: None
        """
        # todo test
        self.request("get", "statuses/go", params=kwargs)

    def emotions(self, **kwargs):
        """
        
        访问级别：普通接口
        频次限制：否
        获取官方表情
        
        请求参数
                        必选	    类型及范围	说明
        type	        false	string	表情类别，face：普通表情、ani：魔法表情、cartoon：动漫表情，默认为face。
        language	    false	string	语言类别，cnname：简体、twname：繁体，默认为cnname。
        
        
        :param kwargs: 
        :return: 
        
        [
            {
                "category": "休闲",
                "common": true,
                "hot": false,
                "icon": "http://img.t.sinajs.cn/t35/style/images/common/face/ext/normal/eb/smile.gif",
                "phrase": "[呵呵]",
                "picid": null,
                "type": "face",
                "url": "http://img.t.sinajs.cn/t35/style/images/common/face/ext/normal/eb/smile.gif",
                "value": "[呵呵]"
            },
            ...
        ]
        """
        return self.request("get", "emotions.json", data=kwargs)

    def share(self, files, **kwargs):
        """
        访问级别：普通接口
        频次限制：是
        第三方分享链接到微博
        
        请求参数
                        必选	    类型及范围	说明
        access_token	true	string	    采用OAuth授权方式为必填参数，OAuth授权后获得。
        status	        true	string	    用户分享到微博的文本内容，必须做URLencode，内容不超过140个汉字，文本中不能包含“#话题词#”，同时文本中必须包含至少一个第三方分享到微博的网页URL，且该URL只能是该第三方（调用方）绑定域下的URL链接，绑定域在“我的应用 － 应用信息 － 基本应用信息编辑 － 安全域名”里设置。
        pic         	true	binary	    用户想要分享到微博的图片，仅支持JPEG、GIF、PNG图片，上传图片大小限制为<5M。上传图片时，POST方式提交请求，需要采用multipart/form-data编码方式。
        rip	            false	string	    开发者上报的操作用户真实IP，形如：211.156.0.1。
        
        
        返回值字段	字段类型	字段说明
        created_at	string	微博创建时间
        id	int64	微博ID
        mid	int64	微博MID
        idstr	string	字符串型的微博ID
        text	string	微博信息内容
        source	string	微博来源
        favorited	boolean	是否已收藏，true：是，false：否
        truncated	boolean	是否被截断，true：是，false：否
        in_reply_to_status_id	string	（暂未支持）回复ID
        in_reply_to_user_id	string	（暂未支持）回复人UID
        in_reply_to_screen_name	string	（暂未支持）回复人昵称
        thumbnail_pic	string	缩略图片地址，没有时不返回此字段
        bmiddle_pic	string	中等尺寸图片地址，没有时不返回此字段
        original_pic	string	原始图片地址，没有时不返回此字段
        geo	object	地理信息字段 详细
        user	object	微博作者的用户信息字段 详细
        retweeted_status	object	被转发的原微博信息字段，当该微博为转发微博时返回 详细
        reposts_count	int	转发数
        comments_count	int	评论数
        attitudes_count	int	表态数
        mlevel	int	暂未支持
        visible	object	微博的可见性及指定可见分组信息。该object中type取值，0：普通微博，1：私密微博，3：指定分组微博，4：密友微博；list_id为分组的组号
        pic_ids	object	微博配图ID。多图时返回多图ID，用来拼接图片url。用返回字段thumbnail_pic的地址配上该返回字段的图片ID，即可得到多个图片url。
        ad	object array	微博流内的推广微博ID

        
        :param kwargs: 
        :return: 
        {
            "created_at": "Wed Oct 24 23:49:17 +0800 2012",
            "id": 3504803600500000,
            "mid": "3504803600502730",
            "idstr": "3504803600502730",
            "text": "分组定向图片微博",
            "source": "新浪微博</a>",
            "favorited": false,
            "truncated": false,
            "in_reply_to_status_id": "",
            "in_reply_to_user_id": "",
            "in_reply_to_screen_name": "",
            "thumbnail_pic": "http://ww2.sinaimg.cn/thumbnail/71666d49jw1dy6q8t3p0rj.jpg",
            "bmiddle_pic": "http://ww2.sinaimg.cn/bmiddle/71666d49jw1dy6q8t3p0rj.jpg",
            "original_pic": "http://ww2.sinaimg.cn/large/71666d49jw1dy6q8t3p0rj.jpg",
            "geo": {
                "type": "Point",
                "coordinates": [
                    40.413467,
                    116.646439
                ]
            },
            "user": {
                "id": 1902538057,
                "idstr": "1902538057",
                "screen_name": "张三",
                "name": "张三",
                "province": "11",
                "city": "8",
                "location": "北京 海淀区",
                "description": "做最受尊敬的互联网产品经理...",
                "url": "",
                "profile_image_url": "http://tp2.sinaimg.cn/1902538057/50/22817372040/1",
                "profile_url": "304270168",
                "domain": "shenbinzhu",
                "weihao": "304270168",
                "gender": "m",
                "followers_count": 337,
                "friends_count": 534,
                "statuses_count": 516,
                "favourites_count": 60,
                "created_at": "Sat Dec 25 14:12:35 +0800 2010",
                "following": false,
                "allow_all_act_msg": true,
                "geo_enabled": true,
                "verified": false,
                "verified_type": 220,
                "allow_all_comment": true,
                "avatar_large": "http://tp2.sinaimg.cn/1902538057/180/22817372040/1",
                "verified_reason": "",
                "follow_me": false,
                "online_status": 0,
                "bi_followers_count": 185,
                "lang": "zh-cn",
                "level": 7,
                "type": 1,
                "ulevel": 0,
                "badge": {
                    "kuainv": {
                        "level": 0
                    },
                    "uc_domain": 0,
                    "enterprise": 0,
                    "anniversary": 0
                }
            },
            "reposts_count": 0,
            "comments_count": 0,
            "attitudes_count": 0,
            "mlevel": 0,
            "visible": {
                "type": 3,
                "list_id": 3469454702570000
            }
        }
        """
        return self.request("post", "statuses/share.json", data=kwargs, files=files)

    def repost(self, **kwargs):
        """
        访问级别：普通接口
        频次限制：是
        转发一条微博信息
        
        请求参数
                        必选	    类型及范围	说明
        access_token	true	string	采用OAuth授权方式为必填参数，OAuth授权后获得。
        id	            true	int64	要转发的微博ID。
        status	        false	string	添加的转发文本，必须做URLencode，内容不超过140个汉字，不填则默认为“转发微博”。
        is_comment	    false	int	    是否在转发的同时发表评论，0：否、1：评论给当前微博、2：评论给原微博、3：都评论，默认为0 。
        rip	            false	string	开发者上报的操作用户真实IP，形如：211.156.0.1。
        
                返回字段说明
        返回值字段	字段类型	字段说明
        idstr	string	字符串型的微博ID
        created_at	string	创建时间
        id	int64	微博ID
        text	string	微博信息内容
        source	string	微博来源
        favorited	boolean	是否已收藏
        truncated	boolean	是否被截断
        in_reply_to_status_id	int64	（暂未支持）回复ID
        in_reply_to_user_id	int64	（暂未支持）回复人UID
        in_reply_to_screen_name	string	（暂未支持）回复人昵称
        mid	int64	微博MID
        bmiddle_pic	string	中等尺寸图片地址
        original_pic	string	原始图片地址
        thumbnail_pic	string	缩略图片地址
        reposts_count	int	转发数
        comments_count	int	评论数
        annotations	array	微博附加注释信息
        geo	object	地理信息字段
        user	object	微博作者的用户信息字段
        retweeted_status	object	转发的微博信息字段
        
        :param kwargs: 
        :return: 
        {
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
            },
            "retweeted_status": {
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
                "comments_count": 8,
                "user": {
                    "id": 1073880650,
                    "screen_name": "檀木幻想",
                    "name": "檀木幻想",
                    "province": "11",
                    "city": "5",
                    "location": "北京 朝阳区",
                    "description": "请访问微博分析家。",
                    "url": "http://www.weibo007.com/",
                    "profile_image_url": "http://tp3.sinaimg.cn/1073880650/50/1285051202/1",
                    "domain": "woodfantasy",
                    "gender": "m",
                    "followers_count": 723,
                    "friends_count": 415,
                    "statuses_count": 587,
                    "favourites_count": 107,
                    "created_at": "Sat Nov 14 00:00:00 +0800 2009",
                    "following": true,
                    "allow_all_act_msg": true,
                    "remark": "",
                    "geo_enabled": true,
                    "verified": false,
                    "allow_all_comment": true,
                    "avatar_large": "http://tp3.sinaimg.cn/1073880650/180/1285051202/1",
                    "verified_reason": "",
                    "follow_me": true,
                    "online_status": 0,
                    "bi_followers_count": 199
                }
            }
        }
        """
        return self.request("post", "statuses/repost.json", data=kwargs)

    def destroy(self, **kwargs):
        """
        访问级别：普通接口
        频次限制：是
        删除微博信息
        
        请求参数
                        必选	    类型及范围	说明
        access_token	true	string	    采用OAuth授权方式为必填参数，OAuth授权后获得。
        id	            true	int64	    需要删除的微博ID。
        
        
        返回字段说明
        返回值字段	字段类型	字段说明
        created_at	string	微博创建时间
        id	int64	微博ID
        mid	int64	微博MID
        idstr	string	字符串型的微博ID
        text	string	微博信息内容
        source	string	微博来源
        favorited	boolean	是否已收藏，true：是，false：否
        truncated	boolean	是否被截断，true：是，false：否
        in_reply_to_status_id	string	（暂未支持）回复ID
        in_reply_to_user_id	string	（暂未支持）回复人UID
        in_reply_to_screen_name	string	（暂未支持）回复人昵称
        thumbnail_pic	string	缩略图片地址，没有时不返回此字段
        bmiddle_pic	string	中等尺寸图片地址，没有时不返回此字段
        original_pic	string	原始图片地址，没有时不返回此字段
        geo	object	地理信息字段 详细
        user	object	微博作者的用户信息字段 详细
        retweeted_status	object	被转发的原微博信息字段，当该微博为转发微博时返回 详细
        reposts_count	int	转发数
        comments_count	int	评论数
        attitudes_count	int	表态数
        mlevel	int	暂未支持
        visible	object	微博的可见性及指定可见分组信息。该object中type取值，0：普通微博，1：私密微博，3：指定分组微博，4：密友微博；list_id为分组的组号
        pic_ids	object	微博配图ID。多图时返回多图ID，用来拼接图片url。用返回字段thumbnail_pic的地址配上该返回字段的图片ID，即可得到多个图片url。
        ad	object array	微博流内的推广微博ID
        
        :param kwargs: 
        :return: 
        
        {
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
        """
        return self.request("post", "statuses/destroy.json", data=kwargs)

    def update(self, **kwargs):
        """
        访问级别：普通接口
        频次限制：是
        发布一条新微博
        
        连续两次发布的微博不可以重复；
        非会员发表定向微博，分组成员数最多200。
        

                        必选	    类型及范围	说明
        access_token	true	string	    采用OAuth授权方式为必填参数，OAuth授权后获得。
        status	        true	string	    要发布的微博文本内容，必须做URLencode，内容不超过140个汉字。
        visible	        false	int	        微博的可见性，0：所有人能看，1：仅自己可见，2：密友可见，3：指定分组可见，默认为0。
        list_id	        false	string	    微博的保护投递指定分组ID，只有当visible参数为3时生效且必选。
        lat	            false	float	    纬度，有效范围：-90.0到+90.0，+表示北纬，默认为0.0。
        long	        false	float	    经度，有效范围：-180.0到+180.0，+表示东经，默认为0.0。
        annotations	    false	string	    元数据，主要是为了方便第三方应用记录一些适合于自己使用的信息，每条微博可以包含一个或者多个元数据，必须以json字串的形式提交，字串长度不超过512个字符，具体内容可以自定。
        rip	            false	string	    开发者上报的操作用户真实IP，形如：211.156.0.1。
        发布一条微博信息
        
        返回字段说明
        返回值字段	字段类型	字段说明
        created_at	string	微博创建时间
        id	int64	微博ID
        mid	int64	微博MID
        idstr	string	字符串型的微博ID
        text	string	微博信息内容
        source	string	微博来源
        favorited	boolean	是否已收藏，true：是，false：否
        truncated	boolean	是否被截断，true：是，false：否
        in_reply_to_status_id	string	（暂未支持）回复ID
        in_reply_to_user_id	string	（暂未支持）回复人UID
        in_reply_to_screen_name	string	（暂未支持）回复人昵称
        thumbnail_pic	string	缩略图片地址，没有时不返回此字段
        bmiddle_pic	string	中等尺寸图片地址，没有时不返回此字段
        original_pic	string	原始图片地址，没有时不返回此字段
        geo	object	地理信息字段 详细
        user	object	微博作者的用户信息字段 详细
        retweeted_status	object	被转发的原微博信息字段，当该微博为转发微博时返回 详细
        reposts_count	int	转发数
        comments_count	int	评论数
        attitudes_count	int	表态数
        mlevel	int	暂未支持
        visible	object	微博的可见性及指定可见分组信息。该object中type取值，0：普通微博，1：私密微博，3：指定分组微博，4：密友微博；list_id为分组的组号
        pic_ids	object	微博配图ID。多图时返回多图ID，用来拼接图片url。用返回字段thumbnail_pic的地址配上该返回字段的图片ID，即可得到多个图片url。
        ad	object array	微博流内的推广微博ID
        
        :param kwargs: 
        :return:
         
         {
            "created_at": "Wed Oct 24 23:39:10 +0800 2012",
            "id": 3504801050130000,
            "mid": "3504801050130827",
            "idstr": "3504801050130827",
            "text": "定向分组内容。",
            "source": "新浪微博</a>",
            "favorited": false,
            "truncated": false,
            "in_reply_to_status_id": "",
            "in_reply_to_user_id": "",
            "in_reply_to_screen_name": "",
            "geo": {
                "type": "Point",
                "coordinates": [
                    40.413467,
                    116.646439
                ]
            },
            "user": {
                "id": 1902538057,
                "idstr": "1902538057",
                "screen_name": "张三",
                "name": "张三",
                "province": "11",
                "city": "8",
                "location": "北京 海淀区",
                "description": "做最受尊敬的互联网产品经理...",
                "url": "",
                "profile_image_url": "http://tp2.sinaimg.cn/1902538057/50/22817372040/1",
                "profile_url": "304270168",
                "domain": "shenbinzhu",
                "weihao": "304270168",
                "gender": "m",
                "followers_count": 337,
                "friends_count": 534,
                "statuses_count": 516,
                "favourites_count": 60,
                "created_at": "Sat Dec 25 14:12:35 +0800 2010",
                "following": false,
                "allow_all_act_msg": true,
                "geo_enabled": true,
                "verified": false,
                "verified_type": 220,
                "allow_all_comment": true,
                "avatar_large": "http://tp2.sinaimg.cn/1902538057/180/22817372040/1",
                "verified_reason": "",
                "follow_me": false,
                "online_status": 0,
                "bi_followers_count": 185,
                "lang": "zh-cn",
                "level": 7,
                "type": 1,
                "ulevel": 0,
                "badge": {
                    "kuainv": {
                        "level": 0
                    },
                    "uc_domain": 0,
                    "enterprise": 0,
                    "anniversary": 0
                }
            },
            "annotations": [
                {
                    "aa": "cc"
                }
            ],
            "reposts_count": 0,
            "comments_count": 0,
            "attitudes_count": 0,
            "mlevel": 0,
            "visible": {
                "type": 3,
                "list_id": 3469454702570000
            }
        }
        """
        return self.request("post", "statuses/update.json", data=kwargs)

    def upload(self, files, **kwargs):
        """
        上传图片并发布一条微博
        访问级别：普通接口
        频次限制：是
        
        
        请求必须用POST方式提交，并且注意采用multipart/form-data编码方式；
        非会员发表定向微博，分组成员数最多200。
        
         	            必选	类型及范围	说明
        access_token	true	string	采用OAuth授权方式为必填参数，OAuth授权后获得。
        status	        true	string	要发布的微博文本内容，必须做URLencode，内容不超过140个汉字。
        visible	        false	int	微博的可见性，0：所有人能看，1：仅自己可见，2：密友可见，3：指定分组可见，默认为0。
        list_id	        false	string	微博的保护投递指定分组ID，只有当visible参数为3时生效且必选。
        pic	            true	binary	要上传的图片，仅支持JPEG、GIF、PNG格式，图片大小小于5M。
        lat	            false	float	纬度，有效范围：-90.0到+90.0，+表示北纬，默认为0.0。
        long	        false	float	经度，有效范围：-180.0到+180.0，+表示东经，默认为0.0。
        annotations	    false	string	元数据，主要是为了方便第三方应用记录一些适合于自己使用的信息，每条微博可以包含一个或者多个元数据，必须以json字串的形式提交，字串长度不超过512个字符，具体内容可以自定。
        rip	            false	string	开发者上报的操作用户真实IP，形如：211.156.0.1。
        
        字段说明
        返回值字段	字段类型	字段说明
        created_at	string	微博创建时间
        id	int64	微博ID
        mid	int64	微博MID
        idstr	string	字符串型的微博ID
        text	string	微博信息内容
        source	string	微博来源
        favorited	boolean	是否已收藏，true：是，false：否
        truncated	boolean	是否被截断，true：是，false：否
        in_reply_to_status_id	string	（暂未支持）回复ID
        in_reply_to_user_id	string	（暂未支持）回复人UID
        in_reply_to_screen_name	string	（暂未支持）回复人昵称
        thumbnail_pic	string	缩略图片地址，没有时不返回此字段
        bmiddle_pic	string	中等尺寸图片地址，没有时不返回此字段
        original_pic	string	原始图片地址，没有时不返回此字段
        geo	object	地理信息字段 详细
        user	object	微博作者的用户信息字段 详细
        retweeted_status	object	被转发的原微博信息字段，当该微博为转发微博时返回 详细
        reposts_count	int	转发数
        comments_count	int	评论数
        attitudes_count	int	表态数
        mlevel	int	暂未支持
        visible	object	微博的可见性及指定可见分组信息。该object中type取值，0：普通微博，1：私密微博，3：指定分组微博，4：密友微博；list_id为分组的组号
        pic_ids	object	微博配图ID。多图时返回多图ID，用来拼接图片url。用返回字段thumbnail_pic的地址配上该返回字段的图片ID，即可得到多个图片url。
        ad	object array	微博流内的推广微博ID
        
        :param files: pic files
        :param kwargs: 
        :return: 
        
        {
            "created_at": "Wed Oct 24 23:49:17 +0800 2012",
            "id": 3504803600500000,
            "mid": "3504803600502730",
            "idstr": "3504803600502730",
            "text": "分组定向图片微博",
            "source": "新浪微博</a>",
            "favorited": false,
            "truncated": false,
            "in_reply_to_status_id": "",
            "in_reply_to_user_id": "",
            "in_reply_to_screen_name": "",
            "thumbnail_pic": "http://ww2.sinaimg.cn/thumbnail/71666d49jw1dy6q8t3p0rj.jpg",
            "bmiddle_pic": "http://ww2.sinaimg.cn/bmiddle/71666d49jw1dy6q8t3p0rj.jpg",
            "original_pic": "http://ww2.sinaimg.cn/large/71666d49jw1dy6q8t3p0rj.jpg",
            "geo": {
                "type": "Point",
                "coordinates": [
                    40.413467,
                    116.646439
                ]
            },
            "user": {
                "id": 1902538057,
                "idstr": "1902538057",
                "screen_name": "张三",
                "name": "张三",
                "province": "11",
                "city": "8",
                "location": "北京 海淀区",
                "description": "做最受尊敬的互联网产品经理...",
                "url": "",
                "profile_image_url": "http://tp2.sinaimg.cn/1902538057/50/22817372040/1",
                "profile_url": "304270168",
                "domain": "shenbinzhu",
                "weihao": "304270168",
                "gender": "m",
                "followers_count": 337,
                "friends_count": 534,
                "statuses_count": 516,
                "favourites_count": 60,
                "created_at": "Sat Dec 25 14:12:35 +0800 2010",
                "following": false,
                "allow_all_act_msg": true,
                "geo_enabled": true,
                "verified": false,
                "verified_type": 220,
                "allow_all_comment": true,
                "avatar_large": "http://tp2.sinaimg.cn/1902538057/180/22817372040/1",
                "verified_reason": "",
                "follow_me": false,
                "online_status": 0,
                "bi_followers_count": 185,
                "lang": "zh-cn",
                "level": 7,
                "type": 1,
                "ulevel": 0,
                "badge": {
                    "kuainv": {
                        "level": 0
                    },
                    "uc_domain": 0,
                    "enterprise": 0,
                    "anniversary": 0
                }
            },
            "reposts_count": 0,
            "comments_count": 0,
            "attitudes_count": 0,
            "mlevel": 0,
            "visible": {
                "type": 3,
                "list_id": 3469454702570000
            }
        }
        """
        return self.request("post", "statuses/upload.json", data=kwargs, files=files)

    def upload_url_text(self, **kwargs):
        """
        访问级别：高级接口（需要授权）
        频次限制：是
        发布一条微博同时指定上传的图片或图片url
        
        picid或url必选一个，两个参数都存在时，取picid参数的值为准；
        连续两次发布的微博不可以重复；
        非会员发表定向微博，分组成员数最多200。
        
        请求参数
                        必选	    类型及范围	说明
        access_token	true	string	采用OAuth授权方式为必填参数，OAuth授权后获得。
        status	        false	string	要发布的微博文本内容，必须做URLencode，内容不超过140个汉字。
        visible	        false	int	    微博的可见性，0：所有人能看，1：仅自己可见，2：密友可见，3：指定分组可见，默认为0。
        list_id	        false	string	微博的保护投递指定分组ID，只有当visible参数为3时生效且必选。
        url	            false	string	图片的URL地址，必须以http开头。
        pic_id	        false	string	已经上传的图片pid，多个时使用英文半角逗号符分隔，最多不超过9个。
        lat	            false	float	纬度，有效范围：-90.0到+90.0，+表示北纬，默认为0.0。
        long	        false	float	经度，有效范围：-180.0到+180.0，+表示东经，默认为0.0。
        annotations	    false	string	元数据，主要是为了方便第三方应用记录一些适合于自己使用的信息，每条微博可以包含一个或者多个元数据，必须以json字串的形式提交，字串长度不超过512个字符，具体内容可以自定。
        rip	            false	string	开发者上报的操作用户真实IP，形如：211.156.0.1。
        
        
        
        返回值字段	字段类型	字段说明
        created_at	string	微博创建时间
        id	int64	微博ID
        mid	int64	微博MID
        idstr	string	字符串型的微博ID
        text	string	微博信息内容
        source	string	微博来源
        favorited	boolean	是否已收藏，true：是，false：否
        truncated	boolean	是否被截断，true：是，false：否
        in_reply_to_status_id	string	（暂未支持）回复ID
        in_reply_to_user_id	string	（暂未支持）回复人UID
        in_reply_to_screen_name	string	（暂未支持）回复人昵称
        thumbnail_pic	string	缩略图片地址，没有时不返回此字段
        bmiddle_pic	string	中等尺寸图片地址，没有时不返回此字段
        original_pic	string	原始图片地址，没有时不返回此字段
        geo	object	地理信息字段 详细
        user	object	微博作者的用户信息字段 详细
        retweeted_status	object	被转发的原微博信息字段，当该微博为转发微博时返回 详细
        reposts_count	int	转发数
        comments_count	int	评论数
        attitudes_count	int	表态数
        mlevel	int	暂未支持
        visible	object	微博的可见性及指定可见分组信息。该object中type取值，0：普通微博，1：私密微博，3：指定分组微博，4：密友微博；list_id为分组的组号
        pic_ids	object	微博配图ID。多图时返回多图ID，用来拼接图片url。用返回字段thumbnail_pic的地址配上该返回字段的图片ID，即可得到多个图片url。
        ad	object array	微博流内的推广微博ID
        
        :param kwargs: 
        :return: 
        
        {
            "created_at": "Wed Oct 24 23:49:17 +0800 2012",
            "id": 3504803600500000,
            "mid": "3504803600502730",
            "idstr": "3504803600502730",
            "text": "分组定向图片微博",
            "source": "新浪微博</a>",
            "favorited": false,
            "truncated": false,
            "in_reply_to_status_id": "",
            "in_reply_to_user_id": "",
            "in_reply_to_screen_name": "",
            "thumbnail_pic": "http://ww2.sinaimg.cn/thumbnail/71666d49jw1dy6q8t3p0rj.jpg",
            "bmiddle_pic": "http://ww2.sinaimg.cn/bmiddle/71666d49jw1dy6q8t3p0rj.jpg",
            "original_pic": "http://ww2.sinaimg.cn/large/71666d49jw1dy6q8t3p0rj.jpg",
            "geo": {
                "type": "Point",
                "coordinates": [
                    40.413467,
                    116.646439
                ]
            },
            "user": {
                "id": 1902538057,
                "idstr": "1902538057",
                "screen_name": "张三",
                "name": "张三",
                "province": "11",
                "city": "8",
                "location": "北京 海淀区",
                "description": "做最受尊敬的互联网产品经理...",
                "url": "",
                "profile_image_url": "http://tp2.sinaimg.cn/1902538057/50/22817372040/1",
                "profile_url": "304270168",
                "domain": "shenbinzhu",
                "weihao": "304270168",
                "gender": "m",
                "followers_count": 337,
                "friends_count": 534,
                "statuses_count": 516,
                "favourites_count": 60,
                "created_at": "Sat Dec 25 14:12:35 +0800 2010",
                "following": false,
                "allow_all_act_msg": true,
                "geo_enabled": true,
                "verified": false,
                "verified_type": 220,
                "allow_all_comment": true,
                "avatar_large": "http://tp2.sinaimg.cn/1902538057/180/22817372040/1",
                "verified_reason": "",
                "follow_me": false,
                "online_status": 0,
                "bi_followers_count": 185,
                "lang": "zh-cn",
                "level": 7,
                "type": 1,
                "ulevel": 0,
                "badge": {
                    "kuainv": {
                        "level": 0
                    },
                    "uc_domain": 0,
                    "enterprise": 0,
                    "anniversary": 0
                }
            },
            "reposts_count": 0,
            "comments_count": 0,
            "attitudes_count": 0,
            "mlevel": 0,
            "visible": {
                "type": 3,
                "list_id": 3469454702570000
            }
        }
        """
        return self.request("post", "statuses/upload_url_text.json", data=kwargs)
