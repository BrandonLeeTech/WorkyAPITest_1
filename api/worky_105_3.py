""" 商家端-公司送審 """
import logging
from tools.response_handler import handle_response
from tools.pre_request import fetch_response
from tools.socket_data_manager import SocketDataManager
from api.worky_303_e import upload_e


def e_shop_validation_request(base_url, e_name):
    """公司送審 API (POST)"""
    file_name = "shop_verify_image.png"
    upload_e(base_url, "shop_verify_image", file_name)

    socket_manager = SocketDataManager()
    api_url = f"{base_url}/v1/employer/shop/validation/request"
    access_token = socket_manager.get_data("E_TOKEN")

    body = {
        "shop_id": socket_manager.get_data("E_shop_id"),
        "verify_name": e_name,
        "verify_city": 19,
        "verify_district": 193,
        "verify_address": "延平南路189號5樓",
        "tax_id_number": "12345678",
        "verify_pic_1": socket_manager.get_data("shop_verify_image"),
        "is_draft": False,
        "validation_type": 1,
    }

    try:
        logging.info("📌 測試 API : 105-3")
        response = fetch_response(api_url, access_token, method="POST", data_1=body)
        handle_response(response)
    except Exception as e:
        raise e


if __name__ == "__main__":
    E_NAME = "lee的商家"
    BASE_URL = "https://next-staging-v210x.api.staging.worky.com.tw"
    e_shop_validation_request(BASE_URL, E_NAME)
