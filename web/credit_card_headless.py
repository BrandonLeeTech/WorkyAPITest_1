""" 商家端-設置信用卡 """

import time
from tools.socket_data_manager import SocketDataManager
from utils.action_click import ClickAction
from utils.action_input import InputAction
from utils.credit_card_number import get_random_value
from web.webdriver_option import launch_edge_driver


def credit_card_bind_h():
    """資訊查詢 API (GET)"""
    socket_manager = SocketDataManager()
    url = socket_manager.get_data("E_credit_card_url")
    driver = launch_edge_driver()
    click_action = ClickAction(driver)
    input_action = InputAction(driver)
    try:
        print("設定信用卡")
        # 打開網頁
        driver.get(url)
        time.sleep(2)
        random_value = get_random_value()
        print(f"隨機選擇卡號的值為: {random_value}")
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
        print("關閉頁面")
        driver.quit()

    except Exception as e:
        print(f"❌ 測試設定信用卡號失敗: {e}")
        raise e


if __name__ == "__main__":
    credit_card_bind_h()
