""" 商家端-評價 """
import logging
from tools.response_handler import handle_response
from tools.pre_request import fetch_response
from tools.socket_data_manager import SocketDataManager


def e_evaluate(base_url, job_sn, stars):
    """評價 API (POST)"""
    socket_manager = SocketDataManager()
    api_url = f"{base_url}/v1/employer/evaluation/evaluate"
    access_token = socket_manager.get_data("E_TOKEN")

    body = {
        "job_sn": str(job_sn),
        "labor_id": int(socket_manager.get_data("L_labor_id")),
        "professional_stars": stars,
        "attitude_stars": stars,
        "cleanliness_stars": stars,
        "content": "很好，表現不錯！",
    }

    try:
        logging.info("📌 測試 API : 126-1")
        response = fetch_response(api_url, access_token, method="POST", data_1=body)
        handle_response(response)
    except Exception as e:
        raise e
