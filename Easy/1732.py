# leetcode 1732: find the highest altitude
# easy
# array, prefix sum
# november 17, 2025

def largestAltitude(gain):

    # altitude array always starts at 0, so the biggest must be 0 or greater
    altitudes = [0]
    displacement = 0
    biggest = 0

    for element in gain:

        # increase total displacement and append to array
        # displacement is essientially the prefix up to a given point
        displacement = displacement + element
        altitudes.append(displacement)

        # check for the biggest value
        if displacement > biggest:
            biggest = displacement

    return biggest

def main():

    #gain = [-5,1,5,0,-7] # expected output is 1
    gain = [-4,-3,-2,-1,4,3,2] # expected output is 0

    print(largestAltitude(gain))

main()