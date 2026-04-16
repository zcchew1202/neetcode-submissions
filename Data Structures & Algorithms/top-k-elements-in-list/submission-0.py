from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        intCount = Counter(nums)
        print(intCount.most_common(k))
        res = []
        for num in intCount.most_common(k):
            res.append(num[0])
        return res