
from pyspark.sql import functions as F
from pyspark.sql.window import Window

#storage_details
storage_account= "storageretaillakehouse"

spark.conf.set(
    f"fs.azure.account.key.{storage_account}.dfs.core.windows.net",
    "<STORAGE KEY>"
)

silver_path = f"abfss://silver@{storage_account}.dfs.core.windows.net/customers"
gold_path = f"abfss://gold@{storage_account}.dfs.core.windows.net/dimensions/dim_customers"


df = spark.read.format("delta").load(silver_path)


required_columns = [
    "customer_id",
    "customer_unique_id",
    "customer_city",
    "customer_state"
]

missing_columns = [c for c in required_columns
                   if c not in df.columns]

if missing_columns:
    raise Exception(f"Missing columns: {missing_columns}")


dim_columns = (
    df.select(required_columns)
    .dropDuplicates(["customer_id"])
      .withColumn("customer_key", F.monotonically_increasing_id())
)


dim_columns.write.format("delta").save(gold_path)
