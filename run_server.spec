# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files, copy_metadata
from PyInstaller.building.build_main import Analysis, PYZ, EXE
import os


# 注意：collect_data_files 是回傳 list of tuples，但 datas 是 list of tuples → 合併 OK
datas = [
    ("app.py", "."),
    ("start_server.py", "."),
    ("api_config.json", "."),
    ('app.log', '.'),
    ('config/*.py', 'config'),
    ("C:/Users/brandon.lee/.conda/envs/py311/Lib/site-packages/streamlit/runtime", "streamlit/runtime"),
]

datas += collect_data_files("streamlit")
datas += copy_metadata("streamlit")

# 定義 Tree-like 行為：直接用 list-comprehension 遞迴加入
def collect_folder(folder, target_root="."):
    collected = []
    for root, _, files in os.walk(folder):
        for f in files:
            fullpath = os.path.join(root, f)
            # 判斷是否與目標同一磁碟，否則用絕對路徑相對化
            try:
                target = os.path.relpath(root, target_root)
            except ValueError:
                # fallback：強制把目錄根設為 folder
                target = os.path.relpath(root, folder)
            collected.append((fullpath, target))
    return collected

for folder in ["utils", "tools", "web", "img", "api", "helper"]:
    datas += collect_folder(folder)

# 加入 WebDriverManager 的暫存驅動
datas += collect_folder(os.path.expanduser("~/.wdm"), os.getcwd())


hidden_imports = [
    'ipaddress',
    'streamlit.web.cli',
    'appium',
    'appium.webdriver',
    'appium.webdriver.common.mobileby',
    'selenium',
    'selenium.webdriver',
    'selenium.webdriver.edge',
    'selenium.webdriver.edge.service',
    'selenium.webdriver.common.by',
    'selenium.webdriver.common.keys',
    'selenium.webdriver.common.action_chains',
    'selenium.webdriver.remote.webdriver',
    'selenium.webdriver.support.expected_conditions',
    'webdriver_manager',
    'webdriver_manager.microsoft'
]


a = Analysis(
    ['run_server.py'],
    pathex=['.'],
    binaries=[],
    datas=datas,
    hiddenimports=hidden_imports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='run_server',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
)
