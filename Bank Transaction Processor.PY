balance = 100
daily_limit = 500
daily_withdrawn = 0

transactions = []
def deposit(amount):
    global balance
    if amount <= 0:
        print("Amount must be positive.")
        return

    balance += amount

    record_transaction("deposit", amount)
    print("Deposit successful.")

def withdraw(amount):
    global balance, daily_withdrawn

    if amount <= 0:
        print("Amount must be positive.")
        return

    if amount > balance:
        print("Insufficient balance.")
        return

    if amount > daily_limit - daily_withdrawn:
        print("Daily withdrawal limit exceeded.")
        return

    balance -= amount
    daily_withdrawn += amount

    record_transaction("withdrawal", amount)
    print("Withdrawal successful.")

def check_balance():
    print("Current balance:", balance)

def record_transaction(transaction_type, amount):
    transactions.append({
        "type": transaction_type,
        "amount": amount,
        "balance_after": balance
    })

def generate_transaction_summary():
    total_deposited = 0
    total_withdrawn = 0

    print("\nTransaction History:")

    for t in transactions:
        print(t)

        if t["type"] == "deposit":
            total_deposited += t["amount"]
        else:
            total_withdrawn += t["amount"]

    print("\nTransaction Summary:")
    print("Total deposited:", total_deposited)
    print("Total withdrawn:", total_withdrawn)
    print("Final balance:", balance)
    print("Daily withdrawal limit:", daily_limit)
    print("Remaining daily limit:", daily_limit - daily_withdrawn)

deposit(10)
withdraw(7)
deposit(26)
withdraw(8)
withdraw(5)
