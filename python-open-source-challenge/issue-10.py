# ISSUE 10
#
# Problem:
# Write a program that accepts a list of integers and finds all the duplicate elements using a set.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def duplicates(values):
    seen = set()
    repeated = set()
    for value in values:
        # TODO: Check how previously observed values are detected.
        if value in seen:
            repeated.add(value)
        seen.add(value)
    # TODO: Check whether the result contains only values seen more than once.
    return repeated
    # TODO: Check whether the result preserves the required information.
    # TODO: Check behavior when the input contains only one item.
    # TODO: Check the result when there are no matching values.
    # TODO: Check that the calculation uses the intended values.

def check_solution():
    assert duplicates([1, 2, 1, 3, 2]) == {1, 2}
    assert duplicates([4, 5]) == set()
    assert duplicates([8, 8, 8]) == {8}

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
