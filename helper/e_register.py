""" 註冊商家 """

# pylint: disable = [unused-wildcard-import], [wildcard-import]
import logging
import traceback
import streamlit as st
from web import *
from api import *

def register_and_validation(base_url, e_phone, e_name, e_shop):
    """註冊商家 > 通過審核"""
    worky_101.e_register(base_url, e_phone)
    worky_102.e_register_confirm(base_url, e_phone)
    worky_105_1.e_shop_create(base_url, e_shop)
    worky_105_3.e_shop_validation_request(base_url, e_name)
    backend_url = base_url.replace("api", "backend", 1)
    shop_audit_passed_h(backend_url, e_phone)


def repeat_register_and_validation(base_url, time, e_phone, e_name, e_shop):
    """註冊(多個)商家"""
    e_phone = int(e_phone)
    time = int(time)

    try:
        # 每次執行後更新 e_phone 和 e_shop, 提取 e_shop 的數字部分增加後重新組合
        for i in range(time):
            logging.info("✅ 第 %s 次測試 ---", (i+1))
            logging.info("E_PHONE: {%s}", e_phone)
            register_and_validation(base_url, e_phone, e_name, e_shop)
            e_phone += 1
            name_prefix = "".join([c for c in e_shop if not c.isdigit()])  # 提取非數字部分
            name_number = "".join([c for c in e_shop if c.isdigit()])      # 提取數字部分
            e_shop = f"{name_prefix}{int(name_number or '0') + 1}"         # 數字部分加 1 (為空時回傳 '0')
        return {"status": "pass", "msg": "商家註冊成功"}

    except ValueError as e:
        st.error(f"輸入錯誤 : {e}")
        return {"status": "fail", "msg": "商家註冊失敗"}
    except Exception as e: # pylint: disable = [broad-exception-caught]
        st.error(f"未預期錯誤，檢查 API LOG : {e}")
        traceback.print_exc()
        return {"status": "fail", "msg": "商家註冊失敗"}
