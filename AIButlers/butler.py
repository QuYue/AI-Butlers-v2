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
        
    def text_response(self, reply):
        message = utils.MyStruct()
        message.msg_key = "sampleText"
        message.msg_param =f'{{"content": "{reply}"}}'
        return message
    
    def implement(self, received_message, config):
        user_id = received_message["senderStaffId"] 
        conversation_id = received_message["conversationId"] 
        content = received_message["text"]["content"]
        if content[:5].strip() == "百度翻译":
            reply = BaiduTranslate.baidu_translater(content[5:], config)
        else:
            chat_code, reply = ChatGPT.chat_gpt(content, config)
        # print(f"ChatGPT: {reply}")
        reply = self.text_response(reply)

        if 'atUsers' not in received_message:
            Send.Sender.send_message(user_id, reply, config)
        else:
            Send.Sender.send_group_message(conversation_id, reply, config)








    
