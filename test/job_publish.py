""" 工作流程-發工作 """
# pylint: disable = w0401, w0614, w0611, w0718
import os
import logging
import traceback
from dotenv import load_dotenv
from api import *
from config.logger_config import LoggerConfig

def job_publish(e_phone, wait, pay):
    """發工作"""
    try:
        worky_103.e_login(e_phone)
        worky_104.e_login_confirm(e_phone)
        worky_106.e_profile()
        # worky_api_109.e_job_publish(wait, pay)
        worky_api_109_1.e_job_publish()
    except Exception as e:
        print(f"❌ 發生例外: {e}")
        traceback.print_exc()

def repeat_job_publish():
    """商家發多個工作"""
    load_dotenv()

    e_phone = os.getenv("E_PHONE")
    wait = os.getenv("J_WAIT")
    pay = os.getenv("J_PAY")
    time = int(os.getenv("REC_TIME"))

    for i in range(time):
        logging.info("✅ 第 %s 次測試 ---", (i+1))
        job_publish(e_phone, wait, pay)


if __name__ == "__main__":
    repeat_job_publish()
