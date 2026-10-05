# ISSUE 17
#
# Problem:
# Write a program that accepts a list of restaurant orders containing item names, quantities and prices and finds the total bill and most frequently ordered item.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def summarize_orders(orders):
    total = 0
    quantities = {}
    for order in orders:
        item = order["item"]
        quantity = order["quantity"]
        price = order["price"]
        # TODO: Check how each line contributes to the bill.
        total += price * quantity
        # TODO: Check how repeated item orders are combined.
        quantities[item] = quantities.get(item, 0) + quantity
    # TODO: Check how an empty order list is handled.
    popular = max(quantities, key=quantities.get, default="")
    # TODO: Check the values returned for both requested results.
    return total, popular

def check_solution():
    orders = [{"item":"tea","quantity":2,"price":3}, {"item":"cake","quantity":1,"price":5}, {"item":"tea","quantity":4,"price":3}]
    assert summarize_orders(orders) == (23, "tea")
    assert summarize_orders([]) == (0, "")

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
