from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int)
        for i,num in enumerate(nums):
            other = target - num
            print(seen)
            if other not in seen:
                seen[num] = i
            else:
                return sorted([i,seen[other]])
            