# ISSUE 60
#
# Problem:
# Write a program that accepts a list of expenses containing person, category and amount and finds the total expense for every category.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def expense_totals(expenses):
    totals = {}
    for expense in expenses:
        category = expense["category"]
        # TODO: Check how each expense amount changes its category total.
        totals[category] = totals.get(category, 0) + expense["amount"]
    # TODO: Check that each category is represented once.
    return totals

def check_solution():
    expenses = [{"person":"A","category":"food","amount":12},{"person":"B","category":"food","amount":8},{"person":"A","category":"travel","amount":20}]
    assert expense_totals(expenses) == {"food":20,"travel":20}
    assert expense_totals([]) == {}

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
