from pymongo import MongoClient
from dataclasses import dataclass, asdict
from typing import List
from datetime import datetime
from food_data import NutritionalAPI
from pydantic import BaseModel


class Item(BaseModel):
    upc: str
    portion: float


class MealDiary(BaseModel):
    _id: int
    date: datetime
    meal_type: str
    items: List[Item]


# from food_data import NutritionalAPI


client = MongoClient("10.69.69.107", 49153)

# for db in client.list_databases():
# print(db)


mydb = client["meal_planner"]

upc = "024000241140"


mycol = mydb["meal_diary"]

# month = datetime.today().month
# day = datetime.today().day
# year = datetime.today().year

# meal_dict = {'_id':1, 'date':datetime(month=month, day=day, year=year) , 'meal_type':'breakfast', 'items': [{'upc':'024000241140', 'portion': 0.5}]}

# meal_entry = MealDiary(**meal_dict)


# mycol.replace_one({'_id':1}, asdict(meal_entry), upsert=True)


meal_entry_mongo = MealDiary(**mycol.find_one({"_id": 1}))

meal_items = [NutritionalAPI(**i.upc) for i in meal_entry_mongo.items]

print(meal_entry_mongo)

# print(meal_entry_mongo)

total_meal_cals = 0

print(f"Meal Date: {meal_entry_mongo.date}")
print(f"Meal Type: {meal_entry_mongo.meal_type}")
for item in meal_items:
    total_meal_cals += meal_entry_mongo.portion * meal_data.data.nf_calories
    print(
        f"Total Calories: {total_meal_cals}\nServing Size: {meal_data.data.nf_serving_size_unit}\nPortion Size: {i.portion}\nPortion Calories: {i.portion * meal_data.data.nf_calories}\n"
    )

# meal_data = NutritionalAPI(meal_entry.upc)

# mycol.replace_one({'_id':upc}, y.data.dict(), upsert=True)
# print(meal_data.data)

# calories_of_portion = meal_data.data.nf_calories * float(meal_entry.portion)

# print(f'Meal type: {meal_entry.meal_type.capitalize()}\nDate: {datetime.strftime(meal_entry.date, "%m/%d/%Y")}\n')

# print(f'Total Calories: {meal_data.data.nf_calories}\nServing Size: {meal_data.data.nf_serving_size_unit}\nPortion Size: {meal_entry.portion}\nPortion Calories: {calories_of_portion}')

# for document in mycol.find({}):

# print(document)
