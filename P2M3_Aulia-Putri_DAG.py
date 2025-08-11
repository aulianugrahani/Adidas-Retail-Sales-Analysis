"""
=================================================
Milestone 3

Name  : Aulia Putri Nugrahani
Batch : FTDS-029-HCK

This program is designed to automate the transformation and loading of data from PostgreSQL to Elasticsearch.  
The dataset used in this project represents Adidas US sales data, containing sales transactions across various states, product types, and retail partners.  
=================================================
"""


# ==== Import Libraries ====
from datetime import datetime
from sqlalchemy import create_engine
from airflow import DAG
from airflow.decorators import task
from airflow.operators.empty import EmptyOperator
from airflow.models import Variable
import pandas as pd
from elasticsearch import Elasticsearch

# ==== DAG Default Configuration ====
default_args= {
    'owner': 'Aulia',
    'start_date': datetime(2024, 6, 1)
}

with DAG(
    dag_id='etl_csv_files',
    description='Extract data from PostgreSQL and clean it',
    schedule_interval='10,20,30 9 * * 6',
    default_args=default_args, 
    catchup=False
    ) as dag:

    start = EmptyOperator(task_id='start')

    @task()
    def extract_from_db():
        '''
        This function extracts raw data from a PostgreSQL database and saves it as a CSV file.

        Process:
        - Establishes a connection to PostgreSQL using SQLAlchemy
        - Reads all records from the table `table_m3`
        - Saves the raw data to a local CSV file

        Parameters:
        None

        Returns:
        None (writes data to /opt/airflow/data/P2M3_Aulia-Putri_data_raw.csv)

        Example usage:
        extract_from_db()
        '''
        database = "data_from_airflow"
        username = "airflow_user"
        password = "airflow_password"
        host = "host.docker.internal"
        port = "5434"

        postgres_url = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"

        engine = create_engine(postgres_url)
        conn = engine.connect()

        df = pd.read_sql('SELECT * FROM table_m3', conn) 

        df.to_csv('/opt/airflow/data/P2M3_Aulia-Putri_data_raw.csv', index=False)
        print("Success EXTRACT")


    @task()
    def preprocess_data():
        '''
        This function cleans the raw data by applying several preprocessing steps
        and then saves the cleaned data to a CSV file.

        Process:
        - Reads data from PostgreSQL
        - Converts column names to lowercase and replaces spaces with underscores
        - Drops rows with missing values
        - Removes duplicate rows
        - Saves the cleaned data to a new CSV file

        Parameters:
        None

        Returns:
        None (writes data to /opt/airflow/data/P2M3_Aulia-Putri_data_cleaned.csv)

        Example usage:
        preprocess_data()
        '''
        # Buat koneksi baru ke database
        database = "data_from_airflow"
        username = "airflow_user"
        password = "airflow_password"
        host = "host.docker.internal"
        port = "5434"

        postgres_url = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
        engine = create_engine(postgres_url)
        conn = engine.connect()

        
        # Connect and read from table_3
        df = pd.read_sql('SELECT * FROM table_m3', conn)

        #Rename columns to lowercase
        df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

        # Drop rows with any missing values
        df.dropna(inplace=True)

        # Remove duplicates
        df.drop_duplicates(inplace=True)

        # Any other preprocessing steps can be added here

        print("Preprocessed data is Success")
        print(df.head())
        df.to_csv('/opt/airflow/data/P2M3_Aulia-Putri_data_cleaned.csv', index=False)


    @task()
    def load_to_elasticsearch():
        '''
        This function loads the cleaned data into an Elasticsearch index.

        Process:
        - Reads the cleaned CSV file
        - Iterates through each row of the DataFrame
        - Inserts each row as a document into the Elasticsearch index "frompostgresql"

        Parameters:
        None

        Returns:
        None (loads data to Elasticsearch)

        Example usage:
        load_to_elasticsearch()
        '''
        
        # Use correct host for Docker network
        es = Elasticsearch(["http://elasticsearch:9200"])

        df = pd.read_csv('/opt/airflow/data/P2M3_Aulia-Putri_data_cleaned.csv')

        for i, row in df.iterrows():
            res = es.index(index="frompostgresql", id=i+1, body=row.to_dict())
            print(res['result'])

    
    end = EmptyOperator(task_id='end')

    # DAG task flow
    start >> extract_from_db() >> preprocess_data() >> load_to_elasticsearch() >> end






