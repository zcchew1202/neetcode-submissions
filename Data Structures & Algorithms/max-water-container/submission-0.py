class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        h, area = 0, 0
        while l < r:
            w = r - l
            h = min(heights[r], heights[l])
            area = max(area, h * w)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return area