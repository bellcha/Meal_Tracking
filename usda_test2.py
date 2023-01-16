from usda import USDA


food = USDA('Sargento', '25')

food_data = food.get_data()


for f in food_data.foods:
    brand = f.brand_name
    desc = f.description
    if f.brand_name is not None:
        serving_size = int(f.serving_size)
        unit = f.serving_size_unit
    else:
        serving_size = f.serving_size
        unit = ''

    print(f'Brand: {brand}\nDescription: {desc}\nServing Size: {serving_size} {unit}\n')

    for n in f.food_nutrients:
        print(n.nutrient_name)
        print(n.nutrient_number, n.unit_name)
    
    print('\n')

