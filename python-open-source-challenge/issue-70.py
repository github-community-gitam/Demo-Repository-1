def completion_by_day(days):
    percentages = {}
    for day, tasks in days.items():
        # Count only completed tasks
        completed = sum(tasks.values())
        total = len(tasks)

        # Calculate percentage using the actual total number of tasks
        percentages[day] = completed / total * 100 if total else 0

    # Days with no tasks are retained as 0%
    return percentages

def check_solution():
    days = {"Mon":{"task1":True,"task2":False},"Tue":{"task1":True,"task2":True},"Wed":{}}
    assert completion_by_day(days) == {"Mon":50.0,"Tue":100.0,"Wed":0}
    assert completion_by_day({}) == {}

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()