def counting_change(amount, coins):
  return _counting_change(amount, coins, 0, {})

def _counting_change(amount, coins, i, memo):
    key = (amount, i)
    if key in memo:
        return memo[key]

    if amount == 0:
        return 1

    if amount < 0:
        return 0
    
    if i == len(coins):
        return 0
    
    coin = coins[i]

    no_of_ways = 0
    for qty in range(0, amount+1):
        remainder = amount - (qty * coin)
        no_of_ways += _counting_change(remainder, coins, i+1, memo)
    
    memo[key] = no_of_ways
    return memo[key]

print(counting_change(4, [1, 2, 3])) # -> 4