# coding = utf-8

'''
获取Excel 数据
1.初始化 操作Excel的方法 OperateExcle
2.获得行数              get_lines（） 备注：OperateExcle 也有相同的方法get_row（）功能一样，这里方便调用，搞了一个get_lines()
3.获取是否执行：       get_is_run（）
4.获取是否携带请求头：  is_header（）
5.获得请求方法：       get_request_method（）
6.获得url：           get_request_url
7.获得请求数据：        get_request_url（）
8.通过关键字获得数据     get_data_for_json（）
9.获得预期结果          get_expect_data（）
'''

from common.operate_excel import OperateExcle
from common.excel_canstant import *
from common.operate_json import OperaterJson


class GetExcelData:

    def __init__(self):
        self.oper_excel = OperateExcle

    # 获得行数
    def get_lines(self):
        return self.oper_excel.get_row()

    # 获得是否执行
    def get_is_run(self,row):
        flag = None
        col = run()
        run_mode= self.oper_excel.get_value(row, col)
        if run_mode == "yes":
            flag = True
        else:
            flag = False
        return flag

    # 是否携带header
    def is_header(self,row):
        col = header()
        headers = self.oper_excel.get_value(row,col)
        if headers == "None":
            return headers
        else:
            return headers
    # 获得请求方法
    def get_request_method(self,row):
        col = request_way()
        request_method= self.oper_excel.get_value(row,col)
        return request_method
    # 获得url
    def get_request_url(self,row):
        col = url()
        request_url= self.oper_excel.get_value(row,col)

    # 获得请求数据
    def get_request_data(self,row):
        col = requst_data()
        data = self.oper_excel.get_value(row,col)
        if data == "":
            return None
        else:
            return data
    # 通过关键字获得数据
    def get_data_for_json(self):
        key = self.get_request_data()
        json_value= OperaterJson().get_json_value(key)
        return json_value

    # 获得预期结果
    def get_expect_data(self,row):
        col = expect()
        expect_data=self.oper_excel.get_value(row,col)
        if expect_data == "":
            return None
        else:
            return expect_data

if __name__ == '__main__':
    print(GetExcelData().get_is_run())