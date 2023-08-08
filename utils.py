# -*- encoding: utf-8 -*-
'''
@Time     :   2023/02/25 02:01:52
@Author   :   QuYue
@File     :   utils.py
@Email    :   quyue1541@gmail.com
@Desc:    :   utils
'''

#%% Import Packages
# Basic
import os
import copy

# Add Path
if __package__ is None:
    import os
    import sys
    os.chdir(os.path.dirname(__file__))

# Self-defined
    
pprint = print # rename print function
#%%  Classes
# My Structure
class MyStruct():
    """
    A template of structure (class)
    """
    def __init__(self):
        pass

    def add_json(self, json_data):
        """
        Add data from json file
        """
        for key, value in json_data.items():
            if key[0] == "@":
                continue
            if isinstance(value, dict):
                temp = MyStruct()
                temp.add_json(value)
                self.__dict__[key] = temp
            else:
                self.__dict__[key] = value

    def add_yaml(self, yaml_data):
        """
        Add data from yaml file
        """
        for key, value in yaml_data.items():
            if key[0] == "@":
                continue
            if isinstance(value, dict):
                temp = MyStruct()
                temp.add_yaml(value)
                self.__dict__[key] = temp
            else:
                self.__dict__[key] = value

    def to_json(self):
        """
        Return the structure as a json
        """
        struct_dict = self.__dict__.copy()
        for key, value in struct_dict.items():
            if isinstance(value, MyStruct):
                struct_dict[key] = value.to_json()
            elif isinstance(value, list) or isinstance(value, tuple):
                struct_dict[key] = self.__list_to_json__(value)
            elif isinstance(value, str) or isinstance(value, int) or isinstance(value, float):
                struct_dict[key] = value
            else:
                struct_dict[key] = str(value)
        return struct_dict
    
    def __list_to_json__(self, list_data):
        """
        Return the list as a json
        """
        list_json = []
        for i, val in enumerate(list_data):
            if isinstance(val, str) or isinstance(val, int) or isinstance(val, float):
                list_json.append(val)
            elif isinstance(val, MyStruct):
                list_json.append(val.to_json())
            elif isinstance(val, list) or isinstance(val, tuple):
                list_json.append(self.__list_to_json__(val))
            else:
                list_json.append(str(val))
        return list_json
    
    def __list_to_parm__(self, list_data):
        """
        Return the list as a json
        """
        list_parm = []
        for i, val in enumerate(list_data):
            if isinstance(val, MyStruct):
                list_parm.append(None)
            elif isinstance(val, list) or isinstance(val, tuple):
                list_parm.append(self.__list_to_parm__(val))
            else:
                list_parm.append(val)
        return list_parm
    
    @property
    def dict(self):
        """
        Return the structure as a dict
        """
        struct_dict = self.__dict__.copy()
        return struct_dict
    
    def get_parm(self):
        """
        Return the Paramters as a dict
        """
        struct_dict = self.__dict__.copy()
        remove_keys = []
        for key, value in struct_dict.items():
            if isinstance(value, MyStruct):
                remove_keys.append(key)
            elif isinstance(value, list) or isinstance(value, tuple):
                struct_dict[key] = self.__list_to_parm__(value)
            else:
                struct_dict[key] = value
        for key in remove_keys:
            struct_dict.pop(key, None)
        return struct_dict
    
    def __repr__(self):
        """
        Print the structure
        """
        return f"{self.__dict__}"
    
#%% Functions
def read_config(path):
    """
    Read config file
    """
    config = MyStruct()
    with open(path, encoding="utf-8") as f:
        file_type = os.path.splitext(path)[-1]
        if file_type == ".json":
            import json
            config.add_json(json.load(f))
        elif file_type == ".yaml":
            import yaml
            config.add_yaml(yaml.load(f, Loader=yaml.FullLoader))
    config.config_path = path # Add config path
    return config

def save_config(Parm, path):
    """
    Save config file
    """
    config = Parm.to_json()
    path_dir = os.path.dirname(path)
    if path_dir == "":
        path_dir = "."
    if not os.path.exists(path_dir):
        os.makedirs(path_dir)
    with open(path, encoding="utf-8", mode="w") as f:
        file_type = os.path.splitext(path)[-1]
        if file_type == ".json":
            import json
            json.dump(config, f, indent=4)
        elif file_type == ".yaml":
            import yaml
            yaml.dump(config, f, indent=4, default_flow_style=False, sort_keys=False)


def print(print_detail, *args):
    """
    Print function based on if_print
    """
    if print_detail:
        pprint(*args)


#%% Main Function
if __name__ == "__main__":
    Parm = read_config("./config.yaml")
    
    
# %%
