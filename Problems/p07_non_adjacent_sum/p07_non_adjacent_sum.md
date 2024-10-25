### Question
Write a function, `non_adjacent_sum`, that takes in a list of numbers as an argument. The function should return the maximum sum of</br>
non-adjacent items in the list. There is no limit on how many items can be taken into the sum as long as they are not adjacent.</br>
### Solution
Whenever we see such questions of including something & excluding something, it's about taking decisions. So, your thinking should</br>
go towards imagining decision tree & obviously recursion is the programmatic way of solving that decition tree.</br>

As usually, will solve the problem for frist case & rest will be taken case by recursion automatically(Recursive leap of faith).</br>
To put it another way, this is nothing but we start our decision tree with complete input `[2, 4, 5, 12, 7]`, then solve the problem</br>
for first element of input. Keep repeating this step, until you end up with smallest input.
![image](https://github.com/user-attachments/assets/09132fd1-35f6-4d3b-965f-6e29b3dc414c)

<ins>Base case:</ins></br>
As we keep progressing, at one point of time, our input becomes smallest(`[]`). Now, treat this smallest input itself as complete</br>
problem & ask the question, what's the `non adjacent sum` of `[]`? It's `0`.
```python
def non_adjacent_sum(nums):
    if len(nums) == 0:
        return 0
```

<ins>Recursive calls</ins></br>
These recursive calls should make input smaller and smaller, gradually progressing towards the Base case.</br>
How many recursive calls need to be made?</br>
From root node, how many branches are diverging?</br>
2 branches(1 left branch & 1 right branch). Hence 2 recursive calls need to be made</br>
- we need to add first element of input`(nums[0])` to first recursive call returned value, because we are considering 2 in the calculation of adjacent sum.
- we don't need to add first element of input`(nums[0])` to second recursive call returned value, because we are not considering 2 in the calculation of adjacent sum.
```python
def non_adjacent_sum(nums):
    if len(nums) == 0:
        return 0
  
    include = nums[0] + non_adjacent_sum(nums[2:])
    exclude = non_adjacent_sum(nums[1:])
    return max(include, exclude)
```

<ins>Improve the code</ins></br>
Slicing takes `O(n)` time & as we are doing slicing in recursive call which will be made O(n) times, it will result in total complexity of `O(n)^2`</br>
To avoid that;
```python
def non_adjacent_sum(nums):
    return _non_adjacent_sum(nums, 0)

def _non_adjacent_sum(nums, i):
    #You need this additional check to avoid index out of bound.
    #There will not be a problem in case of list slicing, because 
    #the index out of bound will just result in empty list 
    if i >= len(nums):
        return 0

    if len(nums) == 0:
        return 0

    include = nums[i] + _non_adjacent_sum(nums, i+2)
    exclude = _non_adjacent_sum(nums, i+1)
    return max(include, exclude)
```
<ins>Memoization</ins></br>
```python
def non_adjacent_sum(nums):
    return _non_adjacent_sum(nums, 0, {})


def _non_adjacent_sum(nums, i, memo):
    if i in memo:
        return memo[i]
    #You need this additional check to avoid index out of bound.
    #There will not be a problem in case of list slicing, because 
    #the index out of bound will just result in empty list 
    if i >= len(nums):
        return 0

    if len(nums) == 0:
        return 0

    include = nums[i] + _non_adjacent_sum(nums, i+2, memo)
    exclude = _non_adjacent_sum(nums, i+1, memo)
    memo[i] = max(include, exclude)
    return memo[i]
```
