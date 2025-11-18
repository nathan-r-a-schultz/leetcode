# leetcode 151: reverse words in a string
# medium
# two pointers, string
# completed Sept 2025


# I completed this one before moving to doing questions on VS Code so this is copy and pasted straight from leetcode
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        s = s.lstrip().split()

        s.reverse()

        s = " ".join(s)

        return s
        