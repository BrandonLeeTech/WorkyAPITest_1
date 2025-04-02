""" 商家端-設置信用卡 """

import random
import time
import platform
import logging
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from tools.socket_data_manager import SocketDataManager
from utils.action_click import ClickAction
from utils.action_input import InputAction

def get_random_value():
    """從字典中隨機選擇一個值並返回"""
    credit_card_dict = {
        "A": 4311951111111111,
        "B": 4311952222222222,
        "C": 4311953333333333,
        "D": 4311954444444444,
        "E": 4311955555555555,
        "F": 4311956666666666,
        "G": 4311957777777777,
        "H": 4311958888888888,
        "I": 4311959999999999,
    }
    return random.choice(list(credit_card_dict.values()))

def credit_card_bind_h():
    """資訊查詢 API (GET)"""
    socket_manager = SocketDataManager()
    credit_card_url = socket_manager.get_data("E_credit_card_url")

    options = webdriver.EdgeOptions()
    options.add_argument("--headless")  # 無頭模式
    options.add_argument("--inprivate")  # 無痕模式
    options.add_argument("--disable-extensions")  # 禁用擴展
    options.add_argument("--remote-debugging-port=9222")  # CI/CD 除錯
    options.add_argument("--window-size=1920,1080")  # 固定視窗大小

    # 根據 OS 選擇 WebDriver
    system_name = platform.system()
    if system_name in ["Windows", "Darwin"]:
        print("Windows/macOS 環境：使用 EdgeChromiumDriverManager")
        options.add_argument("--disable-gpu")  # Windows 必須關閉 GPU
        service = Service(EdgeChromiumDriverManager().install())
        service.log_output = None  # 停止 Edge 內部日誌，但 WebDriver 步驟仍然會輸出
        service.log_level = 1  # INFO 級別
        driver = webdriver.Edge(service=service, options=options)

    else: # Linux / Docker / CI/CD
        print("Linux 環境：使用 Remote WebDriver")
        options.add_argument("--no-sandbox")  # 避免 Docker 權限問題
        options.add_argument("--disable-dev-shm-usage")  # 避免共享記憶體不足
        options.add_argument("--disable-software-rasterizer")  # 防止軟體渲染錯誤
        driver = webdriver.Remote(
            command_executor="http://selenium_edge:4444/wd/hub",  # Selenium Grid / Docker
            options=options,
        )
    print("✅ WebDriver 啟動成功！")

    click_action = ClickAction(driver)
    input_action = InputAction(driver)
    try:
        logging.info("測試 信用卡設定")
        logging.info("[pages/other/credit_card_headless.py]")
        # 打開網頁
        driver.get(credit_card_url)
        time.sleep(2)
        random_value = get_random_value()
        print(f"隨機選擇卡號的值: {random_value}")
        input_action.input_by_send_key(
            "ID", "CardPart1", str(random_value)
        )  # 卡片綁太多次會有問題
        time.sleep(1)

        click_action.click_by_locating("ID", "AuthExpireDateMM", "月份")
        click_action.click_by_locating(
            "Xpath", "//select[@id='AuthExpireDateMM']/option[@value='10']", "10月"
        )
        time.sleep(1)

        click_action.click_by_locating("ID", "AuthExpireDateYY", "年份")
        click_action.click_by_locating(
            "Xpath", "//select[@id='AuthExpireDateYY']/option[text()='2030']", "2031年"
        )
        time.sleep(1)

        input_action.input_by_send_key("ID", "AuthCode", "222")
        time.sleep(1)

        click_action.click_by_locating(
            "Xpath",
            "//div[@class='site-content-wrapper']//div[@class='btnarea clearfix div_center']/a[@id='btn_submit']",
            "送出",
        )
        click_action.click_by_locating(
            "Xpath",
            "//div[@class='site-content-wrapper']//div[@class='btnarea clearfix div_center']/a[@id='btn_submit']",
            "送出",
        )
        time.sleep(10)
        driver.quit()

    except Exception as e:
        raise e


if __name__ == "__main__":
    credit_card_bind_h()
