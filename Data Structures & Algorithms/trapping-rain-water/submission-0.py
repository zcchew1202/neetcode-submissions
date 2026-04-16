class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxLeft, maxRight = height[l], height[r]
        maxArea = 0
        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                maxArea += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight,height[r])
                maxArea += maxRight - height[r]
        return maxArea
