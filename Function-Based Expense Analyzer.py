
def Add_an_expense():
    expense_name = input("Enter the name of the expense: ")
    category = input("Enter the category: ")
    expense_amount = float(input("Enter the amount of the expense: "))
    
    return {
        "description": expense_name,
        "category": category,
        "amount": expense_amount
    }
def Calculate_total_expenses(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total
def calculate_by_category(expenses):
    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
    return category_totals
def find_highest_expense(expenses):
    if not expenses:
        return None
    highest_expense = max(expenses, key=lambda x: x["amount"])
    return highest_expense
def get_expenses_above_threshold(expenses, threshold):
    return [
        expense for expense in expenses
        if expense["amount"] > threshold
    ]
def generate_spending_report(expenses):
    total_expenses = Calculate_total_expenses(expenses)
    category_totals = calculate_by_category(expenses)
    highest_expense = find_highest_expense(expenses)

    report = {
        "total_expenses": total_expenses,
        "category_totals": category_totals,
        "highest_expense": highest_expense
    }
    return report
def expense_example():
    expenses = [
        {"description": "Lunch", "category": "Food", "amount": 180},
        {"description": "Taxi", "category": "Transport", "amount": 120},
        {"description": "Groceries", "category": "Food", "amount": 450},
        {"description": "Internet", "category": "Bills", "amount": 300}
    ]
    return expenses
expenses = expense_example()
new_expense = Add_an_expense()
expenses.append(new_expense)

report = generate_spending_report(expenses)
print("===== SPENDING REPORT =====")
print("Total expenses:", report["total_expenses"])
print("Expenses by category:")
for category, amount in report["category_totals"].items():
    print(f"{category}: {amount}")
print("Highest expense:")
print(report["highest_expense"])
print("Expenses above 200:")
above_threshold = get_expenses_above_threshold(expenses, 200)
for expense in above_threshold:
    print(expense)
