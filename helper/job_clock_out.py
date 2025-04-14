""" 工作流程-打下班卡+評論 """

# pylint: disable = [unused-wildcard-import], [wildcard-import]
import traceback
import streamlit as st
from api import *

def job_clock_out(base_url, e_phone, l_phone, job_sn, j_estar, j_lstar):
    """打下班卡>評論"""
    try:
        worky_103.e_login(base_url, e_phone)
        worky_104.e_login_confirm(base_url, e_phone)
        worky_203.l_login(base_url, l_phone)
        worky_204.l_login_confirm(base_url, l_phone)
        worky_115_2_0.e_shop_schedule_info(base_url, job_sn)
        worky_123.e_send_end_code(base_url, job_sn)
        worky_214.l_job_clock_out(base_url, job_sn)
        worky_126_1.e_evaluate(base_url, job_sn, j_estar)
        worky_219_1.l_evaluate(base_url, job_sn, j_lstar)
        return {"status": "pass", "msg": "打下班卡並評論成功"}

    except ValueError as e:
        st.error(f"輸入錯誤 : {e}")
        return {"status": "fail", "msg": "打下班卡並評論失敗"}
    except Exception as e: # pylint: disable = [broad-exception-caught]
        st.error(f"未預期錯誤，檢查 API LOG : {e}")
        traceback.print_exc()
        return {"status": "fail", "msg": "打下班卡並評論失敗"}
