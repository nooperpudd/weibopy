# encoding:utf-8
from urllib.parse import urlencode

import requests

from .exceptions import WeiboOauth2Error, WeiboRequestError
from .weibo import filter_params


class WeiboOauth2(object):
    """
    weibo OAuth2
    """
    site_url = "https://api.weibo.com/oauth2/"
    mobile_url = "https://open.weibo.cn/oauth2/"

    def __init__(self, client_id, client_secret, redirect_url, **kwargs):
        """
        必选            类型及范围    说明
        client_id       true          string        申请应用时分配的AppKey。
        redirect_ur     true          string        授权回调地址，站外应用需与设置的回调地址一致，站内应用需填写canvas page的地址。
        scope           false         string        申请scope权限所需参数，可一次申请多个scope权限，用逗号分隔。使用文档
        state           false         string        用于保持请求和回调的状态，在回调时，会在Query Parameter中回传该参数。
                                                    开发者可以用这个参数验证请求有效性，也可以记录用户请求授权页前的位置。
                                                    这个参数可用于防止跨站请求伪造（CSRF）攻击

        display         false         string        授权页面的终端类型，取值见下面的说明。
        forcelogin      false         boolean       是否强制用户重新登录，true：是，false：否。默认false。
        language        false         string        授权页语言，缺省为中文简体版，en为英文版。英文版测试中，开发者任何意见可反馈至 @微博API


        sco : all  请求下列所有
        email                          用户的联系邮箱
        direct_messages_write          私信发送接口
        direct_messages_read           私信读取接口
        invitation_write               邀请发送接口
        friendships_groups_read        好友分组读取接口组
        friendships_groups_write       好友分组写入接口组
        statuses_to_me_read            定向微博读取接口组
        follow_app_official_microblog  关注应用官方微博， 只需在应用控制台填写官方帐号即可

        display:
        参数取值          类型说明
        default           默认的授权页面，适用于web浏览器。
        mobile            移动终端的授权页面，适用于支持html5的手机。注：使用此版授权页请用 https://open.weibo.cn/oauth2/authorize 授权接口
        wap               wap版授权页面，适用于非智能手机。
        client            客户端版本授权页面，适用于PC桌面应用。
        apponweibo        默认的站内应用授权页，授权后不返回access_token，只刷新站内应用父框架。

        :param client_id: (required) str,
        :param client_secret: (required) str,
        :param redirect_url: (required) str,
        :param scope: (optional) str,
        :param state: (optional) str,
        :param display:  (optional) str,  [default,mobile,wap,client,apponweibo]
        :param force_login: (optional) bool, default: false
        :param language:  (optional) str
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_url = redirect_url

        self.oauth2_params = kwargs

        self.session = requests.Session()

    @property
    def authorize_url(self):
        """
        authorization url
        request weibo authorization url
        :return:
        code    string    用于第二步调用oauth2/access_token接口，获取授权后的access token。
        state    string    如果传递参数，会回传该参数
        """

        if self.oauth2_params and self.oauth2_params.get("display") == "mobile":
            auth_url = self.mobile_url + "authorize"
        else:
            auth_url = self.site_url + "authorize"

        params = {
            'client_id': self.client_id,
            'redirect_uri': self.redirect_url,
        }
        params.update(self.oauth2_params)

        params = filter_params(params)

        return "{auth_url}?{params}".format(auth_url=auth_url, params=urlencode(params))

    def request(self, method, suffix, data):
        """
        :param method: str, http method ["GET","POST","PUT"]
        :param suffix: the url suffix
        :param data:
        :return:
        """
        url = self.site_url + suffix
        response = self.session.request(method, url, data=data)

        if response.status_code == 200:
            json_obj = response.json()

            if isinstance(json_obj, dict) and json_obj.get("error_code"):

                raise WeiboOauth2Error(
                    json_obj.get("error_code"),
                    json_obj.get("error"),
                    json_obj.get('error_description')
                )
            else:
                return json_obj
        else:
            raise WeiboRequestError(
                "Weibo API request error: status code: {code} url:{url} ->"
                " method:{method}: data={data}".format(
                    code=response.status_code,
                    url=response.url,
                    method=method,
                    data=data
                )
            )

    def auth_access(self, auth_code):
        """
        verify the fist authorization response url code

        response data
        返回值字段      字段类型    字段说明
        access_token    string      用户授权的唯一票据，用于调用微博的开放接口，同时也是第三方应用验证微博用户登录的唯一票据，
                                    第三方应用应该用该票据和自己应用内的用户建立唯一影射关系，来识别登录状态，不能使用本返回值里的UID
                                    字段来做登录识别。

        expires_in      string      access_token的生命周期，单位是秒数。
        remind_in       string      access_token的生命周期（该参数即将废弃，开发者请使用expires_in）。
        uid             string      授权用户的UID，本字段只是为了方便开发者，减少一次user/show接口调用而返回的，第三方应用不能用此字段作为用户
                                    登录状态的识别，只有access_token才是用户授权的唯一票据。

        :param auth_code: authorize_url response code
        :return:

        normal:
         {
               "access_token": "ACCESS_TOKEN",
               "expires_in": 1234,
               "remind_in":"798114",
               "uid":"12341234"
         }
         mobile:
         {
            "access_token": "SlAV32hkKG",
            "remind_in": 3600,
            "expires_in": 3600
            "refresh_token": "QXBK19xm62"
        }

        """
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'authorization_code',
            'code': auth_code,
            'redirect_uri': self.redirect_url
        }
        return self.request("post", "access_token", data=data)

    def revoke_auth_access(self, access_token):
        """
        授权回收接口，帮助开发者主动取消用户的授权。

        应用下线时，清空所有用户的授权
        应用新上线了功能，需要取得用户scope权限，可以回收后重新引导用户授权
        开发者调试应用，需要反复调试授权功能
        应用内实现类似登出微博帐号的功能

        并传递给你以下参数，source：应用appkey，uid ：取消授权的用户，auth_end ：取消授权的时间

        :param access_token:
        :return: bool
        """
        result = self.request("post", "revokeoauth2", data={"access_token": access_token})
        return bool(result.get("result"))

    def refresh_token(self, refresh_token):
        """

        only for mobile
        授权有效期内重新授权
        Refresh Token 也是有有效期的，Refresh Token 的有效期目前为30天，在有效期内随时可以刷新。

        :param refresh_token:
        :return:

        {
            "access_token": "SlAV32hkKG",
            "expires_in": 3600
        }

        """
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "refresh_token",
            "redirect_url": self.redirect_url,
            "refresh_token": refresh_token
        }
        return self.request("post", "access_token", data=data)

    def get_token_info(self, access_token):
        """
        查询用户access_token的授权相关信息，包括授权时间，过期时间和scope权限。

        response:

        返回值字段   字段类型   字段说明
        uid          string     授权用户的uid。
        appkey       string     access_token所属的应用appkey。
        scope        string     用户授权的scope权限。
        create_at    string     access_token的创建时间，从1970年到创建时间的秒数。
        expire_in    string     access_token的剩余时间，单位是秒数。

        :param access_token:
        :return:

          {
           "uid": 1073880650,
           "appkey": 1352222456,
           "scope": null,
           "create_at": 1352267591,
           "expire_in": 157679471
         }
        """
        return self.request("post", "get_token_info", data={"access_token": access_token})
