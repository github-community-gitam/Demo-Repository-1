# ISSUE 32
#
# Problem:
# Write a program that accepts marks of students in multiple subjects and finds the highest and lowest marks obtained in every subject.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def subject_extremes(students):
    subjects = {}
    for student in students:
        for subject, mark in student["marks"].items():
            # TODO: Check how both ends of the subject range are initialized.
            bounds = subjects.setdefault(subject, [mark, mark])
            # TODO: Check how a new high mark updates the range.
            bounds[0] = max(bounds[0], mark)
            # TODO: Check how a new low mark updates the range.
            bounds[1] = min(bounds[1], mark)
    # TODO: Check the order and meaning of each returned bound.
    return subjects

def check_solution():
    students = [{"name":"A","marks":{"math":80,"science":70}},{"name":"B","marks":{"math":95,"science":60}}]
    assert subject_extremes(students) == {"math":[95,80],"science":[70,60]}
    assert subject_extremes([]) == {}

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
