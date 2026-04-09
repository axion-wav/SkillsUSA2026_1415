import math, json, os

def checkout(inventory, cart):
    while True:
        subtotal = 0

        for item in cart:
            price = item[1] * inventory[item[0]]["price"]
            subtotal += price
            print(f"{inventory[item[0]]["name"]} | Quantity: {item[1]} | Price: ${price:.2f}")

        tax = subtotal * 0.08 * 100 / 100

        total = subtotal + tax

        print(f"\n\nSubtotal: ${subtotal:.2f}\n\nSales tax: ${tax:.2f}\n\nTotal: ${total:.2f}\n\n")
        key = input("Do you want to checkout? (0 to exit, 1 to checkout): ")
        if key == "1":
            for item in cart:
                inventory[item[0]]["quantity"] -= item[1]

            order = {
                "items": [
                    {
                        "sku": inventory[item[0]]["sku"],
                        "name": inventory[item[0]]["name"],
                        "quantity": item[1],
                        "price": inventory[item[0]]["price"] * item[1]
                    }
                    for item in cart
                ],
                "subtotal": subtotal,
                "tax": tax,
                "total": total
            }

            base = os.path.dirname(os.path.dirname(__file__))
            path = os.path.join(base, "data", "salesdata.json")

            try:
                with open(path, "r") as f:
                    sales = json.load(f)
                    if isinstance(sales, dict):  # fix legacy single-order file
                        sales = [sales]
            except (FileNotFoundError, json.JSONDecodeError):
                sales = []

            sales.append(order)

            with open(path, "w") as f:
                json.dump(sales, f, indent=4)

            path = os.path.join(base, "data", "inventory_WORKING.json")

            with open(path, "w") as f:
                json.dump({"inventory": inventory}, f, indent=4)

            print("Thank you for shopping with us! Your order confirmation will arrive shortly.")
            return []
        elif key == "0":
            return cart