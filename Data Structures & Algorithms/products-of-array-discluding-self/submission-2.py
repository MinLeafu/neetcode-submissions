class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [0] * n
        prod = 1
        for i in range(n):
            prefix[i] = prod
            prod *= nums[i]

        suffix = [0] * n
        prod = 1
        for i in range(n - 1, -1, -1):
            suffix[i] = prod
            prod *= nums[i]

        output = [0] * n
        for i in range(n):
            output[i] = prefix[i] * suffix[i]
        return output