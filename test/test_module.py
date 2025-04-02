""" 測試用 """

# pylint: disable = [unused-wildcard-import], [wildcard-import]
import traceback
from api import *

def test_func(base_url, e_phone):
    """測試用"""
    try:
        worky_103.e_login(base_url, e_phone)
        worky_104.e_login_confirm(base_url, e_phone)
        worky_106.e_profile(base_url)
        # return {"status": "pass", "msg": "成功"}
        return {"status": "pass"}

    except ValueError as e:
        return {"status": "fail", "msg": f"輸入錯誤 : {e}"}
    except Exception as e: # pylint: disable = [broad-exception-caught]
        traceback.print_exc()
        return {"status": "fail", "msg": f"未預期錯誤，檢查 API LOG : {e}"}


if __name__ == "__main__":
    BASE_URL = "https://next-staging-v210x.api.staging.worky.com.tw"
    E_PHONE = "903310005"

    test_func(BASE_URL, E_PHONE)
