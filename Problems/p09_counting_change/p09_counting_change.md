#### Problem:
Write a function, `counting_change`, that takes in an amount and a list of coins.</br>
The function should return the number of different ways it is possible to make change for the given amount using the coins.</br>
You may reuse a coin as many times as necessary.
#### Solution:
<ins>Visualizing the decision tree</ins>
Usually you will visualize the decision tree as below. But, this deicision tree won't be aligning with the problem.Because,</br>
as per the question, coins combinations of 1,2,1 OR coins 2,1,1 are same. But, in the decision tree, they are 2 separate paths,</br>
because of which the no of combinations increases by 1. 
![Coins_change](https://github.com/user-attachments/assets/0a595889-9d95-419c-8bfa-02aa2f4de6e2)
So, what to do now?</br>
Somehow we need to build tree in such a way that it won't have duplicate paths.</br>
So, think: first of all why duplicate paths are coming in the tree?</br>
It's because, for the first time decision tree is getting branched for all the possibile coins</br>
Then on the reminder nodes, once again decision tree is getting branched for all the possible coins</br>
Because of this nature, same coins comes at multilpe levels of the tree which results in duplicate paths</br>
So, how about branching for single type of coins at one level with all possibilities? Let's check that out..</br>
![image](https://github.com/user-attachments/assets/fbfabd98-362f-424e-a1f4-a8e9892481a5)
<ins>Base case:</ins>
```python
def counting_change(amount, coins):
    if amount == 0:
        return 1
```
<ins>Recursive calls:</ins>








