#!/usr/bin/env python
import os
import sys
import boto3

# Change accordingly
table_name = ''
key_prefix = ''
key_suffix = '/terraform.tfstate-md5'

# Get the LockID key from the local dir name
key = key_prefix + os.getcwd().split('providers/')[1] + key_suffix

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

def read_item(key):
    response = table.get_item(Key={'LockID': key})
    item = response['Item']
    print item['Digest']
    return item['Digest']

def update_item(key, value):
    table.update_item(
    Key={
        'LockID': key,
    },
    UpdateExpression='SET Digest = :val1',
    ExpressionAttributeValues={
        ':val1': value
    }
    )

if __name__ == "__main__":
    if len(sys.argv) == 2:
        value = sys.argv[1]
        previous = read_item(key)
        print "About to change {} in {} to {}".format(previous,table_name,value)
        answer = raw_input("Are you sure? [y/N]: ")
        if answer in 'yY':
            update_item(key,value)

