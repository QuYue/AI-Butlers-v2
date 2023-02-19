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
# arg_parser.add_argument('-n', '--noprint', action='store_true', help='If do not print some details')
#%% Flask
app = Flask(__name__)

#%% Functions
@app.route('/help')
def help_page():
    return "Hello World"

@app.route('/', methods=['POST'])
def interactive():
    received_message = request.json
    utils.print(received_message, args)

    sender_name = received_message["senderNick"]
    senderid = received_message["senderStaffId"] 
    content = received_message["text"]["content"]
    robotcode = received_message["robotCode"]
    print(f"{sender_name}: {content}")

    return "OK"

#%% Main Function
if __name__ == "__main__":
    args = arg_parser.parse_args()
    args = AIButlers.read_config(args.path)
    app.run(host="::", port=1011, debug=True)
