#!/usr/bin/python
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage
from page.address_page import Address
import os


class Main(BasePage):
    def go_to_address(self):
        print(os.getcwd())
        # self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/e0y" and @text="通讯录"]').click()
        self.steps(os.getcwd() + "/pageYaml/main_page.yaml")
        return Address(self._driver)
