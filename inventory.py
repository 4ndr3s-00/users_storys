# Ask for the product name
product_name = input("Enter the product name: ")

# Validate price input
running = True
while running:
    try:
        price = float(input("Enter the price: "))
        if price < 0:
            print("Price cannot be negative.")
            continue
        break
    except:
        print("Invalid value, try again.")

# Validate quantity input
while True:
    try:
        quantity = int(input("Enter the quantity: "))
        if quantity < 0:
            print("Quantity cannot be negative.")
            continue
        break
    except:
        print("Invalid value, try again.")

# Calculate total cost
total_cost = price * quantity

# Display results
print("\n--- SUMMARY ---")
print(f"Product: {product_name}")
print(f"Unit price: {price}")
print(f"Quantity: {quantity}")
print(f"Total cost: {total_cost}")