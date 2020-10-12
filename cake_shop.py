# Runtime -
# Space complexity -
def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    # how do we assign values to each order?

    # Assign values to each order

    # compare to see if the values are
    # increasing order or same
    # ex: [1, 2, 4, 4, 5, 6]
    # we look at 1, 2, 4, etc. Once all have
    # been seen we return True
    # ex: [1, 2, 7, 4, 5, 6]
    # once we would get to 7 we would return False
    # no need to continue

    i = 0
    j = 0
    k = 0

    while k < len(served_orders):

        print(take_out_orders[i])
        print(dine_in_orders[j])
        print(served_orders[k])
        i += 1
        j += 1
        k += 1

    if True:
        print("True")
    else:
        print("False")

    return True


# Should be true
print("This next line should be True")
is_first_come_first_served([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
# Should be false
print("This next line should be False")
is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])


# ------------ notes about the question ----------
# two registers - one for take out
#               - one for customers eating inside
# All the orders are combined into one list
# they are handled FIFO (first in first out)
# What we need to do: check that service is
# order numbers are random, they do not need to be
# in increasing order
#