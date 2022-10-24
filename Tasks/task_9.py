"""
Task 9 - JSON parsing

1. Write a console program that takes an IP and returns the country using the API:

https://ip-api.com/docs/api:json

2. If the IP does not exist, you should throw the error ""This IP does not exist"".


TODO: Write a program that
    1. Get IP & returns country using API.
    2. If IP doesn't exist, throw error "This IP Doesn't Exist!"
    # DONE
"""
import requests

ip_address = input("Enter You IP Address: ")
endpoint = requests.get(f'http://ip-api.com/json/{ip_address}?fields=status,'f'message,country,countryCode,query')


def get_ip(endpoint):
    response = endpoint
    if endpoint.status_code == 200:
        data = response.json()
        if data['status'] == 'success':
            return endpoint.json()['country']
    else:
        raise Exception("This IP Doesn't Exist!")


print("Country:", get_ip(endpoint))



######### PROGRAM #2 ########
#
# def get_ip2():
#     response = requests.get('https://api64.ipify.org?format=json').json()
#     return response["ip"]
#
#
# def get_location2():
#     ip_address = get_ip2()
#     response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
#     location_data = {
#         "ip": ip_address,
#         "city": response.get("city"),
#         "region": response.get("region"),
#         "country": response.get("country_name")
#     }
#     return location_data["country"]
#
#
# print("Your IP Address is:", get_ip2())
# print("Your current location is:", get_location2())
