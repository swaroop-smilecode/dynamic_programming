def max_palin_subsequence(string):
  return max_palin_subsequence_helper(string,0,len(string)-1,{})

def max_palin_subsequence_helper(string,i,j,memo):


print(max_palin_subsequence("luwxult")) # -> 5
