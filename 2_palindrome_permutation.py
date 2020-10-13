# --- general notes ---
# Question :
#
#
# Runtime:
# Space complexity

def palindrome_permutation(given_string):
    # map to save char values
    char_map = {}

    count = 0

    for char in given_string:
        if char in char_map:
            char_map[char] += 1
        else:
            char_map[char] = count + 1

    single_chars = 0

    for v in char_map.values():
        if v % 2 == 0:
            continue
        else:
            single_chars += 1

    if single_chars < 2:
        print("True")
        return False
    else:
        print("False")
        return True


print("Next will be True")
palindrome_permutation('aabcbcd')

print("Next will be True")
palindrome_permutation('aabccbdd')

print("Next will be False")
palindrome_permutation('aabcd')

print("Next will be False")
palindrome_permutation('aabbcd')

print("Next will be True")
palindrome_permutation('')

print("Next will be True")
palindrome_permutation('a')
