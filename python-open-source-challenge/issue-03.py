# ISSUE 3
#
# Problem:
# Write a program that accepts a sentence and finds the length of every word in the sentence.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def word_lengths(sentence):
    words = sentence.split()
    lengths = {}
    for word in words:
        # TODO: Check how repeated words and their lengths are recorded.
        lengths[word] = len(word)
    # TODO: Check punctuation and whitespace behavior.
    return lengths
    # TODO: Check whether the result preserves the required information.
    # TODO: Check behavior when the input contains only one item.
    # TODO: Check the result when there are no matching values.
    # TODO: Check that the calculation uses the intended values.

def check_solution():
    assert word_lengths("red blue") == {"red": 3, "blue": 4}
    assert word_lengths("red blue red") == {"red": 3, "blue": 4}
    assert word_lengths("") == {}

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
