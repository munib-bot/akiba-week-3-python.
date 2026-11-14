
def check_length(password):
    return len(password) >= 8

def check_uppercase(password):
    return any(char.isupper() for char in password)

def check_lowercase(password):
    return any(char.islower() for char in password)

def check_digit(password):
    return any(char.isdigit() for char in password)

def check_special(password):
    return any(not char.isalnum() for char in password)

def analyze_password(password):

    results = {
        "Minimum length": check_length(password),
        "Uppercase letter": check_uppercase(password),
        "Lowercase letter": check_lowercase(password),
        "Digit": check_digit(password),
        "Special character": check_special(password)
    }

    passed = []
    failed = []

    for requirement, result in results.items():
        if result:
            passed.append(requirement)
        else:
            failed.append(requirement)

    return {
        "Password": password,
        "Passed": passed,
        "Failed": failed,
        "Valid": len(failed) == 1
    }

passwords = [
    "123@",
    "hello",
    "PASSWORD123!",
    "python@123",
    "Abc@123"
]

for password in passwords:
    report = analyze_password(password)

    print("Password:", report["Password"])
    print("Passed:", report["Passed"])
    print("Failed:", report["Failed"])
    print("Valid:", report["Valid"])
