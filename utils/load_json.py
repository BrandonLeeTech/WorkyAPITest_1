"""讀取 json 文件"""
import os
import json

CONFIG_PATH = os.path.join(os.getcwd(), "api_config.json")

def get_config(key):
    """ 讀取 JSON 設定檔的 key 的鍵值 """
    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        return json.load(file).get(key)


if __name__ == "__main__":
    get_config("SECRET")
