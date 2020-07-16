# coding = utf-8

'''
封装 requests 方法
返回response
'''

'''
调试接口
1.4、获取一个城市所有监测点的NO2数据

地址	http://www.pm25.in/api/querys/no2.json
方法	GET
参数	
* city：必选
* avg：可选
* stations：可选
      
返回	
一个数组，其中每一项数据包括
* aqi
* area
* no2
* no2_24h
* position_name
* primary_pollutant
* quality
* station_code
* time_point
注意有些接口是放返回页面格式会出现乱码的现象，如果打印类型可能得到ISO-8859-1，需要转码成 ‘bg2321’
下面是例子
# url="https://www.baidu.com"
# res=requests.get(url)
# print(res.status_code)
# print(res.encoding)
# res.encoding = 'gb2321'
# print(res.text)
'''
import requests
import json
from common.read_excel import read_excel
# class RunMain:
#
#     def __init__(self, url, method, data=None):                # 初始化方法 直接调用RunMain().res 就可以得到请求后的数据
#         self.res = self.run_main(url, method, data)
#
#     def send_get(self, url, data=None, headers=None):          # 封装get
#         try:
#             res = requests.get(url=url, headers=headers, params=data, verify=False).json()
#             return res
#         except:
#             print('请求失败')
#     def send_post(self, url, data=None, headers=None):         # 封装post
#         try:
#             res = requests.post(url=url, headers=headers, data=data, verify=False).json()
#             return res
#         except:
#             print('请求失败')
#
#     def run_main(self, url, method, data=None):                # 根据请求方式判断调用哪个
#         res = None
#         if method == "GET":
#             res = self.send_get(url, data)
#         else:
#             res= self.send_post(url, data)
#         return res
#
# if __name__ == '__main__':
#     url="http://www.pm25.in/api/querys/no2.json"
#     data ={
#     "city":"guangzhou",
#     "token": "5j1znBVAsnSf5xQyNQyq"
#     }
#     # print(send_get(url,data))
#     run= RunMain(url,"GET",data)
#     print(run.res)
class Method:
    # # 初始化run_method方法
    # def __init__(self,url,method,data=None,header=None,file=None):
    #     self.res = self.run_method(url,method,data,header,file)
    # get 方法
    def send_get(self,url,data=None,header=None):
        try:
            res = None
            if header != None:
                res = requests.get(url=url, params=data, heades=header, verify=False).json()
            else:
                res = requests.get(url=url, params=data, verify=False).json()
            return res
        except:
            print("get 请求失败")
    # post 方法
    def send_post(self,url,data,header=None,file=None):
        try:
            res = None
            if header != "":
                res =requests.post(url=url,data=data,heades=header,files=file,verify=False).json()
            else:
                res =requests.post(url=url,data=data,files=file,verify=False).json()
            return res
        except:
            print("post 请求失败")
    # 运行方法
    def run_method(self,url,method,data=None,header=None,file=None):
        try:
            res = None
            if method == "GET":
                res = self.send_get(url,data,header)
            else:
                res = self.send_post(url,data,header,file)
            return res
        except:
            print("run_method 请求失败")
if __name__ == '__main__':
    url = "http://www.pm25.in/api/querys/no2.json"
    method="GET"
    header=None
    data={'city': 'guangzhou', 'token': '5j1znBVAsnSf5xQyNQyq'}
    print(Method().run_method(url,method,data,header))
