#### Problem
Write a function, overlap_subsequence, that takes in two strings as arguments. The function should </br>
return the length of the longest overlapping subsequence. A subsequence of a string can be created </br>
by deleting any characters of the string, while maintaining the relative order of characters.
#### Solution
![image](https://github.com/user-attachments/assets/0956efe8-ac35-4fb9-84e6-528e0072e4e3)
![image](https://github.com/user-attachments/assets/df871a32-38c7-4c85-ac9b-19496bd724ce)
<ins>Base case:</ins></br>
```python
def overlap_subsequence(string_1, string_2):
    return _overlap_subsequence(string_1, string_2, 0, 0)

def _overlap_subsequence(string_1, string_2, i, j):
    if i == len(string_1) or j == len(string_2):
        return 0
```
<ins>Recursive calls:</ins></br>
```python
def overlap_subsequence(string_1, string_2):
    return _overlap_subsequence(string_1, string_2, 0, 0)

def _overlap_subsequence(string_1, string_2, i, j):
    if i == len(string_1) or j == len(string_2):
        return 0

    if string_1[i] == string_2[j]:
        return 1 + _overlap_subsequence(string_1, string_2, i + 1, j + 1)
    else:
        return max(
            _overlap_subsequence(string_1, string_2, i + 1, j),
            _overlap_subsequence(string_1, string_2, i, j + 1))
```
<ins>Memoization:</ins></br>
```python
def overlap_subsequence(string_1, string_2):
    return _overlap_subsequence(string_1, string_2, 0, 0, {})

def _overlap_subsequence(string_1, string_2, i, j, memo):
    key = (i, j)
    if key in memo:
        return memo[key]

    if i == len(string_1) or j == len(string_2):
        return 0

    if string_1[i] == string_2[j]:
         memo[key] = 1 + _overlap_subsequence(string_1, string_2, i + 1, j + 1, memo)
    else:
         memo[key] = max(
            _overlap_subsequence(string_1, string_2, i + 1, j, memo),
            _overlap_subsequence(string_1, string_2, i, j + 1, memo))
    return  memo[key]
```
