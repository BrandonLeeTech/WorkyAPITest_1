""" 工作流程-媒合工作 """

# pylint: disable = w0401, w0614, w0611, w0718
import os
import logging
import traceback
from dotenv import load_dotenv
from api import *
from config.logger_config import LoggerConfig


def job_match(e_phone, l_phone, wait, pay):
    """發工作>媒合"""
    try:
        worky_103.e_login(e_phone)
        worky_104.e_login_confirm(e_phone)
        worky_106.e_profile()
        worky_api_203.l_login(l_phone)
        worky_api_204.l_login_confirm(l_phone)
        worky_api_206.l_profile()
        # job_sn = worky_api_109.e_job_publish(wait, pay)
        job_sn = worky_api_109_1.e_job_publish()
        worky_api_210_1.l_job_match_apply()
        worky_api_120_1.e_job_match_accept()
        return job_sn
    except Exception as e:
        print(f"❌ 發生例外: {e}")
        traceback.print_exc()

def repeat_job_match():
    """媒合多個工單"""
    load_dotenv(".env")
    e_phone = int(os.getenv("E_PHONE"))
    l_phone = int(os.getenv("L_PHONE"))
    wait = os.getenv("J_WAIT")
    pay = os.getenv("J_PAY")
    time = int(os.getenv("REC_TIME"))
    job_sn_list = []  # 存放所有 job_sn

    # 每次執行後更新 e_phone 和 l_phone
    for i in range(time):
        logging.info("✅ 第 %s 次測試 ---", (i+1))
        logging.info("E_PHONE: {%s}", e_phone)
        logging.info("L_PHONE: {%s}", l_phone)
        job_sn = job_match(e_phone, l_phone, wait, pay)
        job_sn_list.append(job_sn)
        e_phone += 1
        l_phone += 1
    print(f"✅ 總共媒合 {time} 次")
    print(f"工單編號: {job_sn_list}")
    return job_sn_list  # 返回所有工單編號


if __name__ == "__main__":
    repeat_job_match()
