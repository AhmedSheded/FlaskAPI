import requests

BASE = 'http://127.0.0.1:5000/'

link = 'video/'

data = [{'likes': 10, 'name': 'animals', 'views': 50},
        {'likes': 20, 'name': 'laptop', 'views': 324},
        {'likes': 24, 'name': 'computer', 'views': 578}]

for i in range(len(data)):
    response = requests.put(BASE+link+str(i), data[i])
    print(response.json())


input()
response = requests.get(BASE+link+'15')
print(response.json())

response = requests.patch(BASE+link+'2', {'views': 98})
print(response.json())