### Problem
A knight is on a chess board. Can you figure out the total number of ways the knight can move</br>
to a target position in exactly m moves? On a single move, the knight can move in an "L" shape;</br>
two spaces in any direction, then one space in a perpendicular direction. This means that on a </br>
single move, a knight has eight possible positions it can move to.

Write a function, `knightly_number`, that takes in 6 arguments:</br>

n, m, kr, kc, pr, pc</br>

n = the length of the chess board</br>
m = the number of moves that must be used</br>
kr = the starting row of the knight</br>
kc = the starting column of the knight</br>
pr = the target row</br>
pc = the target column</br>

The function should return the number of different ways the knight can move to the target in exactly m moves.</br>
The knight can revisit positions of the board if needed. The knight cannot move out-of-bounds of the board.</br>
You can assume that rows and columns are 0-indexed. This means that if n = 8, there are 8 rows and 8 columns numbered 0 to 7.</br>

### Solution
<ins>Understanding the question:</ins></br>
Question is asking about: In how many ways, knight can move to the pawn position, just in 2 moves, under below circumstances.</br>
knightly_number(8, 2, 4, 4, 5, 5) # -> 2</br>
Where;</br>
n = the length of the chess board</br>
m = the number of moves that must be used</br>
kr = the starting row of the knight</br>
kc = the starting column of the knight</br>
pr = the target row</br>
pc = the target column</br>
![image](https://github.com/user-attachments/assets/5d0bee71-65d1-4a04-b290-6dfc333bea64)

<ins>Visualizing the decision tree:</ins></br>
First thing to notice is that, among the above mentioned variables. Only 3 things are going to change.</br>
They are</br>
`n`</br>
`kr`</br>
`kc`</br>
![image](https://github.com/user-attachments/assets/f005b2d5-7cb4-4299-bb4b-3f0b07eb6399)

<ins>Base case:</ins>
```python
def knightly_number(n, m, kr, kc, pr, pc):
    return _knightly_number(n, m, kr, kc, pr, pc)

def _knightly_number(n, m, kr, kc, pr, pc):
    if m == 0:
        if (kr, kc) == (pr, pc):
            return 1
        else:
            return 0
```
<ins>To avoid moving out of grid:</ins>
```python
def knightly_number(n, m, kr, kc, pr, pc):
    return _knightly_number(n, m, kr, kc, pr, pc)

def _knightly_number(n, m, kr, kc, pr, pc):
    if kr < 0 or kr >= n or kc < 0 or kc >= n:
        return 0

    if m == 0:
        if (kr, kc) == (pr, pc):
            return 1
        else:
            return 0
```
<ins>Recursive calls:</ins>
```python
def knightly_number(n, m, kr, kc, pr, pc):
    return _knightly_number(n, m, kr, kc, pr, pc)

def _knightly_number(n, m, kr, kc, pr, pc):
    if kr < 0 or kr >= n or kc < 0 or kc >= n:
        return 0

    if m == 0:
        if (kr, kc) == (pr, pc):
            return 1
        else:
            return 0
    
    neighbors = [
        ( kr + 2, kc + 1 ),
        ( kr - 2, kc + 1 ),
        ( kr + 2, kc - 1 ),
        ( kr - 2, kc - 1 ),
        ( kr + 1, kc + 2 ),
        ( kr - 1, kc + 2 ),
        ( kr + 1, kc - 2 ),
        ( kr - 1, kc - 2 ),
    ]
  
    count = 0
    for neighbor in neighbors:
        neighbor_row, neighbor_col = neighbor
        count += _knightly_number(n, m - 1, neighbor_row, neighbor_col, pr, pc)
    return count
```
<ins>Memoization:</ins>
```python
def knightly_number(n, m, kr, kc, pr, pc):
    return _knightly_number(n, m, kr, kc, pr, pc, {})

def _knightly_number(n, m, kr, kc, pr, pc, memo):
    key = (m, kr, kc)
    if key in memo:
        return memo[key]
        
    if kr < 0 or kr >= n or kc < 0 or kc >= n:
        return 0

    if m == 0:
        if (kr, kc) == (pr, pc):
            return 1
        else:
            return 0
    
    neighbors = [
        ( kr + 2, kc + 1 ),
        ( kr - 2, kc + 1 ),
        ( kr + 2, kc - 1 ),
        ( kr - 2, kc - 1 ),
        ( kr + 1, kc + 2 ),
        ( kr - 1, kc + 2 ),
        ( kr + 1, kc - 2 ),
        ( kr - 1, kc - 2 ),
    ]
  
    count = 0
    for neighbor in neighbors:
        neighbor_row, neighbor_col = neighbor
        count += _knightly_number(n, m - 1, neighbor_row, neighbor_col, pr, pc, memo)

    memo[key] = count
    return count

```
