import json, os

def sales():
    base = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(base, "data", "salesdata.json")

    try:
        with open(path, "r") as file:
            sales = json.load(file)
            if isinstance(sales, dict):
                sales = [sales]
    except (FileNotFoundError, json.JSONDecodeError):
        sales = []

    total_rev = 0

    item_totals = {}

    # aggregate totals by sku for the manager sales summary.
    for order in sales:
        total_rev += order["total"]
        for item in order["items"]:
            sku = item["sku"]
            if sku in item_totals:
                item_totals[sku]["quantity"] += item["quantity"]
                item_totals[sku]["revenue"] += item["price"]
            else:
                item_totals[sku] = {
                    "name": item["name"],
                    "quantity": item["quantity"],
                    "revenue": item["price"]
                }


    while True:
        print(f"\nSales summary:\n\nTotal revenue: ${total_rev:.2f}\n\nItem summaries:\n")
        for sku, data in item_totals.items():
            print(f"SKU {sku}: {data['name']} | Sold: {data['quantity']} | Revenue: ${data['revenue']:.2f}")
        
        input("\nPress enter to return.")
        return


def manager(inventory):
    # prompt until valid admin credentials are entered.
    while True:
        un = input("Administrator username: ")
        if un == "admin":
            while True:
                pw = input ("Administrator password: ")
                if pw == "1234":
                    while True:
                        print('\nSALES\n1: View Sales Summary\n\nINVENTORY\n2: Create Item\n3: Remove Item\n4: Edit Item\n\n0: Exit', end='')
                        key = input('\n\nSelect an option: ')
                        match key:
                            case "0":
                                return
                            case "1":
                                sales()
                            case "2":
                                name = input("\nName of the item: ")
                                price = input("\nPrice of the item: ")
                                stock = input("\nQuantity of the item: ")

                                try:
                                    price = float(price)
                                    stock = int(stock)
                                except ValueError:
                                    print("Invalid price or quantity.")
                                    continue

                                new_sku = max((item["sku"] for item in inventory), default=0) + 1

                                inventory.append({
                                    "sku": new_sku,
                                    "name": name,
                                    "price": price,
                                    "quantity": stock
                                })

                                base = os.path.dirname(os.path.dirname(__file__))
                                path = os.path.join(base, "data", "inventory_WORKING.json")

                                with open(path, "w") as f:
                                    json.dump({"inventory": inventory}, f, indent=4)

                                print("Item added!")
                            case "3":
                                while True:
                                    for item in inventory:
                                        print(f"SKU {item['sku']}: {item['name']} | Price: ${item['price']} | Inventory: {item['quantity']}")

                                    try:
                                        sku = int(input("\nEnter an item SKU to remove: "))
                                    except ValueError:
                                        print("Invalid SKU.")
                                        continue

                                    if any(item["sku"] == sku for item in inventory):
                                        inventory[:] = [item for item in inventory if item["sku"] != sku]

                                        base = os.path.dirname(os.path.dirname(__file__))
                                        path = os.path.join(base, "data", "inventory_WORKING.json")

                                        with open(path, "w") as f:
                                            json.dump({"inventory": inventory}, f, indent=4)

                                        print("Item removed!")
                                        break
                                    else:
                                        print("Invalid SKU.")
                            case "4":
                                while True:
                                    for item in inventory:
                                        print(f"SKU {item['sku']}: {item['name']} | Price: ${item['price']} | Inventory: {item['quantity']}")

                                    try:
                                        sku = int(input("\nEnter an item SKU to edit: "))
                                    except ValueError:
                                        print("Invalid SKU.")
                                        continue

                                    if any(item["sku"] == sku for item in inventory):
                                        # empty input keeps the original field value.
                                        name = input("\nName of the item (Enter for no change): ")
                                        price = input("\nPrice of the item (Enter for no change): ")
                                        stock = input("\nQuantity of the item (Enter for no change): ")

                                        valid_edit = True

                                        for item in inventory:
                                            if item["sku"] == sku:
                                                if name:
                                                    item["name"] = name
                                                if price:
                                                    try:
                                                        item["price"] = float(price)
                                                    except ValueError:
                                                        print("Invalid price.")
                                                        valid_edit = False
                                                        break
                                                if stock:
                                                    try:
                                                        item["quantity"] = int(stock)
                                                    except ValueError:
                                                        print("Invalid quantity.")
                                                        valid_edit = False
                                                        break
                                                break

                                        if not valid_edit:
                                            continue

                                        base = os.path.dirname(os.path.dirname(__file__))
                                        path = os.path.join(base, "data", "inventory_WORKING.json")

                                        with open(path, "w") as f:
                                            json.dump({"inventory": inventory}, f, indent=4)

                                        print("Item edited!")
                                        break
                                    else:
                                        print("Invalid SKU.")

                else:
                    print("Invalid password. ")
        else:
            print("Invalid username.")