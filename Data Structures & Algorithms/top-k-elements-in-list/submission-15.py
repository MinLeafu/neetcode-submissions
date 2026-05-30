class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        arr = [[] for _ in range(len(nums))]
        for key in count.keys():
            arr[count[key] - 1].append(key)

        res = []
        for i in range(len(arr) - 1, -1, -1):
            res.extend(arr[i])
            k -= len(arr[i])
            if k == 0:
                break
        return res