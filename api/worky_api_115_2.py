""" 商家端-日程內頁(查看打卡碼) """
import logging
import os
from dotenv import load_dotenv
from tools.response_handler import handle_response
from tools.pre_request import fetch_response
from tools.socket_data_manager import SocketDataManager


def e_shop_schedule_info():
    """日程內頁(查看打卡碼) API (GET)"""
    socket_manager = SocketDataManager()
    env_path = ".env"
    load_dotenv(env_path)
    base_url = os.getenv("BASE_URL")
    api_url = f"{base_url}/v1/employer/shop/schedule/info"
    access_token = socket_manager.get_data("E_TOKEN")
    job_sn = socket_manager.get_data("JOB_SN")

    query_params = {
        "job_sn": str(job_sn)
    }

    try:
        logging.info("📌 測試 API : 115-2")
        response = fetch_response(
            api_url, access_token, method="GET", data_2=query_params
        )
        # 提取上班碼
        start_code = response.json()["data"]["labors"][0].get("start_code")
        socket_manager.set_data("JOB_start_code", start_code)
        # 提取下班碼
        end_code = response.json()["data"]["labors"][0].get("end_code")
        socket_manager.set_data("JOB_end_code", end_code)
        # 提取打工帳號
        labors = response.json()["data"]["labors"]
        new_labor_id = labors[0].get("labor_id")
        socket_manager.set_data("L_labor_id", new_labor_id)
        handle_response(response)
    except Exception as e:
        raise e


if __name__ == "__main__":
    e_shop_schedule_info()
