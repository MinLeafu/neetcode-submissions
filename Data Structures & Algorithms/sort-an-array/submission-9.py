class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)

    def merge_sort(self, nums):
        if len(nums) < 2:
            return nums
        
        mid = (len(nums) + 1) // 2
        left, right = nums[:mid], nums[mid:]

        left = self.merge_sort(left)
        right = self.merge_sort(right)
        return self.merge(left, right)

    def merge(self, left, right):
        result = []

        while left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))

        result.extend(left)
        result.extend(right)
        return result