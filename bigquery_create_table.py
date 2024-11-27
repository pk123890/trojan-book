from google.cloud import bigquery
import os

# Construct a BigQuery client object.
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/prakou/Downloads/translation-llm-86e95fb15e10.json'

# Construct a BigQuery client object.
client = bigquery.Client()

# TODO(developer): Set table_id to the ID of the table to create.
table_id = "translation-llm.engati_test.test_table_creation"

schema = [
    bigquery.SchemaField("request", "JSON", mode="REQUIRED")
]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)
