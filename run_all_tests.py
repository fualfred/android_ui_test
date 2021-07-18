#!/usr/bin/python
# -*- coding: utf-8 -*-
import pytest
import os

if __name__ == "__main__":
    pytest.main()
    os.system("allure generate ./result -o ./report --clean")
