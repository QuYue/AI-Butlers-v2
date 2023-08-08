# -*- encoding: utf-8 -*-
'''
@Time     :   2023/07/25 15:10:58
@Author   :   QuYue
@File     :   ChatGPT4.py
@Email    :   quyue1541@gmail.com
@Desc:    :   ChatGPT4
'''

#%% Import Packages
import os
import sys
import openai

# Self-defined
if __package__ is None:
    os.chdir(os.path.dirname(__file__))


#%% Functions
import openai
openai.api_key = "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"

d = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
print(d.choices[0])