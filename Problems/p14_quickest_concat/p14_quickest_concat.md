#### Problem
Write a function, quickest_concat, that takes in a string and a list of words as arguments. </br>
The function should return the minimum number of words needed to build the string by concatenating</br> 
words of the list. If it is not possible to build the string, then return -1.
You may use words of the list as many times as needed.
#### Solution
<ins>Visualizing the decision tree</ins>
![image](https://github.com/user-attachments/assets/12ac04c6-b1da-4be0-834e-901a383e8c06)
<ins>Base case</ins></br>
```python
def quickest_concat(s, words):
  result = _quickest_concat(s, words)

def _quickest_concat(s, words):
  if s == '':
    return 0
```
<ins>Recursive calls</ins></br>
```python
def quickest_concat(s, words):
    ans = _quickest_concat(s, words)
    if ans == float('inf'):
        return -1
    else:
        return ans


def _quickest_concat(s, words):
    if s == '':
        return 0
  
    min_words = float('inf')
    for word in words:
        if s.startswith(word):
            suffix = s[len(word):]
            attempt = 1 + _quickest_concat(suffix, words)
            min_words = min(attempt, min_words)  

    return min_words
```
<ins>Memoization</ins></br>
```python
def quickest_concat(s, words):
    ans = _quickest_concat(s, words, {})
    if ans == float('inf'):
        return -1
    else:
        return ans


def _quickest_concat(s, words, memo):
    if s in memo:
        return memo[s]
    
    if s == '':
        return 0
  
    min_words = float('inf')
    for word in words:
        if s.startswith(word):
            suffix = s[len(word):]
            attempt = 1 + _quickest_concat(suffix, words, memo)
            min_words = min(attempt, min_words)  

    memo[s] = min_words
    return min_words
```
