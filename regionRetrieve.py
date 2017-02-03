#! /usr/bin/python

import json
import boto.ec2
import sys

def getSortInstances(region, tag):
    
    # connect to amazon
    conn = boto.ec2.connect_to_region(region,
    aws_access_key_id=data["AccessKey"],
    aws_secret_access_key=data["SecretKey"])
    
    # get only instances for region
    instances = conn.get_only_instances(instance_ids=None, filters=None,\
        dry_run=False, max_results=None)
    
    owners = []
    nonOwners= []

    # find out if each instance has tag and place into list
    for instance in instances:
        if tag in instance.tags:
            owners.append(instance)
        else:
            nonOwners.append(instance)

    # sort owners list by tag
    owners.sort(key=lambda x:x.tags[tag])
    # make one large with sorted first then unknowns
    mergedOwners = owners + nonOwners

    return mergedOwners

#change this function to print out more data about instance
def printOut(ownersList, tag):
    
    # print out table header
    template = "{0:19}|{1:7}|{2:13}|{3:12}"
    print(template.format('ID', tag, 'Instance Type', 'Launch Time'))

    for owner in ownersList:
       # print out the sorted list then unknows list

        if tag in owner.tags:
            print(template.format(owner.id, owner.tags[tag], \
                    owner.instance_type, owner.launch_time))
        else:
            print(template.format(owner.id, 'unknown', \
                    owner.instance_type, owner.launch_time))

# open json file with script data as command line argument
# so we can use this script with diffrent data

if len(sys.argv) != 2:
    print("This scirpt takes a json file as a command line argument")
    sys.exit(1)

with open(sys.argv[1]) as data_file:
    data = json.load(data_file)

# call to sort instances by tag
sortedTags = getSortInstances(data["region"], data["tag"])

# print out results seperate from get and sort function
printOut(sortedTags, data["tag"])
