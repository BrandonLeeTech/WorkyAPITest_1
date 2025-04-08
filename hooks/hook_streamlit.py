"""新增 metadata 防止 package not found"""
from PyInstaller.utils.hooks import copy_metadata

datas = copy_metadata("streamlit")
