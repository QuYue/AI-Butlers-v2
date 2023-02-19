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
def chat_gpt(content, args):
    openai.api_key = args.openai.api_key
    try:
        response = openai.Completion.create(
            model = args.openai.model,
            prompt = content + "\n",
            temperature = args.openai.temperature,
            max_tokens = args.openai.max_tokens,
            top_p = args.openai.top_p,
            frequency_penalty = args.openai.frequency_penalty,
            presence_penalty = args.openai.presence_penalty,
            stop = args.openai.stop
        ) 
        reply = response.choices[0].text.strip()
        chat_code = 500
    except:
        reply = "I'm a little tired today. You'd better chat with me tomorrow."
        chat_code = 400
    return chat_code, reply


#%% Main Function
if __name__ == "__main__":
    secret = AIButlers.read_config("../config.json")
    chat_code, reply = chat_gpt("Hello", secret)
    print(f"code: {chat_code}")
    print(reply)
