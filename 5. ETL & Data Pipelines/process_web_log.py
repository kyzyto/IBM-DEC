# import the libraries

from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to write tasks!
from airflow.operators.bash_operator import BashOperator
# This makes scheduling easy
from airflow.utils.dates import days_ago


#defining DAG arguments

# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'Kizito Okoye',
    'start_date': days_ago(0),
    'email': ['kyzyto12@gmail.com'],
}

# defining the DAG

# define the DAG
dag = DAG(
    'process_web_log',
    default_args=default_args,
    description='Capstone DAG',
    schedule_interval=timedelta(minutes=1),
)

# define the task 'extract'

extract_data = BashOperator(
    task_id='extract',
    bash_command='cut -f1 -d"#" accesslog.txt > extracted_data.txt',
    dag=dag,
)

# define the task 'transform'
transform_data = BashOperator(
    task_id='transform',
    bash_command='grep -v -i "198.46.149.143" < extracted_data.txt > transformed_data.txt',
    dag=dag,
)

# define the task 'load'
load_data = BashOperator(
    task_id='load',
    bash_command='tar -cf weblog.tar transformed_data.txt' ,
    dag=dag,
)


# task pipeline

extract_data >> transform_data >> load_data