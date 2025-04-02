""" 商家端-註冊 """
import logging
from tools.response_handler import handle_response
from tools.pre_request import fetch_response
from tools.socket_data_manager import SocketDataManager
from utils.load_json import get_config


def e_register(base_url, phone):
    """註冊 API (POST)"""
    socket_manager = SocketDataManager()
    access_token = get_config("ACCESS_TOKEN")  # 初始化
    api_url = f"{base_url}/v1/employer/register"

    body = {
        "phone": phone
    }

    try:
        logging.info("📌 測試 API : 101")
        response = fetch_response(api_url, access_token, method="POST", data_1=body)
        # 提取驗證碼
        new_code = response.json()["data"].get("code")
        socket_manager.set_data("E_register_code", new_code)
        handle_response(response)
    except Exception as e:
        raise e


if __name__ == "__main__":
    PHONE = "0903310001"
    BASE_URL = "https://next-staging-v210x.api.staging.worky.com.tw"
    e_register(BASE_URL, PHONE)
