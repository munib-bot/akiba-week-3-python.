def calculate_subtotal(items):
    subtotal = 0
    for item in items:
       subtotal += item["price"]*item["quantity"]
    return subtotal
def calculate_discount(subtotal):
    if subtotal >= 3000:
        return subtotal*0.1
    elif subtotal >= 1000:
        return subtotal * 0.05
    else:
        return 0.0
def calculate_tax(amount,tax_rate):
    return amount*tax_rate
def generate_receipt(items,tax_rate):
    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal)
    taxable_amount = subtotal - discount
    tax = calculate_tax(taxable_amount, tax_rate)
    final_total = taxable_amount + tax
    
    return {
        "subtotal": subtotal,
        "discount": discount,
        "tax": tax,
        "final_total": final_total
    }

items = [
    {"name": "Notebook", "price": 3000, "quantity": 3},
    {"name": "Pen", "price": 300, "quantity": 5}
]

receipt = generate_receipt(items, 0.05)

print(f"Subtotal: {receipt['subtotal']} Birr")
print(f"Discount: {receipt['discount']} Birr")
print(f"Tax: {receipt['tax']:.2f} Birr")
print(f"Final Amount: {receipt['final_total']:.2f} Birr")