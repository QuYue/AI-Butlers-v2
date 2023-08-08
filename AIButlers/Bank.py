# -*- encoding: utf-8 -*-
'''
@Time     :   2023/02/24 02:35:10
@Author   :   QuYue
@File     :   Bank.py
@Email    :   quyue1541@gmail.com
@Desc:    :   Bank
'''

#%% Import Packages
# Basic
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
import Send

#%% Classes


#%% Functions
card_template = {   "config": {
                        "autoLayout": True,
                        "enableForward": True
                    },
                    "header": {
                        "title": {
                        "type": "text",
                        "text": "小金库"
                        },
                        "logo": "@lALPDfJ6V_FPDmvNAfTNAfQ"
                    },
                    "contents": [
                        {
                        "type": "markdown",
                        "text": "**我们的小金库**",
                        "id": "text_1677152113234"
                        },
                        {
                        "type": "divider",
                        "id": "divider_1677152113234"
                        },
                        {
                        "type": "section",
                        "fields": {
                            "list": [
                            {
                                "type": "text",
                                "text": "当前余额为1000000",
                                "id": "text_1677152113302"
                            }
                            ]
                        },
                        "extra": {
                            "type": "button",
                            "label": {
                            "type": "text",
                            "text": "查看详情",
                            "id": "text_1677152113329"
                            },
                            "actionType": "openLink",
                            "url": {
                            "all": "http://www.yueming.top:1011/help"
                            },
                            "status": "primary",
                            "id": "button_1646816886531"
                        },
                        "id": "section_1677152113234"
                        },
                        {
                        "type": "action",
                        "actions": [
                            {
                            "type": "button",
                            "label": {
                                "type": "text",
                                "text": "添加帐单",
                                "id": "text_1677152113310"
                            },
                            "actionType": "openLink",
                            "url": {
                                "all": "https://www.dingtalk.com"
                            },
                            "status": "primary",
                            "id": "button_1646816888247"
                            },
                            {
                            "type": "button",
                            "label": {
                                "type": "text",
                                "text": "查看历史",
                                "id": "text_1677152113268"
                            },
                            "actionType": "request",
                            "status": "primary",
                            "id": "button_1646816888257"
                            },
                            {
                            "type": "button",
                            "label": {
                                "type": "text",
                                "text": "帐单统计",
                                "id": "text_1677152113281"
                            },
                            "actionType": "openLink",
                            "url": {
                                "all": "https://www.dingtalk.com"
                            },
                            "status": "primary",
                            "id": "button_1646816888277"
                            }
                        ],
                        "id": "action_1677152113235"
                        }
                    ]
                }
  
card_template={
  "config": {
    "autoLayout": True,
    "enableForward": True
  },
  "header": {
    "title": {
      "type": "text",
      "text": "小金库"
    },
    "logo": "@lALPDfJ6V_FPDmvNAfTNAfQ"
  },
  "contents": [
    {
      "type": "markdown",
      "text": "**我们的小金库**",
      "id": "text_1677152113234"
    },
    {
      "type": "divider",
      "id": "divider_1677152113234"
    },
    {
      "type": "section",
      "fields": {
        "list": [
          {
            "type": "text",
            "text": "当前余额为1000000",
            "id": "text_1677152113302"
          }
        ]
      },
      "extra": {
        "type": "button",
        "label": {
          "type": "text",
          "text": "查看详情",
          "id": "text_1677152113329"
        },
        "actionType": "openLink",
        "url": {
          "all": "http://www.yueming.top:1011/help"
        },
        "status": "primary",
        "id": "button_1646816886531"
      },
      "id": "section_1677152113234"
    },
    {
      "type": "action",
      "actions": [
        {
          "type": "button",
          "label": {
            "type": "text",
            "text": "添加帐单",
            "id": "text_1677152113310"
          },
          "actionType": "openLink",
          "url": {
            "all": "https://www.dingtalk.com"
          },
          "status": "primary",
          "id": "button_1646816888247"
        },
        {
          "type": "button",
          "label": {
            "type": "text",
            "text": "查看历史",
            "id": "text_1677152113268"
          },
          "actionType": "request",
          "status": "primary",
          "id": "button_1646816888257"
        },
        {
          "type": "button",
          "label": {
            "type": "text",
            "text": "帐单统计",
            "id": "text_1677152113281"
          },
          "actionType": "openLink",
          "url": {
            "all": "https://www.dingtalk.com"
          },
          "status": "primary",
          "id": "button_1646816888277"
        }
      ],
      "id": "action_1677152113235"
    },
    {
      "type": "section",
      "content": {
        "type": "text",
        "text": "组织沟通更加高效便捷，激发组织中个体的创新力",
        "id": "text_1677178547276"
      },
      "extra": {
        "type": "select",
        "options": [
          {
            "label": {
              "type": "text",
              "text": "选项一",
              "id": "text_1677178547307"
            },
            "value": "1"
          },
          {
            "label": {
              "type": "text",
              "text": "选项二",
              "id": "text_1677178547326"
            },
            "value": "2"
          }
        ],
        "placeholder": {
          "type": "text",
          "text": "请选择",
          "id": "text_1677178547334"
        },
        "id": "select_1677178547276"
      },
      "id": "section_1677178547276"
    },
    {
      "type": "action",
      "actions": [
        {
          "type": "button",
          "label": {
            "type": "text",
            "text": "打开链接",
            "id": "text_1677178558390"
          },
          "actionType": "openLink",
          "url": {
            "all": "https://www.dingtalk.com"
          },
          "status": "primary",
          "id": "button_1677178558391"
        },
        {
          "type": "button",
          "label": {
            "type": "text",
            "text": "发送请求",
            "id": "text_1677178558391"
          },
          "actionType": "request",
          "value": "1",
          "status": "primary",
          "id": "button_1677178558395"
        },
        {
          "type": "button",
          "label": {
            "type": "text",
            "text": "次级按钮",
            "id": "text_1677178558436"
          },
          "actionType": "openLink",
          "url": {
            "all": "https://www.dingtalk.com"
          },
          "status": "normal",
          "iconCode": "icon_XDS_Todo2",
          "id": "button_1677178558471"
        },
        {
          "type": "button",
          "label": {
            "type": "text",
            "text": "警示按钮",
            "id": "text_1677178558411"
          },
          "actionType": "openLink",
          "url": {
            "all": "https://www.dingtalk.com"
          },
          "status": "warning",
          "id": "button_1677178558448"
        },
        {
          "type": "button",
          "label": {
            "type": "text",
            "text": "禁用按钮",
            "id": "text_1677178558469"
          },
          "actionType": "openLink",
          "url": {
            "all": "https://www.dingtalk.com"
          },
          "status": "primary",
          "disabled": True,
          "id": "button_1677178558454"
        }
      ],
      "id": "action_1677178558391"
    }
  ]
}
#%% Main Function
if __name__ == "__main__":
    config = AIButlers.read_config("../config.json")
    card = {"single_chat_receiver": '{"userId":"manager1393"}',
            "card_data": json.dumps(card_template),
            "card_biz_id": datetime.now().strftime("%Y-%m-%d_%H:%M:%S"),
            "card_template_id": "StandardCard",
            "callback_url": "http://www.yueming.top:1011/card"
            }
    sender = Send.Sender('Alfred', config)
    sender.send_interactive_card(card)
    
