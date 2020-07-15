# coding = utf-8
'''
封装常量，方便读取列的数据和拿到每个单元格做判断
1.固定模板的常量
2.自定义配置的常量
'''

class ExcelCanstant:

    case_name = "1"
    id = "2"
    environment = "3"
    url = "4"
    request_way = "5"
    header = "6"
    depend_id = "7"
    depend_data = "8"
    depend_field = "9"
    requst_data = "10"
    run = "11"
    expect = "12"
    result = "13"

# 获得用例名称列
def case_name():
    return ExcelCanstant.case_name

# 获得用例id列
def id():
    return ExcelCanstant.id

# 获得测试环境列
def environment():
    return ExcelCanstant.environment

# 获得url列
def url():
    return ExcelCanstant.url

# 获得请求方式列
def request_way():
    return ExcelCanstant.request_way

# 获得请求头列
def header():
    return ExcelCanstant.header

# 获得依赖id列
def depend_id():
    return ExcelCanstant.depend_id

# 获得依赖数据列
def depend_data():
    return ExcelCanstant.depend_data

# 获得依赖数据关键字列
def depend_field():
    return ExcelCanstant.depend_field

# 获得请求参数数据列
def requst_data():
    return ExcelCanstant.requst_data

# 获得是否执行列
def run():
    return ExcelCanstant.run

# 获得预期结果列
def expect():
    return ExcelCanstant.expect

# 获得实际结果列
def result():
    return ExcelCanstant.result
