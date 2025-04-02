""" 商家端-通知打上班碼 """
import logging
from tools.response_handler import handle_response
from tools.pre_request import fetch_response
from tools.socket_data_manager import SocketDataManager


def e_send_start_code(base_url):
    """打上班碼 API (POST)"""
    socket_manager = SocketDataManager()
    api_url = f"{base_url}/v1/employer/labor/send-start-code"
    access_token = socket_manager.get_data("E_TOKEN")

    body = {
        "job_sn": socket_manager.get_data("JOB_SN"),
        "labor_id": int(socket_manager.get_data("L_labor_id"))
    }

    try:
        logging.info("📌 測試 API : 122")
        response = fetch_response(api_url, access_token, method="POST", data_1=body)
        handle_response(response)
    except Exception as e:
        raise e


if __name__ == "__main__":
    BASE_URL = "https://next-staging-v210x.api.staging.worky.com.tw"
    e_send_start_code(BASE_URL)
