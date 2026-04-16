class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = len(nums)//2
        left = 0
        right = len(nums) - 1
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] < target:
                left = pivot + 1
            if nums[pivot] > target:
                right = pivot - 1
            if nums[pivot] == target:
                return pivot

        if nums[pivot] == target:
            return pivot


        return -1      