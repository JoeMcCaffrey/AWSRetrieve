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
    ids= 'id'
    print(mergedOwners[0].id)
    return mergedOwners


def printOut(ownersList, field1, tag, field2, field3):

    print("%10s|%10s|%10s|%10s" % (field1, tag, field2, field3))
    
    for owner in ownersList:
        if tag in owner.tags:
            print("%10s %10s %10s %10s" % (owner[field1], owner.tags[tag], \
                owner[field2], owner[field3]))
        else:
            print("%10s %10s %10s %10s" % (owner[field1], 'unknown', owner.field2, \
                owner.field3))


with open('data.json') as data_file:
    data = json.load(data_file)

sortedTags = getSortInstances(data["region"], data["tag"])

printOut(sortedTags, data["field1"],data["tag"],data["field2"], data["field3"])
