# encoding:utf-8

from .weibo import WeiboClient


class Services(WeiboClient):
    """
    """

    def search_topics(self, **kwargs):
        """
        搜索某一话题下的微博
        :param kwargs: 
        :return: 
        """
        pass

    def short_url_shorten(self, **kwargs):
        """
        长链转短链
        :param kwargs: 
        :return: 
        """

        pass

    def short_url_expand(self, **kwargs):
        """
        短链转长链
        :param kwargs: 
        :return: 
        """

    def short_url_share_counts(self, **kwargs):
        """
        获取短链接在微博上的微博分享数
        :return: 
        """
        pass

    def short_url_comment_counts(self, **kwargs):
        """
        获取短链接在微博上的微博评论数
        :param kwargs: 
        :return: 
        """
        pass

    def get_timezone(self, **kwargs):
        """
        获取时区配置表
        :param kwargs: 
        :return: 
        """
        pass

    def get_country(self, **kwargs):
        """
        获取国家列表
        :param kwargs: 
        :return: 
        """
        pass

    def get_province(self, **kwargs):
        """
        获取省份列表
        :param kwargs: 
        :return: 
        """
        pass

    def code_to_location(self, **kwargs):
        """
        通过地址编码获取地址名称
        :param kwargs: 
        :return: 
        """
        pass

    def get_city(self, **kwargs):
        """
        获取城市列表
        :param kwargs: 
        :return: 
        """
        pass

    def rate_limit_staus(self, ):
        """
        获取当前授权用户API访问频率限制
        :return: 
        """
        pass

    def get_uid(self, ):
        """
        授权之后获取用户的UID
        :return: 
        """
        pass

    def profile_email(self, ):
        """
        授权之后获取用户的联系邮箱
        :return: 
        """
        pass
