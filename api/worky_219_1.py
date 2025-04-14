""" 打工端-評價 """
import logging
from tools.pre_request import fetch_response
from tools.response_handler import handle_response
from tools.socket_data_manager import SocketDataManager


def l_evaluate(base_url, job_sn, stars):
    """評價 API (POST)"""
    socket_manager = SocketDataManager()
    api_url = f"{base_url}/v1/labor/evaluation/evaluate"
    access_token = socket_manager.get_data("L_TOKEN")

    body = {
        "job_sn": str(job_sn),
        "atmosphere_stars": stars,
        "environment_stars": stars,
        "communication_stars": stars,
        "content": "很好，老板不錯！",
    }

    try:
        logging.info("📌 測試 API : 219-1")
        response = fetch_response(api_url, access_token, method="POST", data_1=body)
        handle_response(response)
    except Exception as e:
        raise e

