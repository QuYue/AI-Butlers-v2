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


#%% Functions
class Butler():
    def __init__(self, name, config):
        self.name = name
        self.sender = Send.Sender(name, config)
        self.config = config
        self.memory = int(config.openai.memory)
        self.init_conversation()


    def init_conversation(self):
        self.conversation_history = self.config.openai.init_words
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
    
    def implement(self, received_message, config):
        user_id = received_message["senderStaffId"] 
        user_cname = self.config.map.user.id2cname[user_id]
        conversation_id = received_message["conversationId"] 
        content = received_message["text"]["content"].strip()

        if content[:5].strip() == "百度翻译":
            reply = BaiduTranslate.baidu_translater(content[5:], config)
        else:
            self.if_restart_conversation()
            conversation = f"{self.conversation_history}\n{user_cname}: {content}\n{self.name}:"
            chat_code, reply = ChatGPT.chat_gpt(conversation, config)
            if chat_code == 500:
                self.conversation_history += f"\n{user_cname}: {content}\n{self.name}: {reply}"
                # print(self.conversation_history)
            self.last_active_time = datetime.now()
        # print(f"ChatGPT: {reply}")

        reply = self.text_response(reply)
        if 'atUsers' not in received_message:
            self.sender.send_message(user_id, reply)
        else:
            self.sender.send_group_message(conversation_id, reply)








    
