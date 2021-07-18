#!/usr/bin/python
# -*- coding: utf-8 -*-
import allure
from appium.webdriver.common.mobileby import MobileBy
from common.logger import logger
import os


def handle_black(func):
    def wrapper(*args, **kwargs):
        from page.base_page import BasePage
        _black_list = [
            (MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/ae9"]'),
            (MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/fx4"]')
        ]
        _ERROR_NUM = 0
        _MAX_NUM = 3
        self: BasePage = args[0]
        try:
            logger.info(f"args:{args[1:]} kwargs:{kwargs}\n")
            element = func(*args, **kwargs)
            _ERROR_NUM = 0
            self._driver.implicitly_wait(5)
            return element
        except Exception as e:
            logger.error('not find element:\n' + repr(e), exc_info=True)
            self.save_screenshot(os.getcwd() + "/screenshot_tmp/tmp.png")
            allure.attach.file(os.getcwd() + "/screenshot_tmp/tmp.png", attachment_type=allure.attachment_type.PNG)
            self._driver.implicitly_wait(1)
            if _ERROR_NUM > _MAX_NUM:
                raise e
            _ERROR_NUM += 1
            # self._driver.implicitly_wait(1)
            for black in _black_list:
                elements = self._driver.find_elements(*black)
                # 处理异常返回继续查找
                if len(elements) > 0:
                    elements[0].click()
                    return wrapper(*args, **kwargs)

    return wrapper


def handle_save_screenshot(func):
    pass
