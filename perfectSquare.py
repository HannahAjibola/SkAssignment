nums = [[2,4,5], [3,3,5], [6,4,1]]

def pSquare(nums):

    for i in range (0,len(nums)):
        row = 0
        column = 0

        for j in range (0,len(nums)):

            row += nums[i][j];
            column += nums[j][i];

    if row != column:
        return False
    else:
        return True 

print (pSquare(nums))
