# -*- coding:utf-8 -*-
# @Time: 2019/12/11 16:28
# @Author: wenqin_zhu
# @File: common_os.py
# @Software: PyCharm


import os


current_dir = os.getcwd()
print(f"定位当前文件的绝对路径{current_dir}")

base_dir = os.path.split(current_dir)
print(f"主项目的路径{base_dir}")


# 定位到datas目录
datas_dir = os.path.join(base_dir[0], "datas")
print(f"datas的目录路径{datas_dir}")

# 定位到配置文件
BASE_CON = os.path.join(datas_dir, "base_con.config")
print(f"基本配置文件的路径：{BASE_CON}")

# 定位到Excel测试数据
CASE_DATAS = os.path.join(datas_dir, "case_datas.xlsx")
print(f"测试数据的路径：{CASE_DATAS}")




