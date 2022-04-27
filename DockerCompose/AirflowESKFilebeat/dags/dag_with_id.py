from datetime import timedelta, datetime
from textwrap import dedent
import uuid

from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator

args = {
        'owner': 'airflow',
}

with DAG(
        dag_id='amirs_python_operator_withid',
        default_args=args,
        schedule_interval=None,
        start_date=days_ago(2),
        tags=['example'],
) as dag:

    def do_something(**kwargs):
        """This function should run as a task"""
        context = kwargs
        from elasticsearch import Elasticsearch, RequestsHttpConnection
        es = Elasticsearch(hosts=[{"host": "10.2.0.11", "port": 9200}],connection_class=RequestsHttpConnection,)
        es.indices.create(index='amir-id-index', ignore=400)
        log_id = context['dag'].dag_id + "-" + context['task_instance'].task_id + "-" + context['ts'] + "-" + str(context['task_instance'].try_number)
        es.index(index="amir-id-index", id=uuid.uuid1(), body={"log_id": log_id, "message": "new message - hello", "offset": int(datetime.now().timestamp()), "timestamp": datetime.now()})


    my_task = PythonOperator(
        task_id='log_this',
        python_callable=do_something,
            )
