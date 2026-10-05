# ISSUE 7
#
# Problem:
# Write a program that accepts a string and counts the frequency of every character using a dictionary.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def character_counts(text):
    counts = {}
    for char in text:
        # TODO: Check the initial count for a character.
        counts[char] = counts.get(char, 0) + 1
    # TODO: Check that case-sensitive characters remain distinct.
    return counts
    # TODO: Check whether the result preserves the required information.
    # TODO: Check behavior when the input contains only one item.
    # TODO: Check the result when there are no matching values.
    # TODO: Check that the calculation uses the intended values.

def check_solution():
    assert character_counts("aba") == {"a": 2, "b": 1}
    assert character_counts("AaA") == {"A": 2, "a": 1}
    assert character_counts("") == {}

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
