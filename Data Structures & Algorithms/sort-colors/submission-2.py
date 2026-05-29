class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cols = [0] * 3
        for num in nums:
            cols[num] += 1

        idx = 0
        for i in range(len(cols)):
            for _ in range(cols[i]):
                nums[idx] = i
                idx += 1