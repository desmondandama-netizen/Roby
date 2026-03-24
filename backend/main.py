# "food menu"
Food_1 = "Ugali"
Food_2 = "Mushrooms"
Food_3 = "Greens"

day_of_the_week = "Monday"

def suggestor(day_of_the_week):
    if day_of_the_week == "Monday":
        print("Today we will eat,", Food_1)

def check_food_menu(food_menu):
    if food_menu == "Food_3":
        print("food_menu:", Food_3)

# function calls
suggestor("Monday")
check_food_menu("Food_3")
check_food_menu("Greens")

print("program is running")