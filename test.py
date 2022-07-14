import requests

BASE = "http://127.0.0.1:5000/"

response = requests.patch(BASE + "video/0", {"views":99})
print(response.json())


# data = [{"likes":51, "name": "Boufa", "views":321}, 
#     {"likes":950, "name": "Joe", "views":1505},
#     {"likes":75, "name": "Dragon", "views":852}]

# for i in range(len(data)):
#     response = requests.put(BASE + "video/"+ str(i), data[i])
#     print(response.json())

# input()
# response = requests.get(BASE + "video/1")
# print(response.json())