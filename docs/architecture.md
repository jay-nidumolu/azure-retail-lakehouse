# Solution Architecture

## Overview

The Azure Retail Lakehouse Platform follows a Medallion Architecture design pattern to support scalable, modular, and analytics-ready data processing.

The platform ingests raw retail datasets from the Olist E-Commerce Dataset into Azure Data Lake Storage and processes them through Bronze, Silver, and Gold layers using Azure Data Factory, Azure Databricks, PySpark, and Delta Lake.

---

## High-Level Data Flow

```text
Raw CSV Files
      ↓
Azure Data Factory
      ↓
ADLS Landing Layer
      ↓
ADF Raw → Bronze Pipeline
      ↓
ADLS Bronze Layer
      ↓
ADF Bronze → Silver Pipeline
      ↓
Azure Databricks (PySpark)
      ↓
ADLS Silver Layer
      ↓
DQ Audit Logs
      ↓
Gold Layer (Planned)
      ↓
Power BI Dashboards (Planned)
```

---

## Storage Architecture

### Landing Layer

Stores raw source CSV files received from external systems.

### Bronze Layer

Stores immutable raw datasets in Delta Lake format with ingestion metadata.

Metadata captured:

- ingestion_timestamp
- ingestion_date
- source_file_name

### Silver Layer

Stores cleansed, standardized, and validated datasets.

Implemented transformations:

- Column renaming
- Data type standardization
- Null validation
- Duplicate remediation
- Invalid value validation
- Audit logging

### Gold Layer (Planned)

Will contain business-ready fact and dimension tables optimized for reporting and analytics.

Planned tables:

- fact_sales
- dim_customers
- dim_products

---

## Orchestration Architecture

Azure Data Factory is used for metadata-driven orchestration.

### Raw → Bronze Pipeline

Activities used:

- Get Metadata
- Filter Activity
- ForEach Activity
- Copy Activity

### Bronze → Silver Pipeline

Activities used:

- Get Metadata
- ForEach Activity
- Databricks Notebook Activity

The architecture enables scalable multi-entity processing without hardcoded table-specific pipelines.

---

## Data Quality Architecture

The Silver layer includes a reusable Data Quality Framework.

Implemented validations:

- Critical null checks
- Warning-level null checks
- Duplicate detection
- Invalid value checks
- Severity-based validation

Validation results are written to Delta-based audit logs for monitoring and troubleshooting.

---

## Technology Stack

| Layer | Technology |
|---------|---------|
| Storage | Azure Data Lake Storage Gen2 |
| Orchestration | Azure Data Factory |
| Processing | Azure Databricks |
| Transformation | PySpark |
| Storage Format | Delta Lake |
| Analytics | Power BI (Planned) |

---

## Future Architecture Enhancements

- Gold Layer implementation
- Star Schema modeling
- Fact and Dimension tables
- Incremental processing
- Delta MERGE operations
- Slowly Changing Dimensions (SCD)
- KPI aggregation tables
- Power BI dashboards
- CI/CD deployment
- Monitoring and alerting
- Databricks secret scopes