def count_steps(current: int, target: int) -> int:
    if current == target:
        return 0 
    else: 
        return 1 + count_steps(current + 1, target)
print(count_steps(5, 10))  # 5