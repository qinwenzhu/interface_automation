# -*- coding:utf-8 -*-
# @Time: 2019/12/9 18:50
# @Author: wenqin_zhu
# @File: test_login.py
# @Software: PyCharm

import unittest

from API.api_login import ApiLogin
from tools.common_os import CASE_DATAS


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.login = ApiLogin()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_login_success(self):
        # 测试登录成功案例
        login_res = self.login.login()
        self.assertEqual(200, login_res.status_code)


if __name__ == '__main__':
    unittest.main()
