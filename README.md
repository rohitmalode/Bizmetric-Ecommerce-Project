# E-Commerce Order Processing Pipeline (End-to-End Data Engineering Project)

**Rohit Malode**

---

## 1. Project Overview

This project implements a scalable end-to-end data pipeline for an e-commerce platform using Azure and Databricks. The pipeline ingests raw order and product data from APIs, processes it through a Medallion Architecture (Bronze, Silver, Gold), and delivers business insights via dashboards and analytics.

The system supports:
- Medallion Architecture
- Unity Catalog
- Incremental data processing  
- Data quality transformations  
- Statistical analysis  
- End-to-end orchestration  
- BI reporting and visualization
- Flask based Website
- Machine learning  

It represents a production-like data engineering workflow using modern cloud technologies.

<img width="1408" height="768" alt="Project WorkFlow" src="https://github.com/user-attachments/assets/41267e91-fd9e-4b46-84cf-3bf6960e4ebe" />


---

## 2. Architecture Overview

### Data Flow

API (DummyJSON)  
→ Azure Data Factory (ADF)  
→ Azure Data Lake Storage Gen2 (Bronze)  
→ Databricks (Bronze → Silver → Gold)  
→ Azure SQL / Microsoft Fabric Warehouse  
→ Power BI / Databricks Dashboard  
→ Flask Frontend Application  

---

### Data Layers

#### Bronze Layer
- Raw ingestion from APIs
- Stores unprocessed JSON data

#### Silver Layer
- Data cleaning and transformation
- Handles schema standardization and null values
- Flattens nested JSON structures

#### Gold Layer
- Aggregated business-ready data
- KPI generation and analytics datasets
  
---

## 3. Technologies Used

| Category        | Tools |
|----------------|------|
| Data Ingestion  | Azure Data Factory (ADF), REST APIs |
| Storage         | Azure Data Lake Storage Gen2 |
| Processing      | Azure Databricks (PySpark) |
| Governance      | Unity Catalog |
| Warehousing     | Azure SQL / Microsoft Fabric |
| Visualization   | Power BI, Databricks Dashboards |
| Orchestration   | Azure Data Factory Pipelines |
| Backend         | Flask (Python) |
| Analytics       | Statistical Testing (ANOVA, T-Test, Chi-Square) |

---

## 4. Data Sources

- Products API: https://dummyjson.com/products  
- Carts API: https://dummyjson.com/carts  

Data Format: JSON (nested structure)

---

## 5. Data Ingestion (Bronze Layer)

- Used Azure Data Factory Copy Activity to ingest API data
- Stored raw JSON data into ADLS Gen2 Bronze container
- Created structured directories for:
  - Products
  - Carts
- Maintained metadata in a separate container

  <img width="1902" height="781" alt="Screenshot 2026-04-02 183843" src="https://github.com/user-attachments/assets/7fd05d56-f7c8-4a57-8746-a5def4789294" />


---

## 6. Data Storage Design

### ADLS Container Structure

- Bronze → Raw data  
- Silver → Cleaned data  
- Gold → Aggregated data  
- Metastore → Metadata management
  
---

## 7. Databricks & Unity Catalog

### Setup
- Configured Access Connector
- Created Service Principal authentication
- Established Unity Catalog Metastore
- Assigned admin permissions

  <img width="1887" height="803" alt="Screenshot 2026-04-07 124250" src="https://github.com/user-attachments/assets/455cb161-ed4b-4525-8984-2ebf3ee7db45" />


### Unity Catalog Advantages

- Centralized data governance  
- Fine-grained access control (row/column level security)  
- Data lineage tracking  
- Secure external data access  
- Multi-workspace data sharing  

---

## 8. Data Processing (Medallion Architecture)

### Bronze Notebook
- Reads raw JSON from ADLS
- Applies schema inference
- Stores data in Delta format

### Silver Notebook
- Handles nested JSON flattening (major challenge)
- Removes duplicates
- Handles null values
- Standardizes schema

### Gold Notebook
- Performs aggregations for analytics
- Generates KPIs:
  - Daily revenue
  - Top-selling products
  - User behavior metrics
 <img width="1197" height="782" alt="Screenshot 2026-04-03 164959" src="https://github.com/user-attachments/assets/2c30a286-9644-470f-9642-282fefb0b7ef" />
---

## 9. Incremental Data Load

Implemented incremental processing using:
- Unique identifiers (order ID / product ID)
- Timestamp-based filtering
- Processing only new or updated records

Benefits:
- Improved performance
- Reduced compute cost
- Efficient pipeline execution

---

## 10. Orchestration (ADF Pipeline)

Pipeline consists of:

- 2 Copy Activities (API → ADLS)
- Databricks Notebook Activities:
  - Bronze processing
  - Silver processing
  - Gold processing

