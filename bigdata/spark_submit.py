from pyspark import SparkContext, SparkConf
import sys


conf = SparkConf().setAppName('text').set('spark.driver.port', '25392').set('spark.driver.host', '192.168.0.182')
sc = SparkContext(conf=conf)


from pyspark.sql import HiveContext
from pyspark.sql.session import SparkSession
import pandas as pd

sql = HiveContext(sc)
spark = SparkSession.builder.enableHiveSupport().getOrCreate()

print(sys.argv[1], type(sys.argv[1]))
print(sys.argv)
print(spark)
# df = spark.read.csv('hdfs://192.168.0.247:9000/R2SparkTrain/aaa.csv')
df = spark.range(1000000)
print(df.count())

# a = sc.textFile('./spark_.py')
# print(a.count())
