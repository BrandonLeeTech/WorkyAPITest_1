""" 打工端-更新工作偏好 """
import logging
from tools.pre_request import fetch_response
from tools.response_handler import handle_response
from tools.socket_data_manager import SocketDataManager


def l_update_preference(base_url):
    """更新工作偏好 API (POST)"""
    socket_manager = SocketDataManager()
    api_url = f"{base_url}/v1/labor/update/preference"
    access_token = socket_manager.get_data("L_TOKEN")

    body = {
        "chosen_experiences": [],
        "chosen_districts": [409]
    }

    try:
        logging.info("📌 測試 API : 205-2")
        response = fetch_response(api_url, access_token, method="POST", data_1=body)
        handle_response(response)
    except Exception as e:
        raise e


if __name__ == "__main__":
    BASE_URL = "https://next-staging-v210x.api.staging.worky.com.tw"
    l_update_preference(BASE_URL)
