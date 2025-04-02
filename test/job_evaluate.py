""" 工作流程-打下班卡+評論 """

# pylint: disable = [unused-wildcard-import], [wildcard-import]
import os
import logging
import traceback
from dotenv import load_dotenv
from api import *
from web import *
from config.logger_config import LoggerConfig

def job_evaluate(j_estar, j_lstar):
    """打下班卡>評論"""
    try:
        worky_126_1.e_evaluate(j_estar)
        worky_219_1.l_evaluate(j_lstar)
    except Exception as e:
        print(f"❌ 發生例外: {e}")
        traceback.print_exc()

def repeat_job_evaluate():
    """(多個)打下班卡和評論"""
    load_dotenv(".env")
    e_phone = int(os.getenv("E_PHONE"))
    l_phone = int(os.getenv("L_PHONE"))
    j_estar = os.getenv("J_ESTAR")
    j_lstar = os.getenv("J_LSTAR")
    time = int(os.getenv("REC_TIME"))

    # 每次執行後更新 e_phone 和 l_phone
    for i in range(time):
        logging.info("✅ 第 %s 次測試 ---", (i+1))
        logging.info("E_PHONE: {%s}", e_phone)
        logging.info("L_PHONE: {%s}", l_phone)
        job_evaluate(j_estar, j_lstar)
        e_phone += 1
        l_phone += 1
    print(f"✅ 總共打下班卡和評論 {time} 次")


if __name__ == "__main__":
    repeat_job_evaluate()
