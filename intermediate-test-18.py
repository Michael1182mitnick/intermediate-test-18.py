# Write a function to sort a list of dictionaries by a specific key in ascending or descending order.

def sort_dicts_by_key(dicts_list, key, reverse=False):
    """
    Sort a list of dictionaries by a specific key.

    :param dicts_list: List of dictionaries to be sorted.
    :param key: The key in the dictionary to sort by.
    :param reverse: Set to True for descending order, False for ascending order (default is False).
    :return: A new list of dictionaries sorted by the specified key.
    """
    return sorted(dicts_list, key=lambda x: x[key], reverse=reverse)


# Example usage
dicts_list = [
    {'name': 'Alice', 'age': 30, 'salary': 70000},
    {'name': 'Bob', 'age': 25, 'salary': 50000},
    {'name': 'Charlie', 'age': 35, 'salary': 80000},
    {'name': 'David', 'age': 28, 'salary': 60000}
]

# Sort by 'age' in ascending order
sorted_by_age = sort_dicts_by_key(dicts_list, key='age')
print("Sorted by age (ascending):")
print(sorted_by_age)

# Sort by 'salary' in descending order
sorted_by_salary_desc = sort_dicts_by_key(
    dicts_list, key='salary', reverse=True)
print("\nSorted by salary (descending):")
print(sorted_by_salary_desc)
