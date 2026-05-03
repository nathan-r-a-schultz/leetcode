# leetcode 217: valid anagram
# easy
# hash table, string, sorting
# may 3, 2026

# my original solution
def isAnagram(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False
    
    sSorted = sorted(s)
    tSorted = sorted(t)

    for i in range(0, len(s)):
        
        if (sSorted[i] != tSorted[i]):
            return False
        
    return True

# revised optimal solution
def isAnagramEfficient(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

def main():

    s = "anagram"
    t = "nagaram"

    print(isAnagram(s, t))

main()