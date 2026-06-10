class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        missing = 1
        while True:
            if missing not in nums:
                return missing
            missing += 1