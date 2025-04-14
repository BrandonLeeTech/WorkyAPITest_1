""" 工作流程-打上班卡 """

# pylint: disable = [unused-wildcard-import], [wildcard-import]
import traceback
import streamlit as st
from api import *


def job_clock_in(base_url, e_phone, l_phone, job_sn):
    """打上班卡"""
    try:
        worky_103.e_login(base_url, e_phone)
        worky_104.e_login_confirm(base_url, e_phone)
        worky_203.l_login(base_url, l_phone)
        worky_204.l_login_confirm(base_url, l_phone)
        worky_115_2_0.e_shop_schedule_info(base_url, job_sn)
        worky_122.e_send_start_code(base_url, job_sn)
        worky_213.l_job_clock_in(base_url, job_sn)
        return {"status": "pass", "msg": "打上班卡成功"}

    except ValueError as e:
        st.error(f"輸入錯誤 : {e}")
        return {"status": "fail", "msg": "打上班卡失敗"}
    except Exception as e: # pylint: disable = [broad-exception-caught]
        st.error(f"未預期錯誤，檢查 API LOG : {e}")
        traceback.print_exc()
        return {"status": "fail", "msg": "打上班卡失敗"}

if __name__ == "__main__":
    BASE_URL = "https://next-staging-v210x.api.staging.worky.com.tw"
    E_PHONE = "0904140000"
    L_PHONE = "0904140000"
    JOB_SN = 17446042380001

    job_clock_in(BASE_URL, E_PHONE, L_PHONE, JOB_SN)
