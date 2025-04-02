""" 商家端-發票設定 """
import logging
from tools.response_handler import handle_response
from tools.pre_request import fetch_response
from tools.socket_data_manager import SocketDataManager


def e_invoice_update(base_url):
    """發票設定 API (POST)"""
    socket_manager = SocketDataManager()
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
    BASE_URL = "https://next-staging-v210x.api.staging.worky.com.tw"
    e_invoice_update(BASE_URL)
