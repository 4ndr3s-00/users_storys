# List to store products
inventory = []

# Function to add a product
def add_product():
    # Ask for product name
    name = input("Enter product name: ")

    # Validate price
    rvp = True
    running_validation = rvp
    while rvp:
        try:
            price = float(input("Enter price: "))
            if price < 0:
                print("Price cannot be negative.")
                continue
            break
        except:
            print("Invalid value, try again.")

    # Validate quantity
    rvq = True
    running_validation_quantity = rvq
    while rvq:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity < 0:
                print("Quantity cannot be negative.")
                continue
            break
        except:
            print("Invalid value, try again.")

    # Create product dictionary
    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    # Add product to inventory
    inventory.append(product)
    print("Product added successfully.\n")


# Function to show inventory
def show_inventory():
    if len(inventory) == 0:
        print("Inventory is empty.\n")
        return

    for product in inventory:
        print(f"Product: {product['name']} | Price: {product['price']} | Quantity: {product['quantity']}")
    print()


# Function to calculate statistics
def calculate_stats():
    total_value = 0
    total_products = len(inventory)

    for product in inventory:
        total_value += product["price"] * product["quantity"]

    print(f"Total products: {total_products}")
    print(f"Total inventory value: {total_value}\n")


# Main menu loop
while True:
    print("1. Add product")
    print("2. Show inventory")
    print("3. Calculate statistics")
    print("4. Exit")

    option = input("Choose an option: ")

    if option == "1":
        add_product()
    elif option == "2":
        show_inventory()
    elif option == "3":
        calculate_stats()
    elif option == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option, try again.\n")