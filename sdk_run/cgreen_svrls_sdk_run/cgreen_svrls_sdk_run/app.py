#lambda_function.py

import json
import time
import os
from xml.dom.xmlbuilder import DOMEntityResolver
import ldclient
from ldclient.config import Config
import uuid
import boto3

print('Starting function')

# Get environment variables
sdk_key = os.environ.get('SDKKEY_test')
environ = os.environ.get('env')
table_name = os.environ.get("table_name")


start_time = time.time()

ldclient.set_config(Config(sdk_key=sdk_key))
if ldclient.get().is_initialized():
    sdk_init_time = time.time() - start_time
    print("SDK successfully initialized!")
else:
    raise Exception("SDK failed to initialize")
client = ldclient.get()
print("SDK Init Time: --- %s seconds ---" % sdk_init_time)



def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    print("value1 = " + event['key1'])
    print("value2 = " + event['key2'])
    print("value3 = " + event['key3'])

    user = {"key": "user@test.com"}
    flag_start_time = time.time()
    show_feature = client.variation("march-test-flag", user, False)
    flag_eval_time = time.time() - flag_start_time
    print("Flag Eval Time: --- %s seconds ---" % flag_eval_time)
    if show_feature:
        print("Feature flag is on")
    else:
        print("Feature flag is off")

    #update dynamoDB table
    dynamodb = boto3.resource('dynamodb', 'us-east-1')

    table = dynamodb.Table('cgreenSeverlessFlagStore-dev')
    table.put_item(
        Item={
                'runID': str(start_time),
                'run_type': 'SDK',
                'sdk_init_timestamp': str(sdk_init_time),
                'flag_call_timestamp': str(flag_eval_time),
                'flag': 'march-test-flag',
            }
        )


    return event['key1']  # Echo back the first key value

