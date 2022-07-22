import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 78, "name": "Agjd", "views": 10}, 
        {"likes": 42, "name": "John", "views": 100000}, 
        {"likes": 69, "name": "Gleb", "views": 43934}, 
        {"likes": 999, "name": "Jim", "views": 1234}]

s = requests.session()
s.headers = headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}
# https = s.put("https://reqbin.com/echo/post/json", json={"foo": "bar"})
# print(https.status_code)
# print(https.request.headers)

# http = s.get("http://reqbin.com/echo/post/json", json={"foo": "bar"})
# print(http.status_code)
# print(http.request.headers)

for i in range(len(data)):

    response = s.put(BASE + "video/" + str(i), data[i], json={"foo": "bar"})
    print(response.json())

input()
s = requests.delete(BASE + "video/0", json={"foo": "bar"})
print(response)
input()
s = requests.get(BASE + "video/2", json={"foo": "bar"})
print(response.json())
