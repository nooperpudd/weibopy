# encoding:utf-8

from .weibo import WeiboClient


class WeiboQRCode(WeiboClient):
    """
    weibo QR code services
    """

    def create(self, **kwargs):
        """
        本接口用来创建二维码ticket
        
        1、如果action_name=QR_SCENE时，expire_seconds参数空缺，则默认为1800；
        2、目前有2种类型的二维码，分别是临时二维码和永久二维码，前者有过期时间，最大为1800秒，但能够生成较多数量，后者无过期时间，数量较少（目前参数只支持1--100000）；
        3、获取带参数的二维码的过程包括两步，首先通过本接口创建二维码ticket，然后凭借ticket到调用qrcode/show接口换取二维码；
        4、对于临时二维码，过期时间的计时起点是qrcode/create接口的调用时间；
        5、用户一个未过期扫描带场景值二维码时，可能推送以下两种事件：
          
        参数详情：
                        必选	    类型及范围	说明
        access_token	true	string	    在粉丝服务平台 - 高级功能 - 开发者模式页面中获取，或者OAuth2.0授权后获得, 详细参考 获取粉丝服务平台开发接口的access token。
        expire_seconds	false	string	    该二维码有效时间，以秒为单位。 最大不超过1800。
        action_name	    true	string	    二维码类型，QR_SCENE为临时,QR_LIMIT_SCENE为永久。
        action_info	    true	string	    二维码详细信息。
        scene_id	    true	string	    场景值ID，临时二维码时为32位非0整型，永久二维码时最大值为100000（目前参数只支持1--100000）。
        
        :param kwargs: 
        :return: 
        {
            "ticket": "XXX",
            "expire_seconds": 1800
        }
        """
        self.request("post", "eps/qrcode/create.json", data=kwargs)

    def show(self, ticket):
        """
        
        1、本接口无需登录态即可调用；
        2、ticket需要进行UrlEncode;
        
        获取二维码ticket后，开发者可用ticket换取二维码图片。
        :param ticket: 开发者通过eps/qrcode/create生成的ticket
        :return: 调用成功返回一张图片，可以直接展示或者下载；
        """
        return self.request("post", "eps/qrcode/show", params={"ticket": ticket})
