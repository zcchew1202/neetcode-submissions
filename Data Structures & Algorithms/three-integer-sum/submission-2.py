class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i,a in enumerate(nums):
            # means that everything to the right of a is positive and larger than itself
            if a > 0:
                break
            # handle duplicates
            if i > 0 and a == nums[i-1]:
                continue
            left, right = i+1, len(nums) - 1
            while left < right:
                threeSum = a + nums[left] + nums[right]
                if threeSum < 0:
                    left += 1
                elif threeSum > 0:
                    right -= 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left-1] == nums[left] and left < right:
                        left += 1

        return res