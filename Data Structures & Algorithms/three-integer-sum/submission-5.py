class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        print(nums)
        for i, num in enumerate(nums):
            # there cannot be a triplet that sums to 0
            if num > 0:
                break
            #pass over duplicate
            if i > 0 and num == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums)-1
            while l < r:
                threeSum = nums[l] + nums[r] + num
                if (threeSum == 0):
                    res.append([num,nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif threeSum < 0:
                    l += 1
                else:
                    r -= 1
                
        return res

        