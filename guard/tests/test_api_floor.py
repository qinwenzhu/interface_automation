# -*- coding:utf-8 -*-
# @Time: 2019/11/29 11:13
# @Author: wenqin_zhu
# @File: test_api_floor.py
# @Software: PyCharm


import unittest
import random
import requests

from test_cases.test_login import TestLogin


class TestFloor(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cookies = TestLogin().test_login_success()
        print(cookies)
        cls.cookie = {
            "accessToken": cookies
        }
        cls.i = random.randint(0, 9)

    def test_add_floor(self):

        """创建楼层"""
        method = "post"
        url = "http://10.151.3.100/senseguard-map-management/api/v1/floor"
        data = {
            "name": f"楼层{self.i}",
            "parentId": "",
            "remark": "地图楼层命名"
        }

        res = requests.request(method, url, json=data, headers=self.cookie)
        self.assertEqual(200, res.status_code)
        return res.json()["name"]


if __name__ == '__main__':
    unittest.main()
