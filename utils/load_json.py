"""讀取 json 文件"""
import os
import json
import sys

# CONFIG_PATH = os.path.join(os.getcwd(), "api_config.json")
# 自動取得打包 or 本地的路徑
base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(base_path, '..', "api_config.json")


def get_config(key):
    """ 讀取 JSON 設定檔的 key 的鍵值 """
    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        return json.load(file).get(key)


if __name__ == "__main__":
    get_config("SECRET")
