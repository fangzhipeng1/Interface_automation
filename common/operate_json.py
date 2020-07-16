# coding = utf-8
'''
封装读取json方法

'''

import json

class OperaterJson:

    def __init__(self):
        self.data =self.red_json()

    def red_json(self):
        file =r"../data/test.json"
        try:
            with open(file) as f:
                data = json.load(f)
                return data
        except:
            print("josn文件读取失败")

    def get_json_value(self,key):
        return self.data[key]

if __name__ == '__main__':
    file =r"../data/test.json"
    data =OperaterJson()
    print(data.get_json_value("test"))

# with open(r"../data/test.json") as f:
#     print(json.load(f))

