""" 商家端-發工作 """
import logging
from tools.response_handler import handle_response
from tools.pre_request import fetch_response
from tools.socket_data_manager import SocketDataManager

def e_job_publish():
    """發工作 API (POST)"""
    socket_manager = SocketDataManager()
    start_date = [20250325]
    # start_date = [20250321, 20250322]
    start_time = "15:50"
    base_url = "https://next-staging-v210x.api.staging.worky.com.tw"
    api_url = f"{base_url}/v1/employer/shop/job/publish"
    access_token = socket_manager.get_data("E_TOKEN")
    shop_id = int(socket_manager.get_data("E_shop_id"))

    body = {
        "shop_id": shop_id,
        "job_sn": "",
        "job_type_level2": 3,
        "job_type_level3": 8,
        "schedule_type": 1,
        "start_date_list": start_date,
        "start_time_period": start_time,
        "payment_method_id": 1,         # 付款方式
        "work_hours": 1,                # 工作時間，灌資料時有時候會需要超過 1 小時
        "rest_hours": 0,
        "recruit_count": 1,                         # 人數
        "match_target_favor": 0,                    # 最愛夥伴
        "hourly_wage": 666,
        "city_id": 19,
        "district_id": 195,
        "address": "延平南路189號5樓",
        "labor_insurance_deduction_type": 3,
        "cover_photo": "",
        "photos": [],
        "description": "Postman 發佈",
        "remarks": "Postman 發佈",
        "emergency_contact_phone": "09",            # 現場緊急電話
        "contact_time": "14:00-18:00",              # 可聯繫時段
        "custom_name": "自定義工作名稱",             # 自定義工作名稱
    }

    try:
        logging.info("📌 測試 API : 109-1")
        response = fetch_response(api_url, access_token, method="POST", data_1=body)
        # 提取第一個 job_sn
        job_sn = response.json()["data"]["job_sn_list"][0]
        socket_manager.set_data("JOB_SN", job_sn)
        handle_response(response)
        return job_sn
    except Exception as e:
        raise e


if __name__ == "__main__":
    # (離現在時間差幾分鐘, 付款方式)
    # 發失敗可能是 token 過期
    e_job_publish()
