# Azure Retail Lakehouse Platform

An end-to-end cloud-native Data Engineering project built on Azure using Medallion Architecture principles.

---

## Tech Stack

- Azure Data Factory (ADF)
- Azure Data Lake Storage Gen2 (ADLS Gen2)
- Azure Databricks
- PySpark
- Delta Lake
- SQL
- Power BI

---

## Project Overview

This project simulates a production-style retail analytics platform using the Olist e-commerce dataset.

The platform ingests raw retail datasets into Azure Data Lake Storage, processes and transforms data using Azure Databricks and PySpark, and builds analytics-ready Gold tables for business intelligence and reporting.

---

## Project Status

| Layer | Status |
|---------|---------|
| Landing | ✅ Complete |
| Bronze | ✅ Complete |
| Silver | ✅ Complete |
| Gold | 🔄 In Progress |
| Power BI | ⏳ Planned |

---

## Solution Architecture

Bronze → Silver → Gold Medallion Architecture

- Bronze Layer → Raw data ingestion
- Silver Layer → Cleaned and transformed data
- Gold Layer → Business-ready analytics tables

```text
Raw Files
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
Gold Layer (In Progress)
```

---

## Current Progress

### Completed

#### Storage Architecture

- Created Medallion-based storage structure in ADLS Gen2
- Configured Landing, Bronze, Silver, Gold, and Audit containers
- Organized entity-level storage structure for scalable ingestion

---

#### Azure Data Factory Orchestration

- Built metadata-driven Raw → Bronze ingestion pipeline
- Built metadata-driven Bronze → Silver transformation pipeline
- Implemented reusable parameterized datasets
- Automated multi-entity processing using:
  - Get Metadata Activity
  - ForEach Activity
  - Copy Activity
  - Databricks Notebook Activity
- Implemented dynamic path generation and entity routing
- Built modular pipeline orchestration using Execute Pipeline activities
- Developed end-to-end orchestration from Raw → Bronze → Silver

---

#### Databricks & PySpark

- Developed reusable Silver transformation framework
- Implemented metadata-driven processing for multiple entities
- Implemented configurable schema standardization
- Added reusable column renaming framework
- Implemented reusable data type casting framework
- Added ingestion metadata tracking
- Automated Delta Lake writes to Silver layer

---

#### Data Quality Framework

- Implemented reusable DQ validation framework
- Implemented severity-based validation checks:
  - Critical validations
  - Warning-level validations
- Implemented null value validation
- Implemented duplicate detection and remediation
- Implemented invalid value detection
- Implemented DQ audit logging
- Stored audit results in Delta format for monitoring and traceability

---

#### Silver Layer Features

The Silver layer performs data cleansing, standardization, and validation before data is promoted to analytics-ready layers.

Implemented transformations include:

- Column standardization and renaming
- Data type casting
- Null value validation
- Duplicate detection and remediation
- Invalid value validation
- Severity-based data quality checks
- Audit log generation
- Delta Lake storage optimization

Implemented Silver transformations for:

- Customers
- Orders
- Payments
- Order Items
- Products

---

#### Delta Lake

- Implemented Bronze Delta layer
- Implemented Silver Delta layer
- Generated Delta transaction logs (`_delta_log`)
- Built scalable lakehouse storage structure for downstream analytics

---

## Implemented Pipelines

### 1. Raw → Bronze Pipeline

Metadata-driven ingestion pipeline that automatically discovers source entities and ingests raw files into Bronze storage.

---

### 2. Bronze → Silver Pipeline

Metadata-driven transformation pipeline that executes reusable Databricks notebooks for entity-level cleansing, standardization, and Delta table generation.

---

### 3. End-to-End Orchestration Pipeline

Master ADF pipeline that orchestrates:

Raw Files → Bronze → Silver

using Execute Pipeline activities.

---

## Dataset

### Brazilian E-Commerce Public Dataset by Olist

Dataset includes:

- Orders
- Customers
- Products
- Payments
- Order Items
- Reviews
- Sellers
- Geolocation

---

## Repository Structure

```text
azure-retail-lakehouse/
│
├── docs/
│   ├── architecture/
│   ├── screenshots/
│   └── interview_notes/
│
├── adf/
│   ├── pipelines/
│   └── datasets/
│
├── databricks/
│   ├── notebooks/
│   ├── pyspark_jobs/
│   └── sql/
│
├── configs/
│
└── powerbi/
```

---

## Planned Features

- Gold analytics layer
- Star schema modeling
- Fact and Dimension tables
- KPI aggregation tables
- Incremental ETL processing
- Delta Lake MERGE operations
- Slowly Changing Dimensions (SCD)
- Power BI dashboards
- Incremental pipeline orchestration
- CI/CD integration
- Databricks secret scopes
- Monitoring and alerting

---

## Key Engineering Concepts Demonstrated

- Metadata-driven orchestration
- Cloud-native Data Engineering
- Dynamic pipeline parameterization
- Reusable ingestion frameworks
- Distributed data processing with Spark
- Delta Lake transactional storage
- Modular pipeline architecture
- Medallion Architecture implementation
- ADF to Databricks orchestration
- Scalable multi-entity ingestion workflows
- Data Quality Framework Design
- Audit Logging and Monitoring
- Reusable PySpark Transformation Framework
- Severity-Based Data Validation
- Delta Lake Data Management

---

## Current Status

### Completed

✅ Raw → Bronze ingestion

✅ Bronze Delta conversion

✅ Silver transformations

✅ Metadata-driven ADF orchestration

✅ Data Quality Framework

✅ Audit Logging

✅ Delta Lake implementation

### In Progress

🔄 Gold Layer Development

### Upcoming

⏳ fact_sales
⏳ KPI Aggregations
⏳ Power BI Dashboard

---

## Additional Documentation

- [Solution Architecture](docs/architecture.md)
- [Bronze Layer Design](docs/bronze_ingestion_plan.md)
- [Silver Layer Design](docs/silver_transformations_plan.md)
- [Gold Layer Design](docs/gold_analytics_plan.md)
