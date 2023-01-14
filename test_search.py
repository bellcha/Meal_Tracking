from food_data import NutritionalAPI


def main():

    try:

        chips = NutritionalAPI("038000138430")

        if chips.data.item_name is not None:

            print(chips.data)
        else:
            print('No items found.')
    except ValueError as err:
        print(err)


main()
