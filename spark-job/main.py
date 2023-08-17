from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .master("local[1]") \
    .appName("demo-job") \
    .getOrCreate()

df=spark.range(100)
print(df.sample(0.06).collect())
