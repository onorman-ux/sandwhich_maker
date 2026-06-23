import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    is_on = True

    while is_on:
        choice = input("What would you like? small/medium/large: ").lower()

        if choice == "off":
            is_on = False

        elif choice == "report":
            print(f"Bread: {resources['bread']} slice(s)")
            print(f"Ham: {resources['ham']} slice(s)")
            print(f"Cheese: {resources['cheese']} ounce(s)")

        elif choice in recipes:
            sandwich = recipes[choice]
            sandwich_ingredients = sandwich["ingredients"]
            sandwich_cost = sandwich["cost"]

            if sandwich_maker_instance.check_resources(sandwich_ingredients):
                coins = cashier_instance.process_coins()

                if cashier_instance.transaction_result(coins, sandwich_cost):
                    sandwich_maker_instance.make_sandwich(choice, sandwich_ingredients)

        else:
            print("Invalid choice. Please choose small, medium, large, report, or off.")


if __name__ == "__main__":
    main()