from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        max_count = max(count.values()) if count else 0

        buckets = [[] for _ in range(max_count+1)]

        for num,freq in count.items():
            buckets[freq].append(num)
        
        res = []
        for i in range(max_count, 0, -1):
            for num in buckets[i]:
                res.append(num)
            if len(res) == k:
                return res
        return res