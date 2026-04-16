import math
from functools import reduce

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        curRate = 1
        while l <= r:
            k = (l+r)//2
            times = [math.ceil(float(p)/k) for p in piles]
            time = reduce(lambda x,y: x+y, times)
            if time > h:
                l = k + 1
            elif time <= h:
                curRate = k
                r = k - 1
        
        return curRate


                
