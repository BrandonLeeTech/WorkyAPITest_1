""" 打工端-打上班卡 """
import logging
from tools.pre_request import fetch_response
from tools.response_handler import handle_response
from tools.socket_data_manager import SocketDataManager


def l_job_clock_in(base_url):
    """打上班卡 API (POST)"""
    socket_manager = SocketDataManager()
    api_url = f"{base_url}/v1/labor/job/clock-in"
    access_token = socket_manager.get_data("L_TOKEN")

    body = {
        "job_sn": socket_manager.get_data("JOB_SN"),
        "code": socket_manager.get_data("JOB_start_code")
    }

    try:
        logging.info("📌 測試 API : 213")
        response = fetch_response(api_url, access_token, method="POST", data_1=body)
        handle_response(response)
    except Exception as e:
        raise e


if __name__ == "__main__":
    BASE_URL = "https://next-staging-v210x.api.staging.worky.com.tw"
    l_job_clock_in(BASE_URL)
