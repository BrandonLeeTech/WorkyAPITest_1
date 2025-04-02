""" 定位模組 & 顯示等待 """

import logging
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LocateAction:
    """等待元素表現並定位"""

    def __init__(self, driver):
        self.driver = driver

    # "positioning_method" 參數調用的字典
    positioning_method_dict = {
        "ID": AppiumBy.ID,
        "Xpath": AppiumBy.XPATH,
        "ClassName": AppiumBy.CLASS_NAME,
        "Accessiblity_ID": AppiumBy.ACCESSIBILITY_ID,
        "UIAutomator": AppiumBy.ANDROID_UIAUTOMATOR,
        "CSS_SELECTOR": AppiumBy.CSS_SELECTOR,
    }

    # "expected_conditions" 參數調用的字典
    conditions_dict = {
        "title_is": EC.title_is,
        "title_contains": EC.title_contains,
        "presence": EC.presence_of_element_located,  # 判斷元素是否被加入 DOM 樹，並不一定可見
        "presence_all": EC.presence_of_all_elements_located,
        "staleness": EC.staleness_of,  # 判斷元素是否從 DOM 樹移除 (可判斷頁面是否刷新)
        "visibility": EC.visibility_of_element_located,  # 判斷元素是否可見
        "visibility_1": EC.visibility_of,
        "invisibility": EC.invisibility_of_element_located,
        "text": EC.text_to_be_present_in_element,
        "text_value": EC.text_to_be_present_in_element_value,
        "clickable": EC.element_to_be_clickable,  # 判斷元素是否可點擊
        "selected": EC.element_to_be_selected,  # 判斷元素是否被選中 (可在下拉列表使用)
        "selected_1": EC.element_selection_state_to_be,
        "selected_2": EC.element_located_selection_state_to_be,
        "frame": EC.frame_to_be_available_and_switch_to_it,
        "alert": EC.alert_is_present,  # 判斷頁面是否存在警告
    }

    def valid_positioning_method(self, positioning):
        # sourcery skip: class-extract-method
        """檢查填入的 positioning_method (定位方法) 是否符合字典規範"""
        try:
            if (by_positioning := self.positioning_method_dict.get(positioning)) is None:
                raise KeyError()
            return by_positioning
        except KeyError as e:
            logging.error("[101] positioning_method_dict 中沒有 %s", positioning)
            logging.error("異常類型: %s", type(e))
            logging.error("異常消息: %s", str(e))
            raise

    def valid_condition(self, condition):
        """檢查填入的 condition (等待條件) 是否符合字典規範"""
        try:
            if (by_conditions := self.conditions_dict.get(condition)) is None:
                raise KeyError()
            return by_conditions
        except KeyError as e:
            logging.error("[102] conditions_dict 中沒有 %s", condition)
            logging.error("異常類型: %s", type(e))
            logging.error("異常消息: %s", str(e))
            raise

    def wait_for_locate(self, positioning, wait_id, name="", condition="visibility"):
        """等待元素 visibility , 並用給定的 positioning_method 定位
        Args:
            positioning_method : The method of locating (e.g. By.ID)
            wait_id : Element information (e.g. "anyID")
            condition : The expected condition (e.g. visibility)
        Returns:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(By.ID, "anyID"))
        """
        by_positioning = self.valid_positioning_method(positioning)
        by_conditions = self.valid_condition(condition)
        try:
            logging.info("定位: %s", name)
            return WebDriverWait(self.driver, 10).until(
                by_conditions((by_positioning, wait_id))
            )
        except Exception:
            logging.error("[301] 無法定位元素的 %s: %s ", positioning, wait_id)
            # print(self.driver.page_source)  # 輸出當前畫面 XML
            raise
