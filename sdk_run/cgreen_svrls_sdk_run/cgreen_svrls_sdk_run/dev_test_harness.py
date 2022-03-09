from contextlib import nullcontext
import app

test_event = {
  "key1": "value1",
  "key2": "value2",
  "key3": "value3"
}

app.lambda_handler(test_event, nullcontext)