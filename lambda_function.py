#lambda_function.py

import json
import time

print('Starting function')

start_time = time.time()

import ldclient
from ldclient.config import Config
ldclient.set_config(Config("sdk-5ceac771-58d1-47c3-af81-b07acea6fe10"))
# ldclient.set_config(Config(sdk_key='sdk-5ceac771-58d1-47c3-af81-b07acea6fe10',
#     base_uri="http://localhost:8030",
#     stream_uri="http://localhost:8030")
# )
if ldclient.get().is_initialized():
    print("SDK successfully initialized!")
else:
    print("SDK failed to initialize")
client = ldclient.get()
print("SDK Init Time: --- %s seconds ---" % (time.time() - start_time))


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    print("value1 = " + event['key1'])
    print("value2 = " + event['key2'])
    print("value3 = " + event['key3'])
    print("Flag Eval Time: --- %s seconds ---" % (time.time() - start_time))
    show_feature = client.variation("test-flag-dev", {"key": "user@test.com"}, False)
    if show_feature:
        print("Feature flag is on")
    else:
        print("Feature flag is off")
    return event['key1']  # Echo back the first key value
    #raise Exception('Something went wrong')