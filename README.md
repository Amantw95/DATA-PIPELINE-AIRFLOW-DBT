Overview
========

Welcome to our introductory demo project using DBT and Airflow. This project is a simple and practical way to get started with data pipelines, providing a real-world feel. It's designed as a foundational experience for our data testing course.

Pre-Requisites
================
* Python
* Docker
* Astro CLI
* VSCode

Installation
================
1. Astro CLI:
To Install Astro CLI, run below command:

    ```brew install astro```

2. Required Dependencies:
To Install Required Dependencies CLI, run below command:

    ```pip install -r requirements.txt```

Project Contents
================

This project contains the following files and folders:

- dags: This folder contains the Python files for your Airflow DAGs. By default, this directory includes two example DAGs:
    - `demo_dag`[data-pipeline-airflow-dbt/dags/demo_dag.py]: This Airflow DAG, labeled simple_dag, is purpose-built for orchestrating and running tasks with DBT (Data Build Tool). Utilizing the DbtDag class from the cosmos module, the DAG seamlessly incorporates project and profile configurations. In execution, Airflow employs the specified settings and operator arguments to seamlessly initiate DBT tasks within the workflow, ensuring a streamlined and efficient data processing pipeline.
    - `gx_dag`[data-pipeline-airflow-dbt/dags/demo_dag.py]: This Airflow DAG, 'dbt_gx_dag', automates the execution of dbt (data build tool) and Great Expectations tasks. It schedules daily runs for dbt seed and dbt run operations, followed by Great Expectations tests on a PostgreSQL database. The DAG ensures data reliability and quality in analytics workflows, contributing to a robust data pipeline.

- Dockerfile: This file contains a versioned Astro Runtime Docker image that provides a differentiated Airflow experience. If you want to execute other commands or overrides at runtime, specify them here.
- include: This folder contains any additional files that you want to include as part of your project. It is empty by default.
- packages.txt: Install OS-level packages needed for your project by adding them to this file. It is empty by default.
- requirements.txt: Install Python packages needed for your project by adding them to this file. It is empty by default.
- plugins: Add custom or community plugins for your project to this file. It is empty by default.
- airflow_settings.yaml: Use this local-only file to specify Airflow Connections, Variables, and Pools instead of entering them in the Airflow UI as you develop DAGs in this project.

Run Your Project Locally
===========================

1. Start Airflow on your local machine by running 'astro dev start'.

This command will spin up 4 Docker containers on your machine, each for a different Airflow component:

- Postgres: Airflow's Metadata Database
- Webserver: The Airflow component responsible for rendering the Airflow UI
- Scheduler: The Airflow component responsible for monitoring and triggering tasks
- Triggerer: The Airflow component responsible for triggering deferred tasks

2. Verify that all 4 Docker containers were created by running 'docker ps'.

Note: Running 'astro dev start' will start your project with the Airflow Webserver exposed at port 8080 and Postgres exposed at port 5432. If you already have either of those ports allocated, you can either [stop your existing Docker containers or change the port](https://docs.astronomer.io/astro/test-and-troubleshoot-locally#ports-are-not-available).

3. Access the Airflow UI for your local Airflow project. To do so, go to http://localhost:8080/ and log in with 'admin' for both your Username and Password.

You should also be able to access your Postgres Database at 'localhost:5432/postgres'.

