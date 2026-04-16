class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numSet = set(nums)
        res = set()
        length, longest = 0,0
        for n in nums:
            if (n-1) not in numSet:
                length = 1
                while (n+length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest
            


