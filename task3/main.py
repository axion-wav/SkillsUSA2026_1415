from menus.shop import shop
from menus.checkout import checkout
from menus.manager import manager

import sys, json, os

# load the shared inventory once at startup so all menus work on the same list object.
base = os.path.dirname(__file__)
path = os.path.join(base, "data", "inventory_WORKING.json")

with open(path, "r") as file:
    data = json.load(file)

inventory = data["inventory"]

def main():
    # cart entries are managed by menu modules and passed between screens.
    cart = []

    while True:
        print('1: Shop\n2: Cart/Checkout\n3: Manager (Administrator Console)\n4: Exit', end='')
        key = input('\n\nSelect an option: ')

        match key:
            case "1":
                cart = shop(inventory, cart)
            case "2":
                cart = checkout(inventory, cart)
            case "3":
                manager(inventory)
            case "4":
                sys.exit()

main()