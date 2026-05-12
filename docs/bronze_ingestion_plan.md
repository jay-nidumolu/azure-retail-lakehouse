# Bronze Layer Ingestion Plan

## Initial Tables

1. customers
2. orders
3. order_items
4. payments
5. products

---

## Ingestion Strategy

- Source: CSV files
- Landing Zone: ADLS Bronze Layer
- Format: Delta
- Orchestration: Azure Data Factory
- Partitioning: ingestion_date

---

## Bronze Principles

- Append-only
- Immutable raw data
- Minimal transformations
- Add ingestion metadata columns
- Preserve source lineage
- Support downstream Silver transformations

---

## Metadata Columns

The following metadata columns will be added during ingestion:

- ingestion_timestamp
- ingestion_date
- source_file_name

---

## Planned Technologies

| Component | Technology |
|---|---|
| Storage | Azure Data Lake Gen2 |
| Processing | Azure Databricks |
| Transformation | PySpark |
| Orchestration | Azure Data Factory |
| Storage Format | Delta Lake |

---

## Future Enhancements

- Incremental ingestion
- Schema evolution handling
- Data quality validation
- Auto Loader integration
- CDC support