""" 打工端-申請上工 """
import logging
from tools.pre_request import fetch_response
from tools.response_handler import handle_response
from tools.socket_data_manager import SocketDataManager


def l_job_match_apply(base_url):
    """申請上工 API (POST)"""
    socket_manager = SocketDataManager()
    api_url = f"{base_url}/v1/labor/job-match/job-apply"
    access_token = socket_manager.get_data("L_TOKEN")

    body = {
        "job_sn": socket_manager.get_data("JOB_SN")
    }

    try:
        logging.info("📌 測試 API : 210-1")
        response = fetch_response(api_url, access_token, method="POST", data_1=body)
        handle_response(response)
    except Exception as e:
        raise e


if __name__ == "__main__":
    BASE_URL = "https://next-staging-v210x.api.staging.worky.com.tw"
    l_job_match_apply(BASE_URL)
