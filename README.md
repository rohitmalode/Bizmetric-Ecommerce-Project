# Bizmetric E-Commerce Data Engineering Project

## Overview

This project is an end-to-end data engineering and analytics solution built on Microsoft Azure and Databricks. It implements a complete data pipeline using Medallion Architecture (Bronze, Silver, Gold) and integrates data ingestion, transformation, analytics, machine learning experiments, and visualization.

The system processes e-commerce data (Products and Carts) ingested via APIs, stored in Azure Data Lake Storage Gen2, transformed using Databricks, and visualized using Power BI dashboards. A Flask-based frontend application is also developed with authentication and data interaction capabilities.

---

## Architecture

The project follows a modern cloud-based data engineering architecture:

1. Data Ingestion
   - Azure Data Factory (ADF) pulls data from APIs (Products and Carts)
   - Data is stored in Azure Data Lake Storage Gen2 (Bronze Layer)

2. Data Processing (Medallion Architecture)
   - Bronze Layer: Raw ingested JSON data
   - Silver Layer: Cleaned, transformed, and structured data
   - Gold Layer: Aggregated business-ready data

3. Data Transformation
   - Databricks notebooks using PySpark
   - Incremental load handling for new incoming data
   - Data quality checks and validation

4. Data Governance
   - Unity Catalog used for centralized governance and access control
   - External locations configured for secure access to ADLS

5. Analytics and Visualization
   - Databricks dashboards for exploratory analysis
   - Power BI dashboards for business reporting

6. Application Layer
   - Flask web application with login system
   - Face recognition-based authentication using machine learning
   - Data upload and analytics interface

---

## Project Workflow

1. API data ingestion using Azure Data Factory
2. Storage in ADLS Gen2 (Bronze layer)
3. Data transformation using Databricks notebooks
4. Structured data stored in Silver layer
5. Business-level aggregations stored in Gold layer
6. Statistical analysis performed using Python notebooks
7. Power BI dashboards created from Gold layer data
8. Flask application developed for user interaction
9. Orchestration handled via ADF pipelines and Databricks jobs

---

## Technologies Used

- Microsoft Azure Data Factory
- Azure Data Lake Storage Gen2
- Databricks (PySpark, SQL)
- Unity Catalog
- Python (Pandas, NumPy, SciPy, Scikit-learn)
- Power BI
- Flask
- HTML, CSS, JavaScript
- Machine Learning (Face Recognition)

---

## Medallion Architecture

### Bronze Layer
- Raw JSON data from APIs
- Stored without transformation
- Used for auditing and replayability

### Silver Layer
- Cleaned and standardized datasets
- Removed duplicates and null handling
- Structured schema applied

### Gold Layer
- Aggregated business metrics
- Used for dashboards and reporting
- Optimized for analytics queries

---

## Key Features

- End-to-end data pipeline implementation
- API-based data ingestion
- Incremental data loading mechanism
- Medallion architecture design
- Statistical hypothesis testing (t-test, ANOVA, Chi-square)
- Logging and monitoring implementation
- Face recognition authentication system
- Interactive dashboards using Power BI
- Flask-based web interface for data interaction

---

## Statistical Analysis

The project includes statistical experiments:
- T-test for comparing means
- ANOVA for multi-group comparison
- Chi-square test for categorical relationships

These analyses help validate data relationships and business hypotheses.

---

## Challenges Faced

- Handling nested JSON structures from API responses
- Implementing incremental data loading in Databricks
- Ensuring data consistency across Medallion layers
- Managing schema evolution in Delta tables
- Orchestrating multi-step pipelines in ADF

---

## Future Enhancements

- Migration of entire pipeline to Microsoft Fabric
- Real-time streaming ingestion using event-based triggers
- Sentiment analysis on customer reviews
- Sales and demand forecasting using machine learning models
- Advanced monitoring and alerting system
- API-based real-time dashboard updates

---

## Project Structure
