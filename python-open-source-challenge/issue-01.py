# ISSUE 1 
# 
# Problem: 
# Write a program that accepts a string and finds the positions of all vowels in it. 
# 
# This file contains an incomplete implementation. 
# Do not rewrite the program from scratch. 
# 
# Find and repair the mistakes marked with TODO comments. 
# 
# After repairing the code, run this file and make sure all 
# checks pass before submitting your Pull Request. 
 
def vowel_positions(text): 
    positions = [] 
    for index, char in enumerate(text): 
        # TODO: Check which vowels are accepted and how positions are counted. 
        if char.lower() in "aeiou": 
            positions.append(index) 
    # TODO: Check that every matching character is included. 
    return positions 
    # TODO: Check whether the result preserves the required information. 
    # TODO: Check behavior when the input contains only one item. 
    # TODO: Check the result when there are no matching values. 
    # TODO: Check that the calculation uses the intended values. 
 
def check_solution(): 
    assert vowel_positions("OpenAI") == [0, 2, 4, 5] 
    assert vowel_positions("queue") == [1, 2, 3, 4] 
    assert vowel_positions("rhythm") == [] 
 
    print("All checks passed!") 
 
if __name__ == "__main__": 
    check_solution()