""" 商家端-設置信用卡 """

import random
import time
import logging
from tools.socket_data_manager import SocketDataManager
from utils.action_click import ClickAction
from utils.action_input import InputAction
from utils.cleanup_edge import cleanup_edge_processes
from web.webdriver_option import launch_edge_driver


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
    driver = launch_edge_driver()
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
    try:
        # 在啟動 WebDriver 之前清理進程
        cleanup_edge_processes()
        credit_card_bind_h()
    finally:
        # 在腳本結束時清理所有 Edge 相關進程，確保環境乾淨
        print("正在清理測試環境...")
        cleanup_edge_processes()
        print("✅ 測試環境已清理完畢。")
