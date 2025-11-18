// leetcode 70: climbing stairs
// easy
// math, dynamic programming, memoization
// completed jan 19, 2024

// putting the package here just to remove errors
package Easy;

// I completed this one before moving to doing questions on VS Code so this is copy and pasted straight from leetcode
class Solution {
    public int climbStairs(int n) {

        int [] stairClimb = new int [n + 1];
		stairClimb[0] = 1;
		stairClimb[1] = 1;
		
		for (int i = 2; i <= n; i++) {
			stairClimb[i] = stairClimb[i - 1] + stairClimb[i - 2];
		}
		
		return stairClimb[n];
           
    }
	
}
