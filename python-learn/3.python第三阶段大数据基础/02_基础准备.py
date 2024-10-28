"""
演示获取pyspark的执行环境入库对象：SparkContext
并通过SparkContext对象获取当前Pyspark的版本
"""


from  pyspark import SparkConf,SparkContext

#创建SparkConf对象
conf = SparkConf().setMaster("local[*]").setAppName("pyspark")

# conf = SparkConf()
# conf.setMaster("local[*]")
# conf.setAppName("pyspark")



#创建SparkConf类对象创建SparkContext对象

sc = SparkContext(conf=conf)

#打印pyspark的运行版本

print(sc.version)
#停止SparkContext对象的运行（停止Spark程序）
sc.stop()