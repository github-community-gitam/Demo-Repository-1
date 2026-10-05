# ISSUE 88
#
# Problem:
# Write a program that accepts a list of integers and finds the longest continuous section in which no number is repeated.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def longest_unique_run(values):
    best = []
    current = []
    for value in values:
        # TODO: Check how the run changes when a duplicate appears.
        if value in current:
            current = current[current.index(value) + 1 :]
        current.append(value)
        # TODO: Check when a new run replaces the best one.
        if len(current) > len(best):
            best = current[:]
    # TODO: Check behavior when the input is empty.
    return best

def check_solution():
    assert longest_unique_run([1,2,3,2,4,5]) == [3,2,4,5]
    assert longest_unique_run([]) == []

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
