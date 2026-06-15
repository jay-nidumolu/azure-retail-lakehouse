from pyspark.sql.functions import *
from datetime import datetime
from pyspark.sql.types import *

dq_results = {}

#Data Quality checks
def run_dq_check(
    df,
    table_name,
    check_name,
    condition,
    severity="warning"
):

    failed_count = df.filter(condition).count()

    dq_results.setdefault(table_name, [])

    dq_results[table_name].append({
        "check_name": check_name,
        "severity": severity,
        "failed_count": failed_count
    })

    print(
        f"[{severity.upper()}] "
        f"{table_name} | "
        f"{check_name}: "
        f"{failed_count}"
    )

    if severity == "critical" and failed_count > 0:

        raise Exception(
            f"Critical DQ Failure | "
            f"Table: {table_name} | "
            f"Check: {check_name} | "
            f"Failed Count: {failed_count}"
        )

    return failed_count

#metric Check
def run_metric_check(
    table_name,
    check_name,
    failed_count,
    severity="warning"
):

    dq_results.setdefault(table_name, [])

    dq_results[table_name].append({
        "check_name": check_name,
        "severity": severity,
        "failed_count": failed_count
    })

    print(
        f"[{severity.upper()}] "
        f"{table_name} | "
        f"{check_name}: "
        f"{failed_count}"
    )

    if severity == "critical" and failed_count > 0:

        raise Exception(
            f"Critical DQ Failure | "
            f"Table: {table_name} | "
            f"Check: {check_name} | "
            f"Failed Count: {failed_count}"
        )
    return failed_count

# Duplicate Handling
def handle_duplicates(
    df,
    table_name,
    key_columns,
    severity="warning"
):

    before_count = df.count()

    deduped_df = df.dropDuplicates(key_columns)

    after_count = deduped_df.count()

    duplicates_removed = before_count - after_count

    dq_results.setdefault(table_name, [])

    dq_results[table_name].append({
        "check_name": f"duplicate_{'_'.join(key_columns)}",
        "severity": severity,
        "failed_count": duplicates_removed
    })

    print(
        f"[{severity.upper()}] "
        f"{table_name} | "
        f"duplicates_removed: "
        f"{duplicates_removed}"
    )

    return deduped_df


#Schema of the dq dataframe
dq_schema = StructType([
    StructField("run_timestamp", TimestampType(), True),
    StructField("table_name", StringType(), True),
    StructField("check_name", StringType(), True),
    StructField("severity", StringType(), True),
    StructField("failed_count", IntegerType(), True)
])


#Converting all the results into a single data frame
def dq_df_from_dq_results(spark, dq_results):

    dq_rows = []

    for table_name, checks in dq_results.items():

        for check in checks:

            dq_rows.append(
                (
                    datetime.now(),
                    table_name,
                    check["check_name"],
                    check["severity"],
                    check["failed_count"]
                )
            )
    
    return spark.createDataFrame(dq_rows, schema=dq_schema)

