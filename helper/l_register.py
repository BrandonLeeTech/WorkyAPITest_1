""" 註冊打工 """

# pylint: disable = [unused-wildcard-import], [wildcard-import]
import logging
import traceback
import streamlit as st
from api import *
from utils.chinese_to_arabic import increment_chinese_name
from web import *

def register_and_setting(base_url, l_phone, l_name):
    """註冊打工>設定個人資訊"""
    try:
        worky_201.l_register(base_url, l_phone)
        worky_202.l_register_confirm(base_url, l_phone)
        worky_203.l_login(base_url, l_phone)
        worky_204.l_login_confirm(base_url, l_phone)
        worky_205_1.l_update(base_url, l_name)
        worky_205_2.l_update_preference(base_url)
        # labor_verify(base_url, l_phone)
        return {"status": "pass", "msg": "打工註冊成功"}

    except ValueError as e:
        st.error(f"輸入錯誤 : {e}")
        return {"status": "fail", "msg": "打工註冊失敗"}
    except Exception as e: # pylint: disable = [broad-exception-caught]
        st.error(f"未預期錯誤，檢查 API LOG : {e}")
        traceback.print_exc()
        return {"status": "fail", "msg": "打工註冊失敗"}


def repeat_register_and_setting(base_url, l_phone, l_name, time):
    """註冊(多個)打工"""
    l_phone = int(l_phone)
    time = int(time)

    # 每次執行後更新 l_phone 和 labor_name
    for i in range(time):
        logging.info("✅ 第 %s 次測試 ---", (i+1))
        logging.info("L_PHONE: {%s}", l_phone)
        register_and_setting(base_url, l_phone, l_name)
        l_phone += 1
        l_name = increment_chinese_name(l_name) # 如果只能輸入中文可以用這個函數加一
    print(f"✅ 總共註冊打工 {time} 個")


if __name__ == "__main__":
    BASE_URL = "https://next-staging-v210x.api.staging.worky.com.tw"
    L_PHONE = "0904140004"
    L_NAME = "測試4"
    TIME = 2

    repeat_register_and_setting(BASE_URL, L_PHONE, L_NAME, TIME)
