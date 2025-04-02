""" 打工端-註冊 """
import logging
import os
from dotenv import load_dotenv
from tools.response_handler import handle_response
from tools.pre_request import fetch_response
from tools.socket_data_manager import SocketDataManager


def l_register(phone):
    """註冊 API (POST)"""
    socket_manager = SocketDataManager()
    access_token = "42931eaaabae4344ee0699dd5c7d3d647c8089c9b2714ad988342599d05dba75|1|qa"  # 初始化
    env_path = ".env"
    load_dotenv(env_path)
    base_url = os.getenv("BASE_URL")
    api_url = f"{base_url}/v1/labor/register"

    body = {
        "phone": phone
    }

    try:
        logging.info("📌 測試 API : 201")
        response = fetch_response(api_url, access_token, method="POST", data_1=body)
        # 提取驗證碼
        new_code = response.json()["data"].get("code")
        socket_manager.set_data("L_register_code", new_code)
        handle_response(response)
    except Exception as e:
        raise e


if __name__ == "__main__":
    PHONE = "0901090000"
    l_register(PHONE)
