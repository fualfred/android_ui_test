#!/usr/bin/python
# -*- coding: utf-8 -*-
from page.app import App
import pytest
from hamcrest import *
import yaml
import os

test_data = yaml.safe_load(open(os.getcwd() + "/test_data/test_addMember.yaml", encoding="utf-8"))


class TestAddMember:
    def setup(self):
        self.app = App()
        self.app.start()
        self.addMember = self.app.main().go_to_address().go_to_add_member()

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize("user,phone", test_data['test_add_member_success'])
    def test_add_member_success(self, user, phone):
        self.addMember.add_member(user, phone)
        assert_that(self.addMember.go_to_address().find_member(user), equal_to(True))

    @pytest.mark.parametrize("user,phone,expect", test_data['test_add_member_fail'])
    def test_add_member_fail(self, user, phone, expect):
        fail_text = self.addMember.add_member_fail(user, phone)
        assert_that(fail_text, equal_to(expect))
