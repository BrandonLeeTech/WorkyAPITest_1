"""streamlit 頁面可測試的腳本"""

from helper.e_account import setting_account
from helper.e_register import register_and_validation
from helper.l_register import register_and_setting
from helper.job_publish import repeat_job_publish
from helper.job_match import repeat_job_match_single
from helper.job_clock_in import job_clock_in
from helper.job_clock_out import job_clock_out


COMMON_URL = [
    "https://next-staging-v210x.api.staging.worky.com.tw",
    "https://next-staging-v211x.api.staging.worky.com.tw",
    "https://next-v211x.api.test.worky.com.tw/"
]

EVALUATE = [1,2,3,4,5]

SCRIPTS = {
    "商家_註冊": {
        "function": register_and_validation,
        "params": {
            "base_url": COMMON_URL,
            "e_phone": "text",
            "e_name": "text",
            "e_shop": "text"
        }
    },
    "商家_設置帳號": {
        "function": setting_account,
        "params": {
            "base_url": COMMON_URL,
            "e_phone": "text"
        }
    },
    "打工_註冊": {
        "function": register_and_setting,
        "params": {
            "base_url": COMMON_URL,
            "l_phone": "text",
            "l_name": "text"
        }
    },
    "商家發布工作": {
        "function": repeat_job_publish,
        "params": {
            "base_url": COMMON_URL,
            "time": [1,2,3,4,5,6,7,8,9,10],
            "e_phone": "text",
            "work_date": "text",
            "start_time": "text",
            "work_hour": [1,2,4,8,12],
            "custom_name": "text"
        }
    },
    "單人媒合多個工單(每天同時段)": {
        "function": repeat_job_match_single,
        "params": {
            "base_url": COMMON_URL,
            "time": [1,2,3,4,5,6,7,8,9,10],
            "e_phone": "text",
            "l_phone": "text",
            "work_date": "text",
            "start_time": "text",
            "work_hour": [1,2,4,8,12],
            "custom_name": "text"
        }
    },
    "打上班卡": {
        "function": job_clock_in,
        "params": {
            "base_url": COMMON_URL,
            "e_phone": "text",
            "l_phone": "text",
            "job_sn": "text",
        }
    },
    "打下班卡": {
        "function": job_clock_out,
        "params": {
            "base_url": COMMON_URL,
            "e_phone": "text",
            "l_phone": "text",
            "job_sn": "text",
            "j_estar": EVALUATE,
            "j_lstar": EVALUATE,
        }
    }
}
