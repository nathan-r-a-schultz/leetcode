# leetcode 49: group anagrams
# medium
# array, hash table, string, sorting
# may 3, 2026

from collections import defaultdict

# initially i tried an approach that invovled sorting each string and counting the instances
# however, i felt it was too time inefficient and i didn't end up completing it
# i ended up learning and following a solution online, and this is what i ended up with
def groupAnagrams(strs: list[str]) -> list[list[str]]:

    # key will be the anagram itself, value is the indexes of the appearances
    anagramDict = defaultdict(list)

    # for each string in strs, we'll do the following:
    # fill out a count of 
    for str in strs:
        count = [0] * 26

        # count occurrences of characters
        for char in str:
            count[ord(char) - ord("a")] += 1

        # append the string to the corresponding key
        anagramDict[tuple(count)].append(str)

    # return values
    return list(anagramDict.values())

    

def main():

    strs = ["eat","tea","tan","ate","nat","bat"]

    print(groupAnagrams(strs))

main()