"""設置啟動 webdriver 的設定，兼容 linux"""

import tempfile
import platform
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def configure_edge_options():
    """初始 option"""
    options = webdriver.EdgeOptions()
    options.add_argument("--headless=new") # 調適時可將畫面打開觀測
    options.add_argument("--disable-software-rasterizer")
    options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--inprivate")
    options.add_argument("--disable-extensions")
    return options

def launch_edge_driver():
    """兼容跨平台"""
    options = configure_edge_options()
    system_name = platform.system()

    if system_name in ["Windows", "Darwin"]:
        print("Windows/macOS 環境：使用 EdgeChromiumDriverManager")
        options.add_argument("--disable-gpu")  # Windows 必須關閉 GPU

        service = Service(EdgeChromiumDriverManager().install())
        service.log_output = None  # 停止 Edge 內部日誌
        service.log_level = 1      # INFO 級別

        driver = webdriver.Edge(service=service, options=options)

    else:  # Linux / Docker / CI/CD
        print("Linux 環境：使用 Remote WebDriver")
        options.add_argument("--no-sandbox")  # 避免 Docker 權限問題
        options.add_argument("--disable-dev-shm-usage")  # 避免共享記憶體不足
        options.add_argument("--disable-software-rasterizer")  # 再加一次保險

        driver = webdriver.Remote(
            command_executor="http://selenium_edge:4444/wd/hub",
            options=options
        )

    print("✅ WebDriver 啟動成功！")
    return driver
