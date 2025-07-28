import requests
from typing import Union

def exec_get(*, url:str) -> Union[list, dict, str]:
    response = requests.get(url)
    try:
        return response.json()
    except ValueError:
        return f"Response was not JSON: {response.text}"

api_urls=[
    "http://127.0.0.1:5001/api/squads",
    "http://127.0.0.1:5001/api/members",
    "http://127.0.0.1:5001/api/powers",
    "http://127.0.0.1:5001/api/squads/1",
    "http://127.0.0.1:5001/api/members/10",
    "http://127.0.0.1:5001/api/powers/1000" #Will return {"error": "404 Not Found: Object not found"} cause we dont have that many powers
]
reqs = [exec_get(url=api_url) for api_url in api_urls]

import json
for req in reqs:
    if isinstance(req, str):
        print(req)
    else:
        print(json.dumps(req, indent=4))
    print("\n\n\n")