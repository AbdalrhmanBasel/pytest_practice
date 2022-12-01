#  Write a Python program to convert JSON data to Python object
import json

json_data = '{ "name":"John", "age":30, "city":"New York"}'

json_object = json.loads(json_data)

print(json_object['name'])

json_data2 = json.dumps(json_object)

print(json_data2)