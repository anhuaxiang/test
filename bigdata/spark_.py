from pyspark import SparkContext, SparkConf
from pyspark.sql.session import SparkSession

# spark_conf = SparkConf() \
#     .set('spark.executor.cores', '2') \
#     .set('spark.driver.memory', '2000M') \
#     .set('spark.executor.memory', '2000M') \
#     .set('spark.cores.max', '8')
# sc = SparkContext(master='spark://192.168.0.247:7077', conf=spark_conf)
# spark = SparkSession(sc)
# df = spark.read.csv('hdfs://192.168.0.247:9000/R2SparkTrain/aaa.csv')


spark_conf = SparkConf() \
    .set('spark.yarn.appMasterEnv.PYSPARK_PYTHON', '/home/tools/python3.6.5/bin/python') \
    .set('spark.history.ui.port', '18080') \
    .set('spark.executor.id', 'driver') \
    .set('spark.driver.port', '44871') \
    .set('spark.yarn.appMasterEnv.PYSPARK_DRIVER_PYTHON', '/home/tools/python3.6.5/bin/python') \
    .set('spark.master', 'spark://bigdata1:7077') \
    .set('spark.rdd.compress', 'True') \
    .set('spark.driver.host', '192.168.0.182') \
    .set('spark.submit.deployMode', 'client')

# a = [('spark.app.id', 'app-20190919143313-0084'),
#      ('spark.driver.host', 'DESKTOP-6F6UIS0'),
#      ('spark.rdd.compress', 'True'),
#      ('spark.serializer.objectStreamReset', '100'),
#      ('spark.executor.id', 'driver'),
#      ('spark.submit.deployMode', 'client'),
#      ('spark.driver.port', '59762'),
#      ('spark.ui.showConsoleProgress', 'true'),
#      ('spark.app.name', 'pyspark-shell'),
#      ('spark.master', 'spark://192.168.0.247:7077')]

# b = [('spark.eventLog.enabled', 'true'),
#      ('spark.yarn.appMasterEnv.PYSPARK_PYTHON', '/home/tools/python3.6.5/bin/python'),
#      ('spark.history.ui.port', '18080'),
#      ('spark.history.fs.logDirectory', 'hdfs://bigdata1:9000/tmp/spark/events'),
#      ('spark.executor.id', 'driver'),
#      ('spark.driver.port', '44871'),
#      ('spark.yarn.appMasterEnv.PYSPARK_DRIVER_PYTHON', '/home/tools/python3.6.5/bin/python'),
#      ('spark.app.name', 'pyspark-shell'),
#      ('spark.eventLog.dir', 'hdfs://bigdata1:9000/tmp/spark/events'),
#      ('spark.master', 'spark://192.168.0.247:7077'),
#      ('spark.yarn.historyServer.address', 'http://bigdata1:18080'),
#      ('spark.rdd.compress', 'True'),
#      ('spark.app.id', 'app-20190919142231-0083'),
#      ('spark.serializer.objectStreamReset', '100'),
#      ('spark.driver.host', 'bigdata2'),
#      ('spark.submit.deployMode', 'client'),
#      ('spark.ui.showConsoleProgress', 'true')]

sc = SparkContext.getOrCreate(conf=spark_conf)
spark = SparkSession.builder.getOrCreate()
df = spark.read.csv('hdfs://192.168.0.247:9000/R2SparkTrain/aaa.csv')
