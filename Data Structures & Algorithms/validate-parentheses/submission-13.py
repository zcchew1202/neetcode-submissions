class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        brac_map = {
            ']':'[',
            ')':'(',
            '}':'{'
        }
        if s[0] in brac_map.keys():
            return False
        stack = []
        for c in s:
            if c in brac_map.values():
                stack.append(c)
            elif len(stack) > 0 and stack[-1] == brac_map[c]:
                stack.pop()
            else:
                return False
        return len(stack) == 0