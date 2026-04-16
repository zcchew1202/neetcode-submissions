class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
        bracMap = {')':'(', '}':'{',']':'['}
        for c in s:
            if c in bracMap.values():
                stack.append(c)
            elif c in bracMap.keys():
                if len(stack) == 0 or stack[-1] != bracMap[c]:
                    return False
                stack.pop()
        return len(stack) == 0

            
            