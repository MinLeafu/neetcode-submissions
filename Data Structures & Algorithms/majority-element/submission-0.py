class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ht = {}
        for num in nums:
            ht[num] = 1 + ht.get(num, 0)
            
        for key, value in ht.items():
            if value > len(nums) // 2:
                return key