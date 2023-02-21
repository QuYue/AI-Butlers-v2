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
    conversation_history = config.openai.init_words
    print(conversation_history)
    while True:
        user_choose = input("选择用户 1. 曲岳 2. 邵明明: ")
        if user_choose=="1":
            name = "曲岳"
        else:
            name = "邵明明"
        user_input = input(f"{name}: ")
        prompt = f"{conversation_history} {name}: {user_input}\nAlfred:"
        chat_code, reply = chat_gpt(prompt, config)
        # print(f"code: {chat_code}")
        print(f"Alfred: {reply}")
        conversation_history += f"{name}: {user_input}\nAlfred: {reply}"
