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
    sys.path.append('..')
    import AIButlers


#%% Functions
def chat_gpt(content, args):
    openai.api_key = args.openai.api_key
    try:
        response = openai.Completion.create(
            model = "text-davinci-003",
            prompt = content + "\n",
            temperature = 0.9,
            max_tokens = 1000,
            top_p = 1,
            frequency_penalty = 0.0,
            presence_penalty = 0.6,
            stop = ["Human:", "AI:"]
        )
        reply = response.choices[0].text.strip()
        chat_code = 500
    except:
        reply = "I'm a little tired today. You'd better chat with me tomorrow."
        chat_code = 400
    return chat_code, reply


#%% Main Function
if __name__ == "__main__":
    secret = AIButlers.read_secret("../secret.json")
    chat_code, reply = chat_gpt("Hello", secret)
    print(f"code: {chat_code}")
    print(reply)
