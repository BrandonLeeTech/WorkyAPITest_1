""" 處理 Call API 時返回的結果 """

import json

def handle_response(response):
    """處理 API 回應，解析 JSON 或返回錯誤訊息"""
    if response.status_code == 200:
        try:
            formatted_json = json.dumps(response.json(), indent=4, ensure_ascii=False)
            print("API 回應:")
            print(formatted_json)
            return response.json()  # 返回解析的 JSON
        except ValueError as e:
            print("JSON 解析失敗:", e)
            return None
    else:  # 處理失敗的回應
        print(f"請求失敗: {response.status_code}")
        print(f"錯誤內容: {response.text}")
        return None
