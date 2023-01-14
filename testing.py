import json
from food_data import NutritionalAPI


y = NutritionalAPI("014100053293")

y_json = json.loads(y.data.json())

print(json.dumps(y_json, indent=4))
