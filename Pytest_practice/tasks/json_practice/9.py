# Convert list to JSON
import json

data = {"key1": "value1", "key2": "value2"}


def convert_to_JSON(data):
    return json.dumps(data)


print(convert_to_JSON(data))
