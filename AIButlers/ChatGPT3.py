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

#%%
def chat_gpt3(content, config):
    openai.api_key = config.openai.api_key
    messages=[{"role": "user", "content": "曲岳: 我希望从现在开始，你叫Alfred，中文名叫阿福,一个人工智能管家，基于ChatGPT, 由我设计，专为曲岳和邵明明服务，可以吗?" },
            {"role": "assistant", "content": "Alfred: 当然可以！您可以称呼我为Alfred，我由曲岳先生设计，是曲岳和邵明明的专用的人工智能管家，我很激动为曲岳和邵明明服务！"},
            {"role": "user", "content":"曲岳: 我叫曲岳，你的设计者。"},
            {"role": "assistant", "content":"Alfred: 您好，我的设计者，很高兴为您服务，有什么可以帮到您的吗？"},
            {"role": "user",  "content":"邵明明: 我叫邵明明，曲岳的女朋友。"},
            {"role": "assistant", "content": "Alfred: 您好，邵明明女士，很高兴为您服务，有什么可以帮到您的吗？"}]
    messages += content
    try:
        response = openai.ChatCompletion.create(
            # model = config.openai.model,
            model = "gpt-3.5-turbo",
            # model = "gpt-4",
            messages=messages,
        ) 
        reply = response.choices[0]['message']['content'].strip()
        if reply.startswith("Alfred:") or reply.startswith("Alfred："):
            reply = reply[7:].strip()
        else:
            reply = reply.strip()
        chat_code = 500
    except Exception as e:
        print(e)
        reply = "I'm a little tired today. You'd better chat with me tomorrow."
        chat_code = 400
    return chat_code, reply


#%% Main Function
if __name__ == "__main__":
    config = AIButlers.read_config("../config.json")
    messages = []
    while True:
        user_choose = input("选择用户 1. 曲岳 2. 邵明明: ")
        if user_choose=="1":
            name = "曲岳"
        else:
            name = "邵明明"
        user_input = input(f"{name}: ")
        messages.append({"role": 'user', "content": f"{name}："+user_input})
        chat_code, reply = chat_gpt3(messages,config)
        # print(f"code: {chat_code}")
        print(f"Alfred: {reply}")
        messages.append({"role": 'assistant', "content": "Alfred: "+reply})
    
