#!/usr/bin/env python

from my_package import logging
from my_package import storage
import yaml


config_str = storage.get_blob_as_string('training-phase3', 'training_job_config.yaml')

config = yaml.load(config_str)

logging.log('Config: {}'.format(str(config)))

print(config)

print(type(config))

