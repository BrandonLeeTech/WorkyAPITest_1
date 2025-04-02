""" 商家帳務設定 """

# pylint: disable = w0401, w0614, w0611, w0718
import os
import logging
import traceback
from dotenv import load_dotenv
from web import *
from api import *
from config.logger_config import LoggerConfig

def employer_account(e_phone):
    """商家帳務設定"""
    try:
        worky_103.e_login(e_phone)
        worky_104.e_login_confirm(e_phone)
        worky_api_161.e_credit_card_bind()
        credit_card_bind_h()
        worky_api_171.e_invoice_update()
        worky_api_173.e_bank_account_update()
    except Exception as e:
        print(f"❌ 發生例外: {e}")
        traceback.print_exc()

def repeat_employer_account():
    """設定(多個)商家的帳務"""
    load_dotenv(".env")
    e_phone = int(os.getenv("E_PHONE"))
    time = int(os.getenv("REC_TIME"))

    # 每次執行後更新 e_phone
    for i in range(time):
        logging.info("✅ 第 %s 次測試 ---", (i+1))
        logging.info("E_PHONE: {%s}", e_phone)
        employer_account(e_phone)
        e_phone += 1
    print(f"✅ 總共設定 {time} 個商家帳務")


if __name__ == "__main__":
    repeat_employer_account()
