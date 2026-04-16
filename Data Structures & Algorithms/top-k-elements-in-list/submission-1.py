from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        intCount = Counter(nums)
        count = [[] for i in range(len(nums) + 1)]
        for n,c in intCount.items():
            count[c].append(n)
        res = []
        for i in range(len(count)-1, 0, -1):
            for num in count[i]:
                res.append(num)
                if len(res) == k:
                    return res