# ISSUE 74
#
# Problem:
# Write a program that accepts student attendance records and calculates each student's attendance percentage, then identifies the students below a given percentage. Sessions marked "excused" are not counted against a student at all and must be left out of the calculation entirely.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def attendance_report(records, minimum_percent):
    counted = {}
    present = {}
    for record in records:
        student = record["student"]
        # TODO: Check which sessions belong in the denominator.
        counted[student] = counted.get(student, 0) + 1
        # TODO: Check which attendance values count as present.
        if record["status"] != "absent":
            present[student] = present.get(student, 0) + 1
    percentages = {student: present.get(student, 0) / total * 100 for student, total in counted.items()}
    # TODO: Check which students fall below the requested threshold.
    below = [student for student, percent in percentages.items() if percent < minimum_percent]
    # TODO: Check that percentages for all students are returned.
    return percentages, below

def check_solution():
    records = [
        {"student":"Maya","status":"present"},{"student":"Maya","status":"present"},
        {"student":"Maya","status":"absent"},{"student":"Maya","status":"absent"},
        {"student":"Omar","status":"present"},{"student":"Omar","status":"present"},
        {"student":"Omar","status":"present"},{"student":"Omar","status":"excused"},
        {"student":"Priya","status":"present"},{"student":"Priya","status":"absent"},
        {"student":"Priya","status":"absent"},{"student":"Priya","status":"absent"},
    ]
    assert attendance_report(records, 60) == ({"Maya":50.0,"Omar":100.0,"Priya":25.0},["Maya","Priya"])
    assert attendance_report([], 50) == ({},[])

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
