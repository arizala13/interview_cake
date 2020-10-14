# --- general notes ---
# Question: Get best return with stocks from
# previous day. Buy then sell.
# Runtime: O(n) - pass through list only once
# Space complexity: O(1) - nothing new created

def get_max_profit(stock_prices):
    max_profit = 0
    min_price = stock_prices[0]
    for i in range(1, len(stock_prices)):

        # check to see if new min price IF we are lower
        if stock_prices[i] < min_price:
            min_price = stock_prices[i]

        # we check to see if we have a better max_profit
        if max_profit < stock_prices[i] - min_price:
            max_profit = stock_prices[i] - min_price

    print(max_profit)
    return max_profit


get_max_profit([7, 2, 8, 9])
get_max_profit([1, 1, 1, 1])


# --- general notes ----
# This is a greedy approach because at each step get take the
# best solution to the problem. Then continue down the input
# that was given.

