""" 打工端-登入確認驗證碼 """
import logging
import os
from dotenv import load_dotenv
from tools.response_handler import handle_response
from tools.pre_request import fetch_response, hash_password
from tools.socket_data_manager import SocketDataManager


def l_login_confirm(phone):
    """確認驗證碼 API (POST)"""
    socket_manager = SocketDataManager()
    access_token = "42931eaaabae4344ee0699dd5c7d3d647c8089c9b2714ad988342599d05dba75|1|qa"  # 初始化
    env_path = ".env"
    load_dotenv(env_path)
    base_url = os.getenv("BASE_URL")
    api_url = f"{base_url}/v1/labor/login/confirm"
    code = socket_manager.get_data("L_login_code")

    body = {
        "phone": phone,
        "password": code
    }

    try:
        logging.info("📌 測試 API : 204")
        # 對 "password" 進行 MD5 雜湊處理
        body["password"] = hash_password(body["password"])
        response = fetch_response(api_url, access_token, method="POST", data_1=body)
        # 提取 Access Token
        new_access_token = response.json()["data"].get("accessToken")
        socket_manager.set_data("L_TOKEN", new_access_token)
        handle_response(response)
    except Exception as e:
        raise e


if __name__ == "__main__":
    PHONE = "0902120003"
    l_login_confirm(PHONE)
