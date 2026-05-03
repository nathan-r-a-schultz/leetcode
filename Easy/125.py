# leetcode 125: valid palindrome
# easy
# two pointers, string
# may 2, 2026

def isPalindrome(s: str) -> bool:

    leftPtr = 0
    rightPtr = len(s) - 1

    while (leftPtr < rightPtr): 

        while (s[leftPtr].isalnum() == False and leftPtr < rightPtr):
            leftPtr += 1
        
        while (s[rightPtr].isalnum() == False and leftPtr < rightPtr):
            rightPtr -= 1

        if s[leftPtr].lower() != s[rightPtr].lower():
            return False
        
        leftPtr += 1
        rightPtr -= 1

    return True

def main():

    s = "racecar"
    print(isPalindrome(s))

main()