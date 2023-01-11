from food_data import NutritionalAPI


def main():

    chips = NutritionalAPI("0284000908509")

    print(chips.data)


main()
