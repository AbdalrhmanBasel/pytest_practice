#  Write a Python program to convert JSON data to Python object
import json

json_data = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

json_data2 = json.dumps(json_data)

print(json_data2)
