""" 商家端-發工作 """
import logging
from tools.response_handler import handle_response
from tools.pre_request import fetch_response
from tools.socket_data_manager import SocketDataManager
from api.worky_303_e import upload_1


def e_job_publish(base_url, work_date, start_time, work_hour, custom_name="自定義工作名稱"):
    """發工作 API (POST)"""
    file_name = "job_image.png"
    upload_1(base_url, "job_image", file_name)

    socket_manager = SocketDataManager()
    api_url = f"{base_url}/v1/employer/shop/job/publish"
    access_token = socket_manager.get_data("E_TOKEN")

    body = {
        "shop_id": int(socket_manager.get_data("E_shop_id")),
        "job_sn": "",
        "job_type_level2": 3,
        "job_type_level3": 8,
        "schedule_type": 1,
        "start_date_list": [work_date],
        "start_time_period": start_time,
        "work_hours": work_hour,
        "payment_method_id": 1,
        "rest_hours": 0,
        "recruit_count": 1,
        "match_target_favor": 0,
        "hourly_wage": 250,
        "city_id": 19,
        "district_id": 195,
        "address": "延平南路189號5樓",
        "labor_insurance_deduction_type": 3,
        # "cover_photo": "",
        "cover_photo": socket_manager.get_data("job_image"),
        "photos": [],
        "description": "測試 api-109 description 欄位",
        "remarks": "測試 api-109 remarks 欄位",
        "emergency_contact_phone": "0912345678",    # 現場緊急電話
        "contact_time": "09:00-18:00",              # 可聯繫時段
        "custom_name": custom_name                  # 自定義工作名稱
    }

    try:
        logging.info("📌 測試 API : 109")
        response = fetch_response(api_url, access_token, method="POST", data_1=body)
        # 提取第一個 job_sn
        job_sn = response.json()["data"]["job_sn_list"][0]
        socket_manager.set_data("JOB_SN", job_sn)
        handle_response(response)
        return job_sn
    except Exception as e:
        raise e


if __name__ == "__main__":
    BASE_URL = "https://next-staging-v210x.api.staging.worky.com.tw"
    WORK_DATE = 20250401
    START_TIME = "18:00"
    WORK_HOUR = 2
    CUSTOM_NAME = "測試"

    e_job_publish(BASE_URL, WORK_DATE, START_TIME, WORK_HOUR, CUSTOM_NAME)
