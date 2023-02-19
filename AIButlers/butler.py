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


#%% Import Packages
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
        content = received_message["text"]["content"]

        chat_code, reply = ChatGPT.chat_gpt(content, config)
        utils.print(f"ChatGPT: {reply}", config)
        reply = self.text_response(reply)
        Send.Sender.send_message(user_id, reply, config)








    
