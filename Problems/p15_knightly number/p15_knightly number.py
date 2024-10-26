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

knightly_number(8, 2, 4, 4, 5, 5) # -> 2