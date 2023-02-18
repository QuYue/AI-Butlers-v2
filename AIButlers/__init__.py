# -*- encoding: utf-8 -*-
'''
@Time        :2023/02/19 05:19:34
@Author      :Qu Yue
@File        :__init__.py
@Software    :Visual Studio Code
Introduction: 
'''
# %% Import Packages
# basic
import json

# mine
import utils

# %%
def read_secret(secret_path):
    secret = utils.MyStruct()
    with open(secret_path, encoding="utf-8") as f:
        d = f.read()
        d = json.loads(d)
        secret.add_json(d)
    return secret


        


