# coding=utf-8
"""Logging helpers module."""

from google.cloud import logging

logger = None
context_key = None


def log(message, logger_name='iva-ml', logger_context_key=''):
    """Logs and prints a message.
    """
    global logger
    global context_key

    if logger is None:
        logger = logging.Client().logger(logger_name)
        context_key = logger_context_key

    new_message = '[' + context_key + '] ' + message
    print(new_message)
    logger.log_text(new_message)


def get_job_id(pyspark):
    dataproc_job_prefix = 'dataproc_job_'
    tags = pyspark.SparkConf().get('spark.yarn.tags', 'unknown').split(',')
    for tag in tags:
        if tag.startswith(dataproc_job_prefix):
            job_id = tag.strip(dataproc_job_prefix)
            return job_id
