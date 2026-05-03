# leetcode 217: contains duplicate
# easy
# array, hash table, sorting
# may 3, 2026

def containsDuplicate(nums: list[int]) -> bool:

    # sorting to ensure that duplicate items remain next adjacent
    nums.sort()

    for i in range(1, len(nums)):

        # if adjacent nums are identical, return true 
        if nums[i] == nums[i - 1]:
            return True
        
    return False

def main():

    # expected result: true
    nums = [1,1,1,3,3,4,3,2,4,2]

    print(containsDuplicate(nums))

main()