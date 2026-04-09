def shop(inventory, cart):
    while True:
        # show current stock so the shopper can choose a sku.
        for item in inventory:
            print(f"SKU {item['sku']}: {item['name']} | Price: ${item['price']} | Inventory: {item['quantity']}")

        try:
            selected_sku = int(input("\n\nSelect an item (0 to exit): "))
        except ValueError:
            print("Invalid SKU.")
            continue

        selected_item = next((item for item in inventory if item["sku"] == selected_sku), None)

        if selected_item:
            while True:
                try:
                    selected_quantity = int(input("\rSelect a quantity (0 to cancel): "))
                except ValueError:
                    print("Invalid Quantity.")
                    continue

                if selected_item["quantity"] >= selected_quantity and selected_quantity > 0:
                    cart.append((selected_sku, selected_quantity))
                    print(f"{selected_quantity} {selected_item['name']} added to Cart!")
                    break
                elif selected_quantity == 0:
                    break
                else:
                    print("Invalid Quantity.")
        elif selected_sku == 0:
            return(cart)
        else:
            print("Invalid SKU.")