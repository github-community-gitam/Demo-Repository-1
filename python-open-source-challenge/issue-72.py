def category_values(products):
    totals = {}
    for product in products:
        category = product["category"]

        # Calculate product value
        value = product["price"] * product["quantity"]

        # Add value to the category total
        totals[category] = totals.get(category, 0) + value

    # Handle empty product list
    if not totals:
        return {}, ""

    # Find the category with the highest value
    highest = max(totals, key=totals.get)

    return totals, highest


def check_solution():
    products = [
        {"category":"grocery","price":3,"quantity":10},
        {"category":"grocery","price":5,"quantity":4},
        {"category":"toys","price":12,"quantity":2},
        {"category":"books","price":7,"quantity":9},
    ]

    assert category_values(products) == (
        {"grocery":50,"toys":24,"books":63},
        "books"
    )

    assert category_values([]) == ({}, "")

    print("All checks passed!")


if __name__ == "__main__":
    check_solution()