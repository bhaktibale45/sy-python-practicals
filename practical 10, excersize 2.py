def search_inventory(products, item_name):
    # Search for the item
    if item_name in products:
        index = products.index(item_name)
        print(f"Item '{item_name}' is present in the inventory.")
        print(f"Index location: {index}")
    else:
        print(f"Item '{item_name}' was not found in the inventory.")


# Inventory catalog
products = [
    "Laptop",
    "Keyboard",
    "Mouse",
    "Monitor",
    "Printer",
    "Webcam"
]

# Get item name from the user
item_name = input("Enter the product name to search: ")

# Search the inventory
search_inventory(products, item_name)