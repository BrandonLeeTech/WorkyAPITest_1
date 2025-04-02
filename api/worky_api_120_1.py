""" 商家端-同意上工 """
import logging
import os
from dotenv import load_dotenv
from tools.response_handler import handle_response
from tools.pre_request import fetch_response
from tools.socket_data_manager import SocketDataManager


def e_job_match_accept():
    """同意上工 API (POST)"""
    socket_manager = SocketDataManager()
    env_path = ".env"
    load_dotenv(env_path)
    base_url = os.getenv("BASE_URL")
    api_url = f"{base_url}/v1/employer/shop/job-match/accept"
    access_token = socket_manager.get_data("E_TOKEN")
    job_sn = socket_manager.get_data("JOB_SN")
    new_labor_id = int(socket_manager.get_data("L_labor_id"))

    body = {
        "job_sn": job_sn,
        "labor_id": new_labor_id
    }

    try:
        logging.info("📌 測試 API : 120-1")
        response = fetch_response(api_url, access_token, method="POST", data_1=body)
        handle_response(response)
    except Exception as e:
        raise e


if __name__ == "__main__":
    e_job_match_accept()
