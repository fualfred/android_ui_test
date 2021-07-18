#!/usr/bin/python
# -*- coding: utf-8 -*-
import pytest
from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage
import os


class AddMember(BasePage):

    def add_member(self, user, phone):
        self._param = {"user": user, "phone": phone}
        # self.find(MobileBy.XPATH, '//*[@class="android.widget.TextView" and @text="手动输入添加"]').click()
        # elements = self.finds(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/hc6" and @text="快速输入"]')
        # if len(elements) > 0:
        #     self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/hc6" and @text="快速输入"]').click()
        # self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/b09"]').clear().send_keys(user)
        # self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/f7y"]').clear().send_keys(phone)
        # self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/ad2"]').click()
        self.steps(os.getcwd() + "/pageYaml/addMember_page.yaml")

    def add_member_fail(self, user, phone):
        # self._param = {"user": user, "phone": phone}
        self._return["text"] = None
        self._param = {"user": user, "phone": phone}
        # self.add_member(user, phone)
        # return self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/bg4"]').text
        # print(self._driver.contexts)
        self.steps(os.getcwd() + "/pageYaml/addMember_page.yaml")
        # self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/bg8"]').click()
        return self._return["text"]

    def go_to_address(self):
        # self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/hbs"]').click()
        self.steps(os.getcwd() + "/pageYaml/addMember_page.yaml")
        from page.address_page import Address
        return Address(self._driver)
