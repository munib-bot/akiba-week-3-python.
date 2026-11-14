inventory = []
def add_new_product():
    product_name = input("Enter the product name: ")
    product_quantity = int(input("Enter the product quantity: "))
    product_price = float(input("Enter the product price: "))

    new_product = {
        "name": product_name,
        "quantity": product_quantity,
        "price": product_price
    }

    inventory.append(new_product)
    print(f"Product '{product_name}' added successfully!")
def search_product():
    search_name = input("Enter the product name to search: ")
    found_products = [product for product in inventory if product["name"].lower() == search_name.lower()]

    if found_products:
        print("Product(s) found:")
        for product in found_products:
            print(f"Name: {product['name']}, Quantity: {product['quantity']}, Price: ${product['price']:.2f}")
    else:
        print(f"No product found with the name '{search_name}'.")
def update_product_price():
    product_name = input("Enter the product name to update the price: ")
    found_products = [product for product in inventory if product["name"].lower() == product_name.lower()]

    if found_products:
        new_price = float(input(f"Enter the new price for '{product_name}': "))
        for product in found_products:
            product["price"] = new_price
        print(f"Price for '{product_name}' updated successfully!")
    else:
        print(f"No product found with the name '{product_name}'.")
def increase_stock():
    product_name = input("Enter the product name to increase stock: ")
    found_products = [product for product in inventory if product["name"].lower() == product_name.lower()]

    if found_products:
        additional_quantity = int(input(f"Enter the quantity to add for '{product_name}': "))
        for product in found_products:
            product["quantity"] += additional_quantity
        print(f"Stock for '{product_name}' increased by {additional_quantity}.")
    else:
        print(f"No product found with the name '{product_name}'.")
def sell_product():
    product_name = input("Enter the product name to sell: ")
    found_products = [product for product in inventory if product["name"].lower() == product_name.lower()]

    if found_products:
        sell_quantity = int(input(f"Enter the quantity to sell for '{product_name}': "))
        for product in found_products:
            if product["quantity"] >= sell_quantity:
                product["quantity"] -= sell_quantity
                print(f"Sold {sell_quantity} of '{product_name}'.")
            else:
                print(f"Not enough stock for '{product_name}'. Available quantity: {product['quantity']}.")
    else:
        print(f"No product found with the name '{product_name}'.")
def calculate_total_value():
     total_value = sum(product["quantity"] * product["price"] for product in inventory)
     print(f"Total value of inventory: ${total_value:.2f}")
def generate_low_stock_report():
    if not inventory:
        print("Inventory is empty.")
        return

    print("\nInventory Report:")
    for product in inventory:
        print(f"Name: {product['name']}, Quantity: {product['quantity']}, Price: ${product['price']:.2f}")
add_new_product() 
search_product() 
update_product_price() 
increase_stock() 
sell_product() 
calculate_total_value() 
generate_low_stock_report()