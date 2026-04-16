class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valToIndex = {}
        for i,v in enumerate(nums):
            result = target - v
            if result in valToIndex:
                return sorted([valToIndex[result], i])
            valToIndex[v] = i