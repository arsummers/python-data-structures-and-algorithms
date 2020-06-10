"""
Given a list of prices and an amount to spend, what is the maximum number of toys Mark can buy? For example, if prices = [1, 2, 3, 4]  and Mark has k = 7 to spend, he can buy items [1, 2, 3]  for 6, or  [3, 4] for 7 units of currency. He would choose the first group of  items. Note: A toy can't be bought multiple times. Unsure if this means prices can't be duplicated or not. 
"""


def max_toys(prices, k):
    """
    prices is an array representing toy prices. k is an integer representing the amount Mark can spend
    """
    # sort priced array - python can do this for me
    # a variable to check against k as it decrements
    #  alternatively, a variable, j that increments with toys bought, then compares to K
    #  loop through prices.
    #  if j becomes bigger than k, return the list at the index in which it became bigger

    prices.sort()

    j = 0
    for i in prices:
        j += i
        if j > k:
            return prices.index(i)