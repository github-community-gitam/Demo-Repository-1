# ISSUE 55
#
# Problem:
# Write a program that accepts library book details and the number of overdue days and calculates the fine for each borrowed book.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def overdue_fines(books, daily_rate=0.5):
    fines = {}
    for book in books:
        if book["borrowed"]:
            days = book["overdue_days"]
            # TODO: Check how the daily charge is applied.
            fines[book["title"]] = days* daily_rate
    # TODO: Check that borrowed books alone receive a fine.
    return fines

def check_solution():
    books = [{"title":"A","borrowed":True,"overdue_days":4},{"title":"B","borrowed":False,"overdue_days":7},{"title":"C","borrowed":True,"overdue_days":0}]
    assert overdue_fines(books) == {"A":2.0,"C":0}
    assert overdue_fines([]) == {}

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
