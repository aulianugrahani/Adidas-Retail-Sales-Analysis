# Adidas Retail Sales Performance Analysis

## Repository Outline

P2-M3/aulia-putri
|
├── description.md                      : Full project overview: background, objectives, methods, etc.
├── P2M3_aulia_putri_ddl.txt            : Dataset Link, Syntax DDL and DML PostgreSQL
├── P2M3_aulia_putri_data_raw.csv       : Original raw dataset from Kaggle (2020–2021 Adidas sales)
├── P2M3_aulia_putri_data_clean.csv     : Cleaned dataset after preprocessing
├── P2M3_aulia_putri_DAG.py             : Airflow DAG script automating the ETL process
├── P2M3_aulia_putri_DAG_graph.jpg      : DAG visual representation (task flow)
├── P2M3_aulia_putri_conceptual.txt     : High-level data pipeline concept and flow explanation
├── P2M3_Aulia-Putri_GX.ipynb           : Great Expectations notebook for data validation
├── /images                             : Folder containing visual outputs and dashboard plots
│   ├── introduction_objective.png      : Project background and goal visualization
│   ├── plot_01_profit_total.png        : Profit Total plot
│   ├── plot_02_total_sales.png         :Total Sales plot
│   ├── plot_03_avg_sales_by_state.png  : Average Total Sales by State
│   ├── plot_04_top_retailers.png       : Top Retailers by Units Sold
│   ├── plot_05_monthly_profit.png      : Monthly Operating Profit
│   ├── plot_06_sales_method.png        : Sales Method Distribution
│   ├── plot_07_top_products.png        : Top Products by Operating Profit
│   └── plot_08_top_state_profit.png    : Top State by Operating Profit


## Problem Background
Since its establishment in 1954, Adidas has grown into a global household name in the athletic and lifestyle apparel industry. As a leading brand, Adidas operates in highly competitive markets and must continuously adapt to changing trends, consumer behavior, and technological advancements.

The retail landscape in the United States, in particular, has experienced rapid transformation due to the rise of e-commerce, increased competition, and shifts in customer expectations. For companies like Adidas, success depends on effectively analyzing sales performance across regions, product categories, and retail channels.

This project focuses on analyzing Adidas’s U.S. sales data to better understand the key drivers of revenue and profitability, and to provide insights that can support strategic business decisions.

## Project Output
The output of this project is a comprehensive analysis of Adidas US sales data from 2020 to 2021, presented through a series of visualizations and summary insights. The analysis is supported by a dashboard built using Elasticsearch and Kibana, which displays key performance metrics across products, regions, and retail channels.

Key visual outputs include:
1. Total Profit
2. Total Sales
3. Average Total Sales by State
4. Top Retailers by Units Sold
5. Monthly Operating Profit
6. Sales Method Distribution
7. Top Products by Operating Profit
8. Top State by Operating Profit

These visualizations provide stakeholders with a clear understanding of sales trends, regional performance, product profitability, and channel effectiveness, enabling data-driven decision-making across business functions.

## Data
The dataset used in this project is sourced from Kaggle: Adidas Sales Dataset. It contains Adidas sales transaction records from various states in the US and retail channels during the period of 2020 to 2021. The dataset consists of approximately 10,000 rows and includes the following columns:

- Retailer
- Retailer ID
- Invoice Date
- Region
- State
- City
- Product
- Price per Unit
- Units Sold
- Total Sales
- Operating Profit
- Operating Margin
- Sales Method

Retailers represented in the dataset include: Foot Locker, Walmart, Sports Direct, West Gear, Kohl's, and Amazon.

There are no duplicate rows. A single missing value was found in the City column and was removed during preprocessing, as it occurred at random and did not impact the analysis. The dataset required minimal cleaning and was ready for use in analysis and visualization.

Link: https://www.kaggle.com/datasets/heemalichaudhari/adidas-sales-dataset

## Method
This project follows a structured data pipeline approach using Apache Airflow for task automation, PostgreSQL for data storage, and Elasticsearch for data indexing. The dataset undergoes a complete ETL (Extract, Transform, Load) process with the following methods:
1. Data Extraction
The raw dataset is first inserted into a PostgreSQL table named table_m3. Data is extracted from this database using Python.

2. Data Cleaning
Cleaning is performed in Python, which includes:
- Removing duplicate records
- Normalizing column names (changing column names to lowercase and replacing spaces with underscores)
- Handling missing values
- The cleaned dataset is saved as a CSV file.

3. Data Validation
The cleaned data is validated using Great Expectations. Seven expectations are applied, including checks for uniqueness, value range, valid types, and others.

4. Data Loading
The validated, clean data is then loaded into Elasticsearch for visualization in Kibana.

5. EDA and Visualization
Exploratory Data Analysis (EDA) is conducted using various plots to generate insights relevant to the business objective. Visualizations are built in Kibana, accompanied by narratives and recommendations.

All the above processes are orchestrated using Apache Airflow DAGs scheduled weeklyn every Saturday at 09:10, 09:20, and 09:30 AM, starting from November 2nd, 2024, and repeating weekly.

## Stacks
This project utilizes a combination of programming languages, tools, and Python libraries to build a complete data pipeline, from extraction to visualization. Below are the main stacks used:

1. Programming Language:
- Python 3.12.2 (main development)
- Python 3.9.6 (Great Expectations environment)

2. Tools:
- PostgreSQL: Relational database used to store the raw dataset.
- Apache Airflow: Workflow management platform used to orchestrate the ETL pipeline with custom DAGs.
- Elasticsearch: NoSQL search engine used to index the cleaned data for fast querying.
- Kibana: Visualization tool used to build dashboards and perform Exploratory Data Analysis (EDA).

3. Python Libraries:
- Pandas: For data manipulation and cleaning.
- Great Expectations: For validating data quality through automated data checks. (0.18.19)
- psycopg2: To connect and interact with the PostgreSQL database.
- elasticsearch: To send data from Python into Elasticsearch.

These stacks together form an end-to-end system that supports data ingestion, transformation, validation, and insightful analysis through dashboards.

## Reference
https://www.adidas-group.com/en/media/press-releases/adidas-delivers-strong-results-in-2021-and-expects-double-digit-sales-growth-in-2022