# Databricks Practice

This repository contains hands-on practice and learning examples for **Azure Databricks**, focusing on Lakeflow Spark Declarative Pipelines, Auto Loader, backfill processing, and data engineering concepts.


## Repository Structure

```text
src/
├── SDP_Practice Pipeline/
│   └── my_transformation.py
├── auto_loader/
│   └── auto_loader.py
├── backfill/
│   └── backfill.py
└── README.md
```

## Topics Covered

### 1. Lakeflow Spark Declarative Pipelines

- Creating pipeline datasets using Python.
- Working with streaming tables and materialized views.
- Defining transformations using the `pyspark.pipelines` API.
- Applying data-quality filters.
- Understanding Bronze and Silver data layers.
- Exploring pipeline execution and monitoring.

### 2. Auto Loader

- Ingesting JSON files incrementally.
- Using the `cloudFiles` format.
- Configuring Auto Loader to identify the source file format.
- Reading files from Databricks Volumes.
- Understanding incremental ingestion in data pipelines.

### 3. Backfill Processing

- Understanding historical data processing.
- Loading previously available data into a pipeline.
- Working with backfill flows alongside regular ingestion.
- Understanding how backfill processing supports data completeness.

## Learning Objectives

The objectives of this repository are to:

1. Develop practical experience with Databricks data engineering.
2. Understand batch and streaming data processing.
3. Build Bronze and Silver data transformations.
4. Learn incremental ingestion using Auto Loader.
5. Practice pipeline configuration, execution, and troubleshooting.
6. Understand historical data processing and backfill concepts.
