recipes = {
    "small": {
        "ingredients": {
            "bread": 2,
            "ham": 4,
            "cheese": 4,
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,
            "ham": 6,
            "cheese": 8,
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,
            "ham": 8,
            "cheese": 12,
        },
        "cost": 5.50,
    }
}

resources = {
    "bread": 12,
    "ham": 18,
    "cheese": 24
}


class SandwichMachine:

    def __init__(self, machine_resources):
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        for item in ingredients:
            if ingredients[item] > self.machine_resources[item]:
                print(f"Sorry, not enough {item}.")
                return False
        return True

    def process_coins(self):
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))

        total = (
            quarters * 0.25 +
            dimes * 0.10 +
            nickels * 0.05 +
            pennies * 0.01
        )

        return total

    def transaction_result(self, coins, cost):
        if coins >= cost:
            change = round(coins - cost, 2)
            print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]

        print(f"Here is your {sandwich_size} sandwich. Enjoy!")


machine = SandwichMachine(resources)

while True:
    print("\nAvailable sandwiches:")
    print("small")
    print("medium")
    print("large")
    print("quit")

    choice = input("What would you like? ").lower()

    if choice == "quit":
        print("Goodbye!")
        break

    if choice not in recipes:
        print("Invalid choice.")
        continue

    ingredients = recipes[choice]["ingredients"]
    cost = recipes[choice]["cost"]

    if machine.check_resources(ingredients):
        payment = machine.process_coins()

        if machine.transaction_result(payment, cost):
            machine.make_sandwich(choice, ingredients)

    print("\nCurrent resources:")
    print(machine.machine_resources)