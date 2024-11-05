def positioning_plants(costs):
  return _positioning_plants(costs, 0, None, {})

def _positioning_plants(costs, pos, last_plant, memo):
  key = (pos, last_plant)
  if key in memo:
    return memo[key]
  
  if pos == len(costs):
    return 0
  
  min_cost = float('inf')
  
  for plant, cost in enumerate(costs[pos]):
    if plant != last_plant:
      candidate = cost + _positioning_plants(costs, pos + 1, plant, memo)
      min_cost = min(candidate, min_cost)
  
  memo[key] = min_cost
  return min_cost


positioning_plants([
  [4, 3, 7],
  [6, 1, 9],
  [2, 5, 3]
]) # -> 7, by doing 4 + 1 + 2.