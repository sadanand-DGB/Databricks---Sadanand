# Databricks Practice

This repository contains hands-on practice and learning examples for **Azure Databricks**, focusing on Lakeflow Spark Declarative Pipelines, Auto Loader, and data engineering concepts.

Repository: [Databricks---Sadanand](https://github.com/sadanand-DGB/Databricks---Sadanand)

## Repository Structure

```text
src/
├── SDP_Practice Pipeline/
│   └── my_transformation.py
├── auto_loader/
│   └── auto_loader.py
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
- Understanding the role of incremental ingestion in data pipelines.

## Technologies Used

- **Azure Databricks**
- **Apache Spark**
- **PySpark**
- **Lakeflow Spark Declarative Pipelines**
- **Auto Loader**
- **Delta Lake**
- **Python**
- **SQL**

## Learning Objectives

The objectives of this repository are to:

1. Develop practical experience with Databricks data engineering.
2. Understand batch and streaming data processing.
3. Build Bronze and Silver data transformations.
4. Learn incremental ingestion using Auto Loader.
5. Practice pipeline configuration, execution, and troubleshooting.
6. Understand historical data processing and backfill concepts.

## Notes

- These files are intended for learning and practice.
- Source paths and Unity Catalog names may need to be adjusted for your Databricks environment.
- Pipeline execution depends on available compute resources, permissions, and workspace configuration.
- Review each example's comments before executing it.

