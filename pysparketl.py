from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, split


spark = SparkSession.builder \
    .appName("MyApp") \
    .config("spark.driver.memory", "4g") \
    .getOrCreate()


df = spark.read.csv("first10.csv", header=True, inferSchema=True)
print(df)
# df_transformed = (
#   df.select(
#     col("state_name_"),
#     col("name"),
#     split(col("address"), ",\s*").alias("address_parts")
#   )
#   .withColumn("city", col("address_parts")[0])
#   .withColumn("state", col("address_parts")[1])
#   .withColumn("zip_code", col("address_parts")[2])
#   .drop("address_parts")
# )


