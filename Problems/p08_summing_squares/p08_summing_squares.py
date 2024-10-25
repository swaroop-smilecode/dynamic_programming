from math import sqrt, floor

def summing_squares(n):
    return _summing_squares(n, {})

def _summing_squares(n, memo):
    if n in memo:
        return memo[n]
    
    if n == 0:
        return 0
    
    min_squares = float("inf")
    for i in range(1, floor(sqrt(n))+1):
        curr_squares = 1 + _summing_squares(n - i*i, memo)
        min_squares = min(min_squares, curr_squares)
    memo[n] = min_squares
    return memo[n]

print(summing_squares(8)) # -> 2