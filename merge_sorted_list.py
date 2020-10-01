my_list = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]


# this works, but is in O(n lg n) time which
# is not very good
def merge_lists_slow(list1, list2):
    list1 = list1 + list2
    print(sorted(list1))


# An alternative is
def merge_lists(list1, list2):



merge_lists(my_list, alices_list)
# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
# print(merge_lists(my_list, alices_list))