from google.cloud import bigquery

import os

# Construct a BigQuery client object.
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/prakou/Downloads/translation-llm-86e95fb15e10.json'

# Construct a BigQuery client object.
client = bigquery.Client()

datasets = list(client.list_datasets())  # Make an API request.
project = client.project

if datasets:
    print("Datasets in project {}:".format(project))
    for dataset in datasets:
        print("\t{}".format(dataset.dataset_id))
else:
    print("{} project does not contain any datasets.".format(project))