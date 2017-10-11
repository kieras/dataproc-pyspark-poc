#!/usr/bin/env python

""" Main job file.
"""

import sys
import pyspark

from my_package import logging
from my_package import str_lower
from my_package import str_upper
from my_package import bigquery
from my_package import storage


project_id = sys.argv[1] #'prj-retraining'
dataset_name = 'poc_pyspark_sort'
table_name = 'result'

if sys.argv[2] == 'up':
    map_function = str_upper.to_uppercase
else:
    map_function = str_lower.to_lowercase


sc = pyspark.SparkContext()

logging.log('Starting job.', 'ml-training', 'jobid')

config = storage.get_blob_as_string('training-phase3', 'config_test/config.yaml')

logging.log('Config: {}'.format(config))

rdd = sc.parallelize(['Hello,', 'World!', 'DOG', 'elePhant', 'panTher', 'of', 'Blaster'])\
    .filter(lambda w: len(w) > 3)\
    .map(map_function)

words = sorted(rdd.collect())

print(words)

# TODO transform words into words,len,record tuple
data = [
        (u'aaaaaaaaa', 50, dict(amount='aaaaaaaaa', amount_value=1.0)),
        (u'bbbbbbbbb', 60),
    ]

bq = bigquery.BigQueryHelper(project_id, dataset_name, table_name)
bq.stream_data(data)

