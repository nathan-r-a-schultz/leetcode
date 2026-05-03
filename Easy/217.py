# leetcode 217: contains duplicate
# easy
# array, hash table, sorting
# may 3, 2026

# my original solution
def containsDuplicate(nums: list[int]) -> bool:

    # sorting to ensure that duplicate items remain next adjacent
    nums.sort()

    for i in range(1, len(nums)):

        # if adjacent nums are identical, return true 
        if nums[i] == nums[i - 1]:
            return True
        
    return False

# optimal solution i found online
def containsDuplicateEfficient(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))

def main():

    # expected result: true
    nums = [1,1,1,3,3,4,3,2,4,2]

    print(containsDuplicate(nums))

main()