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

---

### Storage Architecture

- Created Medallion-based storage structure in ADLS Gen2
- Configured Landing, Bronze, Silver, Gold, and Checkpoints containers
- Organized entity-level storage structure for scalable ingestion

---

### Azure Data Factory Orchestration

- Built metadata-driven ingestion pipelines using Azure Data Factory
- Implemented reusable parameterized datasets
- Automated multi-entity ingestion using:
  - Get Metadata Activity
  - Filter Activity
  - ForEach Activity
  - Copy Activity
- Implemented dynamic sink routing for entity-based ingestion
- Built modular pipeline orchestration using Execute Pipeline activities
- Integrated Databricks Notebook Activity with ADF orchestration

---

### Databricks & PySpark

- Developed reusable PySpark Bronze-to-Delta conversion workflow
- Implemented parameterized Databricks notebook execution using widgets
- Automated entity-level Delta conversion using ADF pipeline orchestration
- Added ingestion timestamp metadata using PySpark
- Implemented Delta Lake transactional storage format

---

### Delta Lake

- Generated Delta tables with transaction logs (`_delta_log`)
- Built scalable Bronze Delta layer for downstream transformations

---

## Implemented Pipelines

### 1. Raw to Bronze Pipeline

Automates ingestion of raw datasets from Landing layer into Bronze Raw storage using metadata-driven orchestration.

---

### 2. Bronze to Delta Pipeline

Automates Delta Lake conversion of Bronze Raw datasets using Databricks and PySpark.

---

### 3. End-to-End Orchestrated Pipeline

Combines ingestion and Delta conversion into a single orchestrated workflow using Execute Pipeline activities.

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

- Silver layer transformations
- Gold analytics layer
- Star schema modeling
- Incremental ETL processing
- Delta Lake MERGE operations
- Slowly Changing Dimensions (SCD)
- Data quality validation framework
- KPI analytics tables
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

---

## Current Status

The metadata-driven Bronze ingestion and Delta Lake conversion framework has been successfully implemented.

### Current Development Focus

- Silver layer transformations
- Business logic implementation
- Analytics-ready Gold layer modeling
- Power BI dashboard integration