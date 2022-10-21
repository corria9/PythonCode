import requests

r = requests.post('https://catfact.ninja/')
r.status_code
response = r.json()

print(response)
print(r.status_code)