class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 1:
            return 0

        one, two = cost[n - 2], cost[n - 1]
        for i in range(n - 3, -1, -1):
            temp = cost[i] + min(one, two)
            two = one
            one = temp
        return min(one, two)