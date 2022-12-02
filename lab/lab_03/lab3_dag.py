from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator

from timeline import create_timeline_figure

default_args = {
    'owner': 'gero',
    'start_date': datetime(2022, 11, 1),
    'retry_delay': timedelta(minutes=5)
}

with DAG('lab_3', default_args=default_args, catchup=False, schedule='* * * * *') as dag:
    start_task = EmptyOperator(
        task_id='starttask',
        dag=dag
    )
    create_figure = PythonOperator(
        task_id='create_timeline_figure',
        python_callable=create_timeline_figure,
        dag=dag
    )
    start_task >> create_figure
