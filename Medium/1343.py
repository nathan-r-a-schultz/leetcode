# leetcode 1343
# medium
# array, sliding window
# completed at an unknown time

# i don't remember even doing this question, but here's my solution for it
# it was not quite working when i found the file for it but i've fixed it up and it works now
def numOfSubarrays(arr, k, threshold):

    threshold = threshold * k
    subArr = sum(arr[0:k])
    returnVal = int(subArr >= threshold)

    for i in range(1, len(arr) - k + 1):
        subArr = subArr + arr[i + k - 1] - arr[i - 1]
        returnVal += int(subArr >= threshold)

    return returnVal

def main():

    arr = [2,2,2,2,5,5,5,8]
    k = 3
    threshold = 4
    #expected output is 3

    # arr = [11,13,17,23,29,31,7,5,2,3]
    # k = 3
    # threshold = 5
    # expected ouput is 6

    print(numOfSubarrays(arr, k, threshold))

main()