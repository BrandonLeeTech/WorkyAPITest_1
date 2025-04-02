""" 註冊打工 """
# pylint: disable = w0401, w0614, w0611, w0718
import os
import logging
import traceback
from dotenv import load_dotenv
from api import *
from api import worky_303_e
from tools.socket_data_manager import SocketDataManager
from config.logger_config import LoggerConfig
from utils.chinese_to_arabic import increment_chinese_name

def labor_register(l_phone, l_name):
    """註冊打工>設定個人資訊"""
    socket_data = SocketDataManager()
    try:
        # worky_api_201.l_register(l_phone)
        # worky_api_202.l_register_confirm(l_phone)
        worky_api_203.l_login(l_phone)
        worky_api_204.l_login_confirm(l_phone)
        worky_303_e.upload("labor_profile_image")
        img = socket_data.get_data("labor_profile_image")
        worky_api_205_1.l_update(img, l_name)
        worky_api_205_2.l_update_preference()
    except Exception as e:
        print(f"❌ 發生例外: {e}")
        traceback.print_exc()

def repeat_labor_register():
    """註冊(多個)打工"""
    load_dotenv(".env")
    l_phone = int(os.getenv("L_PHONE"))
    l_name = os.getenv("L_NAME")
    time = int(os.getenv("REC_TIME"))

    # 每次執行後更新 l_phone 和 labor_name
    for i in range(time):
        logging.info("✅ 第 %s 次測試 ---", (i+1))
        logging.info("L_PHONE: {%s}", l_phone)
        labor_register(l_phone, l_name)
        l_phone += 1
        l_name = increment_chinese_name(l_name) # 如果只能輸入中文可以用這個函數加一
    print(f"✅ 總共註冊打工 {time} 個")


if __name__ == "__main__":
    repeat_labor_register()
