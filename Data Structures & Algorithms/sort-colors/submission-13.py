class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # l, r, i = 0, len(nums) - 1, 0
        # while i <= r:
        #     match nums[i]:
        #         case 0:
        #             nums[l], nums[i] = nums[i], nums[l]
        #             l += 1
        #             i += 1
        #         case 1:
        #             i += 1
        #         case 2:
        #             nums[i], nums[r] = nums[r], nums[i]
        #             r -= 1

        zero = one = two = 0
        for num in nums:
            match num:
                case 0:
                    nums[two] = 2
                    two += 1
                    nums[one] = 1
                    one += 1
                    nums[zero] = 0
                    zero += 1
                case 1:
                    nums[two] = 2
                    two += 1
                    nums[one] = 1
                    one += 1
                case 2:
                    nums[two] = 2
                    two += 1