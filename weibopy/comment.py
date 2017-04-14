# encoding:utf-8
from .weibo import WeiboClient


class Comments(WeiboClient):
    """
    """

    def show(self, **kwargs):
        """
        获取某条微博的评论列表
        :return: 
        """
        pass

    def by_me(self, **kwargs):
        """
        
        :param kwargs: 
        :return: 
        """
        pass

    def to_me(self, **kwargs):
        """
        :param kwargs: 
        :return: 
        """
        pass

    def timeline(self, **kwargs):
        """
        获取用户发送及收到的评论列表
        :param kwargs: 
        :return: 
        """
        pass

    def metions(self, **kwargs):
        """
        获取@到我的评论
        :param kwargs:
        :return: 
        """
        pass

    def show_batch(self, **kwargs):
        """
        批量获取评论内容
        :param kwargs: 
        :return: 
        """

    def create(self, **kwargs):
        """
        	评论一条微博
        :param kwargs: 
        :return: 
        """
        pass

    def destroy(self, **kwargs):
        """
        删除一条我的评论
        :param kwargs: 
        :return: 
        """
        pass

    def destroy_batch(self, **kwargs):
        """
        批量删除我的评论
        :param kwargs: 
        :return: 
        """
        pass

    def reply(self, **kwargs):
        """
        回复一条我收到的评论
        :param kwargs: 
        :return: 
        """
        pass
