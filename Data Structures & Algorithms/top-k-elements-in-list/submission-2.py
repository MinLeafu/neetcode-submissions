class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        result = []
        for _ in range(k):
            key = max(count, key=count.get)
            result.append(key)
            del count[key]
        return result