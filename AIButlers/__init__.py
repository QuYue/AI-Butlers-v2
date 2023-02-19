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
import json

# Self-defined
import utils
from . import butler

#%% Functions
def read_config(config):
    new_config = utils.MyStruct()
    with open(config.path, encoding="utf-8") as f:
        d = f.read()
        d = json.loads(d)
        new_config.add_json(d)
    return new_config

def get_map(config_path):
    map = utils.MyStruct()
    map.robot = utils.MyStruct()
    map.user = utils.MyStruct()

    map.robot.name2code = dict()
    map.robot.code2name = dict()

    map.user.name2id = dict()
    map.user.name2id = dict()


        


