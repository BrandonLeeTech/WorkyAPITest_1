""" 測試介面 """
import traceback
import importlib
import streamlit as st
from utils.process_manager import ProcessManager


# ----- Streamlit 基本設定 -----
st.set_page_config(
    page_title="QA 測試平台",
    # page_icon="",
    layout="centered",
)
st.title("QA 自動化測試") # 標題
st.info("模擬打 API, 建測試數據") # 副標題
st.markdown("")

# ----- 初始化狀態 -----
if "result_info" not in st.session_state:
    st.session_state.result_info = {}


# ----- 渲染測試結果 -----
def render_result():
    """定義測試結果"""
    result_info = st.session_state.result_info
    if result_info.get("status") == "pass":
        st.success(result_info.get("msg"))
    elif result_info.get("status") == "fail":
        st.error(result_info.get("msg"))
    elif result_info.get("status") == "error":
        st.warning(result_info.get("msg", "⚠️ 例外錯誤"))


# ----- 測試腳本定義 -----
scripts = {
    "test": {
        "module": "test.test_module",
        "func": "test_func",
        "params": {
            "base_url": ["https://next-staging-v210x.api.staging.worky.com.tw"],
            "e_phone": "text",
        }
    },
    "商家註冊":{
        "module": "test.e_register",
        "func": "register_and_validation",
        "params": {
            "base_url": ["https://next-staging-v210x.api.staging.worky.com.tw"],
            "e_phone": "text",
            "e_name": ["張三", "李四", "王五"],
            "e_shop": ["A店", "B店", "C店"]
        }
    }
}


# ----- 使用者輸入區 -----
with st.expander("📌 請輸入測試參數", expanded=True):
    st.markdown("---")
    script_name = st.selectbox("選擇測試模組：", list(scripts.keys()))
    script_info = scripts[script_name]

    inputs = {}
    for param, config in script_info["params"].items():
        if isinstance(config, list):
            # 如果是清單，顯示為下拉式選單
            inputs[param] = st.selectbox(f"選擇 `{param}`", config)
        else:
            # 否則預設為文字輸入
            inputs[param] = st.text_input(f"輸入 `{param}`")


# 測試執行邏輯
def run_test():
    """啟動腳本主邏輯"""
    try:
        process_manager = ProcessManager()
        process_manager.open_console()
        module = importlib.import_module(script_info["module"])
        target_func = getattr(module, script_info["func"])
        result = target_func(**inputs)
        process_manager.close_console()
        if isinstance(result, dict) and result.get("status") == "pass":
            st.session_state.result_info = {
                "status": "pass",
                "msg": result.get("msg", "測試成功")
            }
        else:
            st.session_state.result_info = {
                "status": "fail",
                "msg": result.get("msg")
            }
    except Exception as e: # pylint: disable = [broad-exception-caught]
        st.session_state.result_info = {
            "status": "error",
            "msg": f"例外錯誤: {e}\n{traceback.format_exc()}"
        }


# ----- 按鈕觸發測試 -----
st.markdown("")
if st.button("🚀 執行", type="secondary"):
    # st.toast(':green[成功執行模組]', icon='✔️')
    run_test()
    st.session_state.show_result = True  # 用來控制是否要顯示結果


# ----- 結果顯示（固定位置在畫面下方）-----
if st.session_state.get("show_result", False):
    with st.container():
        st.markdown("---")
        st.markdown("### 📋 Test Result")
        render_result()
