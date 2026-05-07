from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime
import pandas as pd


DATA_PATH = "/opt/airflow/data/loan_prediction_dataset.csv"
CLEAN_PATH = "/opt/airflow/data/cleaned_loan_data.csv"
FINAL_PATH = "/opt/airflow/data/final_loan_data.csv"



def collect_data():
    import os
    print("Files in data folder:", os.listdir("/opt/airflow/data"))

    data = pd.read_csv(DATA_PATH)
    print(f"Data loaded successfully: {data.shape}")



def process_data():
    data = pd.read_csv(DATA_PATH)

    # Convert categorical column
    data = pd.get_dummies(data, columns=['Employment_Status'])

    data.to_csv(CLEAN_PATH, index=False)
    print("Categorical encoding done and saved")


def store_data():
    

    data = pd.read_csv(CLEAN_PATH)
    data.to_csv(FINAL_PATH, index=False)

    print("Final data stored successfully")


# -------------------------
# DAG Definition
# -------------------------
with DAG(
    dag_id="loan_data_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False
) as dag:

    t1 = PythonOperator(
        task_id="collect_data",
        python_callable=collect_data
    )

    t2 = PythonOperator(
        task_id="process_data",
        python_callable=process_data
    )

    t3 = PythonOperator(
        task_id="store_data",
        python_callable=store_data
    )

    t1 >> t2 >> t3