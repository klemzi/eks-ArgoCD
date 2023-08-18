from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .master("local[1]") \
    .appName("my-test-spark-job") \
    .getOrCreate()

df=spark.range(100)
print(df.sample(0.06).collect())
# Output: [Row(id=0), Row(id=2), Row(id=17), Row(id=25), Row(id=26), Row(id=44), Row(id=80)]
