my_list = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]


# this works, but is in O(n lg n) time which
# is not very good
def merge_lists_slow(list1, list2):
    list1 = list1 + list2
    print(sorted(list1))


# Faster way
# time:O(n)
# space: O(n)
def merge_lists(list_1, list_2):
    # get size
    merged_list_size = len(list_1) + len(list_2)
    # make empty list of correct size
    merged_list = [None] * merged_list_size

    # set index for all list 
    current_list_1 = 0
    current_index_2 = 0
    current_index_merged = 0
    
    # loop through the entire size of the merged list
    while current_index_merged < merged_list_size:

        # these two below are used to track if we have seen all
        # items in their respective lists
        is_list_1_exhausted = current_list_1 >= len(list_1)
        is_alices_list_exhausted = current_index_2 >= len(list_2)

        # which list do we pull the value from?
        if (not is_list_1_exhausted and
                (is_alices_list_exhausted or
                 list_1[current_list_1] < list_2[current_index_2])):

            merged_list[current_index_merged] = list_1[current_list_1]
            current_list_1 += 1
        else:
            # we look at list 2
            merged_list[current_index_merged] = list_2[current_index_2]
            current_index_2 += 1

        current_index_merged += 1

    return print(merged_list)


merge_lists(my_list, alices_list)
# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
# print(merge_lists(my_list, alices_list))
