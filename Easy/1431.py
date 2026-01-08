# leetcode 1431: kids with the greatest number of candies
# easy
# array
# completed jan 8 2026

def kidsWithCandies(candies, extraCandies):

    # get the current highest amount of candies
    greatestNum = max(candies)
    returnArr = []

    # give extra candies to each kid and check if they now have the most
    for num in candies:
        if num + extraCandies >= greatestNum:
            returnArr.append(True)
        else:
            returnArr.append(False)

    return returnArr

def main():
    candies = [2,3,5,1,3]
    extraCandies = 3

    print(kidsWithCandies(candies, extraCandies))

main()