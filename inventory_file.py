import json

# File name
FILE_NAME = "inventory.json"


# Load inventory from file
def load_inventory():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []


# Save inventory to file
def save_inventory(inventory):
    with open(FILE_NAME, "w") as file:
        json.dump(inventory, file, indent=4)


# Add product
def add_product(inventory):
    name = input("Enter product name: ")

    # Validate price
    valid_price = False
    while not valid_price:
        try:
            price = float(input("Enter price: "))
            if price < 0:
                print("Price cannot be negative.")
            else:
                valid_price = True
        except:
            print("Invalid value.")

    # Validate quantity
    valid_quantity = False
    while not valid_quantity:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity < 0:
                print("Quantity cannot be negative.")
            else:
                valid_quantity = True
        except:
            print("Invalid value.")

    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    inventory.append(product)
    save_inventory(inventory)

    print("Product saved.\n")


# Show inventory
def show_inventory(inventory):
    if len(inventory) == 0:
        print("Inventory is empty.\n")
        return

    print("\n--- INVENTORY ---")
    for product in inventory:
        print(f"{product['name']} | {product['price']} | {product['quantity']}")
    print()


# Main menu
def main():
    inventory = load_inventory()
    running = True

    while running:
        print("1. Add product")
        print("2. Show inventory")
        print("3. Exit")

        option = input("Choose: ")

        if option == "1":
            add_product(inventory)
        elif option == "2":
            show_inventory(inventory)
        elif option == "3":
            print("Goodbye!")
            running = False
        else:
            print("Invalid option\n")


main()