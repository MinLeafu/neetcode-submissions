class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n

        def dfs(i):
            if dp[i] != -1:
                return dp[i]

            length = 1
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    length = max(length, dfs(j) + 1)
            dp[i] = length
            return length
        return max(dfs(i) for i in range(n))