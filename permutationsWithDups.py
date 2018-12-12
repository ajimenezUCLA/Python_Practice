# Cracking The Coding Interview
# Recursion and Dynamic Programming
# 8.8: Permutations with Duplicates
# O(n!)

##### Solution #####

def charCounter(listo):

    listo = listo.lower() # Assuming we ignore upper/lower cases
    charFreq = {} # Dictionary/Hashmap to store our character counts
    
    for char in listo:
        if char not in charFreq:
            charFreq[char] = 1
        else:
            charFreq[char] += 1

    return charFreq


def perms(listo):

    results = [] # store our results
    freqTable = charCounter(listo) # populate our map
    perms_helper(freqTable, "",len(listo),results) # call the helper func

    return results
                
 
def perms_helper(mapo, prefix, remaining, results):

    if remaining == 0: # Base Case, no more letters
        results.append(prefix) # append our perm to results
        return
    
    for char in mapo: 
        count = mapo[char]
        if count > 0:
            mapo[char] -= 1 # decrease letter count
            perms_helper(mapo, prefix + char, remaining - 1,results) # update and recurse
            mapo[char] = count # return letter count
    
    
##### Testing #####
            
listo = "abc"
print(perms(listo))
