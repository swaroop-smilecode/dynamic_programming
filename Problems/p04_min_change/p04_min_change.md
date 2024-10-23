<ins>Step 1:</ins></br>
Visualizing the decision tree(tree made of base cases and DFS recursive calls).
![image](https://github.com/user-attachments/assets/65015034-4dbe-41a9-8205-92c119aed36f)
```python
def min_change(amount, coins):
  if amount == 0:
    return 0
```
<ins>Step 2:</ins></br>
Making recursive calls with smaller & smaller input, gradually progressing towards base case.
```python
for coin in coins:
  min_change(amount - coin, coins)
```
<ins>Step 3:</ins></br>
At one of point of time, these recursive calls will hit the base case & return you the result.</br>
Think about what to be done with those results while moving up towards the root node.

When base case gets hit, return value is 0, which indicates that to form an amount of 0, we need 0 coins.</br>
As we keep moving up, 1 needs to be added to the result returned from base case. Doing so, will inform us</br> 
how many coins are needed to form an amount mentioned inside that particular node.</br>
In a way, this adding 1 is nothing but, counting the number of edges as you progressing up.</br>
You also need to think about one more thing. If the node at which currently you are at has left node & right node</br>
then, will receive 2 values. Which one to choose? Min(left node return value, right node return value)</br>
because, what we want os the minimum number of coins required to form the given amount.

For better understanding, look at the below picture.
![image](https://github.com/user-attachments/assets/bbca55fa-c55e-4bab-afd9-024296d8aea9)
```python
def min_change(amount, coins):
  if amount == 0:
      return 0

  min_coins = float("inf")
  for coin in coins:
      num_of_coins = 1 + min_change(amount-coin, coins)
      min_coins = min(min_coins, num_of_coins)
  return min_coins
```
There is one more thing you need to think about. Let's consider an path which does not end up as amount == 0.</br>
This means, you can't form the amount using the given coins.</br>
```python
def min_change(amount, coins):
  if amount < 0:
      return float("inf")

  if amount == 0:
      return 0
  
  min_coins = float("inf")
  for coin in coins:
      num_of_coins = 1 + min_change(amount-coin, coins)
      min_coins = min(min_coins, num_of_coins)
  return min_coins
```
<ins>Step 4:</ins></br>
Include memoization.
```python
def min_change(amount, coins):
    ans = _min_change(amount, coins, {})
    return ans

def _min_change(amount, coins, memo):
  if amount in memo:
      return memo[amount]
  
  if amount < 0:
      return float("inf")

  if amount == 0:
      return 0
  
  min_coins = float("inf")
  for coin in coins:
      num_of_coins = 1 + _min_change(amount-coin, coins, memo)
      min_coins = min(min_coins, num_of_coins)

  memo[amount] = min_coins
  return min_coins
```
<ins>Step 5:</ins></br>
Let's think about one edge case.</br>
What happens when none of the paths could form the given amount?</br>
The code returns `float("inf")` which doesn't look so meaning full.</br>
So, will return `-1`
```python
def min_change(amount, coins):
  ans = _min_change(amount, coins, {})
  if ans == float('inf'):
      return -1
  else:
      return ans


def _min_change(amount, coins, memo):
  if amount in memo:
      return memo[amount]
  
  if amount < 0:
      return float("inf")

  if amount == 0:
      return 0
  
  min_coins = float("inf")
  for coin in coins:
      num_of_coins = 1 + _min_change(amount-coin, coins, memo)
      min_coins = min(min_coins, num_of_coins)

  memo[amount] = min_coins
  return min_coins
```
