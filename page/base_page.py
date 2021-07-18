#!/usr/bin/python
# -*- coding: utf-8 -*-
import inspect
import json

from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from common.wrapper import handle_black
import yaml
from common.logger import logger


class BasePage:
    _driver: WebDriver
    _param = {}
    _return = {}

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    @handle_black
    def find(self, locator, value):
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
            return element
        else:
            element = self._driver.find_element(locator, value)
            return element

    def finds(self, locator, value):
        if isinstance(locator, tuple):
            return self._driver.find_elements(*locator)
        else:
            return self._driver.find_elements(locator, value)

    def swipe_down(self):
        x = self._driver.get_window_size()['width']
        y = self._driver.get_window_size()['height']
        self._driver.swipe(x * 0.5, y * 0.5, x * 0.5, 1, 500)

    def wait_for_element(self, locator, value, timeout=10):
        if isinstance(locator, tuple):
            WebDriverWait(self._driver, timeout).until(expected_conditions.element_to_be_clickable(locator))
        else:
            WebDriverWait(self._driver, timeout).until(expected_conditions.element_to_be_clickable((locator, value)))

    def save_screenshot(self, name):
        self._driver.save_screenshot(name)

    def steps(self, path):
        name = inspect.stack()[1].function
        with open(path, encoding="utf-8") as f:
            dat = yaml.safe_load(f)
            steps = dat[name]
            for step in steps:
                raw = json.dumps(step)
                for key, value in self._param.items():
                    raw = raw.replace(f'${{{key}}}', value)
                step = json.loads(raw)
                if "action" in step.keys():
                    if step["action"] == "click":
                        self.find(step['by'], step['locator']).click()
                    if step["action"] == "send":
                        self.find(step['by'], step['locator']).clear().send_keys(step['value'])
                    if step["action"] == "len>click":
                        if len(self.finds(step['by'], step['locator'])) > 0:
                            self.find(step['by'], step['locator']).click()
                    if step["action"] == "wait":
                        self.wait_for_element(step['by'], step['locator'])
                    if step["action"] == "getText":
                        text = self.find(step['by'], step['locator']).text
                        self._return["text"] = text
