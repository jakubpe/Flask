import datetime
import requests
x = datetime.date.today().year
print(x)

AGIFY_API = "https://api.agify.io/"
params = {
    'name': 'michael'
}

response = requests.get(url=AGIFY_API, params=params)
response.raise_for_status()
print(response.json()['age'])