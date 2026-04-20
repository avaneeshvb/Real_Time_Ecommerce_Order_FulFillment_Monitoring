from google.cloud import bigquery
import os

client = bigquery.Client()

DATASET = "ecommerce"


def write(table, row):
    table_id = f"{client.project}.{DATASET}.{table}"
    client.insert_rows_json(table_id, [row])