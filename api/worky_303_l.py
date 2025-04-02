""" 上傳圖片 """
import logging
from tools.socket_data_manager import SocketDataManager
from tools.response_handler import handle_response
from tools.pre_request import fetch_response
from tools.convert_base64 import image_to_base64

def upload_l(base_url, body_type, file_name):
    """上傳圖片 API (POST)"""
    socket_manager = SocketDataManager()
    api_url = f"{base_url}/v1/upload"
    access_token = socket_manager.get_data("L_TOKEN")

    body = {
        "type": body_type,
        "files": [{
            "id": "image1",
            "content": image_to_base64(file_name)
        }]
    }

    try:
        logging.info("📌 測試 API : 303")
        response = fetch_response(api_url, access_token, method="POST", data_1=body)
        image_url = response.json()["data"]["uploadedFiles"][0].get("url")
        socket_manager.set_data(body_type, image_url)
        handle_response(response)
    except Exception as e:
        raise e

if __name__ == "__main__":
    BASE_URL = "https://next-staging-v210x.api.staging.worky.com.tw"
    upload_l(BASE_URL, "labor_id_card_image", "worky.png")
