"""BigQuery helpers module."""

from google.cloud import bigquery


class BigQueryHelper(object):
    bigquery_client = None
    dataset_name = None
    table_name = None
    table = None

    def __init__(self, project_id, dataset_name, table_name):
        self.bigquery_client = bigquery.Client(project=project_id)
        self.dataset_name = dataset_name
        self.table_name = table_name

    def stream_data(self, data):
        """Loads data into BigQuery.

        The dataset and table should already exist.

        :type data: list of tuples
        :param data: Row data to be inserted. Each tuple should contain data
                     for each schema field on the current table and in the
                     same order as the schema fields.

        :raises: Exception if there is any error when inserting data.
        """
        if self.table is None:
            dataset = self.bigquery_client.dataset(self.dataset_name)
            self.table = dataset.table(self.table_name)
            self.table.reload()

        errors = self.table.insert_data(data)

        if len(errors) > 0:
            raise Exception(errors)
