#### Problem
Write a function, max_palin_subsequence, that takes in a string as an argument. The function should </br>
return the length of the longest subsequence of the string that is also a palindrome. A subsequence </br>
of a string can be created by deleting any characters of the string, while maintaining the relative order of characters.
#### Solution
<ins>Visualizing the decision tree:</ins>
![image](https://github.com/user-attachments/assets/e0e54eed-2a0d-48de-9944-1c347bffdccf)
<ins>Base case:</ins>
```python
def max_palin_subsequence(string):
    if len(string) == 0:
        return 0
  
    if len(string) == 1:
        return 1
```
Look a ahead a step. During the recursive calls, you need to call the function with small strings. Isn't it?</br>
How will you do that?</br>
There are 2 options</br>
1. slicing</br>
2. Through indexes</br>

Obviously, will go for `Through indexes` approach, as slicing is results in O(n)^2 complexity inside the recursive calls.</br>
Above base cases will work when you pass sliced string. But, `Through indexes` approach, will pass full string</br>
and then the indexes of the string to work on next recursive call</br>
So, the base cases will be modified as below</br>
```python
def _max_palin_subsequence(string,i,j):
    if i > j:
        return 0
    
    if i == j:
        return 1
```
<ins>Recursive calls:</ins>
```python
def max_palin_subsequence(string):
  return _max_palin_subsequence(string,0,len(string)-1)

def _max_palin_subsequence(string,i,j):
    if i > j:
        return 0
    
    if i == j:
        return 1

    if string[i] == string[j]:
        return 2 + _max_palin_subsequence(string, i + 1, j - 1)
    else:
        return max(
                _max_palin_subsequence(string, i + 1, j),
                _max_palin_subsequence(string, i, j - 1))
```
<ins>Memoization</ins>
```python
def max_palin_subsequence(string):
  return _max_palin_subsequence(string,0,len(string)-1, {})

def _max_palin_subsequence(string,i,j, memo):
    key = (i, j)
    if key in memo:
        return memo[key]
    
    if i > j:
        return 0
    
    if i == j:
        return 1

    if string[i] == string[j]:
        memo[key] = 2 + _max_palin_subsequence(string, i + 1, j - 1, memo)
        return memo[key]
    else:
        memo[key] = max(
                        _max_palin_subsequence(string, i + 1, j, memo),
                        _max_palin_subsequence(string, i, j - 1, memo))
        return memo[key]
```
