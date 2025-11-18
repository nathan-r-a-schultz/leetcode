# leetcode 1480: running sum of 1d array
# easy
# array, prefix sum
# completed June 2, 2022

# I completed this one before moving to doing questions on VS Code so this is copy and pasted straight from leetcode
# looking back at this, I know it can be improved with sum(), but I did this in grade 11 so I'm still proud of it
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = 0
        returnList = []
        
        for i in nums:
            total += i
            returnList.append(total)
            
        return returnList