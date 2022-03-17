#lambda_function.py

import json
import time
import os
import ldclient
from ldclient.config import Config
from ldclient.feature_store import CacheConfig
from ldclient.integrations import DynamoDB
import uuid
import boto3

print('Starting function')

# Get environment variables
sdk_key = os.environ.get('SDKKEY_test')
proxy_table_name = os.environ.get("proxy_table_name")
table_name = os.environ.get("table_name")
flag_name = os.environ.get("flag_name")
base_uri = os.environ.get("base_uri")
stream_uri = os.environ.get("stream_uri")


start_time = time.time()

store = DynamoDB.new_feature_store(proxy_table_name,
    caching=CacheConfig(expiration=30))

config = Config(feature_store=store, sdk_key=sdk_key, use_ldd=True)
ldclient.set_config(config)

if ldclient.get().is_initialized():
    sdk_init_time = time.time() - start_time
    print("Connection with relay proxy successfully initialized!")
else:
    raise Exception("SDK failed to initialize")
    
client = ldclient.get()
print("SDK Init Time: --- %s seconds ---" % sdk_init_time)

sessionID = str(uuid.uuid1())

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    print("value1 = " + event['key1'])
    print("value2 = " + event['key2'])
    print("value3 = " + event['key3'])

    user = {"key": "user@test.com"}
    flag_start_time = time.time()
    show_feature = client.variation(flag_name, user, False)
    flag_eval_time = time.time() - flag_start_time
    print("Flag Eval Time: --- %s seconds ---" % flag_eval_time)
    if show_feature:
        print("Feature flag is on")
    else:
        print("Feature flag is off")

    #update dynamoDB table
    dynamodb = boto3.resource('dynamodb', 'us-east-1')

    table = dynamodb.Table(table_name)
    table.put_item(
        Item={
                'runID': str(uuid.uuid1()),
                'run_type': 'DB',
                'key_id': sdk_key[:8],
                'sdk_init_timestamp': str(sdk_init_time),
                'flag_call_timestamp': str(flag_eval_time),
                'flag': flag_name,
                'sessionID': sessionID,
                'region': 'us-east-1'
            }
        )
    print("Successfully put to: " + table_name)


    return event['key1']  # Echo back the first key value

