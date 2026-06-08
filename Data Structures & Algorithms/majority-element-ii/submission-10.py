class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
            if len(count) > 2:
                for key in list(count):
                    count[key] -= 1
                    if count[key] == 0:
                        del count[key]
        
        res = []
        for num in count:
            if nums.count(num) > len(nums) // 3:
                res.append(num)
        return res