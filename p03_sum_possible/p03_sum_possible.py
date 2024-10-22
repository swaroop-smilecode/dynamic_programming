def sum_possible(amount, numbers):
    if amount < 0:
        return False 
    
    if amount == 0:
        return True    

    for num in numbers:
        if sum_possible(amount-num, numbers) == True:
            return True
    
    return False

print(sum_possible(8, [5, 12, 4])) # -> True, 4 + 4
