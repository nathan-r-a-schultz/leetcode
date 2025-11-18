# leetcode 1768: merge strings alternatively
# easy
# two pointers, string
# completed november 17, 2025

def mergeAlternatively(word1, word2):
    
    word1Arr = []
    word2Arr = []
    returnStr = ""

    # construct two arrays that have alternating blank spaces
    # it should look like this:
    # word1:  a   b   c
    # word2:    p   q   r
    for letter in word1:
        word1Arr.append(letter)
        word1Arr.append("")
    for letter in word2:
        word2Arr.append("")
        word2Arr.append(letter)

    # make sure the arrays are the same length
    while (len(word1Arr) > len(word2Arr)):
        word2Arr.append("")
    while(len(word2Arr) > len(word1Arr)):
        word1Arr.append("")

    # append letters to the return string in an alternating fashion
    for i in range(0, len(word1Arr)):
        if (i % 2 == 0):
            returnStr += word1Arr[i]
        else:
            returnStr += word2Arr[i]

    return returnStr

def main():

    # word1 = "abc"
    # word2 = "pqr" 
    # expected output: "apbqcr"

    # word1 = "ab"
    # word2 = "pqrs" 
    # expected output: "apbqrs"

    word1 = "abcd"
    word2 = "pq"
    # expected output: "apbqcd"

    print(mergeAlternatively(word1, word2))

main()