# ISSUE 69
#
# Problem:
# Write a program that accepts nested product data containing categories, products, prices and quantities and calculates the total value of every category.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def category_inventory_value(categories):
    totals = {}
    for category, products in categories.items():
        value = 0
        for product in products:
            # TODO: Check how product quantity and price determine its value.
            value += product["price"] * product["quantity"]
        totals[category] = value
    # TODO: Check that empty categories remain in the result.
    return totals

def check_solution():
    products = {"food":[{"name":"rice","price":4,"quantity":3},{"name":"tea","price":2,"quantity":5}],"home":[]}
    assert category_inventory_value(products) == {"food":22,"home":0}
    assert category_inventory_value({}) == {}

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
