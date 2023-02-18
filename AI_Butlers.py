# -*- encoding: utf-8 -*-
'''
@Time        :2023/02/19 04:04:42
@Author      :Qu Yue
@File        :AIButlers.py
@Software    :Visual Studio Code
Introduction: 
'''


#%% Import Packages
# basic
from flask import Flask, request
import argparse

# mine
import AIButlers

#%% Parameters
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-p', '--path', type=str, default="./secret.json", help="The path of secret file, default:'./secret.json'")

#%% Flask
app = Flask(__name__)


#%% Functions
@app.route('/help')
def help_page():
    return "Hello World"

#%% Main Function
if __name__ == "__main__":
    args = arg_parser.parse_args()
    AIButlers.read_secret('./secret.json')
    print()
    pass
    # app.run(host="::", port=1011, debug=True)
