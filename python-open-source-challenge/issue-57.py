# ISSUE 57
#
# Problem:
# Write a program that accepts mobile usage records containing call duration and data usage and calculates the charges for every user.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def mobile_charges(usages):
    charges = {}
    for usage in usages:
        user = usage["user"]
        # TODO: Check the per-minute call charge.
        cost = usage["call_minutes"] * 0.10
        # TODO: Check the data charge included in each record.
        cost += usage["data_gb"] * 2
        # TODO: Check how multiple records for one user are accumulated.
        charges[user] = charges.get(user, 0) + cost
    # TODO: Check that users with no usage aren't fabricated.
    return charges

def check_solution():
    usages = [{"user":"A","call_minutes":10,"data_gb":1},{"user":"B","call_minutes":0,"data_gb":2},{"user":"A","call_minutes":20,"data_gb":0}]
    assert mobile_charges(usages) == {"A":5.0,"B":4}
    assert mobile_charges([]) == {}

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
