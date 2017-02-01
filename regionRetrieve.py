#! /usr/bin/python

import json
import boto.ec2

with open('data.json') as data_file:
    data = json.load(data_file)

aws_region = data["region"]

conn = boto.ec2.connect_to_region(aws_region,
    aws_access_key_id=data["AccessKey"],
    aws_secret_access_key=data["SecretKey"])

reservations = conn.get_all_instances(instance_ids=None, filters=None, \
    dry_run=False,max_results =None)

#for res in reservations:
#    for inst in res.instances:

print(reservations[0].instances[0].tags)
