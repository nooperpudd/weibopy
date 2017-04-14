# encoding:utf-8

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
        return self.request("get", "statuses/public_timeline.json",  params=kwargs)

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

        return self.request("get", "statuses/home_timeline.json", params=kwargs)

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
        return self.request("get", "statuses/friends_timeline/ids.json", params=kwargs)

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
        return self.request("get", "statuses/user_timeline.json", params=kwargs)

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
        return self.request("get", "statuses/user_timeline/ids.json", params=kwargs)

    def timeline_batch(self,**kwargs):
        """
        
        批量获取指定的一批用户的微博列表
        
        必选	类型及范围	说明
        access_token	true	string	采用OAuth授权方式为必填参数，OAuth授权后获得。
        uids	false	string	需要查询的用户ID，用半角逗号分隔，一次最多20个。
        screen_names	false	string	需要查询的用户昵称，用半角逗号分隔，一次最多20个。
        count	false	int	单页返回的记录条数，默认为20。
        page	false	int	返回结果的页码，默认为1。
        base_app	false	int	是否只获取当前应用的数据。0为否（所有数据），1为是（仅当前应用），默认为0。
        feature	false	int	过滤类型ID，0：全部、1：原创、2：图片、3：视频、4：音乐，默认为0。
        
        注意事项
        参数uids与screen_name二者必选其一，且只能选其一；
        查询的用户必须是调用应用的授权用户，非授权用户的微博将不返回；
        使用官方移动SDK调用，可多返回30%的非授权用户的微博；
        
        
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
        return self.request("get", "statuses/timeline_batch.json", params=kwargs)

    def repost_timeline(self,**kwargs):
        """
        获取指定微博的转发微博列表

        id	true	int64	需要查询的微博ID。
        since_id	false	int64	若指定此参数，则返回ID比since_id大的微博（即比since_id时间晚的微博），默认为0。
        max_id	false	int64	若指定此参数，则返回ID小于或等于max_id的微博，默认为0。
        count	false	int	单页返回的记录条数，最大不超过200，默认为20。
        page	false	int	返回结果的页码，默认为1。
        filter_by_author	false	int	作者筛选类型，0：全部、1：我关注的人、2：陌生人，默认为0。
        
        
        
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
        """
        return self.request("get", "statuses/repost_timeline.json", params=kwargs)

    def report_timeline_ids(self,**kwargs):
        """
        原创微博的最新转发微博的ID

        只返回授权用户的微博，非授权用户的微博将不返回；
        使用官方移动SDK调用，可多返回30%的非授权用户的微博
        
        access_token	true	string	采用OAuth授权方式为必填参数，OAuth授权后获得。
        id	true	int64	需要查询的微博ID。
        since_id	false	int64	若指定此参数，则返回ID比since_id大的微博（即比since_id时间晚的微博），默认为0。
        max_id	false	int64	若指定此参数，则返回ID小于或等于max_id的微博，默认为0。
        count	false	int	单页返回的记录条数，最大不超过200，默认为20。
        page	false	int	返回结果的页码，默认为1。
        filter_by_author	false	int	作者筛选类型，0：全部、1：我关注的人、2：陌生人，默认为0。
        
        
        
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
        
        :param kwargs: 
        :return: 
        """
        return self.request("get", "statuses/repost_timeline/ids.json", params=kwargs)

    def mentions(self,**kwargs):
        """
        
        获取最新的提到登录用户的微博列表，即@我的微博
        
        注意事项:
        只返回授权用户的微博，非授权用户的微博将不返回；
        使用官方移动SDK调用，可多返回30%的非授权用户的微博；
        
        ccess_token	true	string	采用OAuth授权方式为必填参数，OAuth授权后获得。
        since_id	false	int64	若指定此参数，则返回ID比since_id大的微博（即比since_id时间晚的微博），默认为0。
        max_id	false	int64	若指定此参数，则返回ID小于或等于max_id的微博，默认为0。
        count	false	int	单页返回的记录条数，最大不超过200，默认为20。
        page	false	int	返回结果的页码，默认为1。
        filter_by_author	false	int	作者筛选类型，0：全部、1：我关注的人、2：陌生人，默认为0。
        filter_by_source	false	int	来源筛选类型，0：全部、1：来自微博、2：来自微群，默认为0。
        filter_by_type	false	int	原创筛选类型，0：全部微博、1：原创的微博，默认为0。
        
          
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
        return self.request("get", "statuses/mentions.json", params=kwargs)

    def methions_ids(self,**kwargs):
        """
        获取@当前用户的最新微博的ID
        
        :param kwargs: 
        :return: 
        """

        pass
    def bilateral_timeline(self,**kwargs):
        """
        获取双向关注用户的最新微博
        :param kwargs: 
        :return: 
        """
        pass

    def show(self,**kwargs):
        """
        根据ID获取单条微博信息
        :param kwargs: 
        :return: 
        """
        pass
    def show_batch(self,**kwargs):
        """
        根据微博ID批量获取微博信息 
        :param kwargs: 
        :return: 
        """
        pass

    def querymid(self,**kwargs):
        """
        通过id获取mid
        :param kwargs: 
        :return: 
        """
        pass
    def queryid(self,**kwargs):
        """
        通过mid获取id
        :param kwargs: 
        :return: 
        """
        pass

    def count(self,**kwargs):
        """
        批量获取指定微博的转发数评论数
        :param kwargs: 
        :return: 
        """
        pass

    def go(self,**kwargs):
        """
        根据ID跳转到单条微博页
        :param kwargs: 
        :return: 
        """
        pass
    def emotions(self,**kwargs):
        """
        获取官方表情
        :param kwargs: 
        :return: 
        """
        pass

    def share(self,**kwargs):
        """
        第三方分享链接到微博
        :param kwargs: 
        :return: 
        """
        pass

    def repost(self,**kwargs):
        """
        转发一条微博信息
        :param kwargs: 
        :return: 
        """
        pass

    def destroy(self,**kwargs):
        """
        删除微博信息
        :param kwargs: 
        :return: 
        """
    def update(self,**kwargs):
        """
        发布一条微博信息
        :param kwargs: 
        :return: 
        """
        pass

    def upload(self,**kwargs):
        """
        上传图片并发布一条微博
        :param kwargs: 
        :return: 
        """
        pass

    def upload_url_text(self,**kwargs):
        """
        发布一条微博同时指定上传的图片或图片url
        :param kwargs: 
        :return: 
        """
        pass