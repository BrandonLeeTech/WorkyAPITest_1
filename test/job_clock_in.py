""" 工作流程-打上班卡 """

# pylint: disable = [unused-wildcard-import], [wildcard-import]
import os
import logging
import traceback
from dotenv import load_dotenv
from api import *
from web import *
from config.logger_config import LoggerConfig


def job_clock_in(e_phone, l_phone):
    """打上班卡"""
    try:
        worky_103.e_login(e_phone)
        worky_104.e_login_confirm(e_phone)
        worky_106.e_profile()
        worky_203.l_login(l_phone)
        worky_204.l_login_confirm(l_phone)
        worky_115_1.e_schedule()
        worky_115_2.e_shop_schedule_info()
        worky_122.e_send_start_code()
        worky_213.l_job_clock_in()
    except Exception as e:
        print(f"❌ 發生例外: {e}")
        traceback.print_exc()

def repeat_job_clock_in():
    """(多個)打上班卡"""
    load_dotenv(".env")
    e_phone = int(os.getenv("E_PHONE"))
    l_phone = int(os.getenv("L_PHONE"))
    time = int(os.getenv("REC_TIME"))

    # 每次執行後更新 e_phone 和 l_phone
    for i in range(time):
        logging.info("✅ 第 %s 次測試 ---", (i+1))
        logging.info("E_PHONE: {%s}", e_phone)
        logging.info("L_PHONE: {%s}", l_phone)
        job_clock_in(e_phone, l_phone)
        e_phone += 1
        l_phone += 1
    print(f"✅ 總共打上班卡 {time} 次")


if __name__ == "__main__":
    job_clock_in("0903060020","0903060020")
    # repeat_job_clock_in()
