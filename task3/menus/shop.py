def shop(inventory, cart):
    while True:
        for item in inventory:
            print(f"{item["sku"]}: {item["name"]} | Price: ${item["price"]} | Inventory: {item["quantity"]}")

        selected_sku = int(input("\n\nSelect an item (0 to exit): "))

        if any(item["sku"] == selected_sku for item in inventory):
            while True:
                selected_quantity = int(input("\rSelect a quantity (0 to cancel): "))
                if inventory[(selected_sku - 1)]["quantity"] >= selected_quantity and selected_quantity > 0:
                    cart.append((selected_sku - 1, selected_quantity))
                    print(f"{selected_quantity} {inventory[(selected_sku - 1)]["name"]} added to Cart!")
                    break
                elif selected_quantity == 0:
                    break
                else:
                    print("Invalid Quantity.")
        elif selected_sku == 0:
            return(cart)
        else:
            print("Invalid SKU.")