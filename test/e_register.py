""" 註冊商家 """

# pylint: disable = [unused-wildcard-import], [wildcard-import]
import traceback
import streamlit as st
from web import *
from api import *
# from utils.process_manager import ProcessManager

def register_and_validation(base_url, e_phone, e_name, e_shop):
    """註冊商家 > 通過審核"""
    try:
        backend_url = base_url.replace("api", "backend", 1)
        worky_101.e_register(base_url, e_phone)
        worky_102.e_register_confirm(base_url, e_phone)
        worky_105_1.e_shop_create(base_url, e_shop)
        worky_105_3.e_shop_validation_request(base_url, e_name)
        shop_audit_passed_h(backend_url, e_phone)
        return {"status": "pass", "msg": "商家註冊成功"}

    except ValueError as e:
        st.error(f"輸入錯誤 : {e}")
        return {"status": "fail", "msg": "商家註冊失敗"}
    except Exception as e: # pylint: disable = [broad-exception-caught]
        st.error(f"未預期錯誤，檢查 API LOG : {e}")
        traceback.print_exc()
        return {"status": "fail", "msg": "商家註冊失敗"}



if __name__ == "__main__":
    BASE_URL = "https://next-staging-v210x.api.staging.worky.com.tw"
    E_PHONE = "903310005"
    E_NAME = "Brandon"
    E_SHOP = "Lee's shop"

    register_and_validation(BASE_URL, E_PHONE, E_NAME, E_SHOP)
