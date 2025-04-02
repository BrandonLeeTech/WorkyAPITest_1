""" 商家端-發票設定 """
import logging
import os
from dotenv import load_dotenv
from tools.response_handler import handle_response
from tools.pre_request import fetch_response
from tools.socket_data_manager import SocketDataManager


def e_invoice_update():
    """發票設定 API (POST)"""
    socket_manager = SocketDataManager()
    env_path = ".env"
    load_dotenv(env_path)
    base_url = os.getenv("BASE_URL")
    api_url = f"{base_url}/v1/employer/invoice/update"
    access_token = socket_manager.get_data("E_TOKEN")

    body = {
        "type": 0,
        "phone": "0912345678",
        "email": "leo.tsun@gamehours.com"
    }

    try:
        logging.info("📌 測試 API : 171")
        response = fetch_response(api_url, access_token, method="POST", data_1=body)
        handle_response(response)
    except Exception as e:
        raise e


if __name__ == "__main__":
    e_invoice_update()
