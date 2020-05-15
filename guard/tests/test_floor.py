# -*- coding:utf-8 -*-
# @Time: 2019/12/9 20:20
# @Author: wenqin_zhu
# @File: test_floor.py
# @Software: PyCharm

import unittest


from API.api_floor import ApiFloor


class TestFloor(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.floor = ApiFloor()
        # 添加楼层
        cls.add_floor_res = cls.floor.add_floor()
        cls.floor_id = cls.add_floor_res.json()["floorId"]
        print(cls.floor_id)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_add_floor(self):
        # 测试添加地图层级
        self.assertEqual(200, self.add_floor_res.status_code)

    def test_delete_floor(self):
        # 测试删除地图层级
        delete_floor_res = self.floor.delete_floor(self.floor_id, 0)
        self.assertEqual(200, delete_floor_res.status_code)


if __name__ == '__main__':
    unittest.main()
