# ISSUE 78
#
# Problem:
# Write a program that accepts student marks and converts them into grades, then counts how many students received each grade.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def grade_counts(marks):
    counts = {}
    for name, mark in marks.items():
        # TODO: Check the boundaries used to assign each grade.
        grade = "A" if mark >= 90 else "B" if mark >= 75 else "C" if mark >= 60 else "F"
        # TODO: Check how students sharing a grade are counted.
        counts[grade] = counts.get(grade, 0) + 1
    # TODO: Check that grades with no students are treated consistently.
    return counts

def check_solution():
    assert grade_counts({"Ava":95,"Bo":80,"Cy":61,"Dee":40}) == {"A":1,"B":1,"C":1,"F":1}
    assert grade_counts({}) == {}

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
