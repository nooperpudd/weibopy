# encoding:utf-8

from .weibo import WeiboClient


class User(WeiboClient):
    """
    """
    def show(self,**kwargs):
        """
        获取用户信息
        :param kwargs: 
        :return: 
        """
        pass

    def domain_show(self,**kwargs):
        """
        通过个性域名获取用户信息
        :param kwargs: 
        :return: 
        """
        pass
    def counts(self,**kwargs):
        """
        批量获取用户的粉丝数、关注数、微博数
        :param kwargs: 
        :return: 
        """
        pass