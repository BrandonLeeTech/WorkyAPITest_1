""" 商家端-查詢信用卡 """
import logging
import os
from dotenv import load_dotenv
from tools.response_handler import handle_response
from tools.pre_request import fetch_response
from tools.socket_data_manager import SocketDataManager


def e_credit_card_list():
    """查詢信用卡 API (GET)"""
    socket_manager = SocketDataManager()
    env_path = ".env"
    load_dotenv(env_path)
    base_url = os.getenv("BASE_URL")
    api_url = f"{base_url}/v1/employer/credit-card/list"
    access_token = socket_manager.get_data("E_TOKEN")

    query_params = {}

    try:
        logging.info("📌 測試 API : 160")
        response = fetch_response(
            api_url, access_token, method="GET", data_2=query_params
        )
        # MARK : [item]內是以清單(list)儲存值，get方法僅能處理字典(dict)內的提取，加上[0]提取第一個信用卡
        new_credit_card_id = response.json()["data"]["items"][0].get(
            "id"
        )  # 提取信用卡流水號
        socket_manager.set_data("E_credit_card_id", new_credit_card_id)
        handle_response(response)
    except Exception as e:
        raise e


if __name__ == "__main__":
    e_credit_card_list()
