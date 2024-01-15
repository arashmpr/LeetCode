#
# @lc app=leetcode id=233 lang=python3
#
# [233] Number of Digit One
#
# https://leetcode.com/problems/number-of-digit-one/description/
#
# algorithms
# Hard (34.34%)
# Likes:    1463
# Dislikes: 1433
# Total Accepted:    87.2K
# Total Submissions: 253.8K
# Testcase Example:  '13'
#
# Given an integer n, count the total number of digit 1 appearing in all
# non-negative integers less than or equal to n.
# 
# 
# Example 1:
# 
# 
# Input: n = 13
# Output: 6
# 
# 
# Example 2:
# 
# 
# Input: n = 0
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 0 <= n <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def countDigitOne(self, n: int) -> int:
        ans = 0
        i = 1
        while (i<=n):
            tens = i*10
            term1 = (n//tens)*i
            term2 = min(max(n%tens-i+1, 0), i)
            ans += (term1 + term2)
            i *= 10
        return ans

        
# @lc code=end

