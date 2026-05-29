class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r, i = 0, len(nums) - 1, 0
        while i <= r:
            match nums[i]:
                case 0:
                    nums[l], nums[i] = nums[i], nums[l]
                    l += 1
                    i += 1
                case 1:
                    i += 1
                case 2:
                    nums[i], nums[r] = nums[r], nums[i]
                    r -= 1