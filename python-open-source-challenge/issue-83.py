# ISSUE 83
#
# Problem:
# Write a program that accepts a list of transactions containing transaction type and amount and calculates the total deposits, total withdrawals and final balance.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def account_totals(transactions):
    deposits = withdrawals = 0
    for transaction in transactions:
        amount = transaction["amount"]
        # TODO: Check which transaction type increases the deposit total.
        if transaction["type"] == "deposit":
            deposits += amount
        elif transaction["type"] == "withdrawal":
            # TODO: Check how withdrawals are accumulated.
            withdrawals += amount
    # TODO: Check how the final account balance is derived.
    return deposits, withdrawals, deposits - withdrawals

def check_solution():
    rows = [{"type":"deposit","amount":100},{"type":"withdrawal","amount":30},{"type":"deposit","amount":20}]
    assert account_totals(rows) == (120,30,90)
    assert account_totals([]) == (0,0,0)

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
