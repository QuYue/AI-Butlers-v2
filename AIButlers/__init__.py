# -*- encoding: utf-8 -*-
'''
@Time        :2023/02/19 05:19:34
@Author      :Qu Yue
@File        :__init__.py
@Software    :Visual Studio Code
Introduction: 
'''
#%% Import Packages
# Basic
import os
import sys
import json

# Add Path
if __package__ is None:
    os.chdir(os.path.dirname(__file__))
    sys.path.append('..')
else:
# Self-defined
    from . import butler
import utils

#%% Functions
def read_config(path):
    config = utils.MyStruct()
    with open(path, encoding="utf-8") as f:
        d = f.read()
        d = json.loads(d)
        config.add_json(d)

    get_map(config)
    return config

def get_map(config):
    map = utils.MyStruct()
    map.robot = utils.MyStruct()
    map.user = utils.MyStruct()

    map.robot.name2code = dict()
    map.robot.code2name = dict()

    map.user.name2id = dict()
    map.user.id2name = dict()
    map.user.cname2id = dict()
    map.user.id2cname = dict()

    for user in config.dingtalk.users.dict:
        uid = config.dingtalk.users.dict[user].id
        ucname = config.dingtalk.users.dict[user].cname
        map.user.name2id[user] = uid
        map.user.id2name[uid] = user
        map.user.cname2id[ucname] = uid
        map.user.id2cname[uid] = ucname

    for robot in config.dingtalk.robots.dict:
        robotcode = config.dingtalk.robots.dict[robot].robotCode
        map.robot.name2code[robot] = robotcode
        map.robot.code2name[robotcode] = robot

    config.map = map


#%% Main Function
if __name__ == "__main__":
    config = read_config("../config.json")
    print(config.map.user.id2cname['manager1393'])
        



# %%
