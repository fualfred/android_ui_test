#!/usr/bin/python
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from common.logger import logger
import yaml
from page.base_page import BasePage

if __name__ == '__main__':
    with open("./test_data/test_addMember.yaml", encoding="utf-8") as f:
        data = yaml.safe_load(f)
        print(data, type(data))
