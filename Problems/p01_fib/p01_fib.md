<ins>Visualize the decision tree:</ins></br>
![image](https://github.com/user-attachments/assets/843ef5af-b052-41ca-a9ef-76489e4e13a6)

<ins>Base case:</ins>
```python
def fib(n):
    return _fib(n)

def _fib(n):
    if n == 0 or n == 1:
        return n
```
<ins>Recursive calls:</ins>
```python
def fib(n):
    return _fib(n)

def _fib(n):
    if n == 0 or n == 1:
        return n
    
    return _fib(n - 1) + _fib(n - 2)
```
<ins>Memoizatione:</ins>
```python
def fib(n):
    return _fib(n, {})

def _fib(n, memo):
    if n in memo:
        return memo[n]

    if n == 0 or n == 1:
        return n
    
    memo[n] = _fib(n - 1, memo) + _fib(n - 2, memo)
    return memo[n]
```
