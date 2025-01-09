from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='simple_pipeline',
    start_date=datetime(2025, 1, 9),
    schedule_interval=None, # Run this DAG once on demand
    catchup=False,
) as dag:

    # Task 1: Start of the pipeline (e.g., data ingestion)
    start_task = BashOperator(
        task_id='start_task',
        bash_command='echo "Pipeline started!"'
    )

    # Task 2: Intermediate task (e.g., data transformation)
    intermediate_task = BashOperator(
        task_id='intermediate_task',
        bash_command='echo "Performing some data processing..."'
    )

    # Task 3: End of the pipeline (e.g., data loading)
    end_task = BashOperator(
        task_id='end_task',
        bash_command='echo "Pipeline finished!"'
    )

    # Define task dependencies
    start_task >> intermediate_task >> end_task
