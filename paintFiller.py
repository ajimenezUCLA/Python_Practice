# Cracking the Coding Interview
# Recursion and Dynamic programming
# 8.10: Paint Fill

##### Solution #####

canvas = [[1,0,2,2,1],
          [1,2,2,1,3],
          [1,2,1,1,3],
          [3,3,1,2,1],
          [0,0,1,2,1]]

def canvasPrint(canvas):
    for item in canvas:
        print(item)
        
def paintFillHelper(canvas,row,col,oriColor,newColor):
    if (row < 0) or (row >= len(canvas)) or (col < 0) or (col >= len(canvas[0])):
        return False # out of bounds
    
    if canvas[row][col] == oriColor:
        canvas[row][col] = newColor
        paintFillHelper(canvas,row-1,col,oriColor,newColor) # Up
        paintFillHelper(canvas,row+1,col,oriColor,newColor) # Down
        paintFillHelper(canvas,row,col-1,oriColor,newColor) # Left
        paintFillHelper(canvas,row,col+1,oriColor,newColor) # Right
    return True    
    
def paintFill(canvas,row,col,newColor):
    if canvas[row][col] == newColor:
        return False # same color, do nothing
    return paintFillHelper(canvas,row,col,canvas[row][col],newColor)
        
        
        
        
##### Testing #####
print("BEFORE")
canvasPrint(canvas)
paintFill(canvas,2,2,4) # should replace the 1's with 4's
print("AFTER")
canvasPrint(canvas)
