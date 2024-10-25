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