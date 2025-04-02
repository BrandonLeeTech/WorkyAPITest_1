""" 商家端-帳戶設定 """
import logging
from tools.response_handler import handle_response
from tools.pre_request import fetch_response
from tools.socket_data_manager import SocketDataManager


def e_bank_account_update(base_url):
    """帳戶設定 API (POST)"""
    socket_manager = SocketDataManager()
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
    BASE_URL = "https://next-staging-v210x.api.staging.worky.com.tw"
    e_bank_account_update(BASE_URL)
