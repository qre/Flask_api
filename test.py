import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 78, "name": "Agjd", "views": 10}, 
        {"likes": 42, "name": "John", "views": 100000}, 
        {"likes": 69, "name": "Gleb", "views": 43934}, 
        {"likes": 999, "name": "Jim", "views": 1234}]

for i in range(len(data)):

    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.delete(BASE + "video/0")
print(response)
input()
response = requests.get(BASE + "video/2")
print(response.json())