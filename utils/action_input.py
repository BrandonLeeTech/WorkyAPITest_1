""" 輸入 模組 """

import time
import logging
from utils.action_locate import LocateAction


class InputAction:
    """Input text in the targeted element"""

    def __init__(self, driver):
        self.driver = driver

    def input_by_send_key(self, positioning_method, wait_id, text):
        """根據定位使用 send_key
        Args:
            text_name (str): The text to be input.
        """
        locator = LocateAction(self.driver)
        element = locator.wait_for_locate(positioning_method, wait_id)
        try:
            element.clear()
            element.send_keys(text)
            logging.info("輸入: %s", text)
        except Exception:
            logging.error("[501] 輸入 '%s' 失敗", text)
            raise

    def input_with_keycode(self, positioning_method, wait_id, numbers):
        """根據定位輸入 Android KeyCodes (輸入數字鍵時可用)
        Args:
            text_name (str): The text to be input.
        """
        locator = LocateAction(self.driver)
        element = locator.wait_for_locate(positioning_method, wait_id)
        try:
            element.clear()
            for char in numbers:
                self.driver.press_keycode(7 + int(char))
                time.sleep(0.1)
                logging.info("輸入: %s", char)
        except Exception:
            logging.error("[502] 輸入 '%s' 失敗", numbers)
            raise

    def direct_send_key(self, driver, text):
        """無定位直接使用 send key ，適合用在輸入位置的資訊難以定位時
        Args:
            driver: The Appium driver for the mobile device.
            text_name (str): The text to be input.
        """
        try:
            driver.send_keys(text)
            logging.info("輸入: %s", text)
        except Exception:
            logging.error("[503] 輸入 '%s' 失敗", text)
            raise

    def direct_input_keycodes(self, driver, numbers):
        """無定位直接使用 Android KeyCodes ，適合用在輸入位置的資訊難以定位時(e.g.輸入驗證碼時可用)
        Args:
            driver: The Appium driver for the mobile device.
            numbers (list[int]): The list of numbers to be input.
        """
        try:
            for char in numbers:
                driver.press_keycode(7 + int(char))
                time.sleep(0.1)
            logging.info("輸入: %s", numbers)
        except Exception:
            logging.error("[504] 輸入 '%s' 失敗", numbers)
            raise
