# coding = utf-8
'''
根据 get_execl_data 和 method 获得 请求后的值
'''
from common.get_excel_data import GetExcelData
from common.method import Method
class RunCase:

    def __init__(self):
        self.run_method = Method()
        self.data = GetExcelData()

    # 程序执行的方法
    def go_on_run(self):
        res =None
        row = self.data.get_lines()
        for i in range(2,row+1):
            print(i)
            url = self.data.get_request_url(i)
            print(url)
            method = self.data.get_request_method(i)
            print(method)
            header = self.data.get_is_header(i)
            print(header)
            data = self.data.get_data_for_json(i)
            print(data)
            is_run=self.data.get_is_run(i)
            print(is_run)
            if is_run:
                res =self.run_method.run_method(url,method,data,header)
        return res
if __name__ == '__main__':
    print(RunCase().go_on_run())
