""" 點擊 模組 """

import time
import logging
from subprocess import run
from selenium.webdriver.common.action_chains import ActionChains
from utils.action_locate import LocateAction


class ClickAction:
    """Click button on the targeted element"""

    def __init__(self, driver):
        self.driver = driver

    def click_by_locating(
        self,
        positioning_method,
        wait_id,
        button_name,
        condition="clickable",
        click_times=1,
    ):  # DONE
        """根據 location 模組定位到的元素點擊
        Args:
            button_name (str): Button description for logging.
        """
        locator = LocateAction(self.driver)
        element = locator.wait_for_locate(
            positioning_method, wait_id, button_name, condition
        )
        try:
            for _ in range(click_times):
                element.click()
                logging.info("點擊: %s", button_name)
        except Exception:
            logging.error("[401] 點擊 %s 失敗", button_name)
            raise

    def click_coordinate_by_adb(self, x, y, button_name, click_times):
        """Tap the specified coordinates using ADB shell commands.
        Args:
            x,y (int): The coordinate.
            click_times (int): Times to click.
        """
        cmd = f"adb shell input tap {x} {y}"
        for _ in range(click_times):
            run(cmd, shell=True, check=True)
            logging.info("點擊: %s座標", button_name)
            time.sleep(0.25)

    def click_coordinate_by_appium(self, x, y, button_name, click_times):
        """Tap the specified coordinates using ActionChains module which is part of Selenium.
        Args:
            x,y (int): The coordinate.
            click_times (int): Times to click.
        """
        action = ActionChains(self.driver)
        try:
            for _ in range(click_times):
                action.w3c_actions.pointer_action.move_to_location(
                    x, y
                ).pointer_down().pointer_up()
                action.perform()
                logging.info("點擊: %s座標", button_name)
                time.sleep(0.25)
        except Exception:
            logging.error("[402] 點擊 (%s,%s) 失敗", x, y)
            raise

    def click_by_percentage(
        self, x_percentage, y_percentage, button_name, click_times=1
    ):
        """Tap the specified coordinates using screen percentages.
        Args:
            x_percentage (float): The x-coordinate as a percentage of the screen width (0.0 to 1.0).
            y_percentage (float): The y-coordinate as a percentage of the screen height (0.0 to 1.0).
            click_times (int): Times to click.
        """
        try:
            # 獲取設備的螢幕尺寸 (HTC U23 1080*2400)
            screen_size = self.driver.get_window_size()
            screen_width = screen_size["width"]
            screen_height = screen_size["height"]
            # 計算點擊的實際座標
            x = int(screen_width * x_percentage)
            y = int(screen_height * y_percentage)
            # 調用現有的座標點擊函數
            self.click_coordinate_by_adb(x, y, button_name, click_times)
        except Exception:
            logging.error("[403] 點擊 (%s,%s) 失敗", x_percentage, y_percentage)
            raise
