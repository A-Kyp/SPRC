# Lab 1 SPRC - Comunicare Web HTTP

import requests
import json

# ===================== TASK 1 =====================
url_task1 =    'https://sprc.dfilip.xyz/lab1/task1'
url_task1_ck = 'https://sprc.dfilip.xyz/lab1/task1/check'

url_param = {"nume": "Chiper Alexandra-Diana", 'grupa': '342C4'}
post_param = {"secret": "SPRCisNice",}
header = {"secret2": "SPRCisBest"}

# post(url, data, json, args)
# rt1 = requests.post(url_task1, data=post_param, headers=header, params=url_param)   
# print(rt1.text)

rt1c = requests.post(url_task1_ck, data=post_param, headers=header, params=url_param)   
print("Task1:\n")
print(rt1c.text)

# ===================== TASK 2 =====================
url_task2 = 'https://sprc.dfilip.xyz/lab1/task2'
dict = {'username': 'sprc', 'password': 'admin', 'nume': 'Chiper Alexandra-Diana'}

rt2c = requests.post(url_task2, data=json.dumps(dict))
print("\nTask2:\n")
print(rt2c.text)

# ===================== TASK 3 =====================
url_task3 =    'https://sprc.dfilip.xyz/lab1/task3/login'
url_task3_ck = 'https://sprc.dfilip.xyz/lab1/task3/check'

s = requests.Session()

rt3 = s.post(url_task3, data=json.dumps(dict))
rt3c = s.get(url_task3_ck)

print("\nTask3:\n")
print(rt3c.text)