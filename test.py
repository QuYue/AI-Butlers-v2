# -*- encoding: utf-8 -*-
'''
@Time        :2023/02/19 06:10:09
@Author      :Qu Yue
@File        :test.py
@Software    :Visual Studio Code
Introduction: 
'''

#%%
from alibabacloud_dingtalk.robot_1_0.client import Client as dingtalkrobot_1_0Client
from alibabacloud_dingtalk.oauth2_1_0.client import Client as dingtalkoauth2_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.robot_1_0 import models as dingtalkrobot__1__0_models
from alibabacloud_dingtalk.oauth2_1_0 import models as dingtalkoauth_2__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client(model="robot"):
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        if model == "robot":
            return dingtalkrobot_1_0Client(config)
        elif model == "auth":
            return dingtalkoauth2_1_0Client(config)

    @staticmethod
    def get_access_token(secret) -> None:
        client = Sample.create_client("auth")
        get_access_token_request = dingtalkoauth_2__1__0_models.GetAccessTokenRequest(
            app_key=secret.dingtalk.app_key,
            app_secret=secret.dingtalk.app_secret
        )
        try:
            d = client.get_access_token(get_access_token_request)
            access_token = d.body.access_token
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass
        return access_token


    @staticmethod
    def send_message(secret) -> None:
        client = Sample.create_client("robot")
        batch_send_otoheaders = dingtalkrobot__1__0_models.BatchSendOTOHeaders()
        batch_send_otoheaders.x_acs_dingtalk_access_token = Sample.get_access_token(secret)
        batch_send_otorequest = dingtalkrobot__1__0_models.BatchSendOTORequest(
            robot_code=secret.dingtalk.robots.dict["Alfred"].robotCode,
            user_ids=[
                "manager1393"
            ],
            msg_key='sampleMarkdown',
            msg_param='{"text": "hello text1","title": "hello title"}'
        )
        try:
            client.batch_send_otowith_options(batch_send_otorequest, batch_send_otoheaders, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass


    @staticmethod
    def send_group_message(secret) -> None:
        client = Sample.create_client("robot")
        org_group_send_headers = dingtalkrobot__1__0_models.OrgGroupSendHeaders()
        org_group_send_headers.x_acs_dingtalk_access_token = Sample.get_access_token(secret)
        org_group_send_request = dingtalkrobot__1__0_models.OrgGroupSendRequest(
            msg_param='{"text": "hello text0","title": "hello title"}',
            msg_key='sampleMarkdown',
            robot_code=secret.dingtalk.robots.dict["Alfred"].robotCode,
            open_conversation_id=secret.dingtalk.openConversationId
        )
        try:
            client.org_group_send_with_options(org_group_send_request, org_group_send_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass


#%%
if __name__ == '__main__':
    import AIButlers
    secret = AIButlers.read_secret("./secret.json")
    d = Sample.send_message(secret)