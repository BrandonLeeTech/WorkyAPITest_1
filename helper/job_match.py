""" 工作流程-媒合工作 """

# pylint: disable = [unused-wildcard-import], [wildcard-import]
import logging
import traceback
import streamlit as st
from api import *


def job_match(base_url, e_phone, l_phone):
    """發工作>媒合"""
    worky_103.e_login(base_url, e_phone)
    worky_104.e_login_confirm(base_url, e_phone)
    worky_106.e_profile(base_url)
    worky_203.l_login(base_url, l_phone)
    worky_204.l_login_confirm(base_url, l_phone)
    worky_206.l_profile(base_url)

def repeat_job_match_single(base_url, time, e_phone, l_phone, work_date, start_time, work_hour, custom_name):
    """單人媒合多個工單(每天發同時段工作)"""
    work_date = int(work_date)
    time = int(time)

    try:
        job_match(base_url, e_phone, l_phone)
        # 每次執行後更新 work_date
        for i in range(time):
            logging.info("✅ 第 %s 次測試 ---", (i+1))
            logging.info("WORK_DATE: {%s}", work_date)
            worky_109.e_job_publish(base_url, work_date, start_time, work_hour, custom_name)
            worky_210_1.l_job_match_apply(base_url)
            worky_120_1.e_job_match_accept(base_url)
            work_date += 1
        return {"status": "pass", "msg": "媒合成功，需檢查打工認證跟商家付款"}
    except ValueError as e:
        st.error(f"輸入錯誤 : {e}")
        return {"status": "fail", "msg": "媒合並發工作失敗"}
    except Exception as e: # pylint: disable = [broad-exception-caught]
        st.error(f"未預期錯誤，檢查 API LOG : {e}")
        traceback.print_exc()
        return {"status": "fail", "msg": "媒合並發工作失敗"}



if __name__ == "__main__":
    BASE_URL = "https://next-staging-v210x.api.staging.worky.com.tw"
    E_PHONE = "903310010"
    L_PHONE = "903310000"
    TIME = 1

    WORK_DATE = 20250403
    START_TIME = "20:00"
    WORK_HOUR = 2
    CUSTOM_NAME = "測試工單名稱"

    repeat_job_match_single(BASE_URL, TIME, E_PHONE, L_PHONE, WORK_DATE, START_TIME, WORK_HOUR, CUSTOM_NAME)
