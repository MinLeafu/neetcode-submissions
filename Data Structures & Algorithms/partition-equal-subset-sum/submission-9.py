class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)
        
        dp1 = [False] * (target + 1)
        dp1[0] = True
        dp2 = [False] * (target + 1)
        
        for num in nums:
            for i in range(1, target + 1):
                if num <= i:
                    dp2[i] = dp1[i] or dp1[i - num]
                else:
                    dp2[i] = dp1[i]
            dp1, dp2 = dp2, dp1

        return dp1[target]