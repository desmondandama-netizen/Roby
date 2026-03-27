def tea_types():
    return ["Green", "Black", "Ginger", "Lemon", "Herbal"]


def coffee_types():
    return ["Espresso", "Americano", "Latte", "Cappuccino", "Mocha", "Dark_Roast", "Arabicca"]


def milk_tea_types():
    return ["Bubble_milk_Tea", "Thai_Milk_Tea", "Matcha_Milk_Tea", "Taro_Milk_Tea"]


def juice_types():
    return ["Orange", "Apple", "Mangoe", "Pineapple", "Lemon"]

#function call
def get_drink_types(drink_category):
    if drink_category == "tea":
        return tea_types()
    elif drink_category == "coffee":
        return coffee_types()
    elif drink_category == "milk_tea":
        return milk_tea_types()
    elif drink_category == "juice":
        return juice_types()
    else:
        return "Invalid drink category"
    
#function call
if __name__ == "__main__":
    print(get_drink_types("tea"))
    print(get_drink_types("coffee"))
    print(get_drink_types("milk_tea"))
    print(get_drink_types("juice"))