# coding = utf-8

'''
读取ymal方法
'''
import yaml
class OperateYaml:

    def __init__(self,file):
        self.data = self.read_yaml(file)

    def read_yaml(self, file):
        with open(file, 'r') as f:
            return yaml.load(f, Loader=yaml.FullLoader)

    def get_value(self,key):
        return self.data[key]

if __name__ == '__main__':
    file =r"../data/test.yaml"
    data = OperateYaml(file).get_value("test")
    print(data)