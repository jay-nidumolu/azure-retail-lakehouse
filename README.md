# Azure Retail Lakehouse Platform

An end-to-end cloud-native Data Engineering project built on Azure using Medallion Architecture principles. The platform ingests raw retail data, applies scalable transformation and data quality frameworks, builds dimensional models and KPI aggregation tables, and prepares analytics-ready datasets for business intelligence reporting.

---

## Tech Stack

* Azure Data Factory (ADF)
* Azure Data Lake Storage Gen2 (ADLS Gen2)
* Azure Databricks
* PySpark
* Delta Lake
* SQL
* Power BI

---

## Project Overview

This project simulates a production-grade retail analytics platform using the Brazilian E-Commerce Public Dataset by Olist.

The platform follows a Medallion Architecture approach:

* Bronze Layer → Raw data ingestion and Delta conversion
* Silver Layer → Data cleansing, standardization, and validation
* Gold Layer → Dimensional modeling, fact tables, and KPI aggregations

The solution demonstrates metadata-driven orchestration, reusable transformation frameworks, data quality enforcement, audit logging, and scalable analytics engineering using Azure-native services.

---

## Project Status

| Layer     | Status     |
| --------- | ---------- |
| Landing   | ✅ Complete |
| Bronze    | ✅ Complete |
| Silver    | ✅ Complete |
| Gold      | ✅ Complete |
| KPI Layer | ✅ Complete |
| Power BI  | ⏳ Planned  |

---

## Solution Architecture

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
ADF Silver → Gold Pipeline
    ↓
Gold Layer
    ↓
KPI Aggregation Tables
    ↓
Power BI Dashboard
```

---

## Current Progress

### Storage Architecture

* Created Medallion-based storage structure in ADLS Gen2
* Configured Landing, Bronze, Silver, Gold, and Audit containers
* Organized entity-level storage structure for scalable ingestion
* Implemented Delta Lake storage strategy across all layers

---

### Azure Data Factory Orchestration

* Built metadata-driven Raw → Bronze ingestion pipeline
* Built metadata-driven Bronze → Silver transformation pipeline
* Built Silver → Gold analytics pipeline
* Implemented reusable parameterized datasets
* Automated multi-entity processing using:

  * Get Metadata Activity
  * ForEach Activity
  * Copy Activity
  * Databricks Notebook Activity
  * Execute Pipeline Activity
* Implemented dynamic path generation and entity routing
* Developed end-to-end orchestration from Raw → Bronze → Silver → Gold

---

### Databricks & PySpark

* Developed reusable Silver transformation framework
* Developed reusable Data Quality framework
* Implemented metadata-driven processing
* Implemented configurable schema standardization
* Implemented reusable column renaming framework
* Implemented reusable data type casting framework
* Added ingestion metadata tracking
* Automated Delta Lake writes
* Developed reusable audit logging framework

---

## Data Quality Framework

Implemented a reusable Data Quality framework shared across Silver and Gold layers.

### Features

* Null value validation
* Duplicate detection and remediation
* Invalid value validation
* Severity-based validation checks
* Warning-level validations
* Critical validations
* Automated pipeline failure handling
* Audit log generation
* Delta-based audit storage

### Validation Strategy

| Severity | Action                |
| -------- | --------------------- |
| Warning  | Log and Continue      |
| Critical | Log and Fail Pipeline |

### Gold Layer Validations

* Null customer key validation
* Null product key validation
* Null date key validation
* Duplicate sale key detection
* Row count reconciliation
* Business rule validation
* KPI validation checks

---

## Silver Layer Features

The Silver layer performs cleansing, standardization, and validation before data is promoted to Gold.

### Implemented Transformations

* Column standardization and renaming
* Data type casting
* Null value validation
* Duplicate detection and remediation
* Invalid value validation
* Severity-based DQ checks
* Audit log generation
* Delta Lake optimization

### Silver Entities

* Customers
* Orders
* Payments
* Order Items
* Products

---

## Gold Layer Features

The Gold layer implements dimensional modeling and analytics-ready structures for downstream reporting.

### Dimension Tables

#### dim_customers

* Customer surrogate key generation
* Customer location attributes
* Analytics-ready customer dimension

#### dim_products

* Product surrogate key generation
* Product category enrichment
* Business-friendly category handling
* Analytics-ready product dimension

#### dim_dates

* Calendar dimension generation
* Year
* Quarter
* Month
* Week
* Day
* Time intelligence support

---

### Fact Tables

#### fact_sales

Implemented a star schema fact table integrating:

* Customer Dimension
* Product Dimension
* Date Dimension
* Order Metrics
* Payment Metrics

Features:

* Surrogate key generation
* Dimension key integration
* Revenue analytics support
* Data quality enforcement
* Audit logging
* Row count reconciliation

---

## KPI Aggregation Tables

### sales_summary

Executive-level KPI table containing:

* Total Revenue
* Total Orders
* Average Order Value (AOV)

---

### monthly_sales

Monthly business performance metrics:

* Monthly Revenue
* Monthly Orders
* Average Order Value
* Time-based analytics

---

### revenue_by_state

Customer geography analytics:

* Revenue by State
* Order Volume by State
* Regional performance analysis

---

### category_sales

Product analytics:

* Revenue by Category
* Orders by Category
* Product category performance analysis

---

## Delta Lake Implementation

* Bronze Delta Layer
* Silver Delta Layer
* Gold Delta Layer
* Delta Transaction Logs (`_delta_log`)
* ACID Transactions
* Schema Enforcement
* Scalable Lakehouse Architecture

---

## Implemented Pipelines

### 1. Raw → Bronze Pipeline

Metadata-driven ingestion pipeline that automatically discovers source entities and ingests raw files into Bronze storage.

---

### 2. Bronze → Silver Pipeline

Metadata-driven transformation pipeline that executes reusable Databricks notebooks for cleansing, standardization, validation, and Delta table generation.

---

### 3. Silver → Gold Pipeline

Analytics pipeline that generates:

* Dimension Tables
* Fact Tables
* KPI Aggregation Tables
* Audit Logs

---

### 4. End-to-End Orchestration Pipeline

Master ADF pipeline orchestrating:

```text
Raw Files
   ↓
