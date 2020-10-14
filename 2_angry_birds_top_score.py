# --- general notes ---
# Question: Get top scores for a game given a
# list of scores and a high score. You will rank them
# highest to lowest and it needs to be done faster than
# O(n lg n)
# Runtime:
# Space complexity

# Using method below gets correct answer but is still O(n lg n)

# def sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE):
#     sorted_scores = (sorted(unsorted_scores))[::-1]
#     print(sorted_scores)

def sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE):
    sorted_scores = (sorted(unsorted_scores))[::-1]
    print(sorted_scores)


sort_scores([37, 89, 41, 65, 91, 53], 100)
