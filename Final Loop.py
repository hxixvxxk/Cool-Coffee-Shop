def menu(choices, title="Rald's Menu", prompt="Choose your item: "):
    print(title)
    print(len(title) * "-")
    i = 1
    for c in choices:
        print(i, c)
        i = i + 1

    while True:
        choice = input(prompt)
        allowed_answers = []
        for a in range(1, len(choices) + 1):
            allowed_answers.append(str(a))
        allowed_answers.append("X")
        allowed_answers.append("x")

        if choice in allowed_answers:
            if choice == "X" or choice == "x":
                break
            else:
                answer = choices[int(choice) - 1]
                return answer
        else:
            print("Enter number from 1 to", len(choices), "or X to exit.")

drinks = ["chocolate", "coffee", "decaf"]
flavors = ["caramel", "vanilla", "peppermint", "raspberry", "plain"]
toppings = ["chocolate", "cinnamon", "caramel"]

def get_order():
    print("Welcome to Rald's Coffee Shop!\n")
    name = input("Please enter your name: ")

    drink = menu(drinks, "Rald's Drinks", "Choose your drink: ")
    flavor = menu(flavors, "Rald's Flavors", "Choose your flavor: ")
    topping = menu(toppings, "Rald's Toppings", "Choose your topping: ")

    return {
        "name": name,
        "drink": drink,
        "flavor": flavor,
        "topping": topping
    }

def print_order(order):
    print("Name:", order.get("name"))
    print("Drink:", order.get("drink"))
    print("Flavor:", order.get("flavor"))
    print("Topping:", order.get("topping"))

def save_order(order):
    print("Saving order...")
    return

def main_menu():
    while True:
        order = get_order()

        print("\n Check Your Order ")
        print_order(order)

        while True:
            confirm = input("Confirm? Press Y to confirm, N to cancel: ").strip().upper()
            if confirm == "Y":
                save_order(order)
                print("\n Thanks for your order! ")
                print_order(order)
                return 
            elif confirm == "N":
                print("\nOrder cancelled. Starting over...")
                break 
            else:
                print("Invalid input. Please enter Y or N.")

main_menu()
