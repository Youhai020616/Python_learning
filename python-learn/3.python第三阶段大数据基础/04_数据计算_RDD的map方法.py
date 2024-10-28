#map方法：成员方法（算子）

#map算子
#功能：map算子是将rdd的数据一条条处理（处理的逻辑基于map算子中接收的处理函数），返回新的RDD


"""
演示RDD的成员方法的使用

"""
from pyspark import SparkConf,SparkContext
import os
os.environ["PYSPARK_PYTHON"] = "C:/Users/18055002740/AppData/Local/Programs/Python/Python312/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)


#准备一个RDD
rdd = sc.parallelize([1,2,3,4,5])

#通过map方法将rdd的数据一条条处理

def func(data):
    return  data*10

rdd2 = rdd.map(func).map(lambda x:x+1)
print(rdd2.collect())


#链式调用


