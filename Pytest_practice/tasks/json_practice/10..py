# Access the value of key2 from the following JSON
import json

sampleJson = """{"key1": "value1", "key2": "value2"}"""


def convert_JSON_TO_OBJECT(sampleJson):
    data = json.load(sampleJson)
    return data['key2']

print(convert_JSON_TO_OBJECT(sampleJson))