""" 打工端-登入確認驗證碼 """
import logging
from tools.response_handler import handle_response
from tools.pre_request import fetch_response, hash_password
from tools.socket_data_manager import SocketDataManager
from utils.load_json import get_config


def l_login_confirm(base_url, phone):
    """確認驗證碼 API (POST)"""
    socket_manager = SocketDataManager()
    access_token = get_config("ACCESS_TOKEN")  # 初始化
    api_url = f"{base_url}/v1/labor/login/confirm"

    body = {
        "phone": phone,
        "password": socket_manager.get_data("L_login_code")
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
    BASE_URL = "https://next-staging-v210x.api.staging.worky.com.tw"
    l_login_confirm(BASE_URL, PHONE)
