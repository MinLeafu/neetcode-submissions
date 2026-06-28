class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if sum(nums) % 2 != 0:
            return False
        halfsum = sum(nums) // 2
        dp = [[None] * (halfsum + 1) for _ in range(n)]

        def dfs(i, curr):
            if i == n:
                return curr == halfsum
            if dp[i][curr] is not None:
                return dp[i][curr]
            
            res = dfs(i + 1, curr)
            if curr + nums[i] <= halfsum and dfs(i + 1, curr + nums[i]):
                res = True

            dp[i][curr] = res
            return dp[i][curr]
        
        return dfs(0, 0)