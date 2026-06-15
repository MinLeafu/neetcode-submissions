class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def dp(l, r):
            left = right = 0
            for i in range(l, r + 1):
                left, right = right, max(left + nums[i], right)
            return right
        
        return max(dp(0, n - 2), dp(1, n - 1))