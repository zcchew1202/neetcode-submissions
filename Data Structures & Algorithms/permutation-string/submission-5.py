from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = r = 0
        countS1 = Counter(s1)
        while l < len(s2):
            while (r-l+1) <= len(s1):
                print(s2[l:r+1])
                countS2 = Counter(s2[l:r+1])
                if countS1 == countS2:
                    return True
                else:
                    r += 1
            l += 1
        return False