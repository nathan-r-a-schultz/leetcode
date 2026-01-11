# leetcode 605: can plant flowers
# easy
# array, greedy
# january 11, 2026

import math

def canPlaceFlowers(flowerbed, n):

    # check for some basic base cases
    if n == 0:
        return True
    if n > math.ceil(float(len(flowerbed)) / float(2)): # for whatever reason, leetcode converts division straight to an integer. as such, this line will mess up on leetcode if the two arguments aren't first converted to floats
        return False

    canBePlanted = False

    while n > 0:

        # variable to indicate if a minimum of one plant has been planted on this iteration of the while loop
        minOnePlant = False

        for i in range(0, len(flowerbed)):

            # check the front and back of the pot while account of index out of bounds errors
            if i == 0:
                front = flowerbed[i + 1] if len(flowerbed) > 1 else -1
                behind = -1
            elif i == len(flowerbed) - 1:
                front = -1
                behind = flowerbed[i - 1]
            else: 
                front = flowerbed[i + 1]
                behind = flowerbed[i - 1]

            # planting the plant (if possible)
            if flowerbed[i] == 0 and (front == 0 or front == -1) and (behind == 0 or behind == -1):
                minOnePlant = True
                flowerbed[i] = 1
                n -= 1

            # if n is 0, we break out of the loop and set our result to 0
            if n == 0:
                canBePlanted = True
                break

        # we check if a minimum of one plant has been planted
        # if not, it means no more plants can be planted and we must break and return our result
        if minOnePlant == False:
            break

    return canBePlanted


def main():

    flowerbed = [0]
    n = 1

    print(canPlaceFlowers(flowerbed, n))

main()