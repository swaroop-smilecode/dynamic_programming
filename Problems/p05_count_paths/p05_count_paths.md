<ins>Step 1:</ins> (Visualizing the decision tree(tree made of base cases and DFS recursive calls)</br>
Here, the dicision tree represents all the paths from source to destination inside the grid. For example, one path is highlighted both in grid & </br>
the decision tree.
![image](https://github.com/user-attachments/assets/e98552a0-5c5e-423f-9b85-5907fdc52c87)

<ins>Step 2:</ins> (Writing base case)</br>
Usually, to write the base case, the thinking is of, what needs to be returned for smallest input?</br>
But, it's not rigid principle & sticking to this principle as a thumb rule makes writing base case difficult.</br>

For this problem, let's think with the help of deicision tree.</br>
In terms of decision tree, base case is nothing but what needs to be returned when we reach the goal & here the goal is (2,2).</br>
So, What needs to be returned by the base case when we reach the goal node (2,2)?</br>
Look at the yellow colour box. When recurisve call at node (2,1) asks the question, to node (2,2), hey, how many ways i can reach from me to you?
(2,2) should return 1.</br>
So, any base case that's ending with goal node (2,2) should return 1.</br>
This makes much more sence when you read next step of what needs to be done with returned values from base case.</br>
![image](https://github.com/user-attachments/assets/13711011-23d3-4242-a4a5-d144619856cc)

<ins>Step 3:</ins> (Making recursive calls on neighbour nodes of root node & coding what math to be done on the return values)</br>
For example, consider this situation represented in yellow color box. When 1 & 1 pops up from left child & right child of node (1,1)</br>
what math needs to be done on those returned values. They need to be added</br>
![image](https://github.com/user-attachments/assets/6c657ff8-f2b4-4386-ba75-8c818c740d7a)

![image](https://github.com/user-attachments/assets/43c5900a-92a5-4765-b92b-9354a250af70)





