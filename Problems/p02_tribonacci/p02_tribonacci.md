<ins>Visualize the decision tree:</ins></br>
![image](https://github.com/user-attachments/assets/cbc28a2c-1c72-4439-a15e-6d89b1762f70)

<ins>Base case:</ins>
```python
def tribonacci(n):
    return _tribonacci(n)

def _tribonacci(n):
    if n == 0 or n == 1:
        return 0

    if n == 2:
        return 1
```
<ins>Recursive calls:</ins>
```python
def tribonacci(n):
    return _tribonacci(n)

def _tribonacci(n):
    if n == 0 or n == 1:
        return 0

    if n == 2:
        return 1

    return _tribonacci(n - 1) + _tribonacci(n - 2) + _tribonacci(n - 3)
```
<ins>Memoizatione:</ins>
```python
def tribonacci(n):
  return _tribonacci(n, {})

def _tribonacci(n, memo):
  if n in memo:
    return memo[n]

  if n == 0 or n == 1:
    return 0

  if n == 2:
    return 1

  memo[n] = _tribonacci(n - 1, memo) + _tribonacci(n - 2, memo) + _tribonacci(n - 3, memo)
  return memo[n]

```
