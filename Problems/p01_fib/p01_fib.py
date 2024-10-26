def fib(n):
    return _fib(n, {})

def _fib(n, memo):
    if n in memo:
        return memo[n]

    if n == 0 or n == 1:
        return n
    
    memo[n] = _fib(n - 1, memo) + _fib(n - 2, memo)
    return memo[n]