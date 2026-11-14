
def student_score(score):
    if not isinstance(score, (int, float)):
        return False, "Please enter a valid score data type"

    if 0 <= score <= 100:
        return True, "Valid score"
    else:
        return False, "Invalid score. Score must be between 0 and 100"


def student_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def average_score(students):
    if not students:
        return 0

    total_score = 0
    for student in students:
        total_score += student["score"]

    return total_score / len(students)


def highest_lowest_score(students):
    if not students:
        return None, None

    highest = students[0]["score"]
    lowest = students[0]["score"]

    for student in students:
        score = student["score"]

        if score > highest:
            highest = score

        if score < lowest:
            lowest = score

    return highest, lowest


def passed_fail(students):
    passed = 0
    failed = 0

    for student in students:
        if student["score"] >= 50:
            passed += 1
        else:
            failed += 1

    return passed, failed


def get_above_average_students(students):
    average = average_score(students)
    result = []

    for student in students:
        if student["score"] > average:
            result.append(student)

    return result


def generate_report(students):
    if not students:
        print("No student records available.")
        return

    average = average_score(students)
    highest, lowest = highest_lowest_score(students)
    passed, failed = passed_fail(students)
    above_average = get_above_average_students(students)

    print(" ===== CLASS REPORT =====")
    print(f"Total students: {len(students)}")
    print(f"Average score: {average:.2f}")
    print(f"Highest score: {highest}")
    print(f"Lowest score: {lowest}")
    print(f"Passed students: {passed}")
    print(f"Failed students: {failed}")

    print("----- Student Results -----")

    for student in students:
        score = student["score"]
        grade = student_grade(score)
        print(f"{student['name']}: {score} - Grade {grade}")

    print(" ----- Students Above Average -----")

    if above_average:
        for student in above_average:
            print(f"{student['name']}: {student['score']}")
    else:
        print("No students scored above average.")

    print("==========================")


students = [
    {"name": "Ali", "score": 95},
    {"name": "Hana", "score": 82},
    {"name": "Abdi", "score": 45},
    {"name": "Sara", "score": 35},
    {"name": "Omar", "score": 75}
]

generate_report(students)
