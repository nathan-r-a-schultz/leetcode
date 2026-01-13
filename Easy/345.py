# leetcode 345: reverse vowels in a string
# easy
# two pointers, string
# jan 12, 2026

# i knew how to do this by scanning the string and saving the positions of the vowels
# but i knew it wasn't the optimal solution
# so i gave it my best shot and eventually corrected my solution by checking the answer online
# as such, this is my least original solution to date
def reverseVowels(s):

    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    strList = list(s)

    start = 0
    end = len(s) - 1

    while start < end:
        while start < end and strList[start] not in vowels:
            start += 1
    
        while start < end and strList[end] not in vowels:
            end -= 1

        if start < end:
            strList[start], strList[end] = strList[end], strList[start]
            start += 1
            end -= 1

    return "".join(strList)

def main():

    s = "IceCreAm"

    print(reverseVowels(s))

main()
    