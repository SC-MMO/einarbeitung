import requests

url = "http://127.0.0.1:5001/api/squads"
response = requests.get(url)

print(f"GET {url}: {response.status_code}")
try:
    print(response.json())
except ValueError:
    print("Response was not JSON:", response.text)