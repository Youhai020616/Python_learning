"""
和文件相关的类
"""
import json
from data_define import Record

#先定义一个抽象类用来做顶层设计

class FileReader:

    def read_data(self) -> list[Record]:
        pass
    """用来读取文件的数据，将独到的数据都转换为recprd对象，将她们都封装到list内部返回"""

class TextFileReader(FileReader):
    """文本文件读取类"""
    def __init__(self,path):
        self.path = path
        """初始化文件路径"""

# 复写（实现抽象方法）
    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding='utf-8')

        record_list :list[Record] = []
        for line in f.readlines():
            line = line.strip()  #消除读取到的每一行数据中的\n
            data_list =  line.split(",")
            record =  Record(data_list[0],data_list[1],int(data_list[2]),data_list[3])
            record_list.append(record)

        f.close()
        return record_list

    """用来读取文件的数据，将独到的数据都转换为recprd对象，将她们都封装到list内部返回"""

class JsonFileReader(FileReader):
    """json文件读取类"""
    def __init__(self,path):
        self.path = path
        """初始化文件路径"""

    # 复写（实现抽象方法）
    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding='utf-8')

        record_list :list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record =Record(data_dict["date"],data_dict["order_id"],int(data_dict["money"]),data_dict["province"])
            record_list.append(record)

        f.close()
        return record_list

if __name__ =='__main__':
    text_file_reader = TextFileReader('E:/8天python从入门到精通资料/第13章资料/2011年1月销售数据.txt')
    json_file_reader = JsonFileReader('E:/8天python从入门到精通资料/第13章资料/2011年2月销售数据JSON.txt')
    list1 = text_file_reader.read_data()
    list2 = json_file_reader.read_data()

    for l in list1:
        print(l)

    for l in list2:
        print(l)
