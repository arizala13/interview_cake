def return_true_or(s):
    count_chars = {}

    for char in s:
        if char in count_chars:
            count_chars[char] += 1
        else:
            count_chars[char] = 1

    print(count_chars)


return_true_or("racecar")


# practice of adding a value to a dictionary 
# and keeping track of how many times its been seen
#
