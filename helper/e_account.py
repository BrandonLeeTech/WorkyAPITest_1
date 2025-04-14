""" 商家帳務設定 """

# pylint: disable = [unused-wildcard-import], [wildcard-import]
import logging
import traceback
import streamlit as st
from web import *
from api import *

def setting_account(base_url, e_phone):
    """商家帳務設定"""
    worky_103.e_login(base_url, e_phone)
    worky_104.e_login_confirm(base_url, e_phone)
    worky_161.e_credit_card_bind(base_url)
    worky_171.e_invoice_update(base_url)
    worky_173.e_bank_account_update(base_url)
    credit_card_bind_h()


def repeat_setting_account(base_url, time, e_phone):
    """設定(多個)商家的帳務"""
    e_phone = int(e_phone)
    time = int(time)

    try:
        # 每次執行後更新 e_phone
        for i in range(time):
            logging.info("✅ 第 %s 次測試 ---", (i+1))
            logging.info("E_PHONE: {%s}", e_phone)
            setting_account(base_url, e_phone)
            e_phone += 1
        return {"status": "pass", "msg": "商家帳務設定成功"}
    except ValueError as e:
        st.error(f"輸入錯誤 : {e}")
        return {"status": "fail", "msg": "商家帳務設定失敗"}
    except Exception as e: # pylint: disable = [broad-exception-caught]
        st.error(f"未預期錯誤，檢查 API LOG : {e}")
        traceback.print_exc()
        return {"status": "fail", "msg": "商家帳務設定失敗"}


if __name__ == "__main__":
    BASE_URL = "https://next-staging-v210x.api.staging.worky.com.tw"
    E_PHONE = "0904140004"
    TIME = 1

    repeat_setting_account(BASE_URL, TIME, E_PHONE)
