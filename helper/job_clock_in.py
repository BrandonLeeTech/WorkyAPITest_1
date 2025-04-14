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
        worky_122.e_send_start_code(base_url)
        worky_213.l_job_clock_in(base_url)
        return {"status": "pass", "msg": "媒合成功"}

    except ValueError as e:
        st.error(f"輸入錯誤 : {e}")
        return {"status": "fail", "msg": "媒合失敗"}
    except Exception as e: # pylint: disable = [broad-exception-caught]
        st.error(f"未預期錯誤，檢查 API LOG : {e}")
        traceback.print_exc()
        return {"status": "fail", "msg": "媒合失敗"}



# def job_clock_in(e_phone, l_phone):
#     """打上班卡"""
#     try:
#         worky_103.e_login(e_phone)
#         worky_104.e_login_confirm(e_phone)
#         worky_106.e_profile()
#         worky_203.l_login(l_phone)
#         worky_204.l_login_confirm(l_phone)
#         worky_115_1.e_schedule()
#         worky_115_2.e_shop_schedule_info()
#         worky_122.e_send_start_code()
#         worky_213.l_job_clock_in()
#     except Exception as e:
#         print(f"❌ 發生例外: {e}")
#         traceback.print_exc()

# def repeat_job_clock_in():
#     """(多個)打上班卡"""
#     load_dotenv(".env")
#     e_phone = int(os.getenv("E_PHONE"))
#     l_phone = int(os.getenv("L_PHONE"))
#     time = int(os.getenv("REC_TIME"))

#     # 每次執行後更新 e_phone 和 l_phone
#     for i in range(time):
#         logging.info("✅ 第 %s 次測試 ---", (i+1))
#         logging.info("E_PHONE: {%s}", e_phone)
#         logging.info("L_PHONE: {%s}", l_phone)
#         job_clock_in(e_phone, l_phone)
#         e_phone += 1
#         l_phone += 1
#     print(f"✅ 總共打上班卡 {time} 次")
