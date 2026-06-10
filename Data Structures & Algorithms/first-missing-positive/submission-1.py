class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        seen = [False] * n
        for num in nums:
            if 1 <= num <= n:
                seen[num - 1] = True
        
        for i in range(n):
            if not seen[i]:
                return i + 1
        return n + 1