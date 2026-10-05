# ISSUE 89
#
# Problem:
# Write a program that accepts a list of numbers and finds all continuous subarrays whose sum is equal to a given target.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def subarrays_with_sum(numbers, target):
    matches = []
    for start in range(len(numbers)):
        total = 0
        for end in range(start, len(numbers)):
            # TODO: Check how the current value changes the running sum.
            total += numbers[end]
            if total == target:
                matches.append(numbers[start:end + 1])
    # TODO: Check that every possible starting position is visited.
    return matches

def check_solution():
    assert subarrays_with_sum([1,2,3,2],5) == [[2,3],[3,2]]
    assert subarrays_with_sum([],0) == []

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
