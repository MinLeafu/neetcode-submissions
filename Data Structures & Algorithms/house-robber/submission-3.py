class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        left, right = max(nums[n - 2], nums[n - 1]), nums[n - 1]
        for i in range(n - 3, -1, -1):
            left, right = max(nums[i] + right, left), left
        return left