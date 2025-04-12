""" 啟動的入口 """

import os
import sys
import subprocess
import streamlit.web.cli as stcli

def resolve_path(file_name):
    """根據根目錄位置來啟動"""
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, file_name)


if __name__ == "__main__":
    # socket 4000
    script_path = resolve_path("start_server.py")
    CMD = f'python {script_path}'
    subprocess.Popen(
        ["cmd.exe", "/k", CMD],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )
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
