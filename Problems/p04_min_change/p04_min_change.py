def min_change(amount, coins):
    ans = _min_change(amount, coins, {})
    if ans == float('inf'):
        return -1
    else:
        return ans

def _min_change(amount, coins, memo):
    if amount in memo:
        return memo[amount]
    
    if amount < 0:
        return float("inf")

    if amount == 0:
        return 0
    
    min_coins = float("inf")
    for coin in coins:
        num_of_coins = 1 + _min_change(amount-coin, coins, memo)
        min_coins = min(min_coins, num_of_coins)

    memo[amount] = min_coins
    return min_coins

print(min_change(8, [1, 5, 4, 12])) # -> 2, because 4+4 is the minimum coins possible
