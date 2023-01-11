from food_data import NutritionalAPI

x = NutritionalAPI('1111111111')

y = NutritionalAPI('028400090858')

print(y.data)

print(x._host)