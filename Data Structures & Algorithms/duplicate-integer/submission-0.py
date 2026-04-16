from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        numCounter = Counter(nums)
        for v in numCounter.values():
            if v > 1:
                return True
        return False       