""" 生成 Headers & 處理加密 """
import time
import json
import hashlib
import urllib.parse
import requests
from utils.load_json import get_config

def hash_password(password):
    """對密碼進行 MD5 雜湊處理"""
    return hashlib.md5(password.encode("utf-8")).hexdigest()

def generate_headers(access_token, body=None, query=None, include_signature=False):
    """生成通用的 API Headers"""
    # 處理 Query String, 確保符合 API 簽名規範
    query = query or {}
    sorted_query = sorted(query.items())
    query_string = "&".join(
        f"{key}={urllib.parse.quote_plus(str(value))}" for key, value in sorted_query
    )
    # 處理 Body
    if body:
        body_text_for_signature = json.dumps(body)
        minimal_body = {key: value for key, value in body.items() if key != "files"}
        body_text = json.dumps(minimal_body)
    else:
        body_text_for_signature = body_text = ""
    # 處理 COMMON_VARS, JSON 格式化
    common_vars = get_config("COMMON_VARS").copy()
    common_vars["time"] = int(time.time())
    common_vars_str = json.dumps(common_vars)
    # 設置 Headers
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "X-Worky-Common-Variables": common_vars_str,
    }
    # 處理 X-Worky-Signature
    if include_signature:
        signature_data = (
            query_string
            + body_text_for_signature
            + common_vars_str
            + access_token
            + get_config("SECRET")
        )
        signature = hash_password(signature_data)
        # signature = hashlib.md5(signature_data.encode("utf-8")).hexdigest()
        headers["X-Worky-Signature"] = signature
        headers["X-Debug-Info"] = urllib.parse.quote_plus(
            query_string + body_text + common_vars_str + access_token + get_config("SECRET")
        )
    return headers


def fetch_response(api_url, access_token, method="GET", data_1=None, data_2=None):
    """統一處理 API 請求，支援 GET 和 POST"""
    headers = generate_headers(access_token, body=data_1, query=data_2, include_signature=True)
    if method.upper() == "GET":
        response = requests.get(api_url, headers=headers, params=data_2, timeout=10)
    elif method.upper() == "POST":
        response = requests.post(api_url, headers=headers, json=data_1, timeout=10)
    else:
        raise ValueError(f"不支援的 HTTP 方法: {method}")
    return response
