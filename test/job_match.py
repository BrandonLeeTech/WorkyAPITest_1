""" 工作流程-媒合工作 """

# pylint: disable = [unused-wildcard-import], [wildcard-import]
import logging
import traceback
import streamlit as st
from api import *


def job_match(base_url, e_phone, l_phone):
    """發工作>媒合"""
    try:
        worky_103.e_login(base_url, e_phone)
        worky_104.e_login_confirm(base_url, e_phone)
        worky_106.e_profile(base_url)
        worky_203.l_login(base_url, l_phone)
        worky_204.l_login_confirm(base_url, l_phone)
        worky_206.l_profile(base_url)
        # job_sn = worky_109.e_job_publish(base_url, work_date, start_time, work_hour, custom_name)
        # worky_210_1.l_job_match_apply(base_url)
        # worky_120_1.e_job_match_accept(base_url)
        # return job_sn, {"status": "pass", "msg": "商家帳務設定成功"}
        return {"status": "pass", "msg": "媒合成功"}

    except ValueError as e:
        st.error(f"輸入錯誤 : {e}")
        return {"status": "fail", "msg": "媒合失敗"}
    except Exception as e: # pylint: disable = [broad-exception-caught]
        st.error(f"未預期錯誤，檢查 API LOG : {e}")
        traceback.print_exc()
        return {"status": "fail", "msg": "媒合失敗"}

def repeat_job_match(base_url, e_phone, l_phone, time, work_date, start_time, work_hour, custom_name):
    """多人媒合多個工單"""
    e_phone = int(e_phone)
    l_phone = int(l_phone)
    time = int(time)
    job_sn_list = []  # 存放所有 job_sn

    # 每次執行後更新 e_phone 和 l_phone
    for i in range(time):
        logging.info("✅ 第 %s 次測試 ---", (i+1))
        logging.info("E_PHONE: {%s};\n L_PHONE: {%s}", e_phone, l_phone)
        job_match(base_url, e_phone, l_phone)
        job_sn = worky_109.e_job_publish(base_url, work_date, start_time, work_hour, custom_name)
        worky_210_1.l_job_match_apply(base_url)
        worky_120_1.e_job_match_accept(base_url)
        job_sn_list.append(job_sn)
        e_phone += 1
        l_phone += 1
    print(f"✅ 總共媒合 {time} 次")
    print(f"工單編號: {job_sn_list}")
    return job_sn_list  # 返回所有工單編號


def repeat_job_match_single(base_url, e_phone, l_phone, time, work_date, start_time, work_hour, custom_name):
    """單人媒合多個工單(每天發同時段工作)"""
    work_date = int(work_date)
    time = int(time)
    job_sn_list = []  # 存放所有 job_sn

    job_match(base_url, e_phone, l_phone)
    # 每次執行後更新 work_date
    for i in range(time):
        logging.info("✅ 第 %s 次測試 ---", (i+1))
        logging.info("WORK_DATE: {%s}", work_date)
        job_sn = worky_109.e_job_publish(base_url, work_date, start_time, work_hour, custom_name)
        worky_210_1.l_job_match_apply(base_url)
        worky_120_1.e_job_match_accept(base_url)
        job_sn_list.append(job_sn)
        work_date += 1
    print(f"✅ 總共媒合 {time} 天")
    print(f"工單編號: {job_sn_list}")
    return job_sn_list  # 返回所有工單編號


if __name__ == "__main__":
    BASE_URL = "https://next-staging-v210x.api.staging.worky.com.tw"
    E_PHONE = "903310005"
    L_PHONE = "903310005"
    TIME = 1

    WORK_DATE = 20250401
    START_TIME = "18:00"
    WORK_HOUR = 2
    CUSTOM_NAME = "測試工單名稱"

    repeat_job_match_single(BASE_URL, E_PHONE, L_PHONE, TIME, WORK_DATE, START_TIME, WORK_HOUR, CUSTOM_NAME)
