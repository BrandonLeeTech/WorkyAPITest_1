""" 打工端-更新資訊 """
import logging
from tools.pre_request import fetch_response
from tools.response_handler import handle_response
from tools.socket_data_manager import SocketDataManager
from api.worky_303_l import upload_l
from utils.id_num_generation import generate_id_number


def l_update(base_url, labor_name='測試打工'):
    """更新資訊 API (POST)"""
    file_name = "labor_profile_image.png"
    file_name = "labor_id_card_image.png"
    upload_l(base_url, "labor_profile_image", file_name)
    upload_l(base_url, "labor_id_card_image", file_name)

    socket_manager = SocketDataManager()
    api_url = f"{base_url}/v1/labor/update"
    access_token = socket_manager.get_data("L_TOKEN")
    id_number = generate_id_number()

    body = {
        "step": 4,
        "display_name": labor_name,
        "display_name_english": "Brandon",
        "gender": "male",
        "birthday": "2000-01-01",
        "city": 19,
        "district": 190,
        "address": "延平南路189號8樓",
        "id_number": id_number,
        "email": "abc123@gmail.com",
        "emergency_contact_person": "陳大名",
        "emergency_contact_relation": "父子",
        "emergency_contact_phone": "0933123123",
        "education": 4,
        "school": "台灣大學",
        "school_department": "哲學系",
        "education_status": 1,
        "picture": socket_manager.get_data("labor_profile_image"),
        "id_card_front_image": socket_manager.get_data("labor_id_card_image"),
        "id_card_back_image": socket_manager.get_data("labor_id_card_image"),
        "bank_code": "004",
        "bank_text": "臺灣銀行",
        "bank_branch_code": "1234",
        "bank_account": "1234567890",
        "bank_account_name": "陳老饕",
        "driving_license_ids": "3,6",
        "work_experiences": [
            {
                "id": 0,
                "type_id": 1,
                "work_years": 3,
                "work_months": 4,
                "content": "工作內容...",
            },
            {
                "id": 0,
                "type_id": 2,
                "work_years": 2,
                "work_months": 10,
                "content": "工作內容...",
            },
        ],
    }

    try:
        logging.info("📌 測試 API : 205-1")
        response = fetch_response(api_url, access_token, method="POST", data_1=body)
        handle_response(response)
    except Exception as e:
        raise e


if __name__ == "__main__":
    BASE_URL = "https://next-staging-v210x.api.staging.worky.com.tw"
    LABOR_NAME = "打工夥伴名稱一"
    l_update(BASE_URL, LABOR_NAME)
