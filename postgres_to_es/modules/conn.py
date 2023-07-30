from contextlib import contextmanager
import psycopg2
from elasticsearch import Elasticsearch
from psycopg2.extras import RealDictCursor


@contextmanager
def elasticsearch_conn(dsn: str):
    es_connection = Elasticsearch(dsn)
    try:
        yield es_connection
    finally:
        es_connection.close()


@contextmanager
def postgres_conn(dsn: dict):
    connection = psycopg2.connect(**dsn, cursor_factory=RealDictCursor)
    connection.set_session(autocommit=True)
    try:
        yield connection
    finally:
        connection.close()
