class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        length = 1
        maxLen = 0
        seen = set(nums)
        for num in seen:
            if num-1 not in seen:
                length = 1
                while (num + length) in seen:
                    length += 1
            maxLen = max(maxLen, length)
        return maxLen
