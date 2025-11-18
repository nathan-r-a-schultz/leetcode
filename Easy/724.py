# leetcode 724: find pivot index
# easy
# array, prefix sum
# november 17, 2025

def pivotIndex(nums):

    for i in range(0, len(nums)):

        # get the surrounding sums of i
        left = sum(nums[:i])
        right = sum(nums[i + 1:])

        # if i is at the start or end, the surrounding value is 0
        if i == 0:
            left = 0
        elif i == len(nums) - 1:
            right = 0
        
        # if the surrounding values are equal, return i
        if (left == right):
            return i
    
    # if no pivot is found, return -1
    return -1

def main():

    #nums = [1,7,3,6,5,6] # expected ouput is 3
    #nums = [1,2,3] # expected output is -1
    nums = [2,1,-1] # expected output is 0

    print(pivotIndex(nums))

main()