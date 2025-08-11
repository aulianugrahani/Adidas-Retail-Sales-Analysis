# Adidas Retail Sales Performance Analysis

## Repository Outline  
- `description.md` : Full project overview (background, objectives, methods, etc.)  
- `P2M3_aulia_putri_ddl.txt` : Dataset link, syntax DDL and DML for PostgreSQL  
- `P2M3_aulia_putri_data_raw.csv` : Original raw dataset from Kaggle (2020–2021 Adidas sales)  
- `P2M3_aulia_putri_data_clean.csv` : Cleaned dataset after preprocessing  
- `P2M3_aulia_putri_DAG.py` : Airflow DAG script automating the ETL process  
- `P2M3_aulia_putri_DAG_graph.jpg` : DAG visual representation (task flow)  
- `P2M3_aulia_putri_conceptual.txt` : High-level data pipeline concept and flow explanation  
- `P2M3_Aulia-Putri_GX.ipynb` : Great Expectations notebook for data validation  
- `/images` : Folder containing visual outputs and dashboard plots, including:  
  - `introduction_objective.png`  
  - `plot_01_profit_total.png`  
  - `plot_02_total_sales.png`  
  - `plot_03_avg_sales_by_state.png`  
  - `plot_04_top_retailers.png`  
  - `plot_05_monthly_profit.png`  
  - `plot_06_sales_method.png`  
  - `plot_07_top_products.png`  
  - `plot_08_top_state_profit.png`  

## Problem Background  
Since its establishment in 1954, Adidas has grown into a global household name in the athletic and lifestyle apparel industry. As a leading brand, Adidas operates in highly competitive markets and must continuously adapt to changing trends, consumer behavior, and technological advancements.

The retail landscape in the United States has undergone rapid transformation due to the rise of e-commerce, increased competition, and shifts in customer expectations. For companies like Adidas, success depends on effectively analyzing sales performance across regions, product categories, and retail channels.

This project focuses on analyzing Adidas’s U.S. sales data to better understand key drivers of revenue and profitability, providing insights that support strategic business decisions.

## Project Output  
The project delivers a comprehensive analysis of Adidas US sales data (2020–2021) through visualizations and summary insights, supported by a dashboard built using Elasticsearch and Kibana.

Key visual outputs include:  
- Total Profit  
- Total Sales  
- Average Total Sales by State  
- Top Retailers by Units Sold  
- Monthly Operating Profit  
- Sales Method Distribution  
- Top Products by Operating Profit  
- Top State by Operating Profit  

These visualizations enable stakeholders to understand sales trends, regional performance, product profitability, and channel effectiveness, facilitating data-driven decision-making.

## Data  
The dataset is sourced from Kaggle: [Adidas Sales Dataset](https://www.kaggle.com/datasets/heemalichaudhari/adidas-sales-dataset) and contains:  
- ~10,000 rows of Adidas sales transactions across various U.S. states and retail channels (2020–2021)  
- Columns including Retailer, Retailer ID, Invoice Date, Region, State, City, Product, Price per Unit, Units Sold, Total Sales, Operating Profit, Operating Margin, and Sales Method  
- Retailers include Foot Locker, Walmart, Sports Direct, West Gear, Kohl’s, and Amazon  
- No duplicate rows; one missing `City` value removed during preprocessing  

## Method  
The project implements a structured data pipeline using Apache Airflow, PostgreSQL, Elasticsearch, and Kibana.  

**Steps:**  
- Data Extraction: Raw data inserted into PostgreSQL (`table_m3`) and extracted with Python  
- Data Cleaning: Duplicate removal, column normalization, missing value handling, saved as clean CSV  
- Data Validation: Performed with Great Expectations applying seven data quality checks  
- Data Loading: Validated data loaded into Elasticsearch for indexing and querying  
- EDA & Visualization: Conducted in Kibana with supporting narratives  

The entire pipeline is automated by Apache Airflow DAGs scheduled weekly on Saturdays at 09:10, 09:20, and 09:30 AM starting November 2, 2024.

## Stacks  

**Programming Languages**  
- Python 3.12.2 (main development)  
- Python 3.9.6 (Great Expectations environment)  

**Tools**  
- PostgreSQL (relational database)  
- Apache Airflow (workflow orchestration)  
- Elasticsearch (search and indexing)  
- Kibana (visualization and dashboarding)  

**Python Libraries**  
- pandas (data manipulation)  
- Great Expectations (data validation, v0.18.19)  
- psycopg2 (PostgreSQL connector)  
- elasticsearch (Elasticsearch Python client)  

## Reference  
- [Adidas Delivers Strong Results in 2021 and Expects Double-Digit Sales Growth in 2022](https://www.adidas-group.com/en/media/press-releases/adidas-delivers-strong-results-in-2021-and-expects-double-digit-sales-growth-in-2022)
