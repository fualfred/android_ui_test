#!/usr/bin/python
# -*- coding: utf-8 -*-
import pytest


def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")
