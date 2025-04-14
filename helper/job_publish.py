""" 工作流程-發工作 """

# pylint: disable = [unused-wildcard-import], [wildcard-import]
import logging
import traceback
import streamlit as st
from api import *


def e_login(base_url, e_phone):
    """登入商家"""
    worky_103.e_login(base_url, e_phone)
    worky_104.e_login_confirm(base_url, e_phone)
    worky_106.e_profile(base_url)


def repeat_job_publish(base_url, time, e_phone, work_date, start_time, work_hour, custom_name):
    """商家發多個工作"""
    work_date = int(work_date)
    time = int(time)

    try:
        for i in range(time):
            logging.info("✅ 第 %s 次測試 ---", (i+1))
            e_login(base_url, e_phone)
            worky_109.e_job_publish(base_url, work_date, start_time, work_hour, custom_name)
        return {"status": "pass", "msg": "商家發布工作成功"}
    except ValueError as e:
        st.error(f"輸入錯誤 : {e}")
        return {"status": "fail", "msg": "商家發布工作失敗"}
    except Exception as e: # pylint: disable = [broad-exception-caught]
        st.error(f"未預期錯誤，檢查 API LOG : {e}")
        traceback.print_exc()
        return {"status": "fail", "msg": "商家發布工作失敗"}

if __name__ == "__main__":
    BASE_URL = "https://next-staging-v210x.api.staging.worky.com.tw"
    E_PHONE = "903310010"
    TIME = 1

    WORK_DATE = 20250403
    START_TIME = "20:00"
    WORK_HOUR = 2
    CUSTOM_NAME = "測試工單名稱"
    repeat_job_publish(BASE_URL, TIME, E_PHONE, WORK_DATE, START_TIME, WORK_HOUR, CUSTOM_NAME)
