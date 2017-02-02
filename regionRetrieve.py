#! /usr/bin/python

import json
import boto.ec2


def getSortInstances(region, tag):
    
    conn = boto.ec2.connect_to_region(region,
    aws_access_key_id=data["AccessKey"],
    aws_secret_access_key=data["SecretKey"])

    instances = conn.get_only_instances(instance_ids=None, filters=None,\
        dry_run=False, max_results=None)
    
    owners = []
    nonOwners= []
    for instance in instances:
        if tag in instance.tags:
            owners.append(instance)
        else:
            nonOwners.append(instance)

    owners.sort(key=lambda x:x.tags[tag])
    mergedOwners = owners + nonOwners
    return mergedOwners


def printOut(ownersList, tag):

    print("instance id | %s | instance type | launch time" % tag)
    
    for owner in ownersList:
        if tag in owner.tags:
            print("%s %s %s %s" % (owner.id, owner.tags[tag], \
                owner.instance_type, owner.launch_time))
        else:
            print("%s %s %s %s" % (owner.id, 'unknown', owner.instance_type, \
                owner.launch_time))


with open('data.json') as data_file:
    data = json.load(data_file)

sortedTags = getSortInstances(data["region"], data["tag"])

printOut(sortedTags, data["tag"])
