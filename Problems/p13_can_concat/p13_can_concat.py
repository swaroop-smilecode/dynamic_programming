def can_concat(s, words):
    return _can_concat(s, words, {})

def _can_concat(s, words, memo):
    if s in memo:
        return memo[s]
    
    if s == '':
        return True
    
    for word in words:
        if s.startswith(word):
            suffix = s[len(word):]
            if _can_concat(suffix, words, memo) == True:
                memo[s] = True
                return memo[s]
    memo[s] = False
    return memo[s]
  
can_concat("oneisnone", ["one", "none", "is"]) #  -> True
