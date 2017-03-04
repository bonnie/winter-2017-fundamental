def get_factorial(num):
    """return the factorial of num"""

    # base case
    if num == 1:
        return 1 # which is num in this case

    total = num * get_factorial(num - 1)

    return total

get_factorial(1)


def sum_list_recursively(lst):
    """return the sum of a list of integers, recursively"""

    # base case
    if lst == []:
        return 0

    # recursive case
    return lst[0] + sum_list_recursively(lst[1:])
