# -*- encoding: utf-8 -*-
'''
@Time        :2023/02/19 05:52:57
@Author      :Qu Yue
@File        :butler.py
@Software    :Visual Studio Code
Introduction: 
'''
#%% Import Packages
# Basic
import os
import sys
from datetime import datetime

# Self-defined
import utils
if __package__ is None:
    os.chdir(os.path.dirname(__file__))
    sys.path.append('..')
    import AIButlers
    import ChatGPT
    import Send
else:
    from . import ChatGPT
    from . import Send
    from . import BaiduTranslate
    from . import Weather
    from . import Schedule
    from . import GoodMorning


#%% Functions
class Butler():
    def __init__(self, name, config):
        self.name = name
        self.sender = Send.Sender(name, config)
        self.config = config
        self.memory = int(config.openai.memory)
        self.init_conversation()
        self.tasker = Schedule.ScheduleTasker()
        self.run_tasker()

    def run_tasker(self):
        self.tasker.run()
        GoodMorning.set_good_morning(self.tasker, self.markdown_response, self.sender, self.config)


    def init_conversation(self):
        self.conversation_history = self.config.openai.init_words
        forecast_weather = Weather.forecast_weather_text(Weather.get_forecast_weather(self.config))
        live_weather = Weather.lives_weather_text(Weather.get_lives_weather(self.config))
        self.conversation_history += live_weather
        self.conversation_history += forecast_weather
        # self.conversation_history = ""
        self.last_active_time = datetime.now() # last time of active

    def if_restart_conversation(self):
        minutes = (datetime.now() - self.last_active_time).seconds/60
        if minutes > self.memory:
            self.init_conversation()
        
    def text_response(self, reply):
        message = utils.MyStruct()
        message.msg_key = "sampleText"
        message.msg_param =f'{{"content": "{reply}"}}'
        return message

    def markdown_response(self, reply, title="消息"):
        message = utils.MyStruct()
        message.msg_key = "sampleMarkdown"
        message.msg_param =f'{{"title": "{title}", "text": "{reply}"}}'
        return message

    
    def implement(self, received_message, config):
        user_id = received_message["senderStaffId"] 
        user_cname = self.config.map.user.id2cname[user_id]
        conversation_id = received_message["conversationId"] 
        content = received_message["text"]["content"].strip()

        if content[:5].strip() == "百度翻译":
            reply = BaiduTranslate.baidu_translater(content[5:], config)
            reply = self.text_response(reply)
        elif content in ["天气", "今日天气", "本日天气", "当天天气", "weather", "Weather", "天气预报"]:
            reply = Weather.forecast_weather_markdown(Weather.get_forecast_weather(config)) 
            reply = self.markdown_response(reply, title="天气")
        elif content in ["实时天气", "实况天气", "当前天气"]:
            reply = Weather.lives_weather_markdown(Weather.get_lives_weather(config)) 
            reply = self.markdown_response(reply, title="实时天气")
        elif content in ["clear", "清空", "清空对话", "对话清空"]:
            self.init_conversation()
            reply = self.text_response("对话已清空")
        else:
            self.if_restart_conversation()
            conversation = f"{self.conversation_history}\n{user_cname}: {content}\n{self.name}:"
            chat_code, reply = ChatGPT.chat_gpt(conversation, config)
            if chat_code == 500:
                self.conversation_history += f"\n{user_cname}: {content}\n{self.name}: {reply}"
            self.last_active_time = datetime.now()
            reply = self.text_response(reply)
        # print(f"Alfred: {reply}")

        
        if 'atUsers' not in received_message:
            self.sender.send_message(user_id, reply)
        else:
            self.sender.send_group_message(conversation_id, reply)








    
