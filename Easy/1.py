# leetcode 1: two sum
# easy
# array, hash table
# completed June 2, 2022

# I completed this one before moving to doing questions on VS Code so this is copy and pasted straight from leetcode
# looking back at this, I know it can be improved with sum(), but I did this in grade 11 so I'm still proud of it
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        returnList = []
        
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if (nums[i] + nums[j]) == target and i != j:
                    returnList.append(i)
                    returnList.append(j)
                    return returnList