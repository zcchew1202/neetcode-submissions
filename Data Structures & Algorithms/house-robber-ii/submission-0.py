class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        
        dpLeft = [0] * len(nums)
        dpLeft[0] = nums[0]
        dpLeft[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            if i == len(nums)-1:
                dpLeft[i] = max(dpLeft[i-1],dpLeft[i])
            else:
                dpLeft[i] = max(dpLeft[i-1], nums[i] + dpLeft[i-2])
        dpRight = [0] * len(nums)
        dpRight[-1] = nums[-1]
        dpRight[-2] = max(nums[-1],nums[-2])
        for i in range(len(nums)-3,-1,-1):
            if i == 0:
                dpRight[i] = max(dpRight[i+1],dpRight[i])
            else:
                dpRight[i] = max(dpRight[i+1], nums[i] + dpRight[i+2])
        print(dpRight)

        return max(dpRight[0],dpLeft[-1])

        