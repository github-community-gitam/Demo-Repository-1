# ISSUE 67
#
# Problem:
# Write a program that accepts classroom marks from multiple tests and identifies students whose marks increased in every successive test.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def steadily_improving(students):
    improving = []
    for student in students:
        marks = student["tests"]

        # Check that each test mark is greater than the previous test
        if len(marks) >= 2 and all(
            marks[index] < marks[index + 1]
            for index in range(len(marks) - 1)
        ):
            improving.append(student["name"])

    return improving


def check_solution():
    students = [
        {"name": "A", "tests": [50, 60, 75]},
        {"name": "B", "tests": [70, 65, 80]},
        {"name": "C", "tests": [90]}
    ]

    assert steadily_improving(students) == ["A"]
    assert steadily_improving([]) == []

    print("All checks passed!")


if __name__ == "__main__":
    check_solution()