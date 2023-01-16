import requests as rq
import configparser
import json

config = configparser.ConfigParser()
config.read("config.ini")

api_key = config["USDA"]["Key"]

url = f"https://api.nal.usda.gov/fdc/v1/foods/search?api_key={api_key}"

query = {"query": "Sargento provolone", "pageSize": "10"}

data = rq.post(url, json=query).text

json_data = json.loads(data)

print(json.dumps(json_data, indent=4))
