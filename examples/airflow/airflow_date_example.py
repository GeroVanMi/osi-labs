from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from pathlib import Path


def save_current_date():
    # Saves the current date to ~/last_date.txt
    with open(str(Path.home()) + "/last_date.txt", mode='w') as file:
        now = datetime.now()
        file.write(now.strftime("%Y-%m-%d %H:%M:%S"))


# Default parameters for the workflow
default_args = {
    'depends_on_past': False,
    'owner': 'airflow',
    'start_date': datetime(2022, 11, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
        'date_example_dag',
        default_args=default_args,
        catchup=False,
        schedule='* * * * *'
) as dag:
    start_task = EmptyOperator(
        task_id='start_task',
        dag=dag
    )

    save_date_task = PythonOperator(
        task_id='save_date',
        python_callable=save_current_date,
        dag=dag
    )

    start_task >> save_date_task
