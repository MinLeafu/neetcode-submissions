class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        arr = [[] for _ in range(len(nums))]
        for key, val in count.items():
            arr[val - 1].append(key)

        res = []
        for i in range(len(arr) - 1, -1, -1):
            res.extend(arr[i])
            if len(res) == k:
                return res