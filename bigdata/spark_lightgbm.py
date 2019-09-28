import pyspark
from pyspark.ml import Pipeline
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import VectorAssembler, StringIndexer

spark = pyspark.sql.SparkSession.builder.appName("MyApp")\
    .config("spark.jars.packages", "com.microsoft.ml.spark:mmlspark_2.11:0.18.1")\
    .getOrCreate()


import mmlspark
from mmlspark.lightgbm import LightGBMClassifier
from mmlspark.train import TrainClassifier, ComputeModelStatistics


df = spark.read.csv(r"C:\Users\yanrujing\Desktop\breast_cancer.csv", header=True, inferSchema=True)
train_data, test_data = df.randomSplit([0.8, 0.2], seed=0)
print(df.limit(10).toPandas())

model = TrainClassifier(model=LogisticRegression(), labelCol="class", numFeatures=256).fit(train_data)
prediction = model.transform(test_data)
metrics = ComputeModelStatistics().transform(prediction)
print(metrics.limit(10).toPandas())


f1 = VectorAssembler(inputCols=['clump_thickness', 'unif_cell_size', 'unif_cell_shape', 'marg_adhesion',
                                'single_epith_cell_size', 'bare_nuclei', 'bland_chrom', 'norm_nucleoli', 'mitoses'],
                     outputCol='features')
f2 = StringIndexer(inputCol='class', outputCol='label')

p = Pipeline(stages=[f1, f2]).fit(df)
data = p.transform(df)
train_data, test_data = data.randomSplit([0.8, 0.2], seed=0)
model = LightGBMClassifier(objective='binary').fit(train_data)
test_predict = model.transform(test_data)
metrics = ComputeModelStatistics(evaluationMetric='classification',
                                 labelCol='label',
                                 scoresCol='prediction').transform(test_predict)
