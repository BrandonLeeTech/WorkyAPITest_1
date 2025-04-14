""" 打工端-打下班卡 """
import logging
from tools.pre_request import fetch_response
from tools.response_handler import handle_response
from tools.socket_data_manager import SocketDataManager


def l_job_clock_out(base_url, job_sn):
    """打下班卡 API (POST)"""
    socket_manager = SocketDataManager()
    api_url = f"{base_url}/v1/labor/job/clock-out"
    access_token = socket_manager.get_data("L_TOKEN")

    body = {
        "job_sn": str(job_sn),
        "code": socket_manager.get_data("JOB_end_code")
    }

    try:
        logging.info("📌 測試 API : 214")
        response = fetch_response(api_url, access_token, method="POST", data_1=body)
        handle_response(response)
    except Exception as e:
        raise e

