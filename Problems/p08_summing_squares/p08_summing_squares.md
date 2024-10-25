### Problem:
Write a function, summing_squares, that takes a target number as an argument. The function should return the </br>
minimum number of perfect squares that sum to the target. A perfect square is a number of the form (i*i) where i >= 1.</br> 
For example: 1, 4, 9, 16 are perfect squares, but 8 is not perfect square.
### Solution:
<ins>What is perfect square?</ins></br>
We can create a perfect square number by taking a positive number and multiplying it with itself.</br>
For example; here the perfect square numbers are `1`, `4`, `9` & `16`.</br>
1 * 1 = 1</br>
2 * 2 = 4</br>
3 * 3 = 9</br>
4 * 4 = 16</br>
<ins>Let's understand the question with the help of an example:</ins></br>
Minimum number of perfect squares that are needed to form number `12` are `3`</br>
4 + 4 + 4</br>
You can also form `12` as below, but it's not the minimum number of perfect squares.</br>
9 + 1 + 1 + 1</br>
<ins>Let's visualize the decision tree:</ins></br>
![image](https://github.com/user-attachments/assets/72169df4-c8ab-46ce-943d-821058ae72a7)
<ins>Base case</ins></br>
```python
def _summing_squares(n):
    if n == 0:
        return 0
```
<ins>Recursive calls</ins></br>
Let's use `for` loop to initiate recursive call on each branch.</br>
```python
def summing_squares(n):
    if n == 0:
        return 0
    
    min_squares = float("inf")
    # `sqrt` will return decimal value. To convert into int, we use `floor`.
    # +1 in the range function is needed because the second argument is exclusive in range function,
    # but you want to consider that.
    for i in range(1, floor(sqrt(n))+1):
        curr_squares = 1 + summing_squares(n - i*i)
        min_squares = min(min_squares, curr_squares)
    return min_squares
```

<ins>Memoization</ins></br>
Let's use `for` loop to initiate recursive call on each branch.</br>
```python
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
```
