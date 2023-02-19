# -*- encoding: utf-8 -*-
'''
@Time        :2023/02/19 08:56:15
@Author      :Qu Yue
@File        :ChatGPT.py
@Software    :Visual Studio Code
Introduction: 
'''

#%% Import Packages
# Basic
import os
import sys
import openai

# Self-defined
if __package__ is None:
    os.chdir(os.path.dirname(__file__))
    sys.path.append('..')
    import AIButlers


#%% Functions
def chat_gpt(content, config):
    openai.api_key = config.openai.api_key
    try:
        response = openai.Completion.create(
            model = config.openai.model,
            prompt = content + "\n",
            temperature = config.openai.temperature,
            max_tokens = config.openai.max_tokens,
            top_p = config.openai.top_p,
            frequency_penalty = config.openai.frequency_penalty,
            presence_penalty = config.openai.presence_penalty,
            stop = config.openai.stop
        ) 
        reply = response.choices[0].text.strip()
        chat_code = 500
    except:
        reply = "I'm a little tired today. You'd better chat with me tomorrow."
        chat_code = 400
    return chat_code, reply


#%% Main Function
if __name__ == "__main__":
    config = AIButlers.read_config("../config.json")
    chat_code, reply = chat_gpt("Hello", config)
    print(f"code: {chat_code}")
    print(reply)
