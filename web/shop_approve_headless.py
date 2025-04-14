""" [後台] 審核通過 """

import time
import logging
from utils.action_click import ClickAction
from utils.action_input import InputAction
from utils.cleanup_edge import cleanup_edge_processes
from web.webdriver_option import launch_edge_driver


def shop_audit_passed_h(background, employer_phone):
    """自動適應本機和 Docker/虛擬機環境的 Edge WebDriver"""
    driver = launch_edge_driver()
    click_action = ClickAction(driver)
    input_action = InputAction(driver)
    try:
        logging.info("測試 商家審核")
        logging.info("[pages/other/shop_approve_headless.py]")
        # 打開網頁
        driver.get(background)
        # 登入
        input_action.input_by_send_key("ID", "loginform-username", "brandon.lee")
        input_action.input_by_send_key("ID", "loginform-password", "brandon7068l7")
        click_action.click_by_locating("CSS_SELECTOR", "button[type='submit']", "登入")
        # 點擊 "Home" > "商家管理的列表" > "店舖管理"
        click_action.click_by_locating(
            "CSS_SELECTOR", "a.nav-link[aria-controls='sidebar']", "home"
        )
        time.sleep(2)
        click_action.click_by_locating(
            "CSS_SELECTOR", "i.float-end.fas.fa-angle-left", "商家管理"
        )
        click_action.click_by_locating(
            "Xpath", "//a[@href='/employer/shop/list/index']", "店鋪管理"
        )
        # 輸入 電話號碼並查詢
        input_action.input_by_send_key("ID", "_f-phone", employer_phone)
        click_action.click_by_locating("ID", "w2", "查詢")
        time.sleep(2)
        # 點擊 "審核"
        click_action.click_by_locating("ID", "w7", "審核")
        # 滾動到頁面底部
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        # 點擊 "通過" > "確定"
        click_action.click_by_locating(
            "Xpath", "//button[@data-bs-target='#approveModal']", "通過"
        )
        click_action.click_by_locating(
            "Xpath", "//button[@class='btn btn-success' and text()='確定']", "確定"
        )
        time.sleep(1)
        driver.quit()

    except Exception as e:
        print(f"❌ 無法啟動 Edge WebDriver: {e}")
        raise e

if __name__ == "__main__":
    try:
        # 在啟動 WebDriver 之前清理進程
        cleanup_edge_processes()
        URL = "https://next-staging-v210x.backend.staging.worky.com.tw"
        PHONE = "904120001"
        shop_audit_passed_h(URL, PHONE)
    finally:
        # 在腳本結束時清理所有 Edge 相關進程，確保環境乾淨
        print("正在清理測試環境...")
        cleanup_edge_processes()
        print("✅ 測試環境已清理完畢。")
