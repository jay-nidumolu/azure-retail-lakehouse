from pyspark.sql import functions as F

storage_account= "storageretaillakehouse"

spark.conf.set(
    f"fs.azure.account.key.{storage_account}.dfs.core.windows.net",
    "<STORAGE_KEY>"
)

gold_path = f"abfss://gold@{storage_account}.dfs.core.windows.net/dimensions/dim_dates"

dates = spark.sql("""
SELECT  explode(
    sequence(
        to_date('2016-01-01'),
        to_date('2020-12-31'),
        interval 1 day
    )
    ) AS date
""")

dim_dates = (
    dates
    .withColumn("date_key",
                F.date_format("date","yyyyMMdd"))
    .withColumn("year",
                F.year("date"))
    .withColumn("quarter",
                F.quarter("date"))
    .withColumn("month",
                F.month("date"))
    .withColumn("month_name",
                F.date_format("date","MMMM"))
    .withColumn("week",
                F.weekofyear("date"))
    .withColumn("day",
                F.dayofmonth("date"))
)


# display(dim_dates, limit = 10)

dim_dates.write.mode("overwrite").save(gold_path)
