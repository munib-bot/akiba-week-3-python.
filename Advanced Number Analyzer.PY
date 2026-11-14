def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
def get_divisors(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors
def sum_of_digits(number):
    sum = 0
    while number > 0:
       sum += number % 10
       number= number // 10
    return sum
def reverse_number(number):
    reversed_num = 0
    while number > 0:
        digit = number % 10
        reversed_num = (reversed_num * 10) + digit
        number //= 10
    return reversed_num
def analyze_number(number):
    analysis = {
        "number": number,
        "is_prime": is_prime(number),
        "divisors": get_divisors(number),
        "sum_of_digits": sum_of_digits(number),
        "reversed_number": reverse_number(number)
    }
    return analysis
print("Welcome to the Advanced Number Analyzer!")
print("Enter a number to analyze:")
number = int(input())
analysis = analyze_number(number)
for key, value in analysis.items():
    print(f"{key}: {value}")