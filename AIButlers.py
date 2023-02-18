# -*- encoding: utf-8 -*-
'''
@Time        :2023/02/19 04:04:42
@Author      :Qu Yue
@File        :AIButlers.py
@Software    :Visual Studio Code
Introduction: 
'''


# %% Import Packages
from flask import Flask, request
import argparse

# %% Flask
app = Flask(__name__)

# %% Functions
@app.route('/help')
def help_page():
    return "Hello World"



# %% Main Function
if __name__ == "__main__":
    app.run(host="::", port=1011, debug=True)
