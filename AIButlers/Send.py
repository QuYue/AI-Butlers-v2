# -*- encoding: utf-8 -*-
'''
@Time        :2023/02/19 09:40:27
@Author      :Qu Yue
@File        :Send.py
@Software    :Visual Studio Code
Introduction: 
'''

#%% Import Packages
# Basic
import time
import os
import sys
import requests
from alibabacloud_dingtalk.im_1_0.client import Client as dingtalkim_1_0Client
from alibabacloud_dingtalk.robot_1_0.client import Client as dingtalkrobot_1_0Client
from alibabacloud_dingtalk.oauth2_1_0.client import Client as dingtalkoauth2_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.robot_1_0 import models as dingtalkrobot__1__0_models
from alibabacloud_dingtalk.oauth2_1_0 import models as dingtalkoauth_2__1__0_models
from alibabacloud_dingtalk.im_1_0 import models as dingtalkim__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

# Self-defined
if __package__ is None:
    os.chdir(os.path.dirname(__file__))
    sys.path.append('..')
    import AIButlers
import utils
    

# Functions
class Sender():
    def __init__(self, name, config):
        self.access_token = None
        self.app_key = config.dingtalk.robots.dict[name].app_key
        self.app_secret = config.dingtalk.robots.dict[name].app_secret
        self.robotCode = config.dingtalk.robots.dict[name].robotCode

        self.ding_access_token = None
        self.ding_app_key = config.dingtalk.app_key
        self.ding_app_secret = config.dingtalk.app_secret

        self.update_access_token_max_times = 3
        self.send_message_max_times = 3
        self.send_group_message_max_times = 3
        self.send_card_max_times = 3

        self.config = config

    def create_client(self, model="robot"):
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config_openai = open_api_models.Config()
        config_openai.protocol = 'https'
        config_openai.region_id = 'central'
        if model == "robot":
            return dingtalkrobot_1_0Client(config_openai)
        elif model == "auth":
            return dingtalkoauth2_1_0Client(config_openai)
        elif model == "kim":
            return dingtalkim_1_0Client(config_openai)

    def update_access_token0(self, times=1):
        client = self.create_client("auth")
        get_access_token_request = dingtalkoauth_2__1__0_models.GetAccessTokenRequest(
            app_key=self.app_key,
            app_secret=self.app_secret
        )
        try:
            utils.print(f"Update access_token: {times}", self.config)
            client_info = client.get_access_token(get_access_token_request)
            self.access_token = client_info.body.access_token
            utils.print("Update access token successed", self.config)
        except Exception as err:
            if times >= self.update_access_token_max_times:
                utils.print("Update access token failed T_T")
            else: 
                self.update_access_token(times+1)
    
    def update_access_token(self, times=1):
        req=requests.get(url=f"https://oapi.dingtalk.com/gettoken?appkey={self.app_key}&appsecret={self.app_secret}")
        try:
            self.access_token = req.json()['access_token']
            utils.print(f'Update Dingtalk Access Token Successfully.({times})', self.config)
        except:
            if times >= self.update_access_token_max_times:
                utils.print("Update access token failed T_T")
            else: 
                self.update_access_token(times+1)

    def update_ding_access_token(self, times=1):
        client = self.create_client("auth")
        get_access_token_request = dingtalkoauth_2__1__0_models.GetAccessTokenRequest(
            app_key=self.ding_app_key,
            app_secret=self.ding_app_secret
        )
        try:
            utils.print(f"Update ding access_token: {times}", self.config)
            client_info = client.get_access_token(get_access_token_request)
            self.ding_access_token = client_info.body.access_token
            utils.print("update ding access token successed", self.config)
        except Exception as err:
            if times >= self.update_access_token_max_times:
                utils.print("Update ding ccess token failed T_T")
            else: 
                self.update_ding_access_token(times+1)

    def send_message(self, user_id, message, times=1):
        client = self.create_client("robot")
        if self.access_token is None:
            self.update_access_token()
        batch_send_otoheaders = dingtalkrobot__1__0_models.BatchSendOTOHeaders()
        batch_send_otoheaders.x_acs_dingtalk_access_token = self.access_token
        batch_send_otorequest = dingtalkrobot__1__0_models.BatchSendOTORequest(
            robot_code=self.robotCode,
            user_ids=[user_id],
            msg_key=message.msg_key,
            msg_param=message.msg_param
        )
        try:
            utils.print(f"Send message: {times}", self.config)
            client.batch_send_otowith_options(batch_send_otorequest, batch_send_otoheaders, util_models.RuntimeOptions())
            utils.print(f"Send message success", self.config)
        except Exception as err:
            print(err)
            if times >= self.send_message_max_times:
                print("Send message error!!!!!!!!!!")
            else:
                self.update_access_token()
                self.send_message(user_id, message, times+1)

    def send_group_message(self, conversation_id, message, times=1) -> None:
        client = self.create_client("robot")
        if self.access_token is None:
            self.update_access_token()
        org_group_send_headers = dingtalkrobot__1__0_models.OrgGroupSendHeaders()
        org_group_send_headers.x_acs_dingtalk_access_token = self.access_token
        org_group_send_request = dingtalkrobot__1__0_models.OrgGroupSendRequest(
            msg_param=message.msg_param,
            msg_key=message.msg_key,
            robot_code=self.robotCode,
            open_conversation_id=conversation_id
        )
        try:
            utils.print(f"Send group message: {times}", self.config)
            client.org_group_send_with_options(org_group_send_request, org_group_send_headers, util_models.RuntimeOptions())
            utils.print(f"Send group message success", self.config)
        except Exception as err:
            if times >= self.send_message_max_times:
                print("Send group message error!!!!!!!!!!")
            else:
                self.update_access_token()
                self.send_group_message(conversation_id, message, times+1)

    def send_interactive_card(self, card, times=1) -> None:
        client = self.create_client("kim")
        if self.ding_access_token is None:
            self.update_ding_access_token()
        send_robot_interactive_card_headers = dingtalkim__1__0_models.SendRobotInteractiveCardHeaders()
        send_robot_interactive_card_headers.x_acs_dingtalk_access_token = self.ding_access_token
        send_robot_interactive_card_request = dingtalkim__1__0_models.SendRobotInteractiveCardRequest(
            robot_code=self.robotCode,
            **card
        )
        try:
            utils.print(f"Send card: {times}", self.config)
            client.send_robot_interactive_card_with_options(send_robot_interactive_card_request, send_robot_interactive_card_headers, util_models.RuntimeOptions())
        except Exception as err:
            if times >= self.send_card_max_times:
                print("Send card error!!!!!!!!!!")
            else:
                self.update_ding_access_token()
                self.send_interactive_card(card, times+1)

# %%
if __name__ == '__main__':
    config = AIButlers.read_config("../config.json")
    user_id = "manager1393"
    # user_id = "091228533436436277"
    message = utils.MyStruct()
    message.msg_key = "sampleText"
    message.msg_param ='{"content": "你好！"}'
    sender = Sender("Alfred", config)
    sender.send_group_message(config.dingtalk.openConversationId, message, config)
