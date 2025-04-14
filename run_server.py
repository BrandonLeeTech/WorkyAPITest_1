""" 啟動的入口 """

import os
import sys
import streamlit.web.cli as stcli
from start_server import Server

def resolve_path(file_name):
    """根據根目錄位置來啟動"""
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, file_name)


if __name__ == "__main__":
    # socket 4000
    server = Server()
    if server.is_port_in_use():
        print("⚠️ Socket Server 已經啟動")
    else:
        server.start()
        print("✅ 啟動 socket server")

    # streamlit 8501
    sys.argv = [
        "streamlit", "run", resolve_path("app.py"),
        "--server.port=8501",
        "--global.developmentMode=false",
        "--server.runOnSave=false",
        "--server.headless=true",
    ]
    print("✅ 啟動 streamlit app")
    sys.exit(stcli.main())
