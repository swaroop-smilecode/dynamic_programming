def array_stepper(numbers):
    ans = _array_stepper(numbers, 0, {})
    return ans

def _array_stepper(numbers, i, memo):
    if i in memo:
        return memo[i]

    if i >= len(numbers):
        return False

    if i == len(numbers)-1:
        return True
    
    for step in range(1, numbers[i]+1):
        if _array_stepper(numbers, i + step, memo) == True:
            return True
        
    memo[i] = False 
    return False    
    
print(array_stepper([2, 4, 2, 0, 0, 1])) # -> True