Features:
- Dependency chaining
- Automated workflow execution
- End-to-end orchestration

  <img width="1902" height="781" alt="Screenshot 2026-04-02 183843" src="https://github.com/user-attachments/assets/a5874dfc-f146-410d-8b68-d62f86498266" />


---

## 11. Data Warehousing (Fabric Integration)

Two approaches used:
- Mirroring
- Dataflow integration

Gold layer data is loaded into:
- Lakehouse
- Warehouse

  <img width="1656" height="799" alt="Screenshot 2026-04-05 190923" src="https://github.com/user-attachments/assets/16ecfcbf-d129-4e83-baf6-869852162e2d" />


---

## 12. Dashboard & Visualization

### Databricks Dashboard
- Pipeline monitoring
- KPI visualization
- Data validation metrics

### Power BI Dashboard
- Revenue trends
- Product performance analysis
- Customer insights
- Two-page business report

<img width="1147" height="645" alt="Power Bi 1st Main" src="https://github.com/user-attachments/assets/9899f201-7578-4342-8854-17ab47f3bd8d" />
<img width="1200" height="674" alt="Power Bi 2nd page" src="https://github.com/user-attachments/assets/2fe0e0c3-9187-4560-861c-c87878942ee8" />
<img width="1657" height="792" alt="Databricks Dashboard" src="https://github.com/user-attachments/assets/5c6b8417-1adf-4d0c-a67d-9e1c9de32185" />

---

## 13. Logging & Monitoring

- Created dedicated logging notebook
- Captured pipeline execution logs
- Implemented debugging and tracking mechanisms

<img width="920" height="468" alt="Screenshot 2026-04-07 111818" src="https://github.com/user-attachments/assets/316f0d61-fa1c-4793-abbf-e230f1163053" />

---

## 14. Statistical Analysis

Applied statistical methods to derive insights:

### ANOVA Test
Used to analyze differences in cart totals across categories.

### T-Test
Used to compare cart totals vs discounted totals.

### Chi-Square Test
Used to analyze relationship between product category and availability.

### Conclusion
These tests help identify:
- Category performance differences  
- Discount impact on spending  
- Inventory dependency patterns  

---

## 15. Frontend Application (Flask)

### Features
- User login system
- Face recognition-based authentication (ML model)
- Navigation dashboard:
  - Project overview
  - Analytics
  - Dashboards

<img width="1891" height="812" alt="Frontend Login Page" src="https://github.com/user-attachments/assets/44b6d027-f833-48fb-b415-5d46e29556e6" />
<img width="1903" height="807" alt="Screenshot 2026-04-06 224737" src="https://github.com/user-attachments/assets/68499f84-3009-4342-9d9a-71861c7c14fb" />
<img width="1872" height="815" alt="Frontend Project Overview" src="https://github.com/user-attachments/assets/82d09129-dbb1-47ec-a925-1e5956bb949f" />
<img width="1538" height="868" alt="Screenshot 2026-04-06 224819" src="https://github.com/user-attachments/assets/38a7a3a2-2662-49ca-822e-effb7bcfba0e" />

---

## 16. Automation Enhancement

- Implemented ADF pipeline trigger
- Integrated email notification using Outlook
- Success alerts sent after pipeline execution
- Automated ETL workflow monitoring

<img width="861" height="436" alt="Screenshot 2026-04-05 190943" src="https://github.com/user-attachments/assets/5ecd65a2-fb42-49ed-944a-3c8d7b0e7077" />

---

## 17. Challenges Faced

### 1. Flattening Nested JSON
- Complex hierarchical API structures
- Solved using PySpark explode and struct functions

### 2. Incremental Loading
- Avoiding duplicate processing
- Designed efficient filtering logic using timestamps and IDs

---

## 18. Future Enhancements

- Migration to Microsoft Fabric end-to-end
- Sentiment analysis on product reviews
- Sales forecasting using ML models
- Event-based triggers for real-time pipelines
- Streaming ingestion using Kafka / Event Hubs

---

## 19. Key Achievements

- Built production-like data engineering pipeline
- Implemented Medallion Architecture
- Achieved incremental data processing
- Integrated multiple Azure services
- Developed BI dashboards and analytics layer
- Built ML-based face recognition login system
- Performed statistical hypothesis testing

---

## 20. Conclusion

This project demonstrates strong expertise in:

- End-to-end data engineering workflows
- Cloud-based architecture design
- Data transformation using PySpark
- Pipeline orchestration using Azure Data Factory
- Business intelligence and analytics
- Machine learning integration
- Flask-based application development
- Statistical analysis for business insights

It reflects a real-world scalable, maintainable, and production-ready data engineering solution.
