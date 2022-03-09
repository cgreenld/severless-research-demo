#lambda_function.py

import json
import time
import os
import ldclient
from ldclient.config import Config

print('Starting function')

start_time = time.time()

# Get environment variables
sdk_key = os.environ.get('SDKKEY_test')
environ = os.environ.get('env')
proxy_state = os.environ.get('proxy_state')


if proxy_state == 'off':
    ldclient.set_config(Config(sdk_key=sdk_key))
else:
    ldclient.set_config(Config(sdk_key=sdk_key,
        base_uri="http://localhost:8030", #these don't have cloud urls yet, but will eventually be set with env variables as well
        stream_uri="http://localhost:8030")
    )
if ldclient.get().is_initialized():
    print("SDK successfully initialized!")
else:
    raise Exception("SDK failed to initialize")
client = ldclient.get()
print("SDK Init Time: --- %s seconds ---" % (time.time() - start_time))


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    print("value1 = " + event['key1'])
    print("value2 = " + event['key2'])
    print("value3 = " + event['key3'])
    print("Flag Eval Time: --- %s seconds ---" % (time.time() - start_time))

    user = {"key": "user@test.com"}

    show_feature = client.variation("march-test-flag", user, False)
    if show_feature:
        print("Feature flag is on")
    else:
        print("Feature flag is off")
    return event['key1']  # Echo back the first key value
    #raise Exception('Something went wrong')
