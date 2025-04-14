"""streamlit 頁面可測試的腳本"""

from helper.e_register import repeat_register_and_validation # 商家註冊
from helper.e_account import repeat_setting_account # 商家帳務設定

from helper.l_register import repeat_register_and_setting # 打工註冊

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
GENERATE_TIME = [1,2,5,10]

SCRIPTS = {
    "商家_註冊": {
        "function": repeat_register_and_validation,
        "params": {
            "base_url": COMMON_URL,
            "time": GENERATE_TIME,
            "e_phone": "text",
            "e_name": "text"
        }
    },
    "商家_帳務設置": {
        "function": repeat_setting_account,
        "params": {
            "base_url": COMMON_URL,
            "time": GENERATE_TIME,
            "e_phone": "text"
        }
    },
    "打工_註冊(待審核)": {
        "function": repeat_register_and_setting,
        "params": {
            "base_url": COMMON_URL,
            "time": GENERATE_TIME,
            "l_phone": "text",
            "l_name": "text"
        }
    },
    "商家發布工作": {
        "function": repeat_job_publish,
        "params": {
            "base_url": COMMON_URL,
            "time": GENERATE_TIME,
            "e_phone": "text",
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
    },
    "單一打工媒合多張工單(work_date++)": {
        "function": repeat_job_match_single,
        "params": {
            "base_url": COMMON_URL,
            "time": GENERATE_TIME,
            "e_phone": "text",
            "l_phone": "text",
            "work_date": "text",
            "start_time": "text",
            "work_hour": [1,2,4,8,12],
            "custom_name": "text"
        }
    }
}
