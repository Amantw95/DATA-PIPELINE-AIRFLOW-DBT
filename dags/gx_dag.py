from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from great_expectations_provider.operators.great_expectations import GreatExpectationsOperator
from include.constants import DBT_EXECUTABLE_PATH, DBT_PROJECT_PATH


AIRFLOW_DB_CONN_ID = "postgres_default"
MY_GX_DATA_CONTEXT = "include/gx"
PROJECT_PATH = "data-pipeline-airflow-dbt/dags/dbt/demo_dbt_project"
PROFILES_PATH = f"{os.environ['AIRFLOW_HOME']}/dags/dbt/demo_dbt_project"

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 11, 30),
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'dbt_gx_dag',
    default_args=default_args,
    description='A DAG for running dbt and Great Expectations tasks',
    schedule_interval='@daily',
)

# Task to run dbt seed
dbt_seed_task = BashOperator(
    task_id='dbt_seed',
    bash_command=f"{DBT_EXECUTABLE_PATH} seed --project-dir {DBT_PROJECT_PATH} --profiles-dir {PROFILES_PATH}",
    dag=dag,
)

# Task to run dbt run
dbt_run_task = BashOperator(
    task_id='dbt_run',
    bash_command=f"{DBT_EXECUTABLE_PATH} run --project-dir {DBT_PROJECT_PATH} --profiles-dir {PROFILES_PATH}",
    dag=dag,
)

# Task to run Great Expectations tests
gx_test_task = GreatExpectationsOperator(
    task_id='gx_test',
    conn_id=AIRFLOW_DB_CONN_ID,
    data_context_root_dir=MY_GX_DATA_CONTEXT,
    schema="postgres",
    data_asset_name="customers",
    expectation_suite_name="customers_suite",
    run_name="{{ ds_nodash }}",  # Assuming you want to run a separate test for each day
    dag=dag,
)

# Define your other tasks here...

# Define task dependencies
dbt_seed_task >> dbt_run_task >> gx_test_task
# Set up dependencies for other tasks...

if __name__ == "__main__":
    dag.cli()

 