""" 商家端-新增店鋪 """
import logging
from tools.response_handler import handle_response
from tools.pre_request import fetch_response
from tools.socket_data_manager import SocketDataManager
from api.worky_303_e import upload_e


def e_shop_create(base_url, e_shop_name):
    """新增店鋪 API (POST)"""
    file_name = "shop_company_logo_image.png"
    upload_e(base_url, "shop_company_logo_image", file_name)

    socket_manager = SocketDataManager()
    api_url = f"{base_url}/v1/employer/shop/create"
    access_token = socket_manager.get_data("E_TOKEN")

    body = {
        "name": e_shop_name,
        "branch_name": "台北店",
        "city": 19,
        "district": 193,
        "address": "南京東路",
        "job_type_level1": 1,
        "mobile_phone": "0912345678",
        "email": "lee@outlook.com",
        "company_logo": socket_manager.get_data("shop_company_logo_image"),
    }

    try:
        logging.info("📌 測試 API : 105-1")
        response = fetch_response(api_url, access_token, method="POST", data_1=body)
        shop_id = response.json()["data"].get("shop_id") # 提取 shop_id
        socket_manager.set_data("E_shop_id", shop_id)
        handle_response(response)
    except Exception as e:
        raise e


if __name__ == "__main__":
    E_SHOP_NAME = "測試商家"
    BASE_URL = "https://next-staging-v210x.api.staging.worky.com.tw"
    e_shop_create(BASE_URL, E_SHOP_NAME)
