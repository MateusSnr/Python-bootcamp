MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def checking_the_resources_and_updating(choiced_drink):
    ingredients_and_cost_of_drink = MENU[choiced_drink]
    ingredients_of_drink = ingredients_and_cost_of_drink["ingredients"]
    for ing in ingredients_of_drink:
        if ingredients_of_drink[ing] > resources[ing]:
            print("Sorry there is not enough", ing,".")
            return False
        else:
            resources[ing] = resources[ing] - ingredients_of_drink[ing]
    return True


def insert_coins():
    print("Please insert coins.")
    quartes = float(input("How many quartes:"))
    dimes = float(input("How many dimes: "))
    nickles = float(input("How many nickles: "))
    pennies = float(input("How many pennies: "))
    total = (0.25 * quartes) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    return total


def checking_total(inserted_coins, choice):
    ingredients_and_cost_of_drink = MENU[choice]
    cost = ingredients_and_cost_of_drink["cost"]
    if inserted_coins > cost:
        change = inserted_coins - cost
        print("Here is $", round(change, 2), "in change.")
        return True
    elif inserted_coins == cost:
        return True
    else:
        return False

def replenish_resources(choiced_drink):
    ingredients_and_cost_of_drink = MENU[choiced_drink]
    ingredients_of_drink = ingredients_and_cost_of_drink["ingredients"]
    for ing in ingredients_of_drink:
        resources[ing] = resources[ing] + ingredients_of_drink[ing]
    return


money = 0
is_on = True

while is_on == True:
    choice = input("“What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        for key in resources.keys():
            if key == "coffee":
                print(key, ":", resources[key], "g")
            else:
                print(key, ":", resources[key], "ml")
        if money > 0:
            print("money : $", money)
        else:
            pass

    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        checked_resources = checking_the_resources_and_updating(choice)
        if checked_resources == True:
            if checking_total(insert_coins(), choice) == True:
                ingredients_and_cost = MENU[choice]
                cost = float(ingredients_and_cost["cost"])
                money += cost
                print("Here is your", choice, "☕ .Enjoy!")
            else:
                replenish_resources(choice)
                print("Sorry that's not enough money. Money refunded.")
        else:
            pass
    else:
        print("Invalid option!")