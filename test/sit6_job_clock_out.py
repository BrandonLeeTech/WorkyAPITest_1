""" 工作流程-打下班卡+評論 """

# pylint: disable = w0401, w0614, w0611, w0718
import os
import logging
import traceback
from dotenv import load_dotenv
from api import *
from web import *
from config.logger_config import LoggerConfig

def job_clock_out(e_phone, l_phone):
    """打下班卡>評論"""
    try:
        worky_103.e_login(e_phone)
        worky_104.e_login_confirm(e_phone)
        worky_106.e_profile()
        worky_api_203.l_login(l_phone)
        worky_api_204.l_login_confirm(l_phone)
        worky_115_1.e_schedule()
        worky_api_115_2.e_shop_schedule_info()
        worky_api_123.e_send_end_code()
        worky_api_214.l_job_clock_out()
    except Exception as e:
        print(f"❌ 發生例外: {e}")
        traceback.print_exc()

def repeat_job_clock_out():
    """(多個)打下班卡和評論"""
    load_dotenv(".env")
    e_phone = int(os.getenv("E_PHONE"))
    l_phone = int(os.getenv("L_PHONE"))
    time = int(os.getenv("REC_TIME"))

    # 每次執行後更新 e_phone 和 l_phone
    for i in range(time):
        logging.info("✅ 第 %s 次測試 ---", (i+1))
        logging.info("E_PHONE: {%s}", e_phone)
        logging.info("L_PHONE: {%s}", l_phone)
        job_clock_out(e_phone, l_phone)
        e_phone += 1
        l_phone += 1
    print(f"✅ 總共打下班卡和評論 {time} 次")


if __name__ == "__main__":
    repeat_job_clock_out()
