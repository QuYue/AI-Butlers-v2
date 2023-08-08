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
import os
import sys
import yaml
import requests
from alibabacloud_dingtalk.robot_1_0.client import Client as dingtalkrobot_1_0Client
from alibabacloud_dingtalk.oauth2_1_0.client import Client as dingtalkoauth2_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.robot_1_0 import models as dingtalkrobot__1__0_models
from alibabacloud_tea_util import models as util_models

# Self-defined
if __package__ is None:
    os.chdir(os.path.dirname(__file__))
    sys.path.append('..')


#%% Functions
class Sender():
    def __init__(self, name, config):
        self.load_config(name, config)

    def load_config(self, name, config):
        """
        加载配置文件
        """
        # Dingtalk robot config
        self.config = self.__get_config__(config)
        self.access_token = None
        self.app_key = self.config['robots'][name]['app_key']
        self.app_secret = self.config['robots'][name]['app_secret']
        self.robotCode = self.config['robots'][name]['robot_code']

        # Setting
        self.__try_set__('update_access_token_max_times', 3)
        self.__try_set__('send_message_max_times', 3)
        self.__try_set__('send_group_message_max_times', 3)
        self.__try_set__('show_log', True)

        # User list
        self.user_list = self.config['users']

        # Group list
        self.group_list = self.config['groups']

    def __get_config__(self, config):
        """
        获取配置文件
        """
        if isinstance(config, str):
            config = yaml.load(open(config, "r", encoding="utf-8"), Loader=yaml.FullLoader)
        elif isinstance(config, dict):
            config = config
        else:
            raise TypeError("Config must be dict or str.")
        return config['dingtalk']
    
    def __try_set__(self, name, default_value):
        """
        尝试设置配置一些配置项，如果配置文件中没有，则使用默认值
        """
        try:
            self.__dict__[name] = self.config['setting'][name]
        except:
            self.__dict__[name] = default_value
    
    def get_user_id(self, user_name):
        if user_name in self.user_list:
            return self.user_list[user_name]['id']
        return None
    
    def get_group_id(self, group_name):
        if group_name in self.group_list:
            return self.group_list[group_name]['openConversationId']
        return None
    
    def pprint(self, string):
        if self.show_log:
            print(string)

    def create_client(self, model="robot"):
        """
        使用 Token 初始化账号Client
        @return: Client
        """
        config_openai = open_api_models.Config()
        config_openai.protocol = 'https'
        config_openai.region_id = 'central'
        if model == "robot":
            return dingtalkrobot_1_0Client(config_openai)
        elif model == "auth":
            return dingtalkoauth2_1_0Client(config_openai)

    def update_access_token(self, times=1):
        """
        更新 Robot Access Token
        """
        req=requests.get(url=f"https://oapi.dingtalk.com/gettoken?appkey={self.app_key}&appsecret={self.app_secret}")
        try:
            self.access_token = req.json()['access_token']
            self.pprint('Update Dingtalk Access Token Successfully.')
        except:
            self.access_token = None
            self.pprint('Update Dingtalk Access Token Failed.')
    
    def send_message(self, user_id, message, times=1):
        """
        发送消息
        """
        client = self.create_client("robot")
        if self.access_token is None:
            self.update_access_token()
        batch_send_otoheaders = dingtalkrobot__1__0_models.BatchSendOTOHeaders()
        batch_send_otoheaders.x_acs_dingtalk_access_token = self.access_token
        batch_send_otorequest = dingtalkrobot__1__0_models.BatchSendOTORequest(
            robot_code=self.robotCode,
            user_ids=[user_id],
            msg_param=message['msg_param'],
            msg_key=message['msg_key']
        )
        try:
            self.pprint(f"Send message ({times})...")
            client.batch_send_otowith_options(batch_send_otorequest, batch_send_otoheaders, util_models.RuntimeOptions())
            self.pprint("Send message successfully.")
        except Exception as error:
            self.pprint("Send message failed!!!!!!!!!!")
            self.pprint(error)
            if times < self.send_message_max_times:
                self.update_access_token()
                self.send_message(user_id, message, times+1)

    def send_group_message(self, conversation_id, message, times=1):
        """
        发送群消息
        """
        client = self.create_client("robot")
        if self.access_token is None:
            self.update_access_token()
        org_group_send_headers = dingtalkrobot__1__0_models.OrgGroupSendHeaders()
        org_group_send_headers.x_acs_dingtalk_access_token = self.access_token
        org_group_send_request = dingtalkrobot__1__0_models.OrgGroupSendRequest(
            robot_code=self.robotCode,
            open_conversation_id=conversation_id,
            msg_param=message['msg_param'],
            msg_key=message['msg_key']
        )
        try:
            self.pprint(f"Send group message ({times})...")
            client.org_group_send_with_options(org_group_send_request, org_group_send_headers, util_models.RuntimeOptions())
            self.pprint("Send group message successfully.")
        except Exception as error:
            self.pprint("Send group message failed!!!!!!!!!!")
            self.pprint(error)
            if times < self.send_message_max_times:
                self.update_access_token()
                self.send_group_message(conversation_id, message, times+1)


# %%
if __name__ == '__main__':
    user_name = 'quyue'
    group_name = 'HappyTime'
    message = dict()
    message['msg_key'] = "sampleText"
    message['msg_param'] ='{"content": "测试！"}'

    sender = Sender("Alfred", "../config.yaml")
    sender.send_message(sender.get_user_id(user_name), message)
    # sender.send_group_message(sender.get_group_id(group_name), message)

