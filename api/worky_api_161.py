""" 商家端-綁定信用卡 """
import logging
import time
import os
from dotenv import load_dotenv
from tools.response_handler import handle_response
from tools.pre_request import fetch_response
from tools.socket_data_manager import SocketDataManager


def e_credit_card_bind():
    """綁定信用卡 API (GET)"""
    socket_manager = SocketDataManager()
    env_path = ".env"
    load_dotenv(env_path)
    base_url = os.getenv("BASE_URL")
    api_url = f"{base_url}/v1/employer/credit-card/bind"
    access_token = socket_manager.get_data("E_TOKEN")

    query_params = {}

    try:
        logging.info("📌 測試 API : 161")
        response = fetch_response(
            api_url, access_token, method="GET", data_2=query_params
        )
        time.sleep(2)
        # 提取 funpoint 設置信用卡網址
        new_credit_card_url = response.json()["data"].get("url")
        socket_manager.set_data("E_credit_card_url", new_credit_card_url)
        handle_response(response)
    except Exception as e:
        raise e


if __name__ == "__main__":
    e_credit_card_bind()
