""" 測試介面 """
import os
import traceback
import streamlit as st
from config.scripts_config import SCRIPTS

class StreamlitApp:
    """streamlit 網頁部屬設定"""
    def __init__(self):
        """初始化應用程式狀態"""
        self.init_state()

    def init_state(self):
        """初始化 session_state"""
        if "result_info" not in st.session_state:
            st.session_state.result_info = {}
        if "show_result" not in st.session_state:
            st.session_state.show_result = False

    def render_result(self):
        """渲染測試結果"""
        result_info = st.session_state.result_info
        if result_info.get("status") == "pass":
            st.success(result_info.get("msg"))
        elif result_info.get("status") == "fail":
            st.error(result_info.get("msg"))
        elif result_info.get("status") == "error":
            st.warning(result_info.get("msg", "⚠️ 例外錯誤"))

    def collect_inputs(self, script_info):
        """收集用戶輸入參數"""
        inputs = {}
        with st.expander("📌 請輸入測試參數", expanded=True):
            st.markdown("---")
            for param, config in script_info["params"].items():
                if isinstance(config, list):
                    inputs[param] = st.selectbox(f"選擇 `{param}`", config)
                else:
                    inputs[param] = st.text_input(f"輸入 `{param}`")
        return inputs

    def run_test(self, target_func, inputs):
        """執行測試邏輯"""
        try:
            result = target_func(**inputs)
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
        except Exception as e:  # pylint: disable = [broad-exception-caught]
            st.session_state.result_info = {
                "status": "error",
                "msg": f"例外錯誤: {e}\n{traceback.format_exc()}"
            }

    def render_ui(self):
        """渲染主 UI"""
        st.set_page_config(
            page_title="QA 測試平台",
            # page_icon="",
            layout="centered",
        )
        st.title("QA 自動化測試") # 標題
        st.info("模擬打 API, 建測試數據") # 副標題
        st.markdown("")
        st.write("被執行的 PID：", os.getpid())

        # 選擇模組
        script_name = st.selectbox("選擇測試模組：", list(SCRIPTS.keys()))
        script_info = SCRIPTS[script_name]

        # 收集輸入
        inputs = self.collect_inputs(script_info)

        # 執行按鈕
        if st.button("🚀 執行", type="secondary"):
            self.run_test(script_info["function"], inputs)
            st.write("✅ 模擬執行完成")
            st.session_state.show_result = True

        # 顯示結果
        if st.session_state.show_result:
            with st.container():
                st.markdown("---")
                st.markdown("### 📋 Test Result")
                self.render_result()

    def run(self):
        """應用程式入口"""
        self.render_ui()


# ----- 執行應用程式 -----
if __name__ == "__main__":
    app = StreamlitApp()
    app.run()
