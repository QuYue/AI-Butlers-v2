# -*- encoding: utf-8 -*-
'''
@Time        :2023/02/19 05:23:10
@Author      :Qu Yue
@File        :utils.py
@Software    :Visual Studio Code
Introduction: 
'''

# %% Import Packages
import copy

# %% Rename print
pprint = print

# %% My Structure (Classes)
class MyStruct():
    """
    A template of structure (class)
    """
    def __init__(self):
        pass

    def add_json(self, json_data):
        for x, y in json_data.items():
            if isinstance(y, dict):
                temp = MyStruct()
                temp.add_json(y)
                self.__dict__[x] = temp
            else:
                self.__dict__[x] = y
    
    @property
    def dict(self):
        struct_dict = self.__dict__.copy()
        return struct_dict

    def __repr__(self):
        """
        Print
        """
        return f"{self.__dict__}"


def print(string, args):
    if not args.noprint:
        pprint(string)