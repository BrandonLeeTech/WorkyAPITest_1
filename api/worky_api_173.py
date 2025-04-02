""" 商家端-帳戶設定 """
import logging
import os
from dotenv import load_dotenv
from tools.response_handler import handle_response
from tools.pre_request import fetch_response
from tools.socket_data_manager import SocketDataManager


def e_bank_account_update():
    """帳戶設定 API (POST)"""
    socket_manager = SocketDataManager()
    env_path = ".env"
    load_dotenv(env_path)
    base_url = os.getenv("BASE_URL")
    api_url = f"{base_url}/v1/employer/bank-account/update"
    access_token = socket_manager.get_data("E_TOKEN")

    body = {
        "bank_code": "004",
        "bank_text": "臺灣銀行",
        "bank_branch_code": "1234",
        "bank_account": "1234567890",
        "bank_account_name": "陳老饕",
    }

    try:
        logging.info("📌 測試 API : 173")
        response = fetch_response(api_url, access_token, method="POST", data_1=body)
        handle_response(response)
    except Exception as e:
        raise e


if __name__ == "__main__":
    e_bank_account_update()
