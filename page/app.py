#!/usr/bin/python
# -*- coding: utf-8 -*-
from appium import webdriver

from page.base_page import BasePage
from page.main_page import Main


class App(BasePage):
    _app_package = "com.tencent.wework"
    _app_activity = "launch.WwMainActivity"

    def start(self):
        if self._driver is None:
            caps = {
                "platformName": 'Android',
                "platformVersion": '6.0',
                "appPackage": self._app_package,
                "appActivity": self._app_activity,
                "deviceName": '127.0.0.1:7555',
                "noReset": 'true',
                "unicodeKeyboard": 'true',
                "autoGrantPermissions": 'true',
                "skipDeviceInitialization": 'true',
                "automationName": 'UiAutomator2'
            }
            self._driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", caps)
            self._driver.launch_app()
            self._driver.implicitly_wait(10)
        else:
            self._driver.start_activity(self._app_package, self._app_activity)
            self._driver.implicitly_wait(10)

    def stop(self):
        self._driver.quit()

    def restart(self):
        pass

    def main(self) -> Main:
        return Main(self._driver)
