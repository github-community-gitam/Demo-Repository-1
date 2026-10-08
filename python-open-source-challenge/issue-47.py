# ISSUE 47
#
# Problem:
# Write a program that accepts a list of students and their grades and groups the students by grade while calculating the average marks for every grade.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def students_by_grade(students):
    groups = {}
    marks_by_grade = {}
    for student in students:
        grade = student["grade"]
        bucket = groups.setdefault(grade, [])
        # TODO: Check that student names stay in the grade group.
        bucket.append(student["name"])
        marks_by_grade.setdefault(grade, []).append(student["mark"])
    # TODO: Check how each grade's marks are averaged.
    averages = {grade: sum(marks) / (len(marks)) for grade, marks in marks_by_grade.items()}
    # TODO: Check that every grade has an average in the result.
    return groups, averages

def check_solution():
    students = [{"name":"A","grade":"B","mark":80},{"name":"B","grade":"B","mark":60},{"name":"C","grade":"A","mark":90}]
    assert students_by_grade(students) == ({"B":["A","B"],"A":["C"]},{"B":70,"A":90})
    assert students_by_grade([]) == ({},{})

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
