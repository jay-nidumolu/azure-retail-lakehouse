import sys
import os
from dotenv import load_dotenv
from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp

load_dotenv()

storage_account= os.getenv("AZURE_STORAGE_NAME")
storage_key = os.getenv("AZURE_STORAGE_KEY")

#create spark session
spark = (
    SparkSession.builder
    .appName("bronze_to_delta")
    .getOrCreate()
)

#Storage Configuration
spark.conf.set(
    f"fs.azure.account.key.{storage_account}.dfs.core.windows.net",
    storage_key
)

entity_name = sys.argv[1] if len(sys.argv) > 1 else "orders"

if entity_name in ["customers", "products", "orders"]: 
    source_entity_name = entity_name
else:
    source_entity_name = f"order_{entity_name}"

raw_path = (
    f"abfss://bronze@{storage_account}.dfs.core.windows.net/",
    f"{entity_name}/"
    f"olist_{source_entity_name}_dataset.csv"
)

bronze_delta_path = (
    f"abfss://bronze@{storage_account}.dfs.core.windows.net/"
    f"delta/{entity_name}/"
)

# Read raw csv
df = (
    spark.read
    .option("header", True)
    .csv(raw_path)
)

#Add ingestion Timestamp
bronze_df = (
    df.withColumn("ingestion_timestamp", current_timestamp())
)

# Write delta table
(
    bronze_df.write
    .format("delta")
    .mode("overwrite")
    .save(bronze_delta_path)
)

bronze_df.show(5)