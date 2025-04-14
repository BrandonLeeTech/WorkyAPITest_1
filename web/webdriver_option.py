"""設置啟動 webdriver 的設定，兼容 linux"""

import platform
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def configure_edge_options():
    """初始 option"""
    options = webdriver.EdgeOptions()

    # 調適用：可取消註解顯示視窗
    # options.add_argument("--headless=new")

    options.add_argument("--disable-gpu")  # Windows 下建議關閉 GPU
    options.add_argument("--no-sandbox")  # 避免權限問題
    options.add_argument("--disable-dev-shm-usage")  # 防止共享記憶體不足錯誤
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--inprivate")  # 無痕模式
    options.add_argument("--disable-extensions")
    options.add_argument("--remote-debugging-port=9222")

    return options

def launch_edge_driver():
    """僅支援 Windows 的 WebDriver 啟動"""
    system_name = platform.system()
    if system_name != "Windows":
        raise EnvironmentError("目前僅支援 Windows 環境執行 WebDriver。")

    options = configure_edge_options()
    print("Windows 環境下啟動 Edge WebDriver")

    service = Service(EdgeChromiumDriverManager().install())
    service.log_output = None
    service.log_level = 1

    driver = webdriver.Edge(service=service, options=options)

    print("✅ WebDriver 啟動成功！")
    return driver
