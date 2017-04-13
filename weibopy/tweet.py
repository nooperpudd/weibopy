# encoding:utf-8

import requests

from .exceptions import WeiboAPIError

from .weibo import WeiboClient


class Tweet(WeiboClient):
    """
    """

    def public_timeline(self, **kwargs):
        """
        
        count	false	int	单页返回的记录条数，默认为50。
        page	false	int	返回结果的页码，默认为1。
        base_app	false	int	是否只获取当前应用的数据。0为否（所有数据），1为是（仅当前应用），默认为0。
        
        
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
        """
        url = self.base + "statuses/public_timeline.json"

        return self.request("get", url, params=kwargs)

    def home_timeline(self, **kwargs):
        """
                    必选	类型及范围	说明
        since_id	false	int64	若指定此参数，则返回ID比since_id大的微博（即比since_id时间晚的微博），默认为0。
        max_id	false	int64	若指定此参数，则返回ID小于或等于max_id的微博，默认为0。
        count	false	int	单页返回的记录条数，最大不超过100，默认为20。
        page	false	int	返回结果的页码，默认为1。
        base_app	false	int	是否只获取当前应用的数据。0为否（所有数据），1为是（仅当前应用），默认为0。
        feature	false	int	过滤类型ID，0：全部、1：原创、2：图片、3：视频、4：音乐，默认为0。
        trim_user	false	int	返回值中user字段开关，0：返回完整user字段、1：user字段仅返回user_id，默认为0。
        
        
        return:
        
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
        """

        url = self.base + "statuses/home_timeline.json"

        return self.request("get", url, params=kwargs)

    def friends_timeline_ids(self, **kwargs):
        """
        获取当前登录用户及其所关注用户的最新微博的ID
        
        since_id	false	int64	若指定此参数，则返回ID比since_id大的微博（即比since_id时间晚的微博），默认为0。
        max_id	false	int64	若指定此参数，则返回ID小于或等于max_id的微博，默认为0。
        count	false	int	单页返回的记录条数，最大不超过100，默认为20。
        page	false	int	返回结果的页码，默认为1。
        base_app	false	int	是否只获取当前应用的数据。0为否（所有数据），1为是（仅当前应用），默认为0。
        feature	false	int	过滤类型ID，0：全部、1：原创、2：图片、3：视频、4：音乐，默认为0
        
        
        response:
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
        
        :param kwargs: 
        :return: 
        """
        url = self.base + "statuses/friends_timeline/ids.json"

        return self.request("get", url, params=kwargs)

    def user_timeline(self, **kwargs):
        """
        uid	false	int64	需要查询的用户ID。
        screen_name	false	string	需要查询的用户昵称。
        since_id	false	int64	若指定此参数，则返回ID比since_id大的微博（即比since_id时间晚的微博），默认为0。
        max_id	false	int64	若指定此参数，则返回ID小于或等于max_id的微博，默认为0。
        count	false	int	单页返回的记录条数，最大不超过100，超过100以100处理，默认为20。
        page	false	int	返回结果的页码，默认为1。
        base_app	false	int	是否只获取当前应用的数据。0为否（所有数据），1为是（仅当前应用），默认为0。
        feature	false	int	过滤类型ID，0：全部、1：原创、2：图片、3：视频、4：音乐，默认为0。
        trim_user	false	int	返回值中user字段开关，0：返回完整user字段、1：user字段仅返回user_id，默认为0。
        
        
        获取自己的微博，参数uid与screen_name可以不填，则自动获取当前登录用户的微博；
        指定获取他人的微博，参数uid与screen_name二者必选其一，且只能选其一；
        接口升级后：uid与screen_name只能为当前授权用户；
        读取当前授权用户所有关注人最新微博列表，请使用：获取当前授权用户及其所关注用户的最新微博接口（statuses/home_timeline）；
        此接口最多只返回最新的5条数据，官方移动SDK调用可返回10条；
        
        
        
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
        """
        url = self.base + "statuses/user_timeline.json"
        return self.request("get", url, params=kwargs)

    def user_timeline_ids(self, **kwargs):
        """
        
        
        access_token	true	string	采用OAuth授权方式为必填参数，OAuth授权后获得。
        uid	false	int64	需要查询的用户ID。
        screen_name	false	string	需要查询的用户昵称。
        since_id	false	int64	若指定此参数，则返回ID比since_id大的微博（即比since_id时间晚的微博），默认为0。
        max_id	false	int64	若指定此参数，则返回ID小于或等于max_id的微博，默认为0。
        count	false	int	单页返回的记录条数，最大不超过100，默认为20。
        page	false	int	返回结果的页码，默认为1。
        base_app	false	int	是否只获取当前应用的数据。0为否（所有数据），1为是（仅当前应用），默认为0。
        feature	false	int	过滤类型ID，0：全部、1：原创、2：图片、3：视频、4：音乐，默认为0。
        
        
        参数uid与screen_name二者必选其一，且只能选其一，uid优先
        接口升级后：uid与screen_name只能为当前授权用户；
        读取当前授权用户所有关注人最新微博列表，请使用：获取当前授权用户及其所关注用户的最新微博接口（statuses/home_timeline）；
        此接口最多只返回最新的5条数据，官方移动SDK调用可返回10条；
        
        :param kwargs: 
        :return: 
        """
        url = self.base + "statuses/user_timeline/ids.json"

        return self.request("get", url, params=kwargs)
