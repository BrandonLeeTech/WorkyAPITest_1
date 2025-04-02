""" 商家端-日程列表 """
import logging
from tools.response_handler import handle_response
from tools.pre_request import fetch_response
from tools.socket_data_manager import SocketDataManager


def e_schedule(base_url):
    """日程列表 API (GET)"""
    socket_manager = SocketDataManager()
    api_url = f"{base_url}/v1/employer/shop/schedule/list"
    access_token = socket_manager.get_data("E_TOKEN")

    query_params = {
        "shop_id": int(socket_manager.get_data("E_shop_id")),
        "search_start_date": "20240101",  # UPDATE 這部分會影響提取的欄位要做成變數
        "search_end_date": "20300101",
    }

    try:
        logging.info("📌 測試 API : 115-1")
        response = fetch_response(
            api_url, access_token, method="GET", data_2=query_params
        )
        # 獲取第一個日期鍵值，例如 "20250109"
        # job_date = list(response.json()["data"]["items"].keys())[0]
        # 獲取最後一個日期鍵值
        job_date = list(response.json()["data"]["items"].keys())[-1]

        # 獲取第一個 job_sn 的值 (日程很亂時要注意)
        job_sn = response.json()["data"]["items"][job_date][-1]["job_sn"]
        socket_manager.set_data("JOB_SN", job_sn)
        handle_response(response)
    except Exception as e:
        raise e


if __name__ == "__main__":
    BASE_URL = "https://next-staging-v210x.api.staging.worky.com.tw"
    e_schedule(BASE_URL)
