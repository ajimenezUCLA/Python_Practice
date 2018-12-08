# Cracking The Coding Interview
# Recursion and Dynamic Programming
# 8.6: Towers of Hanoi

##### Non Stack Solution #####

def towerHanoi(n, start, end, aux):
    if n <= 0: # no solution, don't print any steps
        print("DEBUG: base case entered")
        return # Base Case
    
    towerHanoi(n-1,start,aux,end) # if n = 2, n-1 = 1. so move disc 1 from A to B
                                # so we can move disc 2 to C, where it should be
    print("Move disc "+str(n)+" from "+start+" to "+end)
    towerHanoi(n-1,aux,end,start)
    
##### Tests #####
#towerHanoi(0,'A','C','B') # no discs
#print()
#towerHanoi(1,'A','C','B') # single disc
#print()
#towerHanoi(2,'A','C','B') # 2 discs
#print()
#towerHanoi(3,'A','B','C') # 3 discs



##### Stack Based Solution #####

def move_disks(n,start_stack,end_stack,aux_stack):
    if n == 0:
        return
    
    move_disks(n-1,start_stack,aux_stack,end_stack) 
    end_stack.append(start_stack.pop()) # instead of print, we update our end stack
    move_disks(n-1,aux_stack,end_stack,start_stack)
    
    
##### Testing #####
start_stack = [0,1,2,3,4,5]
end_stack = []
aux_stack = []    


print("Before:")
print("start:",start_stack)
print("end:",end_stack)
print("aux:",aux_stack)

move_disks(len(start_stack),start_stack,end_stack,aux_stack)
print()
print("After:")
print("start:",start_stack)
print("end:",end_stack)
print("aux:",aux_stack)
