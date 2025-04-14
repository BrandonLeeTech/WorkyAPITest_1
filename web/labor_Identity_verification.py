""" [後台] 打工夥伴審核通過 """

import time
from utils.action_click import ClickAction
from utils.action_input import InputAction
from web.webdriver_option import launch_edge_driver


def labor_verify(background, labor_phone):
    """自動適應本機和 Docker/虛擬機環境的 Edge WebDriver"""
    driver = launch_edge_driver()
    click_action = ClickAction(driver)
    input_action = InputAction(driver)
    try:
        print("打工夥伴審核")
        # 打開網頁
        driver.get(background)
        # 登入
        input_action.input_by_send_key("ID", "loginform-username", "brandon.lee")
        input_action.input_by_send_key("ID", "loginform-password", "brandon7068l7")
        click_action.click_by_locating("CSS_SELECTOR", "button[type='submit']", "登入")
        # 點擊 "Home"
        click_action.click_by_locating(
            "CSS_SELECTOR", "a.nav-link[aria-controls='sidebar']", "home"
        )
        time.sleep(2)
        click_action.click_by_locating(
            "Xpath", "//p[contains(text(),'打工夥伴')]/i", "打工夥伴"
        )
        click_action.click_by_locating(
            "Xpath", "//p[normalize-space(text())='打工夥伴管理']", "打工夥伴管理"
        )
        print(f"輸入打工帳號: {labor_phone}")
        # 輸入 電話號碼並查詢
        input_action.input_by_send_key("ID", "_f-username", labor_phone)
        click_action.click_by_locating("ID", "w2", "查詢")
        time.sleep(2)
        # 點擊 "待認證"
        click_action.click_by_locating("Xpath", "//span[normalize-space(text())='待認證']", "審核")
        time.sleep(2)
        # 點擊 "通過" > "確定"
        click_action.click_by_locating(
            "ID", "btnValidateSubmit", "提交認證"
        )
        time.sleep(1)
        print("打工通過認證")
        driver.quit()

    except Exception as e:
        print(f"❌ 執行腳本(打工審核)失敗: {e}")
        raise e

if __name__ == "__main__":
    URL = "https://next-staging-v210x.backend.staging.worky.com.tw"
    PHONE = "904140001"
    labor_verify(URL, PHONE)
