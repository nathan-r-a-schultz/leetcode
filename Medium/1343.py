def numOfSubarrays(arr, k, threshold):

    returnVal = 0
    threshold = threshold * k
    subArr = sum(arr[0:k])

    for i in range(0, len(arr) - k + 1):
        subArr = arr[i + k - 1] - arr[i - 1]
        returnVal += int(subArr >= threshold)

    return returnVal

def main():

    # arr = [2,2,2,2,5,5,5,8]
    # k = 3
    # threshold = 4
    # expected output is 3

    arr = [11,13,17,23,29,31,7,5,2,3]
    k = 3
    threshold = 5
    # expected ouput is 6

    print(numOfSubarrays(arr, k, threshold))

main()