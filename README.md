# Azure Retail Lakehouse Platform

An end-to-end , cloud native Data Engineering Project built on Azure using medallion Architecture principles.

## Tech Stack

- Azure Data Factory
- Azure Data Lake Storage Gen2
- Azure Databricks
- PySpark
- Delta Lake
- SQL
- Power BI

## Project Overview

This project stimulates a production-style retail analytics platform using the Olist e-commerce dataset.

The platform ingests raw retail datsets into Azure Data Lake Storage, processes and transforms data using Databricks and PySpark, and builds analytics-ready Gold Tables for business intelligence and reporting.

## Architecture

Bronze → Silver → Gold Medallion Architecture

- Bronze Layer → Raw Ingestion
- Silver Layer → Cleaned and transformed data
- Gold Layer → Business-ready analytics tables

## Planned Features

- Metadata-driven ingestion pipelines
- Incremental ETL processing
- Delta Lake MERGE operations
- Data quality validation
- KPI analytics table
- Power BI dashboards
- Cloud-native orchestration using ADF

## Dataset

Brazillian E-Commerce Public Dataset by Olist

## Status

Project setup and architecture phase in progress.
