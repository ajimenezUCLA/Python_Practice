# Cracking The Coding Interview
# Recursion and Dynamic Programming
# 8.7: Permutations without Dups

##### First Solution #####

def perm1(listo):
    if len(listo) == 0: # base case, empty list
        return []
    elif len(listo) == 1: # another simple case, 1 item to permute
        return listo 
    else:
        tempo = []
        # now we need to disect our string, take the first item
        for i in range(len(listo)):
            first = listo[i] # first item in string/list
            others = listo[:i] + listo[i+1:] # everything before and after i
            for item in perm1(others): # we need to break the others down
                tempo.append(first+item)
        return tempo

##### Second Solution #####
        
# same as above
def perm2(listo):
    n = len(listo)
    result = []
    if n == 0:
        result.append(listo)
        return result
    for i in range(n):
        before = listo[:i]
        after = listo[i+1:]
        partials = perm2(before+after)
        for p in partials:
            result.append(listo[i]+p)
    return result

##### Third Solution #####
    
# I troubleshooted this one for sometime,
# removing the append(" ") breaks it. /shruggie
def perm3(listo):
    permutations = []
    if len(listo) == 0:
        permutations.append(" ")
        return permutations
    first = listo[0]
    #print("DEBUG: first =",first)
    rest = listo[1:]
    #print("DEBUG: rest =",rest)
    #print("DEBUG: Entering recursion")
    words = perm3(rest)
    #print("DEBUG: words =",words)
    for word in words:
        for index in range(len(word)):
            s = insertCharAt(word,first,index)
            permutations.append(s)
    #print("DEBUG: Exiting recursion")
    #print("DEBUG: Permutations =",permutations)
    return permutations


def insertCharAt(word,char,pos):
    start = word[:pos]
    end = word[pos:]
    return start + char + end


##### Testing #####
listo = "abc"
print(perm1(listo))
print(perm2(listo))
print()
print(perm3(listo))
##### Notes #####
# 
# listo = "abcde"
# listo[:2] == ab (excluding the second item ie, 'c')
# listo[2:] == cde (inclusive of our 2nd element 'c')
# instead use listo[i+1:] (for an exclusion of our ith item)
