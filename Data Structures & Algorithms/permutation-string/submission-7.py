from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        countS1 = Counter(s1)
        countS2 = defaultdict(int)
        windowSize = len(s1)
        for i in range(windowSize):
            countS2[s2[i]] += 1
        if countS2 == countS1:
            return True 
        l = 0
        for r in range(windowSize,len(s2)):
            newChar = s2[r]
            countS2[newChar] += 1

            oldChar = s2[l]
            countS2[oldChar] -= 1
            if countS2[oldChar] == 0:
                del countS2[oldChar]
            if countS2 == countS1:
                return True
            l += 1
        return False






