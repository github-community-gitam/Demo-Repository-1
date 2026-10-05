# ISSUE 84
#
# Problem:
# Write a program that accepts temperature records for several cities over multiple days and finds the average, highest and lowest temperature for every city.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def city_temperature_report(readings):
    by_city = {}
    for reading in readings:
        values = by_city.setdefault(reading["city"], [])
        # TODO: Check which temperature value is stored for the city.
        values.append(reading["temperature"])
    # TODO: Check how the average is computed from the city readings.
    return {city:{"average":sum(values)/len(values),"highest":max(values),"lowest":min(values)} for city,values in by_city.items()}

def check_solution():
    readings = [{"city":"Delhi","day":1,"temperature":30},{"city":"Delhi","day":2,"temperature":20},{"city":"Oslo","day":1,"temperature":5}]
    assert city_temperature_report(readings) == {"Delhi":{"average":25,"highest":30,"lowest":20},"Oslo":{"average":5,"highest":5,"lowest":5}}
    assert city_temperature_report([]) == {}

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
