#!/usr/bin/env python

import uuid

from mesos_cook import *
from mesos_cook.model import *
from requests import HTTPError

job_spec = Job(
    name='workshop-{{id}}',
    uuid='{{job_uuid}}',
    priority=75,
    max_retries=2,
    max_runtime=3600000,
    container=Container(
        type='MESOS',
        docker=DockerInfo(
            image='serrep3.services.brown.edu:5000/workshop-task'
        ),
        volumes=[
            Volume(
                host_path='/media/data_cifs',
                container_path='/data_cifs',
                mode='RW'
            )
        ]
    ),
    command='./task.py {{id}}',
    cpus=1,
    gpus=1,
    mem=256
)

jobs = []

for i in range(10):
    job_uuid = uuid.uuid1()
    print("Using job {} for task {}".format(job_uuid, i))
    jobs.append(job_spec.bind(dict(id = i, job_uuid = job_uuid)))

client = CookClient('http://serrep1.services.brown.edu:12321', 'ben', 'x')

try:
    client.launch(jobs)
except HTTPError as e:
    print("{} error: {}".format(e.response.status_code, e.response.text))
