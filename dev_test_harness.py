from contextlib import nullcontext
import lambda_function

test_event = {
  "key1": "value1",
  "key2": "value2",
  "key3": "value3"
}

lambda_function.lambda_handler(test_event, nullcontext)