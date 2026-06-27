class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1] * (n + 1) for _ in range(n)]

        def dfs(i, j):
            if i == n:
                return 0
            if dp[i][j + 1] != -1:
                return dp[i][j + 1]

            length = dfs(i + 1, j)
            if j == -1 or nums[i] > nums[j]:
                length = max(length, 1 + dfs(i + 1, i))
            dp[i][j + 1] = length
            return length
        return dfs(0, -1)