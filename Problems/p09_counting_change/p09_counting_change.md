#### Problem:
Write a function, `counting_change`, that takes in an amount and a list of coins.</br>
The function should return the number of different ways it is possible to make change for the given amount using the coins.</br>
You may reuse a coin as many times as necessary.
#### Solution:
<ins>Visualizing the decision tree</ins>
Usually you will visualize the decision tree as below. But, this deicision tree won't be aligning with the problem.Because,</br>
as per the question, coins choices of `1,2,1` & `2,1,1` are same. But, in the decision tree, they are 2 separate paths,</br>
because of which the no of choices increases by 1. 
![Coins_change](https://github.com/user-attachments/assets/0a595889-9d95-419c-8bfa-02aa2f4de6e2)
So, what to do now?</br>
Somehow we need to build a tree in such a way that it won't have duplicate paths.</br>
Think: first of all why duplicate paths are coming in the tree?</br>
It's because, for the first time, decision tree is getting branched for all coins & Then on the result nodes,</br>
once again decision tree is getting branched for all the coins.</br>
Because of this nature, we are trying to make choices with same coins at multilpe levels of the tree which</br>
results in duplicate paths.</br>
So, how about branching for single type of coins at one level with all possibilities? Let's check that out..</br>
![image](https://github.com/user-attachments/assets/fbfabd98-362f-424e-a1f4-a8e9892481a5)
<ins>Base case:</ins>
```python
def counting_change(amount, coins):
    if amount == 0:
        return 1
```
<ins>Recursive calls:</ins>
There are chances of thinking like this about initiating recursive calls. This is wrong, because at each recursive calls, once again we are trying out
all different types of coins(`for coin in coins`) which we dont want.
```python
def counting_change(amount, coins):
    if amount == 0:
        return 1

    no_of_ways = 0
    for coin in coins:
        for qty in range(0, amount+1):
            remainder = amount - (qty * coin)
            no_of_ways += counting_change(remainder, coins)
    return no_of_ways
```
So, you should not loop over the coins, instead
```python
def _counting_change(amount, coins, i):
    if amount == 0:
        return 1

    if i == len(coins):
        return 0
    
    coin = coins[i]

    no_of_ways = 0
    for qty in range(0, amount+1):
        remainder = amount - (qty * coin)
        no_of_ways += _counting_change(remainder, coins, i+1)
    
    return no_of_ways
```
