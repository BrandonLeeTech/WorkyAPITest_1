""" 打工端-資訊查詢 """
import logging
import os
from dotenv import load_dotenv
from tools.response_handler import handle_response
from tools.pre_request import fetch_response
from tools.socket_data_manager import SocketDataManager


def l_profile():
    """資訊查詢 API (GET)"""
    socket_manager = SocketDataManager()
    env_path = ".env"
    load_dotenv(env_path)
    base_url = os.getenv("BASE_URL")
    api_url = f"{base_url}/v1/labor/profile"
    access_token = socket_manager.get_data("L_TOKEN")

    query_params = {}

    try:
        logging.info("📌 測試 API : 206")
        response = fetch_response(
            api_url, access_token, method="GET", data_2=query_params
        )
        new_labor_id = response.json()["data"].get("id")  # 提取打工帳號
        socket_manager.set_data("L_labor_id", new_labor_id)
        handle_response(response)
    except Exception as e:
        raise e


if __name__ == "__main__":
    l_profile()
