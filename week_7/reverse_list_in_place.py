def reverse_list_in_place(lst):
    """reverse list in place. input: list"""

    for index in range(len(lst)/2):

        index_to_swap = (index + 1) * -1

        # swap values at these indexes
        lst[index], lst[index_to_swap] = lst[index_to_swap], lst[index]






