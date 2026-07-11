class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        a = 0
        while a < n - 3:
            b = a + 1
            while b < n - 2:
                c, d = b + 1, n - 1
                while c < d:
                    curr_sum = nums[a] + nums[b] + nums[c] + nums[d]
                    if curr_sum > target:
                        d -= 1
                    elif curr_sum < target:
                        c += 1
                    else:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        while c < d and nums[c] == nums[c - 1]:
                            c += 1
                b += 1
                while b < n - 2 and nums[b] == nums[b - 1]:
                    b += 1
            a += 1
            while a < n - 3 and nums[a] == nums[a - 1]:
                a += 1
        return res