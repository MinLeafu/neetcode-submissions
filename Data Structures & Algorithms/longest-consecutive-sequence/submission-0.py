class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set()
        for num in nums:
            hs.add(num)

        longest = 0
        for num in nums:
            if num - 1 not in hs:
                length = 1
                while num + 1 in hs:
                    length += 1
                    num += 1
                longest = max(longest, length)
        return longest