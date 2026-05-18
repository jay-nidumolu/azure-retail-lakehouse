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

## Architecture

Bronze → Silver → Gold Medallion Architecture

- Bronze Layer → Raw data ingestion
- Silver Layer → Cleaned and transformed data
- Gold Layer → Business-ready analytics tables

---

## Current Progress

### Completed

- Created medallion storage architecture in ADLS Gen2
- Built metadata-driven ingestion pipeline using Azure Data Factory
- Implemented dynamic dataset parameterization
- Developed automated multi-entity ingestion using:
  - Get Metadata activity
  - Filter activity
  - ForEach activity
  - Copy activity
- Automated raw data movement from Landing layer to Bronze layer
- Developed reusable PySpark bronze-to-delta conversion job
- Implemented Delta Lake storage format
- Added ingestion timestamp metadata using PySpark

### Current Pipeline Flow

```text
Landing Layer
      ↓
Get Metadata
      ↓
Filter Required Files
      ↓
ForEach Loop
      ↓
Copy Activity
      ↓
Bronze Raw Layer
      ↓
Databricks PySpark Job
      ↓
Bronze Delta Layer

```

---

## Planned Features

- Silver layer transformations
- Gold analytics layer
- Incremental ETL processing
- Delta Lake MERGE operations
- Data quality validation
- KPI analytics tables
- Power BI dashboards
- Parameterized Databricks orchestration
- CI/CD integration

---

## Dataset

Brazilian E-Commerce Public Dataset by Olist

---

## Status

Metadata-driven Bronze layer ingestion framework has been successfully implemented. Silver and Gold layer transformations are currently in progress.