class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int)
        for i,num in enumerate(nums):
            other = target - num
            print(seen)
            if other in seen:
                return [seen[other],i]
            else:
                seen[num] = i
        
