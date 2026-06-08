class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        res = []
        for num in nums:
            count[num] += 1
        for key, val in count.items():
            if val > len(nums) // 3:
                res.append(key)
        return res