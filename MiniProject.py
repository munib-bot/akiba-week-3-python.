# ==========================================
# 1. PRODUCT MANAGEMENt
# ==========================================
products = {}
def add_product(product_id, name, price, stock):
    # Adds a new product to the inventory
    if product_id in products:
        print(f"Error: Product ID '{product_id}' already exists.")
        return
    products[product_id] = {
        "name": name,
        "price": price,
        "stock": stock
    }
    print(f"Product '{name}' added successfully!")

def search_product(product_id):
    # Searches for a product by its ID.
    return products.get(product_id, None)

def update_product(product_id, name=None, price=None, stock=None):
    # Updates product details.
    if product_id not in products:
        print(f"Error: Product ID '{product_id}' not found.")
        return
    
    if name is not None:
        products[product_id]["name"] = name
    if price is not None:
        products[product_id]["price"] = price
    if stock is not None:
        products[product_id]["stock"] = stock
    print(f"Product '{product_id}' updated successfully.")

def display_all_products():
    # Displays all available products.
    if not products:
        print("\nNo products available.")
        return
    print("\n--- Current Inventory ---")
    for pid, details in products.items():
        print(f"ID: {pid} | Name: {details['name']} | Price: ${details['price']:.2f} | Stock: {details['stock']}")

# ==========================================
# 2. SALES MANAGEMENT
# ==========================================

sales_history = []

def record_sale(product_id, quantity):
    # Processes transactions, updates stock, and logs sales history.
    product = search_product(product_id)
    
    if not product:
        print(f"Sale failed: Product ID '{product_id}' does not exist.")
        return False

    # Validate stock quantity
    if quantity <= 0:
        print("Sale failed: Quantity must be greater than zero.")
        return False
    if product["stock"] < quantity:
        print(f"Sale failed: Insufficient stock. Only {product['stock']} available.")
        return False

    # Reduce stock
    product["stock"] -= quantity
    total_sale = product["price"] * quantity

    # Log transaction
    sales_history.append({
        "product_id": product_id,
        "name": product["name"],
        "quantity": quantity,
        "total": total_sale
    })

    print(f"Sale successful! Purchased {quantity}x '{product['name']}' for ${total_sale:.2f}.")
    return True

# ==========================================
# 3. REPORTING 
# ==========================================

def display_sales_report():
    # Summarizes and displays business sales performance.
    print("\n--- Sales & Revenue Report ---")
    if not sales_history:
        print("No sales have been recorded yet.")
        return

    total_revenue = sum(sale["total"] for sale in sales_history)
    total_items_sold = sum(sale["quantity"] for sale in sales_history)

    for idx, sale in enumerate(sales_history, start=1):
        print(f"{idx}. {sale['name']} (x{sale['quantity']}) - ${sale['total']:.2f}")

    print(f"\nTotal Items Sold: {total_items_sold}")
    print(f"Total Revenue Generated: ${total_revenue:.2f}")

# ==========================================
# MAIN APPLICATION
# ==========================================

def main():
    # Adding initial sample products for testing
    add_product("P101", "Laptop", 750.00, 10)
    add_product("P102", "Wireless Mouse", 25.00, 50)

    while True:
        print("\n==========================================")
        print("   AKIBA BUSINESS MANAGEMENT TOOLKIT      ")
        print("==========================================")
        print("1. Add Product")
        print("2. Search Product")
        print("3. Update Product")
        print("4. Display All Products")
        print("5. Record a Sale")
        print("6. View Sales Report")
        print("7. Exit")
        
        choice = input("\nEnter choice (1-7): ").strip()

        if choice == "1":
            pid = input("Enter Product ID: ").strip()
            name = input("Enter Product Name: ").strip()
            price = float(input("Enter Product Price: "))
            stock = int(input("Enter Initial Stock: "))
            add_product(pid, name, price, stock)

        elif choice == "2":
            pid = input("Enter Product ID to search: ").strip()
            item = search_product(pid)
            if item:
                print(f"Found: {item['name']} | Price: ${item['price']:.2f} | Stock: {item['stock']}")
            else:
                print("Product not found.")
                

        elif choice == "3":
            pid = input("Enter Product ID to update: ").strip()
            if search_product(pid):
                name = input("Enter new name (leave blank to keep current): ").strip() or None
                price_str = input("Enter new price (leave blank to keep current): ").strip()
                stock_str = input("Enter new stock (leave blank to keep current): ").strip()
                
                price = float(price_str) if price_str else None
                stock = int(stock_str) if stock_str else None
                
                update_product(pid, name, price, stock)
            else:
                print("Product not found.")

        elif choice == "4":
            display_all_products()

        elif choice == "5":
            pid = input("Enter Product ID to purchase: ").strip()
            qty = int(input("Enter quantity: "))
            record_sale(pid, qty)

        elif choice == "6":
            display_sales_report()

        elif choice == "7":
            print("Exiting application. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 7.")

if __name__ == "__main__":
    main()