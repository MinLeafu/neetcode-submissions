class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for _ in range(len(nums)):
            if nums[i] == val:
                nums.pop(i)
                nums.append(val)
            else:
                i += 1
        return i