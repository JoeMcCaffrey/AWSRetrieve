# Sonos Interview
Using your favorite high-level language (Python, Ruby, Perl, or compiled), create a tool which uses AWS API access to list all EC2 instances in any single region, sorted by the value of a tag each instance has called ‘Owner’.  The script should display the results in an easy to read format which includes the instance id, tag value, instance type and launch time.  The script should work for any number of instances, and should display any instances without an Owner tag as type 'unknown' with the instance id, type and launch time.  

Design the script so it could be used later to find tags with other names and output additional instance information by request.

## Dependencies 

This python script uses the boto library to access amazon EC2

Developed with Python version 2.7.12 on Fedora 25 x86


## Instructions

This script takes 1 command line argument which is a .json file.

The .json file should have the secret key, access key, ec2 region, tag, field1, field2, and field3.

The field1..3 can be changed to output diffrent meta data.

## Description

The script will open the .json file and call the getSortInstances function to connect to the ec2 region. 
This function retrieves all the instances in that region and appends the instances with the matching tag into one list and non matching instances into another list. 
The matching tag list is sorted by tag and the two list are concatenated into one.

The printOut function is called to print out the instance data into a table.

To change the tag that the script looks for, change the .json file with 
another tag.

To parse multiple tags, create an array of tags inside of the .json file
and add a loop to the function getSortInstances function multiple times.

To output more meta data about the instance, change the printOut function to index the instance and change the .json file to output diffrent fields

