""" 打工端-登入 """
import logging
from tools.response_handler import handle_response
from tools.pre_request import fetch_response
from tools.socket_data_manager import SocketDataManager
from utils.load_json import get_config


def l_login(base_url, phone):
    """註冊 API (POST)"""
    socket_manager = SocketDataManager()
    access_token = get_config("ACCESS_TOKEN")  # 初始化
    api_url = f"{base_url}/v1/labor/login"

    body = {
        "phone": phone
    }

    try:
        logging.info("📌 測試 API : 203")
        response = fetch_response(api_url, access_token, method="POST", data_1=body)
        new_code = response.json()["data"].get("code")  # 提取驗證碼
        socket_manager.set_data("L_login_code", new_code)
        handle_response(response)
    except Exception as e:
        raise e


if __name__ == "__main__":
    PHONE = "0902120004"
    BASE_URL = "https://next-staging-v210x.api.staging.worky.com.tw"
    l_login(BASE_URL, PHONE)
