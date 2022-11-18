from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator


def calculate_function(x):
    print(x ** 2)


default_args = {
    'owner': 'gero',
    'start_date': datetime(2022, 11, 1),
    'retry_delay': timedelta(minutes=5)
}

with DAG('mydag', default_args=default_args, catchup=False, schedule='0 * * * *') as dag:
    start_task = EmptyOperator(
        task_id='starttask',
        dag=dag
    )
    calculate_20 = PythonOperator(
        task_id='calculate_20',
        python_callable=calculate_function,
        op_kwargs={
            'x': 20
        },
        dag=dag)
    calculate_99 = PythonOperator(
        task_id='calculate_99',
        python_callable=calculate_function,
        op_kwargs={
            'x': 99
        },
        dag=dag)
    start_task >> [calculate_20, calculate_99]
