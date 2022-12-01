# PrettyPrint following JSON data
import json

data = {"id" : 1, "name" : "value2", "age" : 29}

print(json.dumps(data, indent=1))