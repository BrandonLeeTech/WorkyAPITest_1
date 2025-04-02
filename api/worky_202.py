""" 打工端-確認驗證碼 """
import logging
from tools.response_handler import handle_response
from tools.pre_request import fetch_response, hash_password
from tools.socket_data_manager import SocketDataManager
from utils.load_json import get_config


def l_register_confirm(base_url, phone):
    """確認驗證碼 API (POST)"""
    socket_manager = SocketDataManager()
    access_token = get_config("ACCESS_TOKEN")  # 初始化
    api_url = f"{base_url}/v1/labor/register/confirm"

    body = {
        "phone": phone,
        "password": socket_manager.get_data("L_register_code")
    }

    try:
        logging.info("📌 測試 API : 202")
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
    PHONE = "0901090000"
    BASE_URL = "https://next-staging-v210x.api.staging.worky.com.tw"
    l_register_confirm(BASE_URL, PHONE)
