class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0,1
        while left < right and right < len(numbers):
            res = numbers[left] + numbers[right]
            if res == target:
                return [left+1, right+1]
            if right == len(numbers) - 1:
                left += 1
                right = left + 1
                continue
            right += 1
        return []
                
            
