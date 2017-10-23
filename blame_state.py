import os
import sys
import boto3
import json

# Change accordingly
s3_bucket = ''
s3_suffix = '/terraform.tfstate'
s3_path = os.getcwd().split('providers/')[1] + s3_suffix
tempfile = 'temp_state'

s3 = boto3.resource('s3')
s3.Bucket(s3_bucket).download_file(s3_path, tempfile)


s3_contents = ''
with open (tempfile, 'r') as f:
    s3_contents = json.load(f)

os.remove(tempfile)
counter = 0
while True:
    try:
        last_to_touch = s3_contents['modules'][counter]['resources']['data.aws_caller_identity.current']['primary']['attributes']['arn']
        break
    except KeyError:
        counter += 1
    except IndexError:
        print "ERROR: Not found"
        break

print "Last user to touch state: {}".format(last_to_touch.split('user/')[1])
