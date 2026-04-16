class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort ascending so we avoid backtracking
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            l,r = i+1, len(nums) - 1
            if l == len(nums) or num > 0:
                break

            if i > 0 and num == nums[i-1]:
                continue
            while l < r:
                total = nums[l] + nums[r]
                if total == -num:
                    res.append([num, nums[l], nums[r]])
                    l += 1 
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    r -= 1
                elif total > -num:
                    r -= 1
                else:
                    l += 1
                
        return res
