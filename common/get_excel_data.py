# coding = utf-8

'''
获取Excel 数据
1.初始化 操作Excel的方法 OperateExcle
2.获得行数
3.获取是否执行
4.获取
'''

from common.operate_excel import OperateExcle
from excel_canstant import *

class GetExcelData:

    def __init__(self):
        self.oper_excel = OperateExcle


    # 获得行数
    def get_lines(self):
        return self.oper_excel.get_row()

    # 获得是否执行
    def get_is_run(self):
        col =


