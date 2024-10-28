"""
RDD：弹性分布式数据集

演示通过pyspark 代码加载数据，即数据输入
"""

from  pyspark import  SparkConf,SparkContext

conf   = SparkConf().setMaster("local[*]").setAppName("pyspark")
sc = SparkContext(conf=conf)


# #通过parallelize方法将python数据对象加载到Spark内，成为RDD对象
# rdd1 = sc.parallelize([1,2,3,4,5])   #列表
# rdd2 = sc.parallelize((6,7,8,9,10)) #元组
# rdd3 = sc.parallelize({"a":1,"b":2,"c":3})  #字典
# rdd4 = sc.parallelize("hello spark")   #字符串
# rdd5 = sc.parallelize({3,2,5,6,7 })  #集合
#
# #如果要查看RDD里面的内容需要使用collect()方法
# print(rdd1.collect())
# print(rdd2.collect())
# print(rdd3.collect())
# print(rdd4.collect())
# print(rdd5.collect())


#用textFile方法,读取文件数据加载到Spark 内成为RDD对象

rdd = sc.textFile("D:/hello.txt")
print(rdd.collect())
sc.stop()



#RDD是PySpaerk中的数据计算载体：1.提供数据存储 2.提供计算的各类方法 3.数据的方法，返回值依旧是RDD

#如何输入数据到Spark得到RDD对象：1.通过SparkContext的parallelize方法，将python数据容器的内容转化为RDD对象，2.通过SparkContext的textFile成员方法，读取文本文件得到RDD对象





