# -*- coding:utf-8 -*-
# @Time: 2019/11/27 10:29
# @Author: wenqin_zhu
# @File: test_login.py
# @Software: PyCharm


"""
url
https://10.151.3.100/senseguard-oauth2/api/v1/login
method
post
data
{用户名+密码}
"""

import requests
import urllib3
urllib3.disable_warnings()


from tools.component_requests import ComRequest


def user_login():
    method = "post"
    url = "https://10.151.3.100/senseguard-oauth2/api/v1/login"
    data = {"username": "apitest", "password": "888888"}
    res = requests.post(url, json=data, verify=False)
    # res = requests.request("post", url, json=data, verify=False)

    # my_request = ComRequest()
    # res = my_request.main(method, url, data)
    # print(res)

    print(res.json())
    print(res)


if __name__ == '__main__':
    user_login()
