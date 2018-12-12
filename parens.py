# Cracking The Coding Interview
# Recursion and Dynamic Programming
# 8.9: Parens
# Note: to better understand the code, begin with n = 0 and increment  

##### Solution #####

def genParen(remaining):
    print("DEBUG: Entering recursion")
    seto = set() # store our sets
    if remaining == 0: # if empty set, add nothing to set
        print("DEBUG: BASE CASE RAN")
        seto.add("")
    else:
        prev = genParen(remaining - 1) # recurse to begin with n = 0
        print("DEBUG: prev =",prev)
        for item in prev:    #this will load up "", it will run nothing then add "()"
            print("DEBUG: item =",item)
            for i in range(len(item)):
                print("DEBUG: current i =",i)
                if item[i] == "(": # if it finds a left paren, it will add a "()"
                    s = gen_helper(item,i) # add () to the item
                    seto.add(s)
            seto.add("()"+item) # update sets
    return seto

def gen_helper(stringo,index):
    left = stringo[:index+1]
    right = stringo[index+1:]
    return left + "()" + right

##### Clean Solution

def genParenClean(remaining):
    seto = set() # store our sets
    if remaining == 0: # if empty set, add nothing to set
        seto.add("")
    else:
        prev = genParenClean(remaining - 1) # recurse to begin with n = 0
        for item in prev:    #this will load up "", it will run nothing then add "()"
            for i in range(len(item)):
                if item[i] == "(": # if it finds a left paren, it will add a "()"
                    s = gen_helper(item,i) # add () to the item
                    seto.add(s)
            seto.add("()"+item) # update sets
    return seto
          
##### Testing #####
print(genParenClean(0))
print(genParenClean(1))
print(genParenClean(2))
print(genParenClean(3))
