
from pyspark.sql import functions as F
from pyspark.sql.window import Window

#storage_details
storage_account= "storageretaillakehouse"

spark.conf.set(
    f"fs.azure.account.key.{storage_account}.dfs.core.windows.net",
    "<STORAGE KEY>"
)

silver_path = f"abfss://silver@{storage_account}.dfs.core.windows.net/products"
gold_path = f"abfss://gold@{storage_account}.dfs.core.windows.net/dimensions/dim_products"


df = spark.read.format("delta").load(silver_path)


required_columns = [
    "product_id",
    "product_category_name",
    "product_weight_g",
    "product_length_cm",
    "product_height_cm",
    "product_width_cm"
]

missing_columns = [c for c in required_columns
                if c not in df.columns]

if missing_columns:
    raise Exception(f"Missing columns: {missing_columns}")


dim_columns = (
    df.select(required_columns)
    .dropDuplicates(["product_id"])
    .withColumn("product_key", F.monotonically_increasing_id())
)

# dim_columns.printSchema()

# display(dim_columns, limit=10)

dim_columns.write.format("delta").save(gold_path)
