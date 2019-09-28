import pyspark.sql.functions as fn
from pyspark.sql.types import IntegerType, FloatType
from pyspark import SparkContext, Row
from pyspark.sql.session import SparkSession


sc = SparkContext()
ss = SparkSession(sc)

df = ss.read.csv(r"D:\workspace\sample\classification\titanic.train.csv", header=True, inferSchema=True)
df_length = df.count()

print(df.show(2))


origin_dtypes = dict(df.dtypes)
col_type = {}
meta_data = {f: {} for f in origin_dtypes.keys()}

for f, v in origin_dtypes.items():
    tmp = df.withColumn(f'{f}_to_float', df[f'{f}'].cast('float'))
    if tmp.filter(fn.isnull(f'{f}_to_float')).count() < df_length * 0.4:
        num_value = tmp.groupBy(f).count().count()
        if num_value <= 10:
            col_type[f] = 'C'
            meta_data[f]['count'] = num_value
        else:
            col_type[f] = 'N'
            mi, _5, _25, median, _75, _95, mx = tmp.approxQuantile(f'{f}_to_float', [0.0, 0.005, 0.25, 0.5, 0.75, 0.995, 1.0], 0)
            others = tmp.select(fn.mean(f'{f}_to_float'), fn.stddev(f'{f}_to_float'), fn.skewness(f'{f}_to_float')).take(1)[-1].asDict()
            skew = others.get(f'skewness({f})', 0)
            meta_data[f]['max'] = mx
            meta_data[f]['min'] = mi
            meta_data[f]['median'] = median
            meta_data[f]['mean'] = others.get(f'avg({f})', 0)
            meta_data[f]['std'] = others.get(f'stddev_samp({f})', 0)
            meta_data[f]['skew'] = skew

            iqr = _75 - _25
            if skew > 2.5:
                low = _5
                high = mx + 1.5 * iqr
            elif skew < -2.5:
                low = mi - 1.5 * iqr
                high = _95
            elif skew > 0.75:
                low = _25 - 1.5 * iqr
                high = _75 + 3 * iqr
            elif skew < -0.75:
                low = _25 - 3 * iqr
                high = _75 + 1.5 * iqr
            else:
                low = _25 - 1.5 * iqr
                high = _75 + 1.5 * iqr
            meta_data[f]['range'] = [low, high]

    elif df.groupBy(f).count().count() >= min(0.1 * df_length, 1000):
        col_type[f] = 'R'
    else:
        col_type[f] = 'C'
        meta_data[f]['count'] = df.groupBy(f).count().count()

print(meta_data)


for f, _ in origin_dtypes.items():
    if col_type.get(f) == 'N':
        ...
    elif col_type.get(f) == 'C':
        ...
    else:
        ...


# rdd map
def out(row):
    row = row.asDict()
    if row.get('age') > meta_data.get('age').get('range')[1] or row.get('age') < meta_data.get('age').get('range')[0]:
        row['age'] = meta_data.get('age').get('median')
    return Row(**row)
print(df.rdd.map(out).toDF().show(400))
df = df.fillna(meta_data.get('age').get('mean'), 'age')


# udf
df.withColumn('age_square', fn.udf(lambda z: z**2, FloatType())('age'))
df.withColumn('age_square', fn.udf(lambda z: z**2, FloatType())(df.age))


# when
df.withColumn('age_fill', fn.when(df.age > 80, 444.0).when(df.age < 20, 333.0).otherwise(df.age)).show()

