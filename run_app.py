""" 啟動的入口 """

import os
import sys
import streamlit.web.cli as stcli


def resolve_path(file_name):
    """根據根目錄位置來啟動"""
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, file_name)


if __name__ == "__main__":
    sys.argv = [
        "streamlit",
        "run",
        resolve_path("app.py"),
        "--server.port=8501",
        "--global.developmentMode=false",
    ]
    sys.exit(stcli.main())
