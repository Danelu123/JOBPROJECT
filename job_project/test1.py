# testing test1 file

import requests

response = requests.get("http://127.0.0.1:8000/api1/jobs/")
print(response.json())
print(response.status_code)

response = requests.post("http://127.0.0.1:8000/api1/jobs/")
print(response.json())
print(response.status_code)

response = requests.put("http://127.0.0.1:8000/api1/jobs/")
print(response.json())
print(response.status_code)

response = requests.patch("http://127.0.0.1:8000/api1/jobs/")
print(response.json())
print(response.status_code)

response = requests.delete("http://127.0.0.1:8000/api1/jobs/")
print(response.json())
print(response.status_code)
