# -*- encoding: utf-8 -*-
'''
@Time        :2023/02/19 04:04:42
@Author      :Qu Yue
@File        :AIButlers.py
@Software    :Visual Studio Code
Introduction: 
'''

#%% Import Packages
# Basic
from flask import Flask, request
import argparse

# Self-defined
import utils
import AIButlers

#%% Parameters
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-p', '--path', type=str, default="./config.json", help="The path of configure file, default:'./config.json'")

#%% Flask
app = Flask(__name__)

#%% Functions
@app.route('/help')
def help_page():
    return "Hello World"

@app.route('/', methods=['POST'])
def interactive():
    received_message = request.json

    sender_name = received_message["senderNick"]
    senderid = received_message["senderStaffId"] 
    content = received_message["text"]["content"]
    robotcode = received_message["robotCode"]
    utils.print(f"{sender_name}: {content}")
    
    butler.implement(received_message, config)    
    return "OK"

@app.route('/card', methods=['POST'])
def get_card():
    received_message = request.json
    print(received_message)
    return "OK"


#%% Main Function
if __name__ == "__main__":
    args = arg_parser.parse_args()
    config = AIButlers.read_config(args.path)
    butler = AIButlers.Butler("Alfred", config)
    app.run(host="::", port=1011, debug=False)
