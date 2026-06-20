class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maximum = minimum = res = nums[0]
        for i in range(1, n):
            temp_max = maximum
            maximum = max(nums[i], nums[i] * maximum, nums[i] * minimum)
            minimum = min(nums[i], nums[i] * temp_max, nums[i] * minimum)
            res = max(res, maximum)
        return res