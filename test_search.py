from food_data import NutritionalAPI


def main():

    try:

        chips = NutritionalAPI("02840009085!")

        print(chips.data)
    except ValueError as err:
        print(err)


main()
