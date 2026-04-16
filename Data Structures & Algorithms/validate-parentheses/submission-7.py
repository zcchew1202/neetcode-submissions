class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        cList = []
        bracMap = {')': '(', ']':'[', '}': '{'}
        for c in s:
            if c in bracMap:    
                if cList and cList[-1] == bracMap[c]:
                    cList.pop()
                else:
                    return False
            else:
                cList.append(c)
        return len(cList) == 0