Bronze
   ↓
Silver
   ↓
Gold
   ↓
KPI Tables
```

---

## Dataset

### Brazilian E-Commerce Public Dataset by Olist

Entities include:

* Orders
* Customers
* Products
* Payments
* Order Items
* Reviews
* Sellers
* Geolocation

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
│   │
│   ├── bronze/
│   │   ├── notebooks/
│   │   └── pyspark_jobs/
│   │
│   ├── silver/
│   │   ├── notebooks/
│   │   ├── pyspark_jobs/
│   │   └── sql/
│   │
│   ├── gold/
│   │   ├── notebooks/
│   │   ├── pyspark_jobs/
│   │   └── sql/
│   │
│   └── common/
│       └── dq_framework.py
│
├── configs/
│
└── powerbi/
```

---

## Key Engineering Concepts Demonstrated

* Metadata-driven orchestration
* Cloud-native Data Engineering
* Dynamic pipeline parameterization
* Reusable ingestion frameworks
* Reusable Data Quality Framework
* Distributed data processing with Spark
* Delta Lake transactional storage
* Medallion Architecture implementation
* ADF to Databricks orchestration
* Scalable multi-entity ingestion workflows
* Data Quality Framework Design
* Audit Logging and Monitoring
* Reusable PySpark Transformation Framework
* Severity-Based Data Validation
* Pipeline Failure Handling
* Dimensional Modeling
* Star Schema Design
* Surrogate Key Generation
* Fact & Dimension Modeling
* KPI Aggregation Design
* Business Analytics Engineering
* Delta Lake Data Management

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

✅ Gold Dimension Tables

✅ fact_sales Fact Table

✅ Star Schema Modeling

✅ Silver → Gold Pipeline

✅ sales_summary KPI Table

✅ monthly_sales KPI Table

✅ revenue_by_state KPI Table

✅ category_sales KPI Table

### In Progress

🔄 Power BI Dashboard Development

### Upcoming

📊 Interactive Business Dashboards

📈 Revenue Trend Analysis

📍 Regional Sales Analytics

🛍 Product Category Performance Analytics

🔄 Incremental MERGE Processing

🔄 Slowly Changing Dimensions (SCD)

🔄 CI/CD Integration

🔄 Monitoring & Alerting

---

## Additional Documentation

* Solution Architecture
* Bronze Layer Design
* Silver Layer Design
* Gold Layer Design
* Data Quality Framework
* KPI Layer Design
* Power BI Dashboard Design
