"""
文件处理相关的工具模块
"""

def print_file_info(file_name):
    """
    功能是：将给定的路径文件内容输出到控制台中
    :param file_name: 即将被读取的文件路径
    :return: None
    """

    try:
        with open(file_name, "r", encoding="utf-8") as f:
            content = f.read()
            print(content)
        return
    except Exception as e:
        print(e)
        return



#定义函数：append_to_file(file_name,data) 用于接受文件路径以及传入数据，将数据追加到文件中
def append_to_file(file_name, data):
    """
    功能是：接收文件路径和数据，将数据追加到文件中
    :param file_name: 即将被追加的文件路径
    :param data: 要追加的数据
    :return: None
    """

    try:
        with open(file_name, "a", encoding="utf-8") as f:
            f.write(data)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    append_to_file("D:/test.txt","月薪过万")

