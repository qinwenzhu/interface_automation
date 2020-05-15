# -*- coding:utf-8 -*-
# @Time: 2019/11/29 11:13
# @Author: wenqin_zhu
# @File: test_login.py
# @Software: PyCharm


import unittest
import requests

from tools.pack_requests import PackRequests


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.request = PackRequests()

    def test_login_success(self):
        """正常登录"""

        method = "post"
        url = "http://10.151.3.100/senseguard-oauth2/api/v1/login"
        data = {"username": "apitest", "password": "888888"}

        # 发送请求
        res = self.request.send_request(method, url, data)
        # res = requests.request(method, url, json=data)

        # 断言 - 响应状态码为200
        self.assertEqual(200, res.status_code)
        # 断言 - 响应数据中的用户名和期望值一致
        self.assertEqual(data["username"], res.json()["username"])
        # print(f'当前登录用户的用户名为：res.json()["username"]')
        print(f'cookie为：res.json()["accessToken"]')
        return res.json()['accessToken']

    # def test_login_failure(self):
    #     pass


if __name__ == '__main__':
    unittest.main()
