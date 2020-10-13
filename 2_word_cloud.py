# --- general notes ---
# Question: Build word cloud based off how
# many times a word is seen in a string
# -- works below, except does not remove non alpha
# like , : - etc.
# Runtime:
# Space complexity

def word_cloud_map(passed_string):
    word_cloud = {}

    # takes the given list and splits it based off space
    # also make all lower case
    string_list = passed_string.lower().split()

    # how do we remove all extra stuff like , . :
    for word in string_list:
        if word in word_cloud:
            word_cloud[word] += 1
        else:
            word_cloud[word] = 1

    print(word_cloud)


word_cloud_map("After beating the eggs, Dana read the next step:")