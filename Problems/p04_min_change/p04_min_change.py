def min_change(amount, coins):
    if amount == 0:
        return 0
    
    for coin in coins:
        if min_change(amount-coin, coins):
            return True


print(min_change(8, [1, 5, 4, 12])) # -> 2, because 4+4 is the minimum coins possible
