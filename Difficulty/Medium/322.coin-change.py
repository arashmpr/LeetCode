#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (43.70%)
# Likes:    18518
# Dislikes: 433
# Total Accepted:    1.7M
# Total Submissions: 3.9M
# Testcase Example:  '[1,2,5]\n11'
#
# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money.
# 
# Return the fewest number of coins that you need to make up that amount. If
# that amount of money cannot be made up by any combination of the coins,
# return -1.
# 
# You may assume that you have an infinite number of each kind of coin.
# 
# 
# Example 1:
# 
# 
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# 
# 
# Example 2:
# 
# 
# Input: coins = [2], amount = 3
# Output: -1
# 
# 
# Example 3:
# 
# 
# Input: coins = [1], amount = 0
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1]*(amount+1)
        dp[0] = 0
        for i in range(amount+1):
            if dp[i] != -1:
                for coin in coins:
                    if i+coin<=amount:
                        if dp[i+coin] != -1:
                            dp[i+coin] = min(dp[i] + 1, dp[i+coin])
                        else:
                            dp[i+coin] = dp[i] + 1
        return dp[amount]
        
# @lc code=end

