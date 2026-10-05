# ISSUE 4
#
# Problem:
# Write a program that accepts a list of integers and calculates the sum of all positive numbers.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def positive_sum(values):
    # TODO: Check how the running total should start.
    total = 0

    # TODO: Check whether the first list item is skipped.
    for value in values[0:]:
        # TODO: Check the boundary used to select positive values.
        if value >= 0:
            # TODO: Check how each qualifying number changes the total.
            total += value

    # TODO: Check which result is returned to the caller.
    return total

def check_solution():
    assert positive_sum([-2, 3, 0, 5]) == 8
    assert positive_sum([2, -7, 4]) == 6
    assert positive_sum([-1, 0]) == 0

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
