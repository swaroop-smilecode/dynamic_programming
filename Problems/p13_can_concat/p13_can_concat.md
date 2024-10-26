#### Problem
Write a function, can_concat, that takes in a string and a list of words as arguments.</br>
The function should return boolean indicating whether or not it is possible to concatenate</br>
words of the list together to form the string. You may reuse words of the list as many times as needed.
#### Solution
<ins>Visualizing the decision tree</ins></br>
![image](https://github.com/user-attachments/assets/9af90fb2-2285-4ef2-8db2-aa81df15e93d)
<ins>Base case</ins></br>
```python
def can_concat(s, words):
    return _can_concat(s, words)

def _can_concat(s, words):
    if s == '':
        return True
```
<ins>Recursive calls</ins></br>
```python
def can_concat(s, words):
    return _can_concat(s, words)

def _can_concat(s, words):
    if s == '':
        return True
    
    for word in words:
        if s.startswith(word):
            suffix = s[len(word):]
            if _can_concat(suffix, words) == True:
                return True
    return False
```
<ins>Memoization</ins></br>
```python
def can_concat(s, words):
    return _can_concat(s, words, {})

def _can_concat(s, words, memo):
    if s in memo:
        return memo[s]
    
    if s == '':
        return True
    
    for word in words:
        if s.startswith(word):
            suffix = s[len(word):]
            if _can_concat(suffix, words, memo) == True:
                memo[s] = True
                return memo[s]
    memo[s] = False
    return memo[s]
```
