from cosmos import DbtDag, ProjectConfig
from datetime import datetime

from include.constants import DBT_EXECUTABLE_PATH, DBT_PROJECT_PATH, venv_execution_config
from include.profiles import airflow_db

simple_dag = DbtDag(
    project_config=ProjectConfig(str(DBT_PROJECT_PATH)),
    profile_config=airflow_db,
    execution_config=venv_execution_config,
    operator_args={
        "dbt_executable_path": str(DBT_EXECUTABLE_PATH),
    },
    start_date=datetime(2023, 11, 30),
    schedule_interval="@daily",
    catchup=False,
    dag_id = "simple_dag",
    
)

