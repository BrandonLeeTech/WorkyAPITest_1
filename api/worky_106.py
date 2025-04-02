""" 商家端-資訊查詢 """
import logging
from tools.response_handler import handle_response
from tools.pre_request import fetch_response
from tools.socket_data_manager import SocketDataManager


def e_profile(base_url):
    """資訊查詢 API (GET)"""
    socket_manager = SocketDataManager()
    api_url = f"{base_url}/v1/employer/profile"
    access_token = socket_manager.get_data("E_TOKEN")

    query_params = {}

    try:
        logging.info("📌 測試 API : 106")
        response = fetch_response(api_url, access_token, method="GET", data_2=query_params)
        # 提取 shop_id
        new_shop_id = response.json()["data"]["shops"][0].get("id")
        socket_manager.set_data("E_shop_id", new_shop_id)
        handle_response(response)
    except Exception as e:
        raise e


if __name__ == "__main__":
    BASE_URL = "https://next-staging-v210x.api.staging.worky.com.tw"
    e_profile(BASE_URL)
