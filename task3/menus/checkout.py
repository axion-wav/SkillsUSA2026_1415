import math, json, os

def checkout(inventory, cart):
    while True:
        # recalculate totals each time the checkout view opens.
        subtotal = 0

        for item in cart:
            sku = item[0]
            quantity = item[1]

            inv_item = next((inv for inv in inventory if inv["sku"] == sku), None)
            if not inv_item:
                continue

            price = quantity * inv_item["price"]
            subtotal += price
            print(f"{inv_item['name']} | Quantity: {quantity} | Price: ${price:.2f}")

        tax = subtotal * 0.08 * 100 / 100

        total = subtotal + tax

        print(f"\n\nSubtotal: ${subtotal:.2f}\n\nSales tax: ${tax:.2f}\n\nTotal: ${total:.2f}\n\n")
        key = input("Do you want to checkout? (0 to exit, 1 to checkout): ")
        if key == "1":
            # finalize purchase by reducing stock and recording a sales order.
            order_items = []

            for item in cart:
                sku = item[0]
                quantity = item[1]

                inv_item = next((inv for inv in inventory if inv["sku"] == sku), None)
                if not inv_item:
                    continue

                inv_item["quantity"] -= quantity
                order_items.append(
                    {
                        "sku": inv_item["sku"],
                        "name": inv_item["name"],
                        "quantity": quantity,
                        "price": inv_item["price"] * quantity
                    }
                )

            order = {
                "items": order_items,
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

            # persist the updated inventory after checkout completes.
            with open(path, "w") as f:
                json.dump({"inventory": inventory}, f, indent=4)

            print("Thank you for shopping with us! Your order confirmation will arrive shortly.")
            return []
        elif key == "0":
            return cart