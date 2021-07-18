#!/usr/bin/python
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from page.addMember_page import AddMember
from page.base_page import BasePage
import os


class Address(BasePage):
    def go_to_add_member(self):
        self.swipe_down()
        # self.wait_for_element(MobileBy.XPATH, '//*[@class="android.widget.TextView" and @text="添加成员"]')
        # self.find(MobileBy.XPATH, '//*[@class="android.widget.TextView" and @text="添加成员"]').click()
        self.steps(os.getcwd() + "/pageYaml/address_page.yaml")
        return AddMember(self._driver)

    def find_member(self, user):
        elements = self.finds(MobileBy.ANDROID_UIAUTOMATOR,
                              'new UiSelector().className("android.widget.TextView")')
        for element in elements:
            if element.text == user:
                return True
        return False
