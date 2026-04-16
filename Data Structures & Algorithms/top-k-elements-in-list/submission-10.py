from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = Counter(nums)
        max_freq = max(count_nums.values()) if count_nums else 0

        buckets = [[] for _ in range(max_freq+1)]
        for num,freq in count_nums.items():
            buckets[freq].append(num)
        print(buckets)

        result = []
        for i in range(max_freq,0,-1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
