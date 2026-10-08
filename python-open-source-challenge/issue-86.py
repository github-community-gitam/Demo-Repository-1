# ISSUE 86
#
# Problem:
# Write a program that accepts a sentence and creates a dictionary containing each word and the number of times it appears, treating uppercase and lowercase letters as the same.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def word_frequencies(sentence):
    counts = {}
    for word in sentence.lower().split():
        # TODO: Check how each repeated word changes the dictionary count.
        counts[word] = counts.get(word, 0) + 1
    # TODO: Check that words with different capitalization share a key.
    return counts

def check_solution():
    assert word_frequencies("Go go STOP stop stop") == {"go":2,"stop":3}
    assert word_frequencies("") == {}

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
