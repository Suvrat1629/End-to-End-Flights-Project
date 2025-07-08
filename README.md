# Databricks End-to-End Flights Data Pipeline

## Overview

This project demonstrates a complete end-to-end data engineering pipeline for flight-related data using Databricks, Delta Lake, and Delta Live Tables (DLT). It follows the medallion architecture (Bronze → Silver → Gold) to ingest, process, and curate data for analytics and reporting.

## Architecture

- **Bronze Layer:** Raw, incremental ingestion of CSV data using Databricks Autoloader.
- **Silver Layer:** Cleansed, transformed, and CDC-managed tables using Delta Live Tables.
- **Gold Layer:** Curated dimension and fact tables for business analytics.

## Data Sources

The `data/` directory contains sample CSVs for:
- Airports (`dim_airports.csv`, etc.)
- Flights (`dim_flights.csv`, etc.)
- Passengers (`dim_passengers.csv`, etc.)
- Bookings (`fact_bookings.csv`, etc.)

Incremental and SCD (Slowly Changing Dimension) versions are included for simulating real-world data changes.

## Pipeline Flow

1. **Setup**
   - `Setup.py` creates required volumes and schemas in Databricks and sets up raw data directories.

2. **Bronze Layer**
   - `BronzeLayer.py` ingests raw CSV data incrementally from cloud storage into Delta tables using Databricks Autoloader.

3. **Silver Layer**
   - `DLT/dltPipelines.py` defines DLT pipelines for:
     - Staging and transforming raw data.
     - Enforcing data quality rules.
     - Managing CDC (Change Data Capture) for flights, passengers, and airports.
     - Creating business views by joining silver tables.

4. **Gold Layer**
   - `GOLD_DIMS.py` builds dimension tables (Airports, Flights, Passengers) with incremental logic and SCD handling.
   - `GOLD_FACT.py` constructs the fact table (Bookings) by joining with dimension tables and performing upserts.

## Technologies Used

- **Databricks** (Notebooks, Delta Lake, Delta Live Tables)
- **PySpark**
- **Delta Lake**
- **Python**

## File/Folder Structure
```bash
├── BronzeLayer.py         # Bronze layer ingestion logic
├── GOLD_DIMS.py           # Gold layer dimension tables logic
├── GOLD_FACT.py           # Gold layer fact table logic
├── Setup.py               # Initial setup for volumes and schemas
├── SrcParameters.py       # Parameters/configuration, if used
├── DLT/
│   └── dltPipelines.py    # DLT pipeline definitions for Silver layer
└── data/
    ├── dim_airports.csv
    ├── dim_flights.csv
    ├── dim_passengers.csv
    ├── fact_bookings.csv
    └── ... (incremental/SCD versions)
```

## How to Run

1. **Upload Data**
   - Place your CSV files in the `data/` directory or upload to the Databricks File System as needed.

2. **Run Setup**
   - Execute `Setup.py` in a Databricks notebook to create volumes, schemas, and directories.

3. **Ingest Data (Bronze Layer)**
   - Run `BronzeLayer.py` for each data source (e.g., bookings, flights, customers, airports) to ingest raw data.

4. **Process Data (Silver Layer)**
   - Deploy and run the DLT pipeline defined in `DLT/dltPipelines.py` to transform and cleanse data.

5. **Build Gold Tables**
   - Run `GOLD_DIMS.py` to create and update dimension tables.
   - Run `GOLD_FACT.py` to create and update the fact table.

6. **Query Data**
   - Use Databricks SQL or notebooks to query the curated gold tables for analytics.

## Example Use Cases

- Airline business analytics and reporting
- Data warehousing and ETL pipeline demonstration
- Teaching medallion architecture and Delta Live Tables

## Notes

- The pipeline is designed for Databricks and leverages Databricks-specific features (e.g., DLT, dbutils).
- Adjust paths and parameters as needed for your Databricks workspace.
