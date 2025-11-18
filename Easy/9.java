// leetcode 9: palindrome number
// easy
// math
// completed jan 21, 2024

// putting the package here just to remove errors
package Easy;

// I completed this one before moving to doing questions on VS Code so this is copy and pasted straight from leetcode
class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
			return false;
		}
		else if (x < 10 && x > 0) {
			return true;
		}
		else {
			String a = Integer.toString(x);
			
			for (int i = 0; i < a.length(); i++) {
				if(a.charAt(i) != a.charAt(a.length() - 1 - i)) {
					return false;
				}
			}
			
			return true;
			
		}
    }
}