class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        n = len(coins)
        dp = [0] * (amount + 1)
        
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin and dp[i - coin]:
                    if dp[i]:
                        dp[i] = min(dp[i], dp[i - coin] + 1)
                    else:
                        dp[i] = dp[i - coin] + 1
        
        if dp[amount]:
            return dp[amount]
        else:
            return -1