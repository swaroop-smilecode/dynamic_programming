Let's write the recursive solution first.</br>

<ins>Base case:</ins></br>
- Here the question is asking: can you form the given amount, by using the available coins?</br>

- There are 2 inputs. amount & coins.</br>
  Which input needs to be made smallest?</br>
  coins values remains constant, where as the amount formed by those coins is the one which</br> becomes small & small when you start using coins.</br>

- So, let's make the amount smallest(0) & ask the question once again. Can you form the 0 amount</br> 
  by using the available coins?
  Ofcourse, it can be formed. In programmatic terms, it's saying True.
  ```python
  if amount == 0:
    return True
  ```  
<ins>Recursive call:</ins></br>
Any recursive call should do 2 things.
1. Make the input smaller & smaller, gradually progress towards base case.
2. When these recursive calls keep happening, at one point of time, base case will be hit & thats when you will get first return value.</br>
   You need to think what has to be done with that value, so that we can arrive at final answer. For example, in this problem, base case</br>
   returns True which means that the amout can be formed by using the available coins. So, no need to do any extra work on that retuned</br>
   True. Just return that True to top.
```python
for num in numbers:
  if sum_possible(amount-num, numbers) == True:
    return True
```
<ins>A picture representing base cases & recursive calls looks like below</ins></br>
![image](https://github.com/user-attachments/assets/963410be-031a-4936-9c7b-3f8d8a2ee50c)


