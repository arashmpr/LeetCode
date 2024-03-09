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

        