# Cracking the Coding Interview
# 8.4: Power Set
# This code is written in this fashion for ease of understanding
# The debug statements will guide you through the operations
# The comments explain the reason for the code
# This is not clean code, purely for instructional purposes

def pSet(array,index):
    print("DEBUG: Entering recursion")
    print("DEBUG: Current index =", index)
    allSubsets = []  #This is our primary 'set'
    if (index == len(array)) and ([] not in allSubsets): # base case, runs once
        allSubsets.append([]) # we append our empty set []
        print("DEBUG: Base Case Ran")
        print("DEBUG: Updated allSubsets =",allSubsets)
    else:
        allSubsets = pSet(array,index+1) # recurse and update index
        item = array[index] # store the current item in a variable
        print("DEBUG: current item =",item)
        moreSubsets = [] # to store our modded subset
        for subset in allSubsets: # for each subset item in allSubsets
            print("DEBUG: For Loop: subset =",subset)
            newSubset = [] # create a new subset
            newSubset.extend(subset) # must use extend, this is essential
                                    # if you use append, it will add the subset as an item
            newSubset.append(item) # then you add the current item to the subset
                                    # we just took from allsubsets
            print("DEBUG: Current newSubset =",newSubset)
            moreSubsets.append(newSubset) #add this to moresubsets
            print("DEBUG: moreSubsets =",moreSubsets)
            print()
        allSubsets.extend(moreSubsets) # then add all the subsets we just created into allsubsets
        print("DEBUG: Updated AllSubsets =",allSubsets)
    print("DEBUG: Exiting recursion")
    print()
    return allSubsets

##### Pseudo-Code #####
#
# def function(array, index):
#   create primary list for storing subsets
#   if index is equal to size of array:
#       if empty empty set not in primary:
#            append empty set to primary
#   else:
#       recurse through the function, increasing the index by 1
#       store the current item at the index in the array in a variable
#       create secondary list to store subsets
#       for each subset item in the primary subset list:
#           create a temporary subset list
#           add the subset items into the temporary list (use extend)
#           append to the array item to the temporary subset list
#           append the temporary list to the secondary list
#       add the seconday list to the primary list (extend) (we just updated the subsets)
#   return primary list

##### Clean Code #####
def pSet_Clean(array,index):
    allSubsets = [] # This is our primary set list
    if (index == len(array)) and ([] not in allSubsets): 
        allSubsets.append([]) # base case runs once, appends empty set
    else:
        allSubsets = pSet_Clean(array,index+1) # recurse and update index
        item = array[index] # not essential but easier to read

        moreSubsets = [] # to store our modded subset
        for subset in allSubsets: 
            newSubset = [] # temporary subset for modding
            newSubset.extend(subset) # must use extend, this is essential
            newSubset.append(item) # add the current item to the subset (mod it)
            moreSubsets.append(newSubset) # add to moresubsets
        allSubsets.extend(moreSubsets) # add all the subsets we just created into allsubsets
    return allSubsets

##### Testing #####

a = ['A','B','C'] # 3 values, therefore 2**3 == 8
b = [1,2,3,4,5]   # 5 values, therefore 2**5 == 32
print(pSet_Clean(a,0))
print(len(pSet_Clean(a,0)))
print()
print(pSet_Clean(b,0))
print(len(pSet_Clean(b,0)))
print()
print(pSet_Clean([],0))
print(len(pSet_Clean([],0)))
