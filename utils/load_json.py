"""讀取 json 文件"""
import os
import sys
import json


# 支援 PyInstaller 的打包與本地開發環境
def resource_path(relative_path):
    """取得打包後或本地開發路徑"""
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller 打包後的臨時資料夾
        base_path = sys._MEIPASS
    else:
        # 本地開發：取相對於本腳本的路徑
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    return os.path.join(base_path, relative_path)


def get_config(key):
    """ 讀取 JSON 設定檔的 key 的鍵值 """
    config_path = resource_path("api_config.json")
    with open(config_path, "r", encoding="utf-8") as file:
        return json.load(file).get(key)


if __name__ == "__main__":
    print(get_config("SECRET"))
