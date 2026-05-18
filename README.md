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
- Built initial Azure Data Factory ingestion pipeline
- Implemented Bronze raw layer ingestion
- Developed reusable PySpark bronze-to-delta conversion job
- Implemented Delta Lake storage format

### In Progress
- Metadata-driven ingestion orchestration
- Generic parameterized ADF pipelines
- Multi-entity ingestion framework

---

## Planned Features

- Metadata-driven ingestion pipelines
- Incremental ETL processing
- Delta Lake MERGE operations
- Data quality validation
- KPI analytics tables
- Power BI dashboards
- Cloud-native orchestration using ADF

---

## Dataset

Brazilian E-Commerce Public Dataset by Olist

---

## Status

Foundation architecture and Bronze layer ingestion pipelines are currently under development.