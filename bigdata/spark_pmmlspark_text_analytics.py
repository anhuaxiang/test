import pyspark
import pandas as pd
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression, RandomForestClassifier, GBTClassifier

spark = pyspark.sql.SparkSession.builder.appName("MyApp")\
    .config("spark.jars.packages", "com.microsoft.ml.spark:mmlspark_2.11:0.18.1")\
    .getOrCreate()


import mmlspark
from mmlspark.train import TrainClassifier
from mmlspark.automl import TuneHyperparameters
from mmlspark.train import ComputeModelStatistics
from mmlspark.automl import HyperparamBuilder, RangeHyperParam, DiscreteHyperParam, RandomSpace


data = spark.read.csv(r"C:\Users\yanrujing\Desktop\breast_cancer.csv", header=True, inferSchema=True)
data = data.withColumnRenamed('class', 'label')
f1 = VectorAssembler(inputCols=['clump_thickness', 'unif_cell_size', 'unif_cell_shape', 'marg_adhesion',
                                'single_epith_cell_size', 'bare_nuclei', 'bland_chrom', 'norm_nucleoli', 'mitoses'],
                     outputCol='features')
p = Pipeline(stages=[f1]).fit(data)
data = p.transform(data)
train_data, test_data = data.randomSplit([0.8, 0.2], seed=0)

lg = LogisticRegression()
rf = RandomForestClassifier()
gbt = GBTClassifier()

models = [lg, rf, gbt]
mml_models = [TrainClassifier(model=model, labelCol="label") for model in models]
param_builder = HyperparamBuilder() \
    .addHyperparam(lg, lg.regParam, RangeHyperParam(0.1, 0.3)) \
    .addHyperparam(rf, rf.numTrees, DiscreteHyperParam([5, 10])) \
    .addHyperparam(rf, rf.maxDepth, DiscreteHyperParam([3, 5])) \
    .addHyperparam(gbt, gbt.maxBins, RangeHyperParam(8, 16)) \
    .addHyperparam(gbt, gbt.maxDepth, DiscreteHyperParam([3, 5]))

search_space = param_builder.build()
print(search_space)
random_space = RandomSpace(search_space)

best_model = TuneHyperparameters(
    evaluationMetric="accuracy", models=mml_models, numFolds=2,
    numRuns=len(mml_models) * 2, parallelism=1,
    paramSpace=random_space.space(), seed=0
).fit(train_data)


print(best_model.getBestModelInfo())
print(best_model.getBestModel())


prediction = best_model.transform(test_data)
metrics = ComputeModelStatistics().transform(prediction)
print(metrics.limit(10).toPandas())