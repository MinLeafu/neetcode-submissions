class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        bought = prices[0]
        for i in range(len(prices) - 1):
            if prices[i + 1] < prices[i]:
                profit += prices[i] - bought
                bought = prices[i + 1]
        profit += prices[-1] - bought
        return profit