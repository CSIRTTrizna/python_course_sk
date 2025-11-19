import requests

session = requests.Session()

data = {"numbers": [1, 2, 3, 4]}
result = session.post("http://localhost:5000/sum", json=data)

print(result.content.decode())
print(result.json())
