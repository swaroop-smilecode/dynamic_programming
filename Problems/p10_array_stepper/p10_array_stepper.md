#### Problem
Write a function, array_stepper, that takes in a list of numbers as an argument. You start at the first position of the list.</br>
The function should return a boolean indicating whether or not it is possible to reach the last position of the list.</br>
When situated at some position of the list, you may take a maximum number of steps based on the number at that position.</br>
#### Solution
<ins>Visualizing the decision tree:</ins>
![image](https://github.com/user-attachments/assets/28092dd2-f708-49fe-a80c-bd8ea5e1b6cd)
<ins>Base case:</ins>
```python
def array_stepper(numbers):
    ans = _array_stepper(numbers, 0)
    return ans

def _array_stepper(numbers, i):
    if i == len(numbers)-1:
        return True
```
<ins>Recursive calls:</ins>
```python
def array_stepper(numbers):
    ans = _array_stepper(numbers, 0)
    return ans

def _array_stepper(numbers, i):
    if i >= len(numbers):
        return False

    if i == len(numbers)-1:
        return True
    
    for step in range(1, numbers[i]+1):
        if _array_stepper(numbers, i + step) == True:
            return True
    return False
```
<ins>Memoization:</ins>
