""" 啟動的入口 """
import os
import sys
import subprocess

base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
target_path = os.path.join(base_path, 'streamlit_app.py')

# os.system(f"streamlit run \"{target_path}\"")
# 啟動 Streamlit 應用程式
subprocess.run(["streamlit", "run", target_path], check=False)
