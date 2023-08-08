# -*- encoding: utf-8 -*-
'''
@Time     :   2023/02/22 04:43:20
@Author   :   QuYue
@File     :   Weather.py
@Email    :   quyue1541@gmail.com
@Desc:    :   Weather
'''

#%% Import Packages
# Basic
import requests
import json
from datetime import datetime

# Modules

# Add Path
if __package__ is None:
    import os
    import sys
    os.chdir(os.path.dirname(__file__))
    sys.path.append("..")
    import AIButlers

# Self-defined


#%% Classes


#%% Functions
def get_params(config):
    params = dict()
    params['key'] = config.amap.key
    params['city'] = config.amap.city
    params['output'] = "json"
    return params


def get_lives_weather(config):
    params = get_params(config)
    url = "https://restapi.amap.com/v3/weather/weatherInfo"
    params['extensions'] = 'base'
    res = requests.get(url=url, params=params)
    weather = json.loads(res.text)
    return weather

def get_forecast_weather(config):
    params = get_params(config)
    url = "https://restapi.amap.com/v3/weather/weatherInfo"
    params['extensions'] = 'all'
    res = requests.get(url=url, params=params)
    weather = json.loads(res.text)
    return weather

def lives_weather_markdown(weather):
    w = weather['lives'][0]
    now = datetime.strptime(w['reporttime'], "%Y-%m-%d %H:%M:%S")
    text = f"#### **{w['city']}** 实况天气\n\n"
    text += f"发布于 {now.strftime('%Y年%m月%d日 %H:%M:%S')}\n\n"
    text += f"天气: {w['weather']}\n\n"
    text += f"温度: {w['temperature_float']}°C\n\n"
    text += f"风力: {w['windpower']}\n\n"
    text += f"风向: {w['winddirection']}\n\n"
    text += f"湿度: {w['humidity_float']}%\n\n"
    return text

def lives_weather_text(weather):
    w = weather['lives'][0]
    now = datetime.strptime(w['reporttime'], "%Y-%m-%d %H:%M:%S")
    text = f"{w['city']}的实时天气 "
    text += f"发布于{now.strftime('%Y年%m月%d日 %H:%M:%S')},"
    text += f"天气: {w['weather']},"
    text += f"温度: {w['temperature_float']}°C,"
    text += f"风力: {w['windpower']},"
    text += f"风向: {w['winddirection']},"
    text += f"湿度: {w['humidity_float']}%。"
    return text

def forecast_weather_markdown(weather, iftomorrow=True):
    w0 = weather['forecasts'][0]['casts'][0]
    w1 = weather['forecasts'][0]['casts'][1]
    today = datetime.strptime(w0['date'],"%Y-%m-%d")
    tomorrow = datetime.strptime(w1['date'],"%Y-%m-%d")
    text = f"#### **{weather['forecasts'][0]['city']}** 今日天气 \n\n"
    if iftomorrow:
        text += f"{today.strftime('%Y年%m月%d日')}\n\n"
    text += f"白天天气: {w0['dayweather']}\n\n"
    text += f"白天温度: {w0['daytemp']}°C\n\n"
    text += f"白天风力: {w0['daypower']}\n\n"
    text += f"白天风向: {w0['daywind']}\n\n"
    text += f"夜间天气: {w0['nightweather']}\n\n"
    text += f"夜间温度: {w0['nighttemp']}°C\n\n"
    text += f"夜间风力: {w0['nightpower']}\n\n"
    text += f"夜间风向: {w0['nightwind']}\n\n"
    if iftomorrow:
        text += f"#### **{weather['forecasts'][0]['city']}** 明日天气\n\n"
        text += f"{tomorrow.strftime('%Y年%m月%d日')}\n\n"
        text += f"白天天气: {w1['dayweather']}\n\n"
        text += f"白天温度: {w1['daytemp']}°C\n\n"
        text += f"白天风力: {w1['daypower']}\n\n"
        text += f"白天风向: {w1['daywind']}\n\n"
        text += f"夜间天气: {w1['nightweather']}\n\n"
        text += f"夜间温度: {w1['nighttemp']}°C\n\n"
        text += f"夜间风力: {w1['nightpower']}\n\n"
        text += f"夜间风向: {w1['nightwind']}\n\n"
    return text

def forecast_weather_text(weather):
    w0 = weather['forecasts'][0]['casts'][0]
    w1 = weather['forecasts'][0]['casts'][1]
    today = datetime.strptime(w0['date'],"%Y-%m-%d")
    tomorrow = datetime.strptime(w1['date'],"%Y-%m-%d")
    text = f"{weather['forecasts'][0]['city']}的今日预计天气 "
    text += f"{today.strftime('%Y年%m月%d日')} "
    text += f"白天天气: {w0['dayweather']} "
    text += f"白天温度: {w0['daytemp']}°C "
    text += f"白天风力: {w0['daypower']} "
    text += f"白天风向: {w0['daywind']} "
    text += f"夜间天气: {w0['nightweather']} "
    text += f"夜间温度: {w0['nighttemp']}°C "
    text += f"夜间风力: {w0['nightpower']} "
    text += f"夜间风向: {w0['nightwind']}。 "
    text += f"明日预计天气 "
    text += f"{tomorrow.strftime('%Y年%m月%d日')}"
    text += f"白天天气: {w1['dayweather']} "
    text += f"白天温度: {w1['daytemp']}°C "
    text += f"白天风力: {w1['daypower']} "
    text += f"白天风向: {w1['daywind']} "
    text += f"夜间天气: {w1['nightweather']} "
    text += f"夜间温度: {w1['nighttemp']}°C "
    text += f"夜间风力: {w1['nightpower']} "
    text += f"夜间风向: {w1['nightwind']} 。"
    return text

#%% Main Function
if __name__ == "__main__":
    config = AIButlers.read_config("../config.yaml")
    weather = get_forecast_weather(config)
    weather_markdown = forecast_weather_text(weather)
    print(weather_markdown)
    