import requests

res = requests.get("https://zenquotes.io/api/random")

if res.status_code == 200:
    data = res.json()
else:
    print("There was an error, code:", res.status_code)

