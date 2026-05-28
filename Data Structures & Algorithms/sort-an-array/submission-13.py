class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums, 0, len(nums) - 1)
        return nums

    def merge_sort(self, nums, left, right):
        if left >= right:
            return
        
        mid = (left + right) // 2
        self.merge_sort(nums, left, mid)
        self.merge_sort(nums, mid + 1, right)

        self.merge(nums, left, mid, right)
    
    def merge(self, nums, l, m, r):
        left, right = nums[l:m + 1], nums[m + 1:r + 1]

        i, j, k = l, 0, 0

        while j < len(left) and k < len(right):
            if left[j] <= right[k]:
                nums[i] = left[j]
                j += 1
            else:
                nums[i] = right[k]
                k += 1
            i += 1
        
        while j < len(left):
            nums[i] = left[j]
            j += 1
            i += 1
        
        while k < len(right):
            nums[i] = right[k]
            k += 1
            i += 1