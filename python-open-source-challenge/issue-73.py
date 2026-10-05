# ISSUE 73
#
# Problem:
# Write a program that accepts employee records containing department, salary and performance score and finds the average salary and highest-performing employee in each department.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def department_performance(employees):
    salary_totals, counts, top_by_dept = {}, {}, {}
    for employee in employees:
        department = employee["department"]
        salary = employee["salary"]
        # TODO: Check how salary totals are accumulated by department.
        salary_totals[department] = salary_totals.get(department, 0) + salary
        counts[department] = counts.get(department, 0) + 1
        # TODO: Check which performance score should replace the current leader.
        if department not in top_by_dept or employee["performance_score"] > top_by_dept[department]["performance_score"]:
            top_by_dept[department] = employee
    averages = {dept: total / counts[dept] for dept, total in salary_totals.items()}
    # TODO: Check that the top employee record has the expected shape.
    # TODO: Check how the selected employee records are reported.
    leaders = {dept: employee["name"] for dept, employee in top_by_dept.items()}
    return averages, leaders

def check_solution():
    employees = [{"name":"A","department":"Design","salary":40,"performance_score":70},{"name":"B","department":"Design","salary":60,"performance_score":90},{"name":"C","department":"Sales","salary":80,"performance_score":85}]
    assert department_performance(employees) == ({"Design":50,"Sales":80},{"Design":"B","Sales":"C"})
    assert department_performance([]) == ({},{})

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
