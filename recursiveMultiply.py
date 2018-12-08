# Cracking The Coding Interview
# Recursion and Dynamic Programming
# 8.5 Recursive Multiply
# Assumptions: Positive Integers Only, cannot use * or / operator
#            : Can use +, -, <<, >> (bit shifting)

##### Simple Solution #####

# This solution could be much more simpler and inefficient
def recMult_simple(a,b):
    smaller = a if a < b else b # smaller = a < b ? a : b
    bigger = b if a < b else a # bigger = a < b ? b : a
    print("DEBUG: smaller =",smaller)
    print("DEBUG: bigger =",bigger)
    if a == 0 or b == 0:
        return 0
    if a == 1 or b == 1:
        return bigger
    return recMult_simpHelper(smaller,bigger)
    
def recMult_simpHelper(smaller,bigger):
    if smaller == 0: # base case for exiting recursion
        return 0
    return bigger + recMult_simpHelper(smaller-1,bigger)

##### Non-Trivial Solution #####
    
def recMult(a,b):
    smaller = a if a < b else b # smaller = a < b ? a : b
    bigger = b if a < b else a # bigger = a < b ? b : a
    print("DEBUG: smaller =",smaller)
    print("DEBUG: bigger =",bigger)
    if a == 0 or b == 0:
        return 0
    return recMult_helper(smaller,bigger)
    
def recMult_helper(smaller,bigger):
    if smaller == 1: # Base case
        return bigger
    bitdiv = smaller >> 1; # essentially integer division, x >> y == x // 2**y
    halfProduct = recMult_helper(bitdiv,bigger)
    if smaller % 2 == 0: # if the smallest is divisble by 2, do half work and add together
        return halfProduct + halfProduct 
    else: # its odd, therefore add half the work and add the bigger to the odd portion
        return halfProduct + halfProduct + bigger 
    
##### Testing #####
a = 5
b = 3
print("Trivial solution")
print(recMult_simple(a,b))
print()
print("Non-Trivial solution")
print(recMult(a,b))
