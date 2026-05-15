# Retail Sales Data Warehouse POC

This project implements a data warehouse for retail sales using a star schema design. The ETL pipeline is built in Python, where data is ingested from CSV files, validated to prevent duplicates, and then loaded into PostgreSQL tables. Deduplication is handled both at the application level and database level using SELECT checks and unique constraints. This ensures data integrity and makes the pipeline idempotent and production-ready.

This project demonstrates the implementation of a Retail Sales Data Warehouse using:

Python (ETL scripts)
PostgreSQL (Data Warehouse)
SQL (Data modeling & transformations)
CSV files (Source data)

The system loads, cleans, and organizes retail data into a star schema, enabling efficient analytics and reporting.

Architecture
Source Data (CSV)
        ↓
   Python ETL (Ingestion + Validation)
        ↓
   PostgreSQL Data Warehouse
        ↓
   Dimension Tables + Fact Table


Data Model (Star Schema)
Dimension Tables:
dim_product
dim_customer
dim_store
dim_date

Fact Table:fact_sales

ETL Process
Step 1: Data Ingestion

Data is read from CSV files using Python (csv.DictReader)
Represents the Extract phase

Step 2: Validation & Deduplication

Each record is checked against the database
If record exists → skipped
If not → inserted

Example:
SQLSELECT 1 FROM dim_product WHERE product_name = %s   AND category = %s   AND subcategory = %s   AND unit_price = %s;Show more lines

Step 3: Data Loading

Clean data is inserted into dimension/fact tables
Ensures no duplicate records


Duplicate Handling Strategy
This project uses two-level duplicate prevention:
1. Python-level validation

Checks existing records before insert

2. Database-level constraints
SQLUNIQUE (product_name, category, subcategory, unit_price)Show more lines

 How to Run
activate environment
installed dependencies---
pip install pandas sqlalchemy psycopg2-binary python-dotenv--- These libraries enable Extract, Transform, and Load (ETL) into PostgreSQL.**

pandas is used for data extraction and transformation,sqlalchemy acts as a database abstraction and SQL execution layer.,This is the PostgreSQL database driver for Python.python-dotenv is used for secure configuration management.


pip install pytest great-expectations--- These libraries ensure data correctness and quality assurance.

pytest is a testing framework used for validating ETL outcomes, great-expectations is a data quality and validation framework.,


How ETL Connects to PostgreSQL
Key Connector
ETL connects to PostgreSQL using:

Python database drivers (e.g., psycopg2)
Standard PostgreSQL connection parameters

3. Open PostgreSQL (psql Shell)--  & "C:\Program Files\PostgreSQL\16\bin\psql.exe" -U postgres

we'll get postgre=# then we have to give this cmd


4.Create Database


CREATE DATABASE retail_dw;


5.Connect to Database

\c retail_dw


6.Create Tables (DDL)

\i database/ddl/dim_date.sql
\i database/ddl/dim_customer.sql
\i database/ddl/dim_product.sql
\i database/ddl/dim_store.sql
\i database/ddl/fact_sales.sql

then quit\q

SQL files only define the schema, but tables are created only when that SQL is executed in PostgreSQL

Writing SQL files only defines the schema logically, but tables are physically created only when the SQL is executed in PostgreSQL.
 
Creating tables in project code does NOT mean they exist in the PostgreSQL database.
Tables exist only after they are executed in PostgreSQL.


7.Verify Tables-- & "C:\Program Files\PostgreSQL\16\bin\psql.exe" -U postgres -d retail_dw -c "\dt" ------- one o/p

It's a star‑schema data warehouse, consisting of: dim_customer, dim_date, dim_product, dim_store, fact_sales

CSV source data is extracted, Transformed using Python, Loaded via SQL scripts, Stored in relational tables



8.Load Dimension Tables (Python ETL) -------2 0/p

python -m etl.python.load_dim_date

→ Runs the ETL script that loads and populates the Date dimension table in the data warehouse.


python -m etl.python.load_dim_customer

→ Executes the ETL process to load customer master data into the Customer dimension.


python -m etl.python.load_dim_product

→ Loads cleaned and transformed product data into the Product dimension table.


python -m etl.python.load_dim_store

→ Inserts and updates store-related data into the Store dimension for analysis.

9. Load Fact Table

python -m etl.python.load_fact_sales - This runs the ETL process that loads transactional sales data into the Fact Sales table in the data warehouse.
10: Validate Data Load

& "C:\Program Files\PostgreSQL\16\bin\psql.exe" -U postgres -d retail_dw

Inside psql, run:

& "C:\Program Files\PostgreSQL\16\bin\psql.exe" -U postgres -d retail_dw
→ Opens a PostgreSQL terminal session by connecting to the retail_dw database using the postgres user.


SELECT COUNT(*) FROM dim_customer;
→ Verifies how many customer records were successfully loaded into the Customer dimension table.


SELECT COUNT(*) FROM dim_product;
→ Checks the total number of product records in the Product dimension table.


SELECT COUNT(*) FROM dim_store;
→ Confirms the number of store entries loaded in the Store dimension table.


SELECT COUNT(*) FROM fact_sales;
→ Validates the total number of sales transactions loaded into the Fact table.


SELECT SUM(sales_amount) FROM fact_sales;
→ Ensures the accuracy of total revenue by summing all sales amounts in the Fact table.


\q
→ Exits the PostgreSQL psql session.

11. run analytics queries

& "C:\Program Files\PostgreSQL\16\bin\psql.exe" -U postgres -d retail_dw

\i analytics/sql/sales_by_month.sql
this output represents a monthly time‑based aggregation of retail sales, showing the total sales amount for January 2024 derived by summarizing all transactional sales records for that month.

\i analytics/sql/top_products.sql
This output shows a product‑wise sales aggregation, identifying the top‑revenue products by summing total sales revenue for each product and ranking them accordingly.

\i analytics/sql/store_performance.sql
This output represents store‑wise sales aggregation, showing the total revenue generated by each store by summing all sales transactions per store.

\q



Technologies Used

Python
PostgreSQL
SQL
CSV


Key Concepts Implemented

ETL (Extract, Transform, Load)
Data Ingestion
Data Validation
Deduplication
Surrogate Keys
Star Schema



