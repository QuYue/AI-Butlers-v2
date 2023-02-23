# -*- encoding: utf-8 -*-
'''
@Time     :   2023/02/23 11:54:50
@Author   :   QuYue
@File     :   Schedule.py
@Email    :   quyue1541@gmail.com
@Desc:    :   Schedule
'''
#%% Import Packages
# Basics
import datetime

# Modules

# Add Path
if __package__ is None:
    import os
    import sys
    os.chdir(os.path.dirname(__file__))
    sys.path.append("..")
    # Self-defined
    import Send

else:
    from . import Send
    from . import Weather
    from . import Schedule

#%% Classes
#%% Funtions
def good_morning(tasker, markdown_response, sender, config):
    now = datetime.datetime.now()
    week_map = {1: "一", 2: "二", 3: "三", 4: "四", 5: "五", 6:"六", 7: "日"}
    weather_info = Weather.forecast_weather_markdown(Weather.get_forecast_weather(config), False) 
    day_info = now.strftime(f"%Y年%m月%d日\n### 星期{week_map[now.weekday()+1]} %H:%M")
    text = f"# 早安 又是愉快的一天\n### 今天是{day_info}\n"
    text +="![screenshot](http://5b0988e595225.cdn.sohucs.com/images/20190121/73cc568180f449fa846818dd6e56fbc3.jpeg)\n\n"
    text += weather_info

    reply = markdown_response(text, "早安")
    sender.send_group_message(config.dingtalk.openConversationId, reply)

def set_good_morning(tasker, markdown_response, sender, config):
    clock = config.tasks.goodmorning
    tasker.create_day_task(good_morning, clock, tasker, markdown_response, sender, config)



    

#%% Main Function
if __name__ == "__main__":
    pass
